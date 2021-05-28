from __future__ import annotations

import logging
from asyncio import sleep

import aiohttp
from bs4 import BeautifulSoup

from scrapetools.credentials import API_KEY
from scrapetools.validation import validate_params


async def fetch(url: str, **kwargs: int) -> BeautifulSoup | None:
    """
    uses scraperapi-sdk to send async requests to the given url
    returns Coroutine[None, None,BeautifulSoup|None] if failure happened
    you can configure sleeping time
    """
    sleeping_t = validate_params(url, **kwargs)
    logging.debug(f"Sleeping for {sleeping_t} seconds")
    sleep(sleeping_t)

    link = f"http://api.scraperapi.com/?api_key={API_KEY}&url={url}"

    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            if response.status != 200:
                logging.error(
                    f"Failed to fetch for url: {url} with error code: {response.status}"
                )
                return None
            html = await response.text()
    logging.info(f"Fetched for url {url} successfully!")
    soup = BeautifulSoup(html, "html.parser")
    return soup
