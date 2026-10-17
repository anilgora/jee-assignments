# -*- coding: utf-8 -*-
"""Word (.docx) builders with NATIVE 2D equations (OMML). Every product is built from the chapter spec."""
import re, zipfile
from xml.sax.saxutils import escape
from kit_common import TEMPLATE, pick, is_pure_math
from kit_grading import numbering, xref, item_grade_lines, legend

GRADE_COL = {'High': 'C00000', 'Medium': 'C55A11', 'Low': '7F7F7F'}
SEC_COL = {'blue': '1F3864', 'teal': '0E6B6B', 'green': '2E7D32', 'orange': 'B85C00', 'red': 'A61C1C', 'violet': '5B3A8C', 'brown': '6D4C41'}


def rpr(bold=False, color=None, size=None, italic=False):
    x = ''
    if bold: x += '<w:b/>'
    if italic: x += '<w:i/>'
    if color: x += f'<w:color w:val="{color}"/>'
    if size: x += f'<w:sz w:val="{size}"/>'
    return x


def ppr(style=None, shade=None, box=None, left=0, hanging=0, before=0, after=60, line=252, jc=None, keep_next=False, bar_bottom=None):
    x = ''
    if style: x += f'<w:pStyle w:val="{style}"/>'
    if keep_next: x += '<w:keepNext/>'
    if box:
        st, sz, col = box
        x += '<w:pBdr>' + ''.join(f'<w:{s} w:val="{st}" w:sz="{sz}" w:space="3" w:color="{col}"/>' for s in ('top', 'left', 'bottom', 'right')) + '</w:pBdr>'
    elif bar_bottom:
        x += f'<w:pBdr><w:bottom w:val="single" w:sz="8" w:space="1" w:color="{bar_bottom}"/></w:pBdr>'
    if shade: x += f'<w:shd w:val="clear" w:color="auto" w:fill="{shade}"/>'
    x += f'<w:spacing w:before="{before}" w:after="{after}" w:line="{line}" w:lineRule="auto"/>'
    if left or hanging: x += f'<w:ind w:left="{left}" w:hanging="{hanging}"/>'
    if jc: x += f'<w:jc w:val="{jc}"/>'
    return x


def P(content, pp=''):
    return f'<w:p><w:pPr>{pp}</w:pPr>{content}</w:p>'


def line_p(M, text, pp, rp=''):
    """a paragraph for a text line; a pure equation line becomes a centred display equation"""
    if is_pure_math(text):
        d = M.display(text)
        if d: return P(d, pp + '<w:jc w:val="center"/>' if '<w:jc' not in pp else pp)
    return P(M.runs(text, rp), pp)


def sect(cols=1, continuous=False, in_p=False):
    typ = '<w:type w:val="continuous"/>' if continuous else ''
    c = f'<w:cols w:num="{cols}" w:space="500" w:sep="1"/>' if cols > 1 else '<w:cols w:space="720"/>'
    return (f'<w:sectPr>{typ}<w:pgSz w:w="11906" w:h="16838"/>'
            '<w:pgMar w:top="850" w:right="850" w:bottom="850" w:left="850" w:header="400" w:footer="400" w:gutter="0"/>'
            f'{c}</w:sectPr>')


def write_docx(body, path):
    zin = zipfile.ZipFile(TEMPLATE)
    doc = zin.read('word/document.xml').decode('utf-8')
    i = doc.index('<w:body>') + len('<w:body>'); j = doc.index('</w:body>')
    doc = doc[:i] + body + doc[j:]
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == 'word/document.xml': data = doc.encode('utf-8')
            elif item.filename == 'word/settings.xml':          # template has <w:zoom/> without percent (schema error)
                data = re.sub(rb'<w:zoom(?![^>]*w:percent)([^>]*)/>', rb'<w:zoom w:percent="100"\1/>', data)
            zout.writestr(item, data)


# ------------------------------------------------------------------ Quick Review (one batch, one language)
def qr_texts(spec, ctx_list):
    out = []
    byid, newno = numbering(spec)
    for sec in spec['quick_review']['sections']:
        for it in sec['items']:
            out += [pick(it['q'], 'en'), pick(it['q'], 'hi')]
            for l in it['a']: out += [pick(l, 'en'), pick(l, 'hi')]
    return out


