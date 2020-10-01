"""Fetch the latest CORD19 data dump. Due to the time difference between
EU and US, the latest data dump might have yesterday's date.
"""

import requests
from datetime import datetime, timedelta

URL = "https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com"


def _today():
    """Get a string of today's date in YYYY-MM-DD format."""
    return datetime.today().strftime("%Y-%m-%d")


def _yesterday():
    """Get a string of yesterday's date in YYYY-MM-DD format."""
    return (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")


def get_latest_cord19(
    URL=URL,
    files=["metadata.csv", "document_parses.tar.gz", "cord_19_embeddings.tar.gz"],
):
    """Download the latest CORD19 files and store them in the working directory."""
    for file in files:
        try:
            # Try getting today's file
            url = f"{URL}/{_today()}/{file}"
            # Request file
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.HTTPError as h:
            # Get yesterday's file
            url = f"{URL}/{_yesterday()}/{file}"
            # Request file
            r = requests.get(url)

        # Write file to working directory
        with open(file, "wb") as f:
            f.write(r.content)
