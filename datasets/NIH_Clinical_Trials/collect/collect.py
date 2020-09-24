"""Collects all full studies from NIH Clinical Trials.

API documentation: https://clinicaltrials.gov/api/gui/
"""

import requests


def collect_full_studies(expr, min_rnk, max_rnk, fmt="JSON"):
    r = requests.get(
        f"https://clinicaltrials.gov/api/query/full_studies?expr={expr}&min_rnk={min_rnk}&max_rnk={max_rnk}&fmt={fmt}"
    )
    r.raise_for_status()
    return r.json()


def main():
    # Collect the first 100 studies
    return collect_full_studies(expr="", min_rnk=1, max_rnk=100)


if __name__ == "__main__":
    main()
