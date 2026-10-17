#!/usr/bin/env python3
"""Split the all-chapters Quick Review (one PDF, usually a scan) into a per-chapter prompt index.

Usage:
  python split_master.py --pdf master.pdf --out master_index.json [--workdir DIR] [--dpi 200]
  python split_master.py --ocr-dir DIR --out master_index.json        # reuse OCR output made earlier (pg-NN.png.tsv files)

Layout assumed (same for every chapter): a centred chapter title (the first chapter of a unit also has a larger unit title above it), then
bold topic headings at the left margin and numbered prompts ("1. ...") whose wrapped lines are indented. Numbering restarts at 1 per chapter.
Output JSON: {"chapters": [{"unit","title","pages":[first,last],"headings":[{"title","items":[{"no","text"}]}]}], "warnings": [...]}
Also writes <out>.review.md: a readable listing per chapter with warnings (number gaps, low-confidence OCR lines) to check once by eye.
Text-layer PDFs are handled through `pdftotext -bbox-layout`; scans are OCR'd with tesseract (needs `tesseract`, `pdftoppm`; ~4 s/page on one CPU).
"""
import argparse, csv, collections, glob, json, os, re, statistics, subprocess, sys, tempfile
import xml.etree.ElementTree as ET


# ------------------------------------------------------------------ page lines (left, top, width, height, text, conf)
def has_text_layer(pdf):
    out = subprocess.run(['pdffonts', pdf], capture_output=True, text=True).stdout.strip().split('\n')
    return len(out) > 2


