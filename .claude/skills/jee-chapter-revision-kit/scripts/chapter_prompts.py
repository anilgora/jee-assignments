#!/usr/bin/env python3
"""Pull ONE chapter's prompt list out of the master index.

Usage:
  python chapter_prompts.py master_index.json --list                      # chapter names
  python chapter_prompts.py master_index.json "Quadratic Equation" --out DIR [--pdf master.pdf]
Writes DIR/<chapter>_prompts.json (headings + numbered prompts, ready to become the spec's quick_review items) and, when --pdf is given,
PNGs of the chapter's pages (DIR/page-NN.png) so math-heavy prompts can be read from the image - the OCR text is only reliable for plain words.
"""
import argparse, json, os, re, subprocess, sys

ap = argparse.ArgumentParser()
ap.add_argument('index'); ap.add_argument('chapter', nargs='?'); ap.add_argument('--list', action='store_true'); ap.add_argument('--out'); ap.add_argument('--pdf')
a = ap.parse_args()
idx = json.load(open(a.index, encoding='utf-8'))
if a.list or not a.chapter:
    for c in idx['chapters']:
        print(f"{c['title']:40s} pages {c['pages'][0]}-{c['pages'][1]}  prompts {sum(len(h['items']) for h in c['headings'])}")
    sys.exit(0)
names = {c['title'].lower(): c for c in idx['chapters']}
ch = names.get(a.chapter.lower()) or next((c for k, c in names.items() if a.chapter.lower() in k), None)
if ch is None: sys.exit(f"chapter '{a.chapter}' not in the index; known: {[c['title'] for c in idx['chapters']]}")
os.makedirs(a.out, exist_ok=True)
slug = re.sub(r'[^A-Za-z0-9]+', '_', ch['title']).strip('_')
out = dict(chapter=ch['title'], unit=ch.get('unit', ''), pages=ch['pages'], headings=ch['headings'])
json.dump(out, open(os.path.join(a.out, f'{slug}_prompts.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"{ch['title']}: {sum(len(h['items']) for h in ch['headings'])} prompts in {len(ch['headings'])} headings, master pages {ch['pages'][0]}-{ch['pages'][1]}")
if a.pdf:
    subprocess.run(['pdftoppm', '-r', '110', '-f', str(ch['pages'][0]), '-l', str(ch['pages'][1]), '-png', a.pdf, os.path.join(a.out, 'page')], check=True)
    print('page images written to', a.out)
