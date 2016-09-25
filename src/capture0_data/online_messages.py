import csv
import functools
import logging
import pprint
from collections import Mapping

import markdown
from capture0_data.utils import csv_lines

MESSAGES_URL = "https://docs.google.com/spreadsheets/d/103yky1HqNULD2awB4aZvzazSO8i-aVONWVa5C66XzBo/pub?gid=555715211&single=true&output=csv"

log = logging.getLogger(__name__)


class Messages(object):
    def __init__(self, messages: Mapping):
        self.messages = messages

    def get(self, k: str) -> str:
        try:
            return self.messages[k].md()
        except KeyError:
            return "no message: %s" % k


class Message(object):
    def __init__(self, key: str, message: str):
        self.key = key
        self.message = message

    @classmethod
    def build_from_row(cls, row) -> "Message":
        return cls(row["key"], row["message"])

    def md(self) -> str:
        return markdown.markdown(self.message)

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return "<%s.%s %s>" % (self.__class__.__module__, self.__class__.__name__, str(self))


def get_messages_generator(url):
    reader = csv.DictReader(csv_lines(url))
    for row in reader:
        m = Message.build_from_row(row)
        yield (m.key, m)


@functools.lru_cache(1)
def get_messages(url=MESSAGES_URL):
    log.warn("Cache has expired... fetching companies.")
    return Messages(dict(get_messages_generator(url)))


if __name__ == "__main__":
    import sys

    print(sys.version)
    for k, m in get_messages().messages.items():
        pprint.pprint("%s => %s" % (k, m.md()))
