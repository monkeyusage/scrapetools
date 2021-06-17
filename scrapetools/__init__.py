"""
scrapetools is a webscraping tool that uses scraper_api and bs4 to make your webscrapping experience easier
"""
from __future__ import annotations
__version__ = "0.2.1"
__author__ = "monkeyusage"

from random import randint

from scrapetools.credentials import API_KEY, CLIENT
from scrapetools.scrapetools import fetch