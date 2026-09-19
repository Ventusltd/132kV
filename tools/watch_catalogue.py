#!/usr/bin/env python3
r"""tools/watch_catalogue.py - which public datasets describe the 132 kV network, and when do they change.

    python tools/watch_catalogue.py [--dry]

Asks a network operator's PUBLIC open data catalogue one question: which datasets mention 132 kV.
It records only what the catalogue itself publishes about each dataset: its identifier, title,
licence, number of records and the date it was last modified. IT COPIES NO RECORDS. Some of these
datasets are under CC BY 4.0 and some under the operator's own shared data licence; the facts that a
dataset exists, how many records it has and when it changed are recorded for both, and nothing else.

    data/catalogue.tsv   the catalogue as it stands now, one row per dataset
    data/ledger.tsv      APPEND ONLY: one row each time a dataset's record count or modified date changes
    NOW.md               rebuilt from the two, newest change first

WHY THE COUNT MATTERS. The number of records in the 132 kV underground cable dataset is the number of
cable sections the operator has mapped. When it rises, cable has gone in the ground, and roughly a
quarter of a gigawatt of capacity comes with each circuit (see tools/capacity.py).

SAFEGUARDS. No key, no login, public catalogue only. Everything about to be written passes the digest
guard first. If the catalogue does not answer, nothing is written: no answer is not no change.
"""
import io
import json
import os
import sys
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
sys.path.insert(0, os.environ.get('KB_TOOLS', os.path.join(ROOT, 'kb', 'tools')))
from check_proof import leaks

PORTAL = 'https://ukpowernetworks.opendatasoft.com'
SOURCE = 'UK Power Networks Open Data Portal'
QUERY = 'search("132kv")'


def catalogue():
    out, offset = [], 0
    while True:
        url = PORTAL + '/api/explore/v2.1/catalog/datasets?' + urllib.parse.urlencode({'where': QUERY, 'limit': 100, 'offset': offset})
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': '132kV-public-data'}), timeout=60))
        for r in d.get('results', []):
            m = r.get('metas', {}).get('default', {})
            out.append((r['dataset_id'], (m.get('title') or '').replace('\t', ' '), (m.get('license') or 'not stated').replace('\t', ' '),
                        int(m.get('records_count') or 0), (m.get('modified') or '')[:19]))
        offset += 100
        if offset >= d.get('total_count', 0):
            return sorted(out)


def last(path):
    seen = {}
    if os.path.exists(path):
        for l in io.open(path, encoding='utf-8'):
            if l.strip() and l[0] != '#':
                c = l.rstrip('\n').split('\t')
                seen[c[1]] = (int(c[2]), c[3])
    return seen


def main():
    dry = '--dry' in sys.argv
    try:
        rows = catalogue()
    except Exception as e:
        print('FAIL: the catalogue did not answer (%s); nothing written' % type(e).__name__)
        return 1
    if not rows:
        print('FAIL: the catalogue answered with nothing; nothing written')
        return 1
    os.makedirs(os.path.join(ROOT, 'data'), exist_ok=True)
    lp = os.path.join(ROOT, 'data', 'ledger.tsv')
    known, now = last(lp), int(time.time())
    changed = [r for r in rows if known.get(r[0]) != (r[3], r[4])]
    add = ''.join('%d\t%s\t%d\t%s\t%s\n' % (now, r[0], r[3], r[4],
                  ('first seen' if r[0] not in known else 'records %+d' % (r[3] - known[r[0]][0]))) for r in changed)
    cat = '# dataset\ttitle\tlicence\trecords\tmodified\n' + ''.join('%s\t%s\t%s\t%d\t%s\n' % r for r in rows)
    md = ['# NOW', '', 'Rebuilt by `tools/watch_catalogue.py`. Source: %s, %s. Catalogue facts only; no records are copied.' % (SOURCE, PORTAL), '',
          '| dataset | records | last modified | licence |', '|---|---:|---|---|']
    for r in sorted(rows, key=lambda r: r[4], reverse=True):
        md.append('| [%s](%s/explore/dataset/%s/) | %s | %s | %s |' % (r[1], PORTAL, r[0], format(r[3], ','), r[4][:10], r[2]))
    md = '\n'.join(md) + '\n'
    if leaks(cat + add + md):
        print('REFUSED: a private digest matched; nothing written')
        return 2
    print('%d datasets mention 132 kV; %d changed since last seen' % (len(rows), len(changed)))
    for r in rows:
        if '132kv' in r[0]:
            print('  %-58s %10s records  modified %s' % (r[0], format(r[3], ','), r[4][:10]))
    if dry:
        print('dry run: nothing written')
        return 0
    io.open(os.path.join(ROOT, 'data', 'catalogue.tsv'), 'w', encoding='utf-8', newline='\n').write(cat)
    if not os.path.exists(lp):
        io.open(lp, 'w', encoding='utf-8', newline='\n').write('# seen_unix\tdataset\trecords\tmodified\twhat_changed\n')
    if add:
        io.open(lp, 'a', encoding='utf-8', newline='\n').write(add)
    io.open(os.path.join(ROOT, 'NOW.md'), 'w', encoding='utf-8', newline='\n').write(md)
    return 0


if __name__ == '__main__':
    sys.exit(main())
