from __future__ import annotations
from scraper_api import ScraperAPIClient
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from os import environ, path, mkdir
import logging

if not path.exists(".scrapetools"):
    mkdir(".scrapetools")

logging.basicConfig(
    filename=".scrapetools/debug.log",
    filemode="a",
    datefmt="%Y-%m-%d %H:%M:%S",
    level="DEBUG",
)

proxy = environ.get("scraperapi_proxy")
if proxy is None:
    logging.error("Could not find proxy environment variable")
    raise EnvironmentError(
        "Did not find proxy secret key environment variable inside the system"
    )

CLIENT = ScraperAPIClient(proxy)


def fetch(
    url: str,
    client: ScraperAPIClient = CLIENT,
    min_sleep: int = 10,
    max_sleep: int = 20,
    exact_sleep: int | None = None,
) -> BeautifulSoup | None:
    """
    uses scraper_api to send requests to the given url
    returns BeautifulSoup object or None if failure happened
    you can configure sleeping time
    """
    if not url.startswith("http"):
        raise ValueError("url should use http protocol")
    for arg in (min_sleep, max_sleep):
        if not isinstance(arg, int):
            raise ValueError(f"{arg.__name__} must be an int")
    if (exact_sleep is not None) and not isinstance(exact_sleep, int):
        raise ValueError("exact_sleep must be either None or int")
    sleeping_time = (
        randint(min_sleep, max_sleep) if exact_sleep is None else exact_sleep
    )
    logging.debug(f"sleeping for {sleeping_time} seconds")
    sleep(sleeping_time)
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
