#!/usr/bin/env python3
"""Find Question Bank questions that are the same as a batch's JM questions (they must be counted once).

Usage: python detect_overlaps.py question_index.json  -> prints, per J-M(<batch>), the QB numbers that look identical.
Similarity is on the English stem letters/digits (maths symbols are lost in the PDF text, so the threshold is low) plus the
answer letter; always eyeball the candidates before putting them in the spec ("qb_overlap").
"""
import json, re, sys, difflib


def norm(s): return re.sub(r'[^a-z0-9]', '', s.lower())


def main(path):
    idx = json.load(open(path, encoding='utf-8'))
    if 'QB' not in idx: print('no QB in index'); return
    res = {}
    for src, qs in idx.items():
        if not src.startswith('J-M('): continue
        batch = src[4:-1]; hits = []
        for qb in idx['QB']:
            best = max(((difflib.SequenceMatcher(None, norm(qb['stem']), norm(q['stem'])).ratio(), q) for q in qs), key=lambda t: t[0], default=(0, None))
            if best[0] >= 0.6:
                hits.append((qb['no'], best[1]['no'], round(best[0], 2)))
        res[batch] = hits
        print(f'batch {batch}: QB question -> {src} question (similarity)')
        for h in hits: print('  ', h, 'LIKELY SAME' if h[2] >= 0.76 else 'possible - check by eye')
    print('suggested qb_overlap:', json.dumps({b: [h[0] for h in hs if h[2] >= 0.76] for b, hs in res.items()}))


if __name__ == '__main__':
    main(sys.argv[1])
