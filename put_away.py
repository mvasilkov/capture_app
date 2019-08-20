#!/usr/bin/env python3

from pathlib import Path
import re

from utils.encodings import dont_google
from utils.swap_part1_2 import swap_part1_2

MOVE_PATH = dont_google('q0n6rzpx2op')


def put_away():
    a = Path('Captured Files').resolve()
    b = Path('../ru-RU').resolve() / MOVE_PATH
    assert a.exists(), f'Folder not found: {a}'
    assert b.exists(), f'Folder not found: {b}'

    author_title = input('author_title? ')
    pair = re.match('(.+)«(.+)»', author_title)
    if pair:
        author, title = pair.groups()
    else:
        author = author_title
        title = input('title? ')

    author = author.strip()
    title = title.strip()
    assert author and title, 'Author and title cannot be empty'

    print('---')
    print(f"Author = '{author}'")
    print(f"Title = '{title}'")

    _continue = input('Continue? ')
    if _continue.strip() not in {'yes', 'y'}:
        print('Interrupted by user')
        return

    swap_part1_2()
    (b / author).mkdir(exist_ok=True)
    a.rename(b / author / title)


if __name__ == '__main__':
    put_away()
