#!/usr/bin/env python3

from pathlib import Path


def run():
    p = Path()
    part1 = list(p.glob('Captured Files/*.part1.html'))
    part2 = list(p.glob('Captured Files/*.part2.html'))

    if len(part1) == 1 and len(part2) == 1:
        part1 = part1[0]
        part2 = part2[0]
        print(f'Swapping `{part1}` and `{part2}`')
        a = part1.with_suffix('.a')
        part1.rename(a)
        part2.rename(part1)
        a.rename(part2)
        return

    print('Could not find parts')


if __name__ == '__main__':
    run()
