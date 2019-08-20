#!/usr/bin/env python3

from pathlib import Path

from .captured_files import content_location


def swap_part1_2():
    p = Path()
    part1 = list(p.glob('Captured Files/*.part1.html'))
    part2 = list(p.glob('Captured Files/*.part2.html'))

    if len(part1) == 1 and len(part2) == 1:
        part1 = part1[0]
        part2 = part2[0]
        loc1 = content_location(part1)
        loc2 = content_location(part2)

        if loc1.endswith('?') or not loc2.endswith('?'):
            print(f'Not swapping `{part1}` and `{part2}`')
            return

        print(f'Swapping `{part1}` and `{part2}`')
        a = part1.with_suffix('.a')
        part1.rename(a)
        part2.rename(part1)
        a.rename(part2)
        return

    print('Could not find parts')


if __name__ == '__main__':
    swap_part1_2()
