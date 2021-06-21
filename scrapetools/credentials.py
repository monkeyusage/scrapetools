"""
retrieves API_KEY from os environment variables
"""
from __future__ import annotations

from os import environ, mkdir, path
from warnings import warn

API_KEY = environ.get("scraperapi_proxy")
if API_KEY is None:
    warn(
        """
        Did not find proxy secret key
        environment variable <scraperapi_proxy> inside the system
        you'll be using your own IP for the requests you make
    """
    )


if not path.exists("debug"):
    mkdir("debug")
