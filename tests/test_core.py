import pytest
from bs4 import BeautifulSoup
from scrapetools import fetch


@pytest.mark.asyncio
async def test_fetch() -> None:
    resp = await fetch("http://www.google.com", sleep=0)
    assert type(resp) == BeautifulSoup
    
