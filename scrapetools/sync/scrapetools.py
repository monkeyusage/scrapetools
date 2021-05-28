from __future__ import annotations

import logging
from time import sleep

from bs4 import BeautifulSoup
from scraper_api import ScraperAPIClient

from scrapetools.credentials import CLIENT
from scrapetools.validation import validate_params


def fetch(
    url: str, client: ScraperAPIClient = CLIENT, **kwargs: int
) -> BeautifulSoup | None:
    """
    uses scraperapi-sdk to send requests to the given url
    returns BeautifulSoup object or None if failure happened
    you can configure sleeping time
    """
    sleeping_t = validate_params(url, **kwargs)
    logging.debug(f"Sleeping for {sleeping_t} seconds")
    sleep(sleeping_t)
    response = client.get(url)
    if not response.ok:
        logging.error(
            f"Failed to fetch for url: {url} with error code: {response.status_code}"
        )
        return None
    logging.info(f"Fetched for url {url} successfully!")
    soup = BeautifulSoup(
        str(response.content, encoding="utf8", errors="ignore"), "html.parser"
    )
    return soup
