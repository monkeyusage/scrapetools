"""
core library module, implements default async fetch functions
"""
from __future__ import annotations

import asyncio
from typing import Any

import aiohttp
from bs4 import BeautifulSoup

from scrapetools import API_KEY


async def fetch(
    url: str, use_proxy: bool = True, verbose: bool = False, json:bool = False, **kwargs: Any
) -> BeautifulSoup | None:
    """
    sends async requests to the given url
    returns Coroutine[None, None,BeautifulSoup|None]
    """

    link = f"http://api.scraperapi.com/?api_key={API_KEY}&url={url}"

    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            if response.status != 200:
                if verbose:
                    print(
                        f"Failed to fetch for url: {url} with error code: {response.status}"
                    )
                return None
            if verbose:
                print(f"Fetched for url {url} successfully!")
            if json:
                data = await response.json()
                return data
            html = await response.text()
            return BeautifulSoup(html, "html.parser")


async def fetch_many(
    urls: list[str],
    use_proxy: bool = True,
    verbose: bool = False,
    workers: int = 20,
    **kwargs: int,
) -> list[BeautifulSoup | None]:
    """
    Fetches many urls using a given amount of workers and a queue to pull urls from
    """
    urls_queue: asyncio.Queue[tuple[int, str]] = asyncio.Queue()
    for idx, url in enumerate(urls):
        urls_queue.put_nowait((idx, url))
    responses: list[BeautifulSoup | None] = [None for _ in urls]

    async def worker(queue: asyncio.Queue[tuple[int, str]]) -> None:
        """
        Consumes a urls queue until it's empty, filling the responses list on every iteration
        We do not worry about the list 'responses' ownership since asyncio is single threaded
        """
        while True:
            index, url = await queue.get_nowait()
            response = await fetch(url, use_proxy=use_proxy, verbose=verbose, **kwargs)
            if response is not None:
                responses[index] = response
            queue.task_done()

    tasks = [asyncio.create_task(worker(urls_queue)) for _ in range(workers)]
    await urls_queue.join()
    for task in tasks:
        task.cancel()
    await asyncio.gather(*tasks)

    return responses
