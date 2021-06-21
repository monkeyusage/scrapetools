from scrapetools.validation import (
    validate_url,
    validate_kwargs,
    get_sleeping_time,
)
import pytest


def test_validate_url() -> None:
    with pytest.raises(AssertionError):
        validate_url("ftp:\\www.google.com")

    with pytest.raises(AssertionError):
        validate_url("")


def test_validate_kwargs() -> None:
    with pytest.raises(AssertionError):
        validate_kwargs(some_unallowed_argument=3)


def test_get_sleeping_time() -> None:
    assert get_sleeping_time(sleep=10) == 10
    assert 21 > get_sleeping_time() > 9
    with pytest.raises(AssertionError):
        get_sleeping_time(min_t=100, max_t=5)
