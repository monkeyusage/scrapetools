"""
core module of the library, implements the sync version of the library
"""
from __future__ import annotations

import asyncio
from typing import Any

from scrapetools.scrapetools import ScrapetoolsResult
from scrapetools.scrapetools import fetch as async_fetch
from scrapetools.scrapetools import fetch_many as async_fetch_many


def fetch(
    url: str, verbose: bool = False, json: bool = False, **kwargs: Any
) -> ScrapetoolsResult:
    """
    uses scrapetools async fetch function with asyncio.run
    checkout fetch implementation in scrapetools
    """
    return asyncio.run(async_fetch(url, verbose, json, **kwargs))


def fetch_many(
    urls: list[str], verbose: bool = False, workers: int = 25, **kwargs: Any
) -> list[ScrapetoolsResult]:
    """
    fetches url by url using the sync function
    or calls the equivalent fetch_many function in a blocking manner
    """
    return asyncio.run(async_fetch_many(urls, verbose, workers, **kwargs))
