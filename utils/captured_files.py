from http.client import parse_headers
from io import BytesIO
from pathlib import Path


def content_location(path):
    a = path.read_bytes()
    b = BytesIO(a[:a.index(b'\n\n')])
    return parse_headers(b)['Content-Location']


def delete_headers(path):
    if isinstance(path, str):
        path = Path(path)

    a = path.read_bytes()
    path.write_bytes(a[a.index(b'\n\n') + 2:])
