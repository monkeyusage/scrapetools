"""
validation module, helps arguments for both async and sync versions of the library
"""
from __future__ import annotations

from random import randint

from scrapetools.credentials import API_KEY


def validate_url(url: str) -> None:
    """simple http protocol check"""
    assert url.startswith("http"), f"url should use http protocol. Got {url}"


def validate_proxy_param(proxy_param: bool) -> None:
    """checks if use of proxy parameter is okay"""
    if proxy_param is True:
        assert API_KEY is not None, "Cannot use proxy without an api key"


def validate_kwargs(**kwargs: int) -> None:
    """
    validates kwargs entered when fetching for online data
    the current setup accepts the following parameters:
        - min_t for min time sleeping
        - max_t for max time sleeping
        - sleep for exact amount of time sleeping
    all of these arguments are integers representing seconds
    """
    allowed_kwargs = set(
        [
            "min_t",
            "max_t",
            "sleep",
        ]
    )
    assert all(
        map(lambda kw: kw in allowed_kwargs, kwargs.keys())
    ), f"Unauthorized key word argument used, use one of the following: {allowed_kwargs}"

    assert all(
        map(lambda v: isinstance(v, int), kwargs.values())
    ), "All keyword values should be integers"


def get_sleeping_time(**kwargs: int) -> int:
    """
    if sleep is provided we just return it
    else if we get both min_t and max_t and min_t < max_t
      we randomly choose a number in that range and return it
    otherwise we randomly choose between 10 and 20
    """
    min_t: int | None = kwargs.get("min_t")
    max_t: int | None = kwargs.get("max_t")
    sleep: int | None = kwargs.get("sleep")

    if sleep is not None:
        return sleep
    if (min_t is not None) and (max_t is not None):
        assert min_t < max_t, "min_t must be smaller than max_t"
        return randint(min_t, max_t)
    return randint(10, 20)


def validate_params(url: str, use_proxy: bool, **kwargs: int) -> int:
    """
    validates url then sleeping kwargs
    """
    validate_url(url)
    validate_proxy_param(use_proxy)
    validate_kwargs(**kwargs)
    sleeping_time = get_sleeping_time(**kwargs)
    return sleeping_time
