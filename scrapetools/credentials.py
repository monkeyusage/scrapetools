from __future__ import annotations
from scraper_api import ScraperAPIClient
from os import environ, path, mkdir
import logging

if not path.exists(".scrapetools"):
    mkdir(".scrapetools")

logging.basicConfig(
    filename=".scrapetools/debug.log",
    filemode="a",
    datefmt="%Y-%m-%d %H:%M:%S",
    level="DEBUG",
)

API_KEY = environ.get("scraperapi_proxy")
if API_KEY is None:
    logging.error("Could not find proxy environment variable")
    raise EnvironmentError(
        "Did not find proxy secret key environment variable inside the system"
    )

CLIENT = ScraperAPIClient(API_KEY)
