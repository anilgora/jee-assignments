#!/usr/bin/env python3
"""Step 5b. Print every question stem and options for the stem review.

Usage:  python review_stems.py PAPER_DIR

Read each English stem as a student seeing it for the first time and answer, per question:
  1. Is every symbol and function introduced (name, domain, meaning)?
  2. Is every condition stated (quantifiers, intervals, signs, "largest", "distinct")?
  3. Is there only one way to read each sentence?
  4. Is the answer unique and does it match the Answer Plan?
  5. Do the options have one form, and is the Hindi a faithful mirror?
Fix problems in the question files, then record the result in each question's "stem_review" field
(at least one sentence; say what you checked and anything you changed). build_paper.py refuses a question
without it.
"""
import json, os, re, sys

def main():
    d = sys.argv[1]
    files = sorted(f for f in os.listdir(d) if re.match(r'q\d+\.json$', f))
    for f in files:
        q = json.load(open(os.path.join(d, f), encoding='utf-8'))
        print('=' * 78)
        print(f"{f[:-5].upper()}  {q.get('type')}  plan: {q.get('answer_plan', '-')}")
        for l in q.get('english', []):
            print('  ' + l)
        print('  --- review: symbols defined? conditions complete? one reading? answer unique? options one form?')
        if q.get('stem_review'):
            print('  recorded:', q['stem_review'])
    print('=' * 78)

if __name__ == '__main__':
    main()
