from scraper_api import ScraperAPIClient
from bs4 import BeautifulSoup

def fetch(url: str, use_proxy: bool, client: ScraperAPIClient | None, **kwargs: int) -> BeautifulSoup | None: ...
def fetch_many(
    urls: list[str],
    use_proxy: bool,
    verbose: bool,
    client: ScraperAPIClient | None,
    sequential: bool,
    workers: int,
    **kwargs: int
) -> list[BeautifulSoup | None]: ...