#!/usr/bin/env python3
r"""tools/capacity.py - what a three phase circuit carries, from arithmetic alone.

    python tools/capacity.py            print the table
    python tools/capacity.py --check    exit 1 if data/capacity.tsv is not what the arithmetic gives

    power (MVA) = 1.732 x voltage (kV) x current (A) / 1000          1.732 is the square root of 3

This is the power that flows at that current. It is NOT a cable rating. What current a buried cable
can carry continuously depends on its size, how it is laid, how its screens are bonded, and the soil,
and is a calculation to IEC 60287 for the real route. This table only turns a current into a power.
"""
import io
import math
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
KV = [11, 33, 66, 132, 275, 400]
AMPS = [400, 630, 800, 1000, 1100, 1200, 1312, 1600, 2000]


def table():
    rows = ['# amps\t' + '\t'.join('%skV_MVA' % v for v in KV)]
    for a in AMPS:
        rows.append('%d\t' % a + '\t'.join('%.1f' % (math.sqrt(3) * v * a / 1000) for v in KV))
    return '\n'.join(rows) + '\n'


def main():
    t, p = table(), os.path.join(ROOT, 'data', 'capacity.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(p) and io.open(p, encoding='utf-8').read() == t
        print('capacity.tsv %s the arithmetic' % ('matches' if ok else 'DOES NOT MATCH'))
        return 0 if ok else 1
    os.makedirs(os.path.dirname(p), exist_ok=True)
    io.open(p, 'w', encoding='utf-8', newline='\n').write(t)
    print(t)
    return 0


if __name__ == '__main__':
    sys.exit(main())
