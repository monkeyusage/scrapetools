from __future__ import annotations

from os import environ, mkdir, path
from warnings import warn

from scraper_api import ScraperAPIClient

API_KEY = environ.get("scraperapi_proxy")
if API_KEY is None:
    warn(
        "Did not find proxy secret key environment variable <scraperapi_proxy> inside the system \
            you'll be using your own IP for the request you make"
    )
    CLIENT = None
else:
    CLIENT = ScraperAPIClient(API_KEY)

if not path.exists("debug"):
    mkdir("debug")
