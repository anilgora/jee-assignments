# -*- coding: utf-8 -*-
"""LaTeX -> native Word (OMML) equations, via one batched pandoc call, plus helpers that build
WordprocessingML paragraphs with inline / display equations while keeping all formatting."""
import os, re, subprocess, tempfile, zipfile
from xml.sax.saxutils import escape
from lxml import etree
from kit_common import MATH_RE, split_math, is_pure_math

M_NS = 'http://schemas.openxmlformats.org/officeDocument/2006/math'
W_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'


ORDER = {   # OOXML math schema child order for property elements
    'rPr': ['lit', 'nor', 'scr', 'sty', 'brk', 'aln'],
    'dPr': ['begChr', 'sepChr', 'endChr', 'grow', 'shp', 'ctrlPr'],
    'mcPr': ['count', 'mcJc'],
    'mPr': ['baseJc', 'plcHide', 'rSp', 'cSp', 'rSpRule', 'cGpRule', 'cGp', 'mcs', 'ctrlPr'],
    'fPr': ['type', 'ctrlPr'],
    'naryPr': ['chr', 'limLoc', 'grow', 'subHide', 'supHide', 'ctrlPr'],
    'accPr': ['chr', 'ctrlPr'], 'barPr': ['pos', 'ctrlPr'], 'borderBoxPr': ['hideTop', 'hideBot', 'hideLeft', 'hideRight', 'strikeH', 'strikeV', 'strikeBLTR', 'strikeTLBR', 'ctrlPr'],
    'eqArrPr': ['baseJc', 'maxDist', 'objDist', 'rSpRule', 'rSp', 'ctrlPr'], 'groupChrPr': ['chr', 'pos', 'vertJc', 'ctrlPr'],
    'radPr': ['degHide', 'ctrlPr'], 'sSubSupPr': ['alnScr', 'ctrlPr'], 'limLowPr': ['ctrlPr'], 'limUppPr': ['ctrlPr'], 'funcPr': ['ctrlPr'],
}


def _normalise(el):
    """Re-order children of math property elements into schema order (pandoc output is valid for Word but not strictly ordered)."""
    for e in el.iter():
        if not isinstance(e.tag, str) or not e.tag.startswith('{%s}' % M_NS): continue
        name = e.tag.split('}')[1]
        order = ORDER.get(name)
        if not order: continue
        if name == 'rPr':      # schema: nor excludes scr/sty
            if any(k.tag == '{%s}nor' % M_NS for k in e):
                for k in list(e):
                    if k.tag in ('{%s}sty' % M_NS, '{%s}scr' % M_NS): e.remove(k)
        kids = list(e)
        key = lambda k: order.index(k.tag.split('}')[1]) if (isinstance(k.tag, str) and k.tag.split('}')[1] in order) else 99
        if any(isinstance(k.tag, str) and k.tag.split('}')[1] not in order for k in kids):
            continue
        srt = sorted(kids, key=key)
        if srt != kids:
            for k in kids: e.remove(k)
            for k in srt: e.append(k)


def latex_to_omml(snippets):
    """snippets: iterable of LaTeX strings (without $). Returns {snippet: '<m:oMath>..</m:oMath>'}."""
    snips = sorted({s.strip() for s in snippets if s.strip()})
    if not snips:
        return {}
    d = tempfile.mkdtemp()
    open(d + '/a.md', 'w', encoding='utf-8').write('\n\n'.join(f'${s}$' for s in snips))
    r = subprocess.run(['pandoc', d + '/a.md', '-o', d + '/a.docx'], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError('pandoc failed: ' + r.stderr[:300])
    root = etree.fromstring(zipfile.ZipFile(d + '/a.docx').read('word/document.xml'))
    maths = [m for p in root.iter('{%s}p' % W_NS) for m in p.findall('{%s}oMath' % M_NS)]
    if len(maths) != len(snips):
        raise RuntimeError(f'pandoc returned {len(maths)} equations for {len(snips)} snippets')
    out = {}
    for s, m in zip(snips, maths):
        _normalise(m)
        x = etree.tostring(m, encoding='unicode')
        x = re.sub(r'\sxmlns:\w+="[^"]+"', '', x)          # namespaces are declared on the document root
        out[s] = x
    return out


class Math:
    """Collects every equation in the spec, converts once, then renders runs."""
    def __init__(self, texts):
        sn = set()
        for t in texts:
            for p in split_math(t):
                if p.startswith('$') and len(p) > 1:
                    sn.add(p.strip('$'))
        self.map = latex_to_omml(sn)

    def omml(self, snippet):
        return self.map.get(snippet.strip(), None)

    def runs(self, text, rpr=''):
        """text with $..$ -> w:r runs and inline m:oMath"""
        out = []
        for p in split_math(text):
            if not p:
                continue
            if p.startswith('$') and len(p) > 1:
                o = self.omml(p.strip('$'))
                out.append(o if o else f'<w:r><w:rPr>{rpr}</w:rPr><w:t xml:space="preserve">{escape(p)}</w:t></w:r>')
            else:
                out.append(f'<w:r><w:rPr>{rpr}</w:rPr><w:t xml:space="preserve">{escape(p)}</w:t></w:r>')
        return ''.join(out)

    def display(self, text):
        """a pure-math line -> centred display equation content (no w:p wrapper)"""
        o = self.omml(text.strip().strip('$'))
        return f'<m:oMathPara>{o}</m:oMathPara>' if o else None
