"""
core library module, implements default async fetch functions
"""
from __future__ import annotations

import asyncio
from asyncio import QueueEmpty
from os import environ
from typing import Any

import aiohttp
from aiohttp import ContentTypeError
from bs4 import BeautifulSoup

API_KEY = environ["proxy"]


async def fetch(
    url: str,
    verbose: bool = False,
    json: bool = False,
    **kwargs: Any
) -> BeautifulSoup | dict[Any, Any] | None:
    """
    sends async requests to the given url
    returns Coroutine[None, None,BeautifulSoup|None|dict[Any,Any]]
    """

    payload = {"api_key": API_KEY, "url": url}

    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://api.scraperapi.com", params=payload, **kwargs
        ) as response:
            if response.status != 200:
                if verbose:
                    print(
                        f"Failed to fetch for url: {url} with error code: {response.status}"
                    )
                return None
            if verbose:
                print(f"Fetched for url {url} successfully!")
            try:
                if json:
                    data: dict[Any, Any] = await response.json()
                    return data
                html = await response.text()
                return BeautifulSoup(html, "html.parser")
            except ContentTypeError:
                return None


async def fetch_many(
    urls: list[str],
    verbose: bool = False,
    workers: int = 25,
    json: bool = False,
    **kwargs: int,
) -> list[BeautifulSoup | dict[Any, Any] | None]:
    """
    Fetches many urls using a given amount of workers and a queue to pull urls from
    """
    urls_queue: asyncio.Queue[tuple[int, str]] = asyncio.Queue()
    for idx, url in enumerate(urls):
        urls_queue.put_nowait((idx, url))
    responses: list[BeautifulSoup | dict[Any, Any] | None] = [None for _ in urls]

    async def worker(queue: asyncio.Queue[tuple[int, str]]) -> None:
        """
        Consumes a urls queue until it's empty, filling the responses list on every iteration
        We do not worry about the list 'responses' ownership since asyncio is single threaded
        """
        while True:
            try:
                index, url = queue.get_nowait()
            except QueueEmpty:
                return None
            response = await fetch(url, verbose=verbose, json=json, **kwargs)
            if response is not None:
                responses[index] = response
            queue.task_done()

    tasks = [asyncio.create_task(worker(urls_queue)) for _ in range(workers)]
    await urls_queue.join()
    await asyncio.gather(*tasks)

    return responses
