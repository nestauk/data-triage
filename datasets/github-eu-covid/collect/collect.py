import requests
from datetime import datetime as dt
import time

REL_NEXT = 'rel="next"'
API_URL = 'https://api.github.com/search/{}'
TOPIC_HEADER = 'application/vnd.github.mercy-preview+json'
HEADER_LOOKUP = {'topics': TOPIC_HEADER,
                 'repositories': TOPIC_HEADER}


def search(endpoint, q='', per_page=1000, **kwargs):
    query = (q, *(f'{k}:{v}' for k, v in kwargs.items()))
    headers = ({'Accept': HEADER_LOOKUP[endpoint]}
               if endpoint in HEADER_LOOKUP else {})
    page, link = 1, REL_NEXT
    while REL_NEXT in link:
        # Make the request
        start = time.time()
        r = requests.get(url=API_URL.format(endpoint),
                         params={'q': ' '.join(query),
                                 'per_page': per_page, 'page': page},
                         headers=headers)
        r.raise_for_status()
        # Extract info from the request
        metadata = r.json()
        total_count = metadata['total_count']
        head = r.headers
        link = head['link'] if 'link' in head else ''
        ratelim = 60 / (int(head['X-Ratelimit-Limit']) - 1)
        ratelim_remaining = int(head['X-Ratelimit-Remaining'])
        ratelim_reset_time = dt.fromtimestamp(int(head['X-Ratelimit-Reset']))
        # Yield results
        try:
            for result in metadata['items']:
                yield total_count, result
        # Need to catch generator "break", to clean up the rate limit
        except GeneratorExit:
            link = ''  # <-- Will break us out of the while loop
        # Otherwise increment the page
        else:
            page += 1
        # Mind your rate limit
        sleepy_time = (ratelim_reset_time - dt.now()).total_seconds()
        if ratelim_remaining < 2 and sleepy_time > 0:
            time.sleep(sleepy_time + 10)
        while time.time() - start < ratelim:
            time.sleep(0.5)