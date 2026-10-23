#!/usr/bin/env python3
"""Build a Master-format Word file (used for PDF input, or Word input in any other layout).

Usage:
    python build_master.py questions.json output.docx

questions.json:
{
  "title": "JEE Mathematics Practice Paper",          # optional, this is the default
  "questions": [
    {"number": "01",
     "english":  ["question line", "", "(A) $29$", "(B) $61$", ...],   # transcribed as printed
     "hindi":    ["...", "", "(A) $29$", ...],                          # [] if the paper has no Hindi
     "solution": ["line", "", "Correct Option: (B)"]}                   # shortened solution
  ]
}
Every list item is one line; "" is a blank line. Output matches the user's Master Question Paper:
Title, then for each question a 'Question NN' Heading 2, one block
[Question in English] / [Question in Hindi] / [Solution in English], and a dashed separator.
Styles come from assets/master_template.docx (the user's own file with its content removed).
"""
import json, os, sys, zipfile
from xml.sax.saxutils import escape

TEMPLATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'master_template.docx')
SEP = '-' * 60


def para(text, style=None):
    ppr = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>' if style else ''
    return f'<w:p>{ppr}<w:r><w:t xml:space="preserve">{escape(text)}</w:t></w:r></w:p>'


def block(lines):
    parts = []
    for n, line in enumerate(lines):
        if line:
            parts.append(f'<w:t xml:space="preserve">{escape(line)}</w:t>')
        if n < len(lines) - 1:
            parts.append('<w:br/>')
    return '<w:p><w:r>' + ''.join(parts) + '</w:r></w:p>'


def main(src, dst):
    d = json.load(open(src, encoding='utf-8'))
    xml = [para(d.get('title', 'JEE Mathematics Practice Paper'), 'Title')]
    for q in d['questions']:
        num = str(q['number'])
        num = num.zfill(2) if num.isdigit() else num
        lines = ['[Question in English]', ''] + q['english'] + ['']
        if q.get('hindi'):
            lines += ['[Question in Hindi]', ''] + q['hindi'] + ['']
        lines += ['[Solution in English]', ''] + q['solution']
        xml += [para(f'Question {num}', 'Heading2'), block(lines), para(SEP)]
    zin = zipfile.ZipFile(TEMPLATE)
    doc = zin.read('word/document.xml').decode('utf-8')
    i = doc.index('<w:body>') + len('<w:body>')
    doc = doc[:i] + ''.join(xml) + doc[i:]
    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            zout.writestr(item, doc.encode('utf-8') if item.filename == 'word/document.xml'
                          else zin.read(item.filename))
    print(f"Wrote {dst}: {len(d['questions'])} questions")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
