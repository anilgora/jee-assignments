#!/usr/bin/env python3
"""Check that the machine can run the kit. Exit 0 = ready; exit 1 = lists what is missing (write it to RUN_FAILED.md in routine mode)."""
import importlib, shutil, subprocess, sys
need_bin = {'xelatex': 'XeLaTeX (texlive-xetex + amsmath, tcolorbox, enumitem, multicol, titlesec, needspace, adjustbox, pgf/tikz)',
            'pandoc': 'pandoc (LaTeX -> native Word equations)', 'pdftoppm': 'poppler-utils (pdftoppm, pdftotext, pdfinfo)', 'pdftotext': 'poppler-utils'}
opt_bin = {'tesseract': 'tesseract-ocr (only to re-read a scanned master Quick Review)'}
need_py = ['lxml', 'openpyxl', 'sympy', 'PIL']
missing = []
for b, why in need_bin.items():
    if not shutil.which(b): missing.append(f'{b}: {why}')
for m in need_py:
    try: importlib.import_module(m)
    except Exception: missing.append(f'python module {m}')
for b, why in opt_bin.items():
    if not shutil.which(b): print(f'note: {b} not found ({why})')
# LaTeX packages used by the PDFs
for pkg in ('tcolorbox.sty', 'enumitem.sty', 'multicol.sty', 'titlesec.sty', 'needspace.sty', 'adjustbox.sty', 'tikz.sty', 'fontspec.sty'):
    r = subprocess.run(['kpsewhich', pkg], capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout.strip(): missing.append(f'LaTeX package {pkg}')
if missing:
    print('NOT READY. Missing:'); [print(' -', m) for m in missing]; sys.exit(1)
print('READY: all tools present')
