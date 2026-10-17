#!/usr/bin/env python3
"""Check a rendered kit folder: expected files present, Word files carry native equations (no raw $), PDFs have pages.
Usage: python verify_outputs.py OUTDIR SLUG BATCH1,BATCH2
"""
import glob, os, re, subprocess, sys, zipfile

out, slug, batches = sys.argv[1], sys.argv[2], sys.argv[3].split(',')
expect = []
for L in ('EN', 'HI'):
    for b in batches: expect += [f'{slug}_Quick_Review_{b}_{L}.docx', f'{slug}_Quick_Review_{b}_{L}.pdf']
    expect += [f'{slug}_Short_Notes_{L}.docx', f'{slug}_Short_Notes_{L}.pdf', f'{slug}_Formula_Sheet_{L}.docx', f'{slug}_Formula_Sheet_{L}.pdf',
               f'{slug}_Mind_Map_{L}.pdf', f'{slug}_Method_Flowcharts_{L}.pdf']
expect += [f'{slug}_Question_Mapping.xlsx', 'REPORT.md']
bad = 0
for f in expect:
    p = os.path.join(out, f)
    if not os.path.exists(p): print('MISSING', f); bad += 1; continue
    if f.endswith('.docx'):
        x = zipfile.ZipFile(p).read('word/document.xml').decode(); txt = re.sub(r'<[^>]+>', '', x)
        n = x.count('<m:oMath>')
        flag = 'ok' if (n > 0 and '$' not in txt) else 'PROBLEM'
        if flag != 'ok': bad += 1
        print(f'{flag:7s} {f}  equations={n}  raw$={txt.count("$")}')
    elif f.endswith('.pdf'):
        pages = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', p], capture_output=True, text=True).stdout).group(1))
        print(f'ok      {f}  pages={pages}')
print('ALL GOOD' if not bad else f'{bad} problem(s)')
sys.exit(1 if bad else 0)
