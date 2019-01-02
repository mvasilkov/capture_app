from collections import defaultdict
from pathlib import Path, PurePath
from urllib.parse import urlparse

from mitmproxy import http

from capture import Capture
from utils import dont_google

GOOD_ORIGIN = dont_google('uggcf://ernqre.obbxzngr.pbz/')
GOOD_PATH = dont_google('/pbagragf/')


def good_addr(a: str):
    return a.startswith(GOOD_ORIGIN) and GOOD_PATH in a


def good_type(a: str):
    return a == 'text/html' or a.startswith('image/')


def get_name(a: str):
    return PurePath(urlparse(a).path).name


def get_key(a: str):
    return a[len(GOOD_ORIGIN):a.index(GOOD_PATH)]


class CaptureParts(Capture):
    def __init__(self):
        super().__init__()

        self.counters = defaultdict(int)

    def should_capture(self, flow: http.HTTPFlow):
        content_type = flow.response.headers.get('content-type', 'unknown content type')
        if good_addr(flow.request.url) and good_type(content_type):
            if content_type != 'text/html':
                return get_name(flow.request.url)

            key = get_key(flow.request.url)
            self.counters[key] += 1

            assert 'referer' in flow.request.headers
            return get_name(flow.request.headers['referer']) + f'.part{self.counters[key]}.html'

        return None


addons = [CaptureParts()]
