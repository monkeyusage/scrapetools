import pytest
from bs4 import BeautifulSoup

from scrapetools import fetch
from scrapetools.scrapetools import fetch_many


@pytest.mark.asyncio
async def test_fetch() -> None:
    resp = await fetch("http://www.google.com", sleep=0)
    assert type(resp) == BeautifulSoup


@pytest.mark.asyncio
async def test_fetch_many() -> None:
    resps = await fetch_many(
        ["https://www.google.com", "https://www.bing.com"], workers=2, sleep=0
    )
    assert all([type(result) == BeautifulSoup for result in resps])
