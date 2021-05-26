from setuptools import setup

setup(
    name="scrapetools",
    version="0.1.0",
    description="A library for scraping more easily",
    url="https://github.com/monkeyusage/scrapetools",
    author="monkeyusage",
    author_email="monkeyusage@gmail.com",
    license="MIT",
    packages=["scrapetools"],
    install_requires=[
        "requests",
        "beautifulsoup4",
        "scraperapi-sdk",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.9",
    ],
)
