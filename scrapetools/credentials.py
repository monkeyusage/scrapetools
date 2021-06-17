from __future__ import annotations
from scraper_api import ScraperAPIClient
from os import environ, path, mkdir
import logging

API_KEY = environ.get("scraperapi_proxy")
if API_KEY is None:
    raise EnvironmentError(
        "Did not find proxy secret key environment variable <scraperapi_proxy> inside the system"
    )

CLIENT = ScraperAPIClient(API_KEY)

if not path.exists("debug"):
    mkdir("debug")

logging.basicConfig(
    filename="debug/debug.log",
    format="%(asctime)s %(levelname)s %(message)s",
    filemode="a",
    datefmt="%Y-%m-%d %H:%M:%S",
    level="DEBUG",
)