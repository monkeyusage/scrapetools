from __future__ import annotations

from time import sleep

import requests
from bs4 import BeautifulSoup
from scraper_api import ScraperAPIClient

from scrapetools.credentials import API_KEY
from scrapetools.validation import validate_params

if API_KEY is not None:
    CLIENT = ScraperAPIClient(API_KEY)
else:
    CLIENT = None


def fetch(
    url: str,
    use_proxy: bool = True,
    client: ScraperAPIClient | None = CLIENT,
    **kwargs: int,
) -> BeautifulSoup | None:
    """
    uses scraperapi-sdk to send requests to the given url
    returns BeautifulSoup object or None if failure happened
    you can configure sleeping time
    """
    sleeping_t = validate_params(url, use_proxy, **kwargs)
    print(f"Sleeping for {sleeping_t} seconds")
    sleep(sleeping_t)
    response = (
        client.get(url) if (use_proxy and client is not None) else requests.get(url)
    )
    if not response.ok:
        print(f"Failed to fetch for url: {url} with error code: {response.status_code}")
        return None
    print(f"Fetched for url {url} successfully!")
    soup = BeautifulSoup(
        str(response.content, encoding="utf8", errors="ignore"), "html.parser"
    )
    return soup


def fetch_many(
    urls: list[str],
    use_proxy: bool = True,
    client: ScraperAPIClient | None = CLIENT,
    **kwargs: int,
) -> list[BeautifulSoup | None]:
    responses = []
    for url in urls:
        response = fetch(url, use_proxy, client, **kwargs)
        responses.append(response)
    return responses
