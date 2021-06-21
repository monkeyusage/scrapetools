"""
core library module, implements default async fetch functions
"""
from __future__ import annotations

import asyncio
from asyncio import sleep

import aiohttp
from bs4 import BeautifulSoup

from scrapetools.credentials import API_KEY
from scrapetools.validation import validate_params


async def fetch(
    url: str, use_proxy: bool = True, verbose: bool = False, **kwargs: int
) -> BeautifulSoup | None:
    """
    sends async requests to the given url
    returns Coroutine[None, None,BeautifulSoup|None] if failure happened
    you can configure sleeping time
    """
    sleeping_t = validate_params(url, use_proxy, **kwargs)
    if verbose:
        print(f"Sleeping for {sleeping_t} seconds")
    await sleep(sleeping_t)

    link = (
        f"http://api.scraperapi.com/?api_key={API_KEY}&url={url}"
        if (use_proxy and API_KEY is not None)
        else url
    )

    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            if response.status != 200:
                if verbose:
                    print(
                        f"Failed to fetch for url: {url} with error code: {response.status}"
                    )
                return None
            html = await response.text()
    if verbose:
        print(f"Fetched for url {url} successfully!")
    soup = BeautifulSoup(html, "html.parser")
    return soup


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
        Consumes a urls queue until it's empty, filling the responses list on evert iteration
        We do not worry about the list 'responses' ownership since asyncio is single threaded
        """
        while True:
            try:
                index, url = queue.get_nowait()
            except asyncio.QueueEmpty:
                break
            response = await fetch(url, use_proxy=use_proxy, verbose=verbose, **kwargs)
            if response is not None:
                responses[index] = response
            queue.task_done()

    tasks = [asyncio.create_task(worker(urls_queue)) for _ in range(workers)]
    await urls_queue.join()
    await asyncio.gather(*tasks)

    return responses