def lines_from_tsv(path):
    rows = list(csv.DictReader(open(path, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE))
    W = H = 0; words = []
    for r in rows:
        if r['level'] == '1': W, H = int(r['width']), int(r['height'])
        if r['level'] == '5' and r['text'].strip():
            words.append(dict(text=r['text'], left=int(r['left']), top=int(r['top']), w=int(r['width']), h=int(r['height']), conf=float(r['conf'])))
    if not words: return [], W, H
    med = statistics.median(w['h'] for w in words)
    words.sort(key=lambda w: (w['top'] + w['h'] / 2, w['left']))
    rowsw = []
    for w in words:                                    # cluster words into rows by vertical centre
        cy = w['top'] + w['h'] / 2
        if rowsw and abs(cy - rowsw[-1]['cy']) <= 0.6 * med:
            rowsw[-1]['ws'].append(w); rowsw[-1]['cy'] = statistics.mean(x['top'] + x['h'] / 2 for x in rowsw[-1]['ws'])
        else:
            rowsw.append(dict(cy=cy, ws=[w]))
    out = []
    for r in rowsw:
        ws = sorted(r['ws'], key=lambda w: w['left'])
        confs = [w['conf'] for w in ws if w['conf'] >= 0]
        out.append(dict(text=' '.join(w['text'] for w in ws), left=ws[0]['left'], width=ws[-1]['left'] + ws[-1]['w'] - ws[0]['left'],
                        top=min(w['top'] for w in ws), h=max(w['h'] for w in ws), conf=statistics.mean(confs) if confs else 0))
    return out, W, H


def lines_from_bbox(pdf, page):
    x = subprocess.run(['pdftotext', '-bbox-layout', '-f', str(page), '-l', str(page), pdf, '-'], capture_output=True, text=True).stdout
    x = re.sub(r'<!DOCTYPE[^>]*>', '', x); x = re.sub(r'xmlns="[^"]+"', '', x)
    root = ET.fromstring(x); pg = root.find('.//page'); W, H = float(pg.get('width')), float(pg.get('height'))
    out = []
    for ln in root.iter('line'):
        words = [w.text or '' for w in ln.iter('word')]
        x0, x1, y0, y1 = (float(ln.get(k)) for k in ('xMin', 'xMax', 'yMin', 'yMax'))
        out.append(dict(text=' '.join(words), left=x0, width=x1 - x0, top=y0, h=y1 - y0, conf=100))
    return out, W, H


# ------------------------------------------------------------------ build the index
NUM = re.compile(r'^\s*(\d{1,3})\s*[.,)]\s*(.*)$')
GARBLED_NUM = re.compile(r'^\s*([A-Za-z|!]{1,2}\d?|\d[A-Za-z|!]{1,2})\.\s+([A-Z][a-z]+(?:\s+\S+){3,})$')   # '74.' read as 'TA.' / '7A.'


def build(pages):
    """pages: list of (pageno, lines, W, H)"""
    chapters = []; warnings = []; cur = None; head = None; item = None; last_ch_no = 0
    pending_unit = ''
    for pno, lines, W, H in pages:
        lines = [l for l in lines if 'MATRIX JEE ACADEMY' not in l['text'] and 'matrixedu' not in l['text'].lower()]
        if not lines: continue
        med = statistics.median(l['h'] for l in lines)
        # indent reference: left margin = most common left among lines that start with a number or are headings
        lefts = sorted(l['left'] for l in lines)
        margin = statistics.median(lefts[:max(3, len(lefts) // 3)])
        chapters_started_on_page = False
        for l in lines:
            t = re.sub(r'\s+', ' ', l['text']).strip()
            if not t: continue
            center = (l['left'] + l['width'] / 2) / W
            letters = len(re.findall(r'[A-Za-z]', t))
            is_title = (l['left'] > 0.25 * W and 0.33 <= center <= 0.67 and l['top'] < 0.30 * H
                        and re.fullmatch(r'[A-Za-z][A-Za-z0-9 &:\-]{2,45}', t) is not None and len(t.split()) <= 6)
            if is_title and cur is not None and not cur['headings'] and cur['pages'][0] == pno:
                continue                                        # second title line / subtitle of the chapter just started
            if is_title:
                if l['h'] >= 1.40 * med and not chapters_started_on_page:      # unit title (Algebra, Calculus ...), informational only
                    if re.fullmatch(r"[A-Za-z][A-Za-z &]{4,40}", t): pending_unit = t
                    continue
                cur = dict(unit=pending_unit or (chapters[-1]['unit'] if chapters else ''), title=t, pages=[pno, pno], headings=[])
                chapters.append(cur); head = None; item = None; chapters_started_on_page = True; last_ch_no = 0
                pending_unit = ''
                continue
            if cur is None: continue
            cur['pages'][1] = pno
            m = NUM.match(t)
            last_no = last_ch_no
            if not m and cur is not None and l['left'] < margin + 0.025 * W:
                g = GARBLED_NUM.match(t)
                if g: m = re.match(r'(\d+)(.*)', f"{last_no + 1}. {g.group(2)}"); m = type('M', (), {'group': lambda self, k, _m=m: _m.group(k)})()
            if m and (l['left'] < margin + 0.025 * W or int(m.group(1)) == last_no + 1):
                no = int(m.group(1))
                if head is None:
                    head = dict(title='', items=[]); cur['headings'].append(head)
                item = dict(no=no, text=m.group(2).strip(), conf=round(l['conf']), rows=[m.group(2).strip()])
                head['items'].append(item); last_ch_no = no
            elif l['left'] > margin + 0.020 * W and item is not None:      # wrapped line of the previous prompt
                item['text'] += ' ' + t; item['rows'].append(t); item['conf'] = min(item['conf'], round(l['conf']))
            elif letters < 3 or (cur and t.lower() == cur['title'].lower()):    # stray maths fragment / repeated chapter title
                if item is not None and letters < 3 and l['h'] >= 0.7 * med: item['text'] += ' ' + t
            else:                                                          # topic heading
                head = dict(title=t, items=[]); cur['headings'].append(head); item = None
                if re.match(r'extra reading', t, re.I): last_ch_no = 0
    # checks
    for ch in chapters:
        seq = []; segs = [[]]
        for h in ch['headings']:
            if re.match(r'extra reading', h['title'], re.I) and segs[-1]: segs.append([])
            segs[-1] += [i['no'] for i in h['items']]
        for k, nos in enumerate(segs):
            exp = list(range(1, len(nos) + 1))
            if nos != exp:
                gaps = [(a, b) for a, b in zip(exp, nos) if a != b][:4]
                warnings.append(f"{ch['title']}{'' if len(segs) == 1 else f' (part {k+1})'}: numbering is not 1..{len(nos)} (first mismatches: {gaps})")
        for h in ch['headings']:
            if not h['items']: warnings.append(f"{ch['title']}: heading '{h['title']}' has no prompts")
            for i in h['items']:
                if i['conf'] < 80: warnings.append(f"{ch['title']} #{i['no']}: low OCR confidence ({i['conf']}) - check by eye")
    renumber(chapters)
    return dict(chapters=chapters, warnings=warnings)


def renumber(chapters):
    """sequential numbering inside each chapter (restarting after an 'Extra Reading Material' heading); the printed number is kept when it differs"""
    for ch in chapters:
        n = 0
        for h in ch['headings']:
            if re.match(r'extra reading', h['title'], re.I): n = 0
            for i in h['items']:
                n += 1
                if i.get('no') != n: i['printed_no'] = i.get('printed_no', i.get('no')); i['no'] = n
                i.pop('conf', None); i.pop('rows', None)


def apply_corrections(idx, corrections):
    """corrections: list of {"chapter","op",...}.  ops: set_text(no,text) | split_item(no,keep,new) | merge_heading(heading,into) | set_heading(old,new)"""
    done = []
    for c in corrections:
        ch = next((x for x in idx['chapters'] if x['title'] == c['chapter']), None)
        if ch is None: done.append(f"corrections: chapter {c['chapter']} not found"); continue
        op = c['op']
        if op in ('set_text', 'split_item'):
            hit = [(h, k) for h in ch['headings'] for k, i in enumerate(h['items']) if i['no'] == c['no']]
            if not hit: done.append(f"corrections: {c['chapter']} item {c['no']} not found"); continue
            h, k = hit[0]
            if op == 'set_text': h['items'][k]['text'] = c['text']
            else:
                h['items'][k]['text'] = c['keep']; h['items'].insert(k + 1, dict(no=0, text=c['new']))
        elif op == 'merge_heading':
            src = next((h for h in ch['headings'] if h['title'] == c['heading']), None); dst = next((h for h in ch['headings'] if h['title'] == c['into']), None)
            if src is None or dst is None: done.append(f"corrections: heading not found in {c['chapter']}"); continue
            dst['items'] += src['items']; ch['headings'].remove(src)
        elif op == 'set_heading':
            for h in ch['headings']:
                if h['title'] == c['old']: h['title'] = c['new']
        renumber([ch])
    idx['warnings'] = [w for w in idx['warnings'] if 'numbering' not in w and 'has no prompts' not in w] + done
    for ch in idx['chapters']:
        for h in ch['headings']:
            if not h['items']: idx['warnings'].append(f"{ch['title']}: heading '{h['title']}' has no prompts")
    return idx


def review_md(idx):
    L = ['# Master Quick Review: split check', '']
    for ch in idx['chapters']:
        n = sum(len(h['items']) for h in ch['headings'])
        L.append(f"## {ch['unit']} / {ch['title']}  (pages {ch['pages'][0]}-{ch['pages'][1]}, {n} prompts, {len(ch['headings'])} headings)")
        for h in ch['headings']:
            L.append(f"- **{h['title'] or '(no heading)'}**")
            for i in h['items']: L.append(f"  - {i['no']}. {i['text']}")
        L.append('')
    L.append('## Warnings'); L += [f'- {w}' for w in idx['warnings']] or ['- none']
    return '\n'.join(L) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pdf'); ap.add_argument('--ocr-dir'); ap.add_argument('--workdir'); ap.add_argument('--dpi', type=int, default=200); ap.add_argument('--time-budget', type=int, default=0, help='stop OCR after N seconds (exit code 3); re-run with the same --workdir to resume')
    ap.add_argument('--out', required=True); ap.add_argument('--corrections', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'references', 'master_corrections.json'))
    a = ap.parse_args()
    pages = []
    if a.ocr_dir:
        tsvs = sorted(glob.glob(os.path.join(a.ocr_dir, 'pg-*.png.tsv')), key=lambda p: int(re.search(r'pg-(\d+)', p).group(1)))
        for p in tsvs:
            ls, W, H = lines_from_tsv(p); pages.append((int(re.search(r'pg-(\d+)', p).group(1)), ls, W, H))
    elif a.pdf:
        n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', a.pdf], capture_output=True, text=True).stdout).group(1))
        if has_text_layer(a.pdf):
            for p in range(1, n + 1):
                ls, W, H = lines_from_bbox(a.pdf, p); pages.append((p, ls, W, H))
        else:
            wd = a.workdir or tempfile.mkdtemp(prefix='ocr_'); os.makedirs(wd, exist_ok=True)
            subprocess.run(['pdftoppm', '-r', str(a.dpi), '-gray', '-png', a.pdf, os.path.join(wd, 'pg')], check=True)
            import time; t0 = time.time()
            for png in sorted(glob.glob(os.path.join(wd, 'pg-*.png'))):
                if not os.path.exists(png + '.tsv'):
                    if a.time_budget and time.time() - t0 > a.time_budget:
                        print('OCR time budget used; re-run the same command (same --workdir) to continue'); sys.exit(3)
                    subprocess.run(['tesseract', png, png, '--psm', '4', 'tsv', 'txt'], capture_output=True)
                ls, W, H = lines_from_tsv(png + '.tsv'); pages.append((int(re.search(r'pg-(\d+)', png).group(1)), ls, W, H))
    else:
        sys.exit('give --pdf or --ocr-dir')
    idx = build(pages)
    if os.path.exists(a.corrections):
        idx = apply_corrections(idx, json.load(open(a.corrections, encoding='utf-8')))
        print('applied corrections from', os.path.abspath(a.corrections))
    json.dump(idx, open(a.out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    open(a.out + '.review.md', 'w', encoding='utf-8').write(review_md(idx))
    print(f"{len(idx['chapters'])} chapters; warnings: {len(idx['warnings'])}")
    for ch in idx['chapters']:
        print(f"  {ch['unit'][:14]:14s} | {ch['title'][:38]:38s} | pages {ch['pages'][0]:2d}-{ch['pages'][1]:2d} | prompts {sum(len(h['items']) for h in ch['headings']):3d} | headings {len(ch['headings'])}")


if __name__ == '__main__':
    main()
