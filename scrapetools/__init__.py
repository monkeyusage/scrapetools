"""
scrapetools is a webscraping tool that uses:
    scraper_api, aiohttp, asyncio and bs4
to make your webscrapping experience easier

>>> await scrapetools.fetch_many(urls) # using async api
>>> scratools.sync.fetch_many(urls) # using the sync api

many options are available
"""
from __future__ import annotations

from os import mkdir, path

from scrapetools.scrapetools import fetch, fetch_many

__version__ = "0.3.1"
__author__ = "monkeyusage"

if not path.exists("debug"):
    mkdir("debug")
