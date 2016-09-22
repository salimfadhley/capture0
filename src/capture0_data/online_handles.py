import csv
import logging
import pprint
from typing import Set, Optional
from urllib.request import urlopen

import cachetools

HANDLES_URL = "https://docs.google.com/spreadsheets/d/10wfHtH8aq22IElC2xOswYGf0MEHC-6Kq3p8x7qfs0a8/pub?output=csv"

log = logging.getLogger(__name__)

cache = cachetools.TTLCache(1, 500)

class IndexCompany(object):
    def __init__(self, company: str, index: str, handles: Optional[Set[str]], ticker: Optional[str], reddit_positive: Optional[Set[str]],
                 reddit_negative: Optional[Set[str]]):
        self.company = company
        self.index = index
        self.handles = handles
        self.ticker = ticker
        self.reddit_positive = reddit_positive
        self.reddit_negative = reddit_negative

    @staticmethod
    def split_keywords(keyword_string: str) -> Set[str]:
        keywords = [k.strip() for k in keyword_string.split(";")]

        return {k for k in keywords if k}

    @classmethod
    def build_from_row(cls, row):

        handle_columns = {v for k,v in row.items() if (v and "handle" in k.lower())}
        handles = {h.strip().lstrip("@") for hc in handle_columns for h in hc.split(",")}
        ticker = row["Ticker"]

        return cls(
            company=row["Company Name"],
            index=row["Sub Index"],
            handles=handles,
            ticker=ticker,
            reddit_positive=cls.split_keywords(row["Reddit Positive"]),
            reddit_negative=cls.split_keywords(row["Reddit Negative"]),
        )

    def __str__(self)->str:
        return "Company: {company}({ticker}), index: {index}, handles: {handles} reddit: {reddit_positive}/{reddit_negative}".format(**self.__dict__)

    def __repr__(self)->str:
        return "<%s.%s %s" % (self.__class__.__module__, self.__class__.__name__, str(self))


def csv_lines():
    with urlopen(HANDLES_URL) as f:
        for line in f:
            yield line.decode("utf-8")


def get_companies():
    log.warn("Cache has expired... fetching companies.")
    return list(get_companies_generator())


@cachetools.cached(cache)
def get_companies_generator():
    reader = csv.DictReader(csv_lines())
    for row in reader:
        yield (IndexCompany.build_from_row(row))


if __name__ == "__main__":
    import sys
    print(sys.version)
    for c in get_companies():
        pprint.pprint(c)

