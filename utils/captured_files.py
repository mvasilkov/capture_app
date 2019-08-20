from http.client import parse_headers
from io import BytesIO


def content_location(path):
    a = path.read_bytes()
    b = BytesIO(a[: a.index(b'\n\n')])
    return parse_headers(b)['Content-Location']
