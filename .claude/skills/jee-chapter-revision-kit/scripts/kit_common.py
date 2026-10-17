# -*- coding: utf-8 -*-
"""Shared helpers for the chapter revision kit: paths, LaTeX text wrapping, XeLaTeX runner."""
import os, re, subprocess, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FONTS = os.path.join(ROOT, 'assets', 'fonts')
TEMPLATE = os.path.join(ROOT, 'assets', 'master_template.docx')
MATH_RE = re.compile(r'(\$\$.+?\$\$|\$[^$]*\$)')
DEVA = r'[\u0900-\u097F]'


def pick(x, lang):
    """x is a plain string (same in both languages) or an [en, hi] pair."""
    return x if isinstance(x, str) else x[0 if lang == 'en' else 1]


def split_math(s):
    return MATH_RE.split(s)


def is_pure_math(s):
    return re.fullmatch(r'\$[^$]+\$', s.strip()) is not None


def esc_text(t):
    t = t.replace('&', r'\&').replace('%', r'\%').replace('#', r'\#')
    out, op = [], True                      # straight double quotes -> typographic
    for ch in t:
        if ch == '"':
            out.append('``' if op else "''"); op = not op
        else:
            out.append(ch)
    return ''.join(out)


def hwrap(t):
    """Wrap Devanagari runs so XeLaTeX uses the Devanagari font."""
    return re.sub(DEVA + r'+(?:[ ,.:;\-\u0964]+' + DEVA + r'+)*', lambda m: '{\\hindifont ' + m.group(0) + '}', t)


def tex(t, hindi):
    """Text with $...$ math -> LaTeX body text (math passes through)."""
    return ''.join(p if (p.startswith('$') and len(p) > 1) else (hwrap(esc_text(p)) if hindi else esc_text(p))
                   for p in split_math(t))


def hindi_preamble():
    return ("\\usepackage{fontspec}\n\\newfontfamily\\hindifont[Script=Devanagari,Path=%s/,Extension=.ttf,"
            "BoldFont=NotoSansDevanagari-Bold]{NotoSansDevanagari}\n" % FONTS.replace('\\', '/'))


def run_xelatex(tex_source, workdir, name, out_pdf):
    os.makedirs(workdir, exist_ok=True)
    base = os.path.join(workdir, name)
    open(base + '.tex', 'w', encoding='utf-8').write(tex_source)
    r = None
    for _ in range(2):
        r = subprocess.run(['xelatex', '-interaction=nonstopmode', '-halt-on-error', '-output-directory', workdir, base + '.tex'],
                           capture_output=True, text=True)
    log = open(base + '.log', encoding='utf-8', errors='ignore').read()
    if r.returncode != 0 or not os.path.exists(base + '.pdf'):
        print(log[-2500:]); sys.exit(f'xelatex failed for {name} (usually a bad LaTeX command inside $...$)')
    miss = re.findall(r'Missing character: (.*)', log)
    if miss:
        print('WARNING missing glyphs in', name, sorted(set(miss))[:6])
    shutil.copy(base + '.pdf', out_pdf)
