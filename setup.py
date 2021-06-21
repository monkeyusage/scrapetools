from setuptools import setup

setup(
    name="scrapetools",
    version="0.3.1",
    description="A library for easy scraping",
    url="https://github.com/monkeyusage/scrapetools",
    author="monkeyusage",
    author_email="monkeyusage@gmail.com",
    license="MIT",
    packages=["scrapetools", "scrapetools.sync"],
    install_requires=["requests", "beautifulsoup4", "scraperapi-sdk", "aiohttp"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.9",
    ],
)