def build_quick_review(spec, ctx, lang, M, path, titles):
    byid, newno = numbering(spec)
    ql, al = ('Question', 'Model Answer') if lang == 'en' else ('प्रश्न', 'आदर्श उत्तर')
    body = [P(M.runs(titles[lang]), ppr(style='Title', after=80)), P(M.runs(legend(ctx, lang), rpr(size=18, color='404040')), ppr(after=140))]
    for sec in spec['quick_review']['sections']:
        body.append(P(M.runs(pick([sec['en'], sec['hi']], lang)), ppr(style='Heading1', keep_next=True, before=200, after=80)))
        for it in sec['items']:
            body.append(P(M.runs(f'{ql} {it["n"]:02d}'), ppr(style='Heading2', keep_next=True, before=120, after=40)))
            body.append(P(M.runs(f'[{ql}]', rpr(bold=True, color='595959', size=18)), ppr(after=20, keep_next=True)))
            body.append(line_p(M, xref(pick(it['q'], lang), newno), ppr(after=60)))
            body.append(P(M.runs(f'[{al}]', rpr(bold=True, color='595959', size=18)), ppr(after=20, keep_next=True)))
            for l in it['a']:
                body.append(line_p(M, xref(pick(l, lang), newno), ppr(after=50)))
            g, ml, ol = item_grade_lines(ctx, it['id'], lang)
            from kit_grading import LV, LABELS
            gp = (M.runs(LABELS[lang]['grade'] + ' - ', rpr(bold=True, size=20)) + M.runs(LV[lang][g], rpr(bold=True, color=GRADE_COL[g], size=22)))
            body.append(P(gp, ppr(before=60, after=20)))
            for t in (ml, ol):
                body.append(P(M.runs(t, rpr(size=17, color='404040')), ppr(after=20)))
    body.append(sect())
    write_docx(''.join(body), path)


# ------------------------------------------------------------------ Short notes
LABEL = {'en': {'formula': 'FORMULAS', 'points': 'KEY POINTS', 'steps': 'STEPS', 'watch': 'WATCH OUT'},
         'hi': {'formula': 'सूत्र', 'points': 'मुख्य बिन्दु', 'steps': 'चरण', 'watch': 'सावधानी'}}
BOXC = {'formula': ('EAF1FB', '2F6DB5'), 'watch': ('FDECEA', 'C62828')}


def build_notes(spec, lang, M, path, title):
    body = [P(M.runs(title), ppr(style='Title', after=60)),
            P(M.runs(pick(spec['notes']['howto'], lang), rpr(size=18, color='595959')), ppr(after=100))]
    for sec in spec['notes']['sections']:
        col = SEC_COL.get(sec['color'], '1F3864')
        body.append(P(M.runs(pick([sec['en'], sec['hi']], lang), rpr(bold=True, color='FFFFFF', size=26)),
                      ppr(style='Heading1', shade=col, before=160, after=60, keep_next=True, left=60)))
        for kind, lines in sec['blocks']:
            lc = BOXC.get(kind, (None, col))[1]
            body.append(P(M.runs(LABEL[lang][kind], rpr(bold=True, color=lc, size=18)), ppr(before=50, after=20, keep_next=True)))
            for i, l in enumerate(lines, 1):
                t = pick(l, lang)
                if kind == 'steps':
                    body.append(P(M.runs(f'{i}.  ') + M.runs(t), ppr(left=480, hanging=330, after=20)))
                elif kind == 'points':
                    body.append(P(M.runs('\u2022  ') + M.runs(t), ppr(left=480, hanging=330, after=20)))
                else:
                    sh, bc = BOXC[kind]
                    body.append(line_p(M, t, ppr(shade=sh, box=('single', 8, bc), left=100, after=40)))
    body.append(sect())
    write_docx(''.join(body), path)


# ------------------------------------------------------------------ Formula sheet (two columns)
def formula_display_split(t):
    m = re.fullmatch(r'(.*?): (\$[^$]+\$)', t)
    if m and not (len(m.group(2)) <= 34 and '\\dfrac' not in m.group(2) and '\\left' not in m.group(2)):
        return m.group(1) + ':', m.group(2)
    return None


def build_formula(spec, lang, M, path, title):
    body = [P(M.runs(title), ppr(style='Title', after=60)),
            f'<w:p><w:pPr>{sect(1)}</w:pPr></w:p>']
    for sec in spec['formula']['sections']:
        body.append(P(M.runs(pick([sec['en'], sec['hi']], lang), rpr(bold=True, color='1F3864', size=22)),
                      ppr(before=150, after=50, keep_next=True, bar_bottom='1F3864')))
        for l in sec['lines']:
            t = pick(l, lang)
            sp = formula_display_split(t)
            if sp:
                body.append(P(M.runs(sp[0]), ppr(after=0, keep_next=True)))
                body.append(line_p(M, sp[1], ppr(after=50)))
            else:
                body.append(line_p(M, t, ppr(after=50)))
    body.append(sect(2, continuous=True))
    write_docx(''.join(body), path)
