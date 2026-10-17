#!/usr/bin/env python3
"""Extract the question index from the chapter PDFs (text layer required).

Usage:
  python extract_questions.py --reference-sheet XII.pdf --batch XII=XII.pdf --batch XIII=XIII.pdf \
        [--dpp DPP.pdf] [--qb QB.pdf] --out question_index.json

 * The reference sheet supplies every exercise except JM (J-I, J-II, J-A, C-I, C-II); each --batch sheet supplies its own J-M.
 * Output keys: J-I, J-II, J-A, C-I, C-II, J-M(<batch>), DPP-<n>, QB.  Each question: no, header, stem (English, truncated), opts, ans.
 * Hindi in these PDFs is in a legacy font and comes out garbled; it is dropped. Figures are not read - questions that depend
   on a figure need to be looked at on the page image (pdftoppm) when mapping.
Exercise names can be changed with --patterns patterns.json  ({"J-I": "<regex>", ...}).
"""
import argparse, json, re, subprocess, sys

DEFAULT_PATTERNS = {
    'J-I':  r'Exercise\s*J\s*[-–]\s*I\b(?!I)',
    'J-II': r'Exercise\s*J\s*[-–]\s*II\b',
    'J-M':  r'Exercise\s*J\s*[-–]\s*M\b',
    'J-A':  r'Exercise\s*J\s*[-–]\s*A\b',
    'C-I':  r'Exercise\s*C\s*[-–]\s*I\b(?!I)',
    'C-II': r'Exercise\s*C\s*[-–]\s*II\b',
}
ORDER = ['J-I', 'J-II', 'J-M', 'J-A', 'C-I', 'C-II']
HIN = re.compile(r"(;fn |lehdj|\bds\b|\bdk\b|\brks\b|\bgSa\b|\bgS\b|ekuk |fdl |\bfy;s\b|\bvkSj\b|rFkk|\bgksa|\bdh\b|Åij|\besa\b|fn;k|ijokoy|ewy|dsoy|funZs'k)")


def clean(s): return re.sub(r'\s+', ' ', s).strip()


def pdf_text(path):
    return subprocess.run(['pdftotext', '-layout', path, '-'], capture_output=True, text=True).stdout


def split_questions(text):
    out = []; cur = None; header = ''
    for ln in text.split('\n'):
        if 'MATRIX JEE ACADEMY' in ln or ln.strip().startswith('JEE MAIN QUESTION BANK'): continue
        h = re.match(r'^\s{0,12}(BASED ON[^\n]*|[A-Z][A-Z &/,\-–\(\)0-9]{12,})\s*$', ln)
        if h and not re.match(r'^\s*\d+\.', ln) and 'Exercise' not in ln and 'DPP' not in ln:
            header = clean(h.group(1)); continue
        m = re.match(r'^\s{0,12}(\d{1,3})\.(?:\s+(\S.*))?\s*$', ln)      # the number may stand alone on its line
        if m and (cur is None or int(m.group(1)) == cur[0] + 1):
            if cur: out.append(cur)
            cur = [int(m.group(1)), header, [m.group(2) or '']]
        elif cur:
            cur[2].append(ln)
    if cur: out.append(cur)
    return out


def stem_of(lines):
    eng = []; opts = ''; ans = ''
    for ln in lines:
        s = ln.strip()
        if re.match(r'^Ans\.?', s): ans = clean(re.sub(r'^Ans\.?', '', s))[:40]; break
        if re.match(r'^Sol\.?', s): break
        if HIN.search(s) and not re.search(r'\b(the|of|is|if|then|equal|roots|find|value|number)\b', s, re.I): continue
        if re.match(r'^\(A\)', s):
            if not opts: opts = clean(s)
            continue
        if re.match(r'^\([B-D]\)', s): continue
        eng.append(s)
    return clean(' '.join(eng)), opts, ans


def parse(text, source):
    res = []
    for no, header, blk in split_questions(text):
        st, op, an = stem_of(blk)
        res.append(dict(src=source, no=no, header=header, stem=st[:330], opts=op[:140], ans=an))
    return res


def exercise_regions(text, patterns):
    """start offset of each exercise; a heading counts only if question 1 follows it (skips the contents page)"""
    starts = {}
    for name in ORDER:
        for m in re.finditer(patterns[name], text):
            if re.search(r'\n\s{0,12}1\.\s+\S', text[m.end(): m.end() + 4000]):
                starts[name] = m.start(); break
    found = sorted(starts.items(), key=lambda kv: kv[1])
    regions = {}
    for i, (name, s) in enumerate(found):
        e = found[i + 1][1] if i + 1 < len(found) else len(text)
        regions[name] = text[s:e]
    return regions


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--reference-sheet', required=True); ap.add_argument('--batch', action='append', default=[], help='NAME=sheet.pdf (gives that batch its J-M)')
    ap.add_argument('--dpp'); ap.add_argument('--qb'); ap.add_argument('--patterns'); ap.add_argument('--out', required=True)
    a = ap.parse_args()
    pats = dict(DEFAULT_PATTERNS)
    if a.patterns: pats.update(json.load(open(a.patterns)))
    idx = {}
    ref = exercise_regions(pdf_text(a.reference_sheet), pats)
    for name in ORDER:
        if name == 'J-M': continue
        if name in ref: idx[name] = parse(ref[name], name)
        else: print(f'WARNING: exercise {name} not found in the reference sheet')
    for b in a.batch:
        nm, path = b.split('=', 1)
        reg = exercise_regions(pdf_text(path), pats)
        if 'J-M' in reg: idx[f'J-M({nm})'] = parse(reg['J-M'], f'J-M({nm})')
        else: print(f'WARNING: J-M not found in batch sheet {nm}')
    if a.dpp:
        t = pdf_text(a.dpp); parts = re.split(r'DPP\s*#\s*(\d+)', t)
        for i in range(1, len(parts) - 1, 2):
            idx[f'DPP-{parts[i]}'] = parse(parts[i + 1], f'DPP-{parts[i]}')
    if a.qb: idx['QB'] = parse(pdf_text(a.qb), 'QB')
    json.dump(idx, open(a.out, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print({k: len(v) for k, v in idx.items()})


if __name__ == '__main__':
    main()
