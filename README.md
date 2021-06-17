# scrapetools
A small wrapper around aiohttp and requests that lets developers use their scraperapi account to make requests

To use it you should save your API KEY inside your environment variable with the name "scraperapi_proxy"


The library expose the "fetch" function from both:
    - the default scrapetools lib -> which is async
    - the sync scapetools lib -> from scrapetools.sync

Defaults are:
    - min_t -> minimum random sleeping time
    - max_t -> maximum random sleeping time
    - sleep -> None
    - scraperapi_proxy -> the name of your apikey in your system environment variables

Install it using "pip install ."

Contributions are welcome!