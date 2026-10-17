#!/usr/bin/env python3
"""Search the all-chapters Quick Review for a concept (cross-chapter coverage check).

Usage: python search_master.py master_index.json "modulus" "composite function" ...
Each argument is one query; a prompt/heading matches when ALL words of the query appear in it (case-insensitive).
Add --any to match any word. Prints chapter / heading / prompt number / text.

Rule used by the kit: if a concept is already an item (or heading) in ANOTHER chapter's Quick Review, it is NOT added to this chapter.
"""
import json, re, sys

def main():
    args = [a for a in sys.argv[1:] if a != '--any']; anyw = '--any' in sys.argv
    idx = json.load(open(args[0], encoding='utf-8'))
    for q in args[1:]:
        words = [w.lower() for w in re.split(r'\s+', q.strip()) if w]
        print(f'=== "{q}"'); n = 0
        for ch in idx['chapters']:
            for h in ch['headings']:
                for it in [dict(no='', text='(heading)')] + h['items']:
                    hay = (h['title'] + ' ' + it['text']).lower()
                    if (any if anyw else all)(w in hay for w in words):
                        print(f"  {ch['title']} | {h['title'][:40]} | {it['no']} {it['text'][:110]}"); n += 1
                        if it['no'] == '': break
        if not n: print('  (no match in any chapter)')

if __name__ == '__main__':
    main()
