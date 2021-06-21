from scrapetools.validation import (
    validate_url,
    validate_proxy_param,
    validate_kwargs,
    validate_params
)
import pytest

def test_validate_url():
    with pytest.raises(AssertionError):
        validate_url("ftp:\\www.google.com")

def test_validate_proxy_param():
    with pytest.raises(AssertionError):
        API_KEY = None
        validate_proxy_param(True)
        