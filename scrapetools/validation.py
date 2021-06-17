from __future__ import annotations
import warnings
from random import randint

def validate_url(url: str) -> None:
    """simple http protocol check"""
    if not url.startswith("http"):
        raise ValueError("url should use http protocol")


def validate_sleep(**kwargs: int) -> int:
    """
    validates kwargs entered when fetching for online data
    the current setup accepts the following parameters:
        - min_t for min time sleeping
        - max_t for max time sleeping
        - sleep for exact amount of time sleeping
    all of these arguments are integers representing seconds
    if sleep is provided we just return it
    else if we get both min_t and max_t and min_t < max_t
      we randomly choose a number in that range and return it
    otherwise we randomly choose between 10 and 20
    """
    for key, value in kwargs.items():
        if not isinstance(value, int):
            warnings.warn("key word arguments for fetch function are specific to sleep parameters")
            warnings.warn("the validation function accepts: min_t, max_t and sleep")
            raise ValueError(f"Sleep argument {key} must be an int")
    min_t: int | None = kwargs.get("min_t")
    max_t: int | None = kwargs.get("max_t")
    sleep: int | None = kwargs.get("sleep")

    if sleep:
        return sleep
    elif (min_t is not None) and (max_t is not None) and (min_t < max_t):
        return randint(min_t, max_t)
    return randint(10, 20)


def validate_params(url: str, **kwargs: int) -> int:
    """
    validates url then sleeping kwargs
    """
    validate_url(url)
    return validate_sleep(**kwargs)
