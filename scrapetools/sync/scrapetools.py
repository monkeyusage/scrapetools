"""
core module of the library, implements the sync version of the library
"""
from __future__ import annotations

import asyncio
from time import sleep

import requests
from bs4 import BeautifulSoup
from scraper_api import ScraperAPIClient

from scrapetools.credentials import API_KEY
from scrapetools.scrapetools import fetch_many as async_fetch_many
from scrapetools.validation import validate_params

CLIENT = ScraperAPIClient(API_KEY) if API_KEY is not None else None


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
    verbose: bool = False,
    client: ScraperAPIClient | None = CLIENT,
    sequential: bool = True,
    workers: int = 20,
    **kwargs: int,
) -> list[BeautifulSoup | None]:
    """
    fetches url by url using the sync function
    or calls the equivalent fetch_many function in a blocking manner
    """
    if sequential:
        responses = []
        for url in urls:
            response = fetch(url, use_proxy, client, **kwargs)
            responses.append(response)
        return responses
    return asyncio.run(
        async_fetch_many(
            urls, use_proxy=use_proxy, verbose=verbose, workers=workers, **kwargs
        )
    )
