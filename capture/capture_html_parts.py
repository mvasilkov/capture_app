from collections import defaultdict
from pathlib import Path, PurePath
from urllib.parse import urlparse, urlunparse

from mitmproxy import http

from capture import Capture
from utils.encodings import dont_google

GOOD_ORIGIN = dont_google('uggcf://ernqre.obbxzngr.pbz/-')
GOOD_PATH = dont_google('/pbagragf/-')


def good_addr(a: str):
    return a.startswith(GOOD_ORIGIN) and GOOD_PATH in a


def good_type(a: str):
    return a == 'text/html' or a.startswith('image/')


def get_canon_addr(a: str):
    return urlunparse(urlparse(a))


def get_name(a: str):
    return PurePath(urlparse(a).path).name


def get_key(a: str):
    return a[len(GOOD_ORIGIN):a.index(GOOD_PATH)]


class CaptureParts(Capture):
    def __init__(self):
        super().__init__()

        self.counters = defaultdict(int)
        self.addr_part = dict()
        self.captured_pages = set()

    def request(self, flow: http.HTTPFlow):
        canon_addr: str = get_canon_addr(flow.request.url)
        if (good_addr(canon_addr) and canon_addr.endswith('.html')
                and canon_addr not in self.addr_part):
            key = get_key(canon_addr)
            self.counters[key] += 1
            self.addr_part[canon_addr] = f'.part{self.counters[key]}.html'

    def should_capture(self, flow: http.HTTPFlow):
        content_type = flow.response.headers.get('content-type', 'unknown content type')
        canon_addr = get_canon_addr(flow.request.url)
        if (good_addr(canon_addr) and good_type(content_type)
                and canon_addr not in self.captured_pages):
            self.captured_pages.add(canon_addr)

            if content_type != 'text/html':
                return get_name(canon_addr)

            assert 'referer' in flow.request.headers
            assert canon_addr in self.addr_part
            return get_name(flow.request.headers['referer']) + self.addr_part[canon_addr]

        return None


addons = [CaptureParts()]
