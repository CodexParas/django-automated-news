# Download market data from Yahoo! Finance's API
    
<table border=1 cellpadding=10><tr><td>

#### \*\*\* IMPORTANT LEGAL DISCLAIMER \*\*\*

---

**Yahoo!, Y!Finance, and Yahoo! finance are registered trademarks of
Yahoo, Inc.**

yfinance is **not** affiliated, endorsed, or vetted by Yahoo, Inc. It's
an open-source tool that uses Yahoo's publicly available APIs, and is
intended for research and educational purposes.

**You should refer to Yahoo!'s terms of use**
([here](https://policies.yahoo.com/us/en/yahoo/terms/product-atos/apiforydn/index.htm),
[here](https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html), and
[here](https://policies.yahoo.com/us/en/yahoo/terms/index.htm)) **for
details on your rights to use the actual data downloaded. Remember - the
Yahoo! finance API is intended for personal use only.**

</td></tr></table>


<a target="new" href="https://pypi.python.org/pypi/yfinance"><img border=0 src="https://img.shields.io/badge/python-2.7,%203.6+-blue.svg?style=flat" alt="Python version"></a>
<a target="new" href="https://pypi.python.org/pypi/yfinance"><img border=0 src="https://img.shields.io/pypi/v/yfinance.svg?maxAge=60%" alt="PyPi version"></a>
<a target="new" href="https://pypi.python.org/pypi/yfinance"><img border=0 src="https://img.shields.io/pypi/status/yfinance.svg?maxAge=60" alt="PyPi status"></a>
<a target="new" href="https://pypi.python.org/pypi/yfinance"><img border=0 src="https://img.shields.io/pypi/dm/yfinance.svg?maxAge=2592000&label=installs&color=%2327B1FF" alt="PyPi downloads"></a>
<a target="new" href="https://travis-ci.com/github/ranaroussi/yfinance"><img border=0 src="https://img.shields.io/travis/ranaroussi/yfinance/main.svg?maxAge=1" alt="Travis-CI build status"></a>
<a target="new" href="https://www.codefactor.io/repository/github/ranaroussi/yfinance"><img border=0 src="https://www.codefactor.io/repository/github/ranaroussi/yfinance/badge" alt="CodeFactor"></a>
<a target="new" href="https://github.com/ranaroussi/yfinance"><img border=0 src="https://img.shields.io/github/stars/ranaroussi/yfinance.svg?style=social&label=Star&maxAge=60" alt="Star this repo"></a>
<a target="new" href="https://twitter.com/aroussi"><img border=0 src="https://img.shields.io/twitter/follow/aroussi.svg?style=social&label=Follow&maxAge=60" alt="Follow me on twitter"></a>


**yfinance** offers a threaded and Pythonic way to download market data from [Yahoo!Ⓡ finance](https://finance.yahoo.com).

→ Check out this [Blog post](https://aroussi.com/#post/python-yahoo-finance) for a detailed tutorial with code examples.

[Changelog »](https://github.com/ranaroussi/yfinance/blob/main/CHANGELOG.rst)

---

## Quick Start

### The Ticker module

The `Ticker` module, which allows you to access ticker data in a more Pythonic way:

If you want to use a proxy server for downloading data, use:

### Multiple tickers

To initialize multiple `Ticker` objects, use

To download price history into one table:

#### `yf.download()` and `Ticker.history()` have many options for configuring fetching and processing. [Review the Wiki](https://github.com/ranaroussi/yfinance/wiki) for more options and detail.

### Logging

`yfinance` now uses the `logging` module to handle messages, default behaviour is only print errors. If debugging, use `yf.enable_debug_mode()` to switch logging to debug with custom formatting.

### Smarter scraping

To use a custom `requests` session (for example to cache calls to the
API or customize the `User-agent` header), pass a `session=` argument to
the Ticker constructor.

Combine a `requests_cache` with rate-limiting to avoid triggering Yahoo's rate-limiter/blocker that can corrupt data.

### Managing Multi-Level Columns

The following answer on Stack Overflow is for [How to deal with
multi-level column names downloaded with
yfinance?](https://stackoverflow.com/questions/63107801)

-   `yfinance` returns a `pandas.DataFrame` with multi-level column
    names, with a level for the ticker and a level for the stock price
    data
    -   The answer discusses:
        -   How to correctly read the the multi-level columns after
            saving the dataframe to a csv with `pandas.DataFrame.to_csv`
        -   How to download single or multiple tickers into a single
            dataframe with single level column names and a ticker column

### `pandas_datareader` override

If your code uses `pandas_datareader` and you want to download data
faster, you can "hijack" `pandas_datareader.data.get_data_yahoo()`
method to use **yfinance** while making sure the returned data is in the
same format as **pandas\_datareader**'s `get_data_yahoo()`.


### Timezone cache store

When fetching price data, all dates are localized to stock exchange timezone. 
But timezone retrieval is relatively slow, so yfinance attemps to cache them 
in your users cache folder. 
You can direct cache to use a different location with `set_tz_cache_location()`:

---
### Requirements

-   [Python](https://www.python.org) \>= 2.7, 3.4+
-   [Pandas](https://github.com/pydata/pandas) \>= 1.3.0
-   [Numpy](http://www.numpy.org) \>= 1.16.5
-   [requests](http://docs.python-requests.org/en/master) \>= 2.31
-   [lxml](https://pypi.org/project/lxml) \>= 4.9.1
-   [appdirs](https://pypi.org/project/appdirs) \>= 1.4.4
-   [pytz](https://pypi.org/project/pytz) \>=2022.5
-   [frozendict](https://pypi.org/project/frozendict) \>= 2.3.4
-   [beautifulsoup4](https://pypi.org/project/beautifulsoup4) \>= 4.11.1
-   [html5lib](https://pypi.org/project/html5lib) \>= 1.1
-   [peewee](https://pypi.org/project/peewee)  \>= 3.16.2

---
## Installation

Install `yfinance` using `pip`:

``` {.sourceCode .bash}
$ pip install yfinance --upgrade --no-cache-dir
```

Test new features by installing betas, provide feedback in [corresponding Discussion](https://github.com/ranaroussi/yfinance/discussions):
``` {.sourceCode .bash}
$ pip install yfinance --upgrade --no-cache-dir --pre
```

To install `yfinance` using `conda`, see
[this](https://anaconda.org/ranaroussi/yfinance).



---

### P.S.

Please drop me an note with any feedback you have.

**Ran Aroussi**