import pytest
from bs4 import BeautifulSoup

from scrapetools import fetch, fetch_many
from scrapetools.sync import fetch as sync_fetch
from scrapetools.sync import fetch_many as sync_fetch_many


@pytest.mark.asyncio
async def test_fetch() -> None:
    resp = await fetch("http://www.google.com")
    assert type(resp) == BeautifulSoup


def test_sync_fetch() -> None:
    resp = sync_fetch("https://www.google.com")
    assert type(resp) == BeautifulSoup


@pytest.mark.asyncio
async def test_fetch_many() -> None:
    resps = await fetch_many(
        ["https://www.google.com", "https://www.bing.com"], workers=2
    )
    assert all([type(result) == BeautifulSoup for result in resps])


def test_sync_fetch_many() -> None:
    resps = sync_fetch_many(
        ["https://www.google.com", "https://www.bing.com"], workers=2
    )
    assert all([type(result) == BeautifulSoup for result in resps])


@pytest.mark.asyncio
async def test_json() -> None:
    data = await fetch("https://jsonplaceholder.typicode.com/todos/1", json=True)
    assert type(data) in (dict, None)
