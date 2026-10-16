# -*- coding: utf-8 -*-
"""PDF (XeLaTeX) builders: Quick Review, short notes, formula sheet (2 columns), mind map, method flowcharts."""
import re, os
from kit_common import pick, tex, hwrap, esc_text, is_pure_math, hindi_preamble, run_xelatex
from kit_grading import numbering, xref, item_grade_lines, legend, LABELS, LV

GRADE_TEX = {'High': 'red!70!black', 'Medium': 'orange!85!black', 'Low': 'black!55'}
PALETTE = ['blue', 'teal', 'green', 'orange', 'red', 'violet', 'brown', 'magenta', 'cyan', 'olive']


def hbold(t, hindi):
    return hwrap(esc_text(t)) if hindi else esc_text(t)


# ------------------------------------------------------------------ Quick Review
def build_quick_review(spec, ctx, lang, out_pdf, title, workdir, tag):
    hindi = lang == 'hi'
    byid, newno = numbering(spec)
    ql, al = ('Question', 'Model Answer') if lang == 'en' else ('प्रश्न', 'आदर्श उत्तर')
    pre = ("\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.2cm]{geometry}\n\\usepackage{amsmath,amssymb}\n" + hindi_preamble() +
           "\\usepackage{titlesec}\n\\usepackage{xcolor}\n\\usepackage{needspace}\n"
           "\\titleformat{\\section}{\\large\\bfseries\\color{blue!50!black}}{}{0pt}{}[\\vspace{-2pt}{\\color{blue!50!black}\\hrule}]\n"
           "\\titlespacing*{\\section}{0pt}{16pt}{8pt}\n\\setlength{\\parindent}{0pt}\\setlength{\\parskip}{0pt}\\setlength{\\emergencystretch}{3em}\n"
           "\\newcommand{\\lab}[1]{\\par\\vspace{5pt}{\\small\\bfseries\\color{black!65}#1}\\par\\vspace{2pt}}\n\\begin{document}\n")
    o = [pre, r'{\Large\bfseries ' + hbold(title, hindi) + r'\par}\vspace{4pt}\hrule\vspace{6pt}',
         r'{\small ' + tex(legend(ctx, lang), hindi) + r'}\par\vspace{4pt}']
    for sec in spec['quick_review']['sections']:
        o.append(r'\needspace{8\baselineskip}\section*{' + hbold(pick([sec['en'], sec['hi']], lang), hindi) + '}')
        for it in sec['items']:
            o.append(r'\needspace{9\baselineskip}')
            o.append(r'\par\vspace{4pt}{\bfseries ' + (r'{\hindifont ' + ql + '}' if hindi else ql) + f' {it["n"]:02d}' + r'}\par\vspace{1pt}')
            o.append(tex(xref(pick(it['q'], lang), newno), hindi) + r'\par')
            o.append(r'\lab{' + (r'{\hindifont ' + al + '}' if hindi else al) + '}')
            for l in it['a']:
                t = xref(pick(l, lang), newno)
                o.append((r'\[' + t.strip()[1:-1] + r'\]') if is_pure_math(t) else tex(t, hindi) + r'\par\vspace{3pt}')
            g, ml, ol = item_grade_lines(ctx, it['id'], lang)
            gl = hbold(LV[lang][g], hindi); gw = hbold(LABELS[lang]['grade'], hindi)
            o.append(r'\vspace{2pt}{\small\textbf{' + gw + r'} - \textbf{\color{' + GRADE_TEX[g] + '}' + gl + r'}}\par')
            for t in (ml, ol):
                o.append(r'{\footnotesize ' + tex(t, hindi) + r'}\par')
            o.append(r'\vspace{4pt}')
    o.append(r'\end{document}')
    run_xelatex('\n'.join(o), workdir, f'qr_{tag}_{lang}', out_pdf)


# ------------------------------------------------------------------ Short notes
NOTE_LAB = {'en': {'formula': 'Formulas', 'points': 'KEY POINTS', 'steps': 'STEPS', 'watch': 'Watch out'},
            'hi': {'formula': 'सूत्र', 'points': 'मुख्य बिन्दु', 'steps': 'चरण', 'watch': 'सावधानी'}}


def build_notes(spec, lang, out_pdf, title, workdir):
    hindi = lang == 'hi'
    nl = NOTE_LAB[lang]
    tt = lambda s: ('{\\hindifont ' + s + '}') if hindi else s
    pre = ("\\documentclass[10pt,a4paper]{article}\n\\usepackage[margin=1.6cm,top=1.4cm,bottom=1.4cm]{geometry}\n\\usepackage{amsmath,amssymb}\n" + hindi_preamble() +
           "\\usepackage{xcolor}\n\\usepackage[most]{tcolorbox}\n\\usepackage{enumitem}\n\\usepackage{needspace}\n\\linespread{1.02}\n"
           "\\setlength{\\parindent}{0pt}\\setlength{\\parskip}{0pt}\\setlength{\\emergencystretch}{3em}\n"
           "\\setlength{\\abovedisplayskip}{2pt}\\setlength{\\belowdisplayskip}{2pt}\\setlength{\\abovedisplayshortskip}{1pt}\\setlength{\\belowdisplayshortskip}{1pt}\n"
           "\\definecolor{cblue}{HTML}{1F3864}\\definecolor{cteal}{HTML}{0E6B6B}\\definecolor{cgreen}{HTML}{2E7D32}\\definecolor{corange}{HTML}{B85C00}"
           "\\definecolor{cred}{HTML}{A61C1C}\\definecolor{cviolet}{HTML}{5B3A8C}\\definecolor{cbrown}{HTML}{6D4C41}\n"
           "\\tcbset{breakable,enhanced,boxrule=0.8pt,arc=2pt,left=6pt,right=6pt,top=2.5pt,bottom=2.5pt,before skip=3pt,after skip=3pt,fonttitle=\\bfseries\\small}\n"
           "\\newtcolorbox{formbox}{colback=blue!5,colframe=blue!55!black,title={%s}}\n" % tt(nl['formula']) +
           "\\newtcolorbox{warnbox}{colback=red!5,colframe=red!60!black,title={%s}}\n" % tt(nl['watch']) +
           "\\setlist[itemize]{leftmargin=1.4em,itemsep=0.5pt,topsep=0pt,label=\\textbullet}\n\\setlist[enumerate]{leftmargin=1.7em,itemsep=0.5pt,topsep=0pt,label=\\bfseries\\arabic*.}\n"
           "\\newcommand{\\lab}[1]{\\par\\vspace{2pt}{\\footnotesize\\bfseries\\color{black!65} #1}\\par}\n\\begin{document}\n")
    o = [pre, r'{\LARGE\bfseries ' + hbold(title, hindi) + r'\par}\vspace{3pt}\hrule\vspace{5pt}',
         r'{\small ' + tex(pick(spec['notes']['howto'], lang), hindi) + r'}\par\vspace{4pt}']
    for sec in spec['notes']['sections']:
        col = sec['color'] if sec['color'] in ('blue', 'teal', 'green', 'orange', 'red', 'violet', 'brown') else 'blue'
        o.append(r'\needspace{5\baselineskip}')
        o.append(r'\begin{tcolorbox}[colback=c%s,colframe=c%s,coltext=white,boxrule=0pt,arc=3pt,top=3pt,bottom=3pt,before skip=7pt,after skip=2pt,breakable=false]{\large\bfseries %s}\end{tcolorbox}'
                 % (col, col, tex(pick([sec['en'], sec['hi']], lang), hindi)))
        for kind, lines in sec['blocks']:
            ls = [pick(l, lang) for l in lines]
            if kind in ('formula', 'watch'):
                env = 'formbox' if kind == 'formula' else 'warnbox'
                o.append(r'\begin{%s}' % env)
                for i, t in enumerate(ls):
                    o.append((r'\[' + t.strip()[1:-1] + r'\]') if (kind == 'formula' and is_pure_math(t)) else tex(t, hindi) + (r'\par\vspace{1pt}' if i < len(ls) - 1 else ''))
                o.append(r'\end{%s}' % env)
            elif kind == 'points':
                o.append(r'\lab{' + tt(nl['points']) + r'}\begin{itemize}' + ''.join(r'\item ' + tex(t, hindi) + '\n' for t in ls) + r'\end{itemize}')
            else:
                o.append(r'\lab{' + tt(nl['steps']) + r'}\begin{enumerate}' + ''.join(r'\item ' + tex(t, hindi) + '\n' for t in ls) + r'\end{enumerate}')
    o.append(r'\end{document}')
    run_xelatex('\n'.join(o), workdir, f'notes_{lang}', out_pdf)


# ------------------------------------------------------------------ Formula sheet (two columns)
def _fsplit(t):
    m = re.fullmatch(r'(.*?): (\$[^$]+\$)', t)
    if m and not (len(m.group(2)) <= 34 and '\\dfrac' not in m.group(2) and '\\left' not in m.group(2)):
        return m.group(1), m.group(2)
    return None


def build_formula(spec, lang, out_pdf, title, workdir):
    hindi = lang == 'hi'
    pre = ("\\documentclass[10pt,a4paper]{article}\n\\usepackage[margin=1.4cm]{geometry}\n\\usepackage{multicol}\n"
           "\\setlength{\\columnsep}{0.7cm}\\setlength{\\columnseprule}{0.4pt}\n\\usepackage{amsmath,amssymb}\n" + hindi_preamble() +
           "\\usepackage{titlesec}\n\\usepackage{xcolor}\n\\usepackage{needspace}\n"
           "\\titleformat{\\section}{\\normalsize\\bfseries\\color{blue!50!black}}{}{0pt}{}[\\vspace{-3pt}{\\color{blue!50!black}\\hrule}]\n"
           "\\titlespacing*{\\section}{0pt}{9pt}{5pt}\n\\setlength{\\parindent}{0pt}\\setlength{\\parskip}{0pt}\\setlength{\\emergencystretch}{3em}\n"
           "\\setlength{\\abovedisplayskip}{1pt}\\setlength{\\belowdisplayskip}{3pt}\\setlength{\\abovedisplayshortskip}{1pt}\\setlength{\\belowdisplayshortskip}{3pt}\n\\begin{document}\n")
    o = [pre, r'{\Large\bfseries ' + hbold(title, hindi) + r'\par}\vspace{3pt}\hrule\vspace{2pt}', r'\begin{multicols}{2}']
    for sec in spec['formula']['sections']:
        o.append(r'\needspace{8\baselineskip}\section*{' + tex(pick([sec['en'], sec['hi']], lang), hindi) + '}')
        for l in sec['lines']:
            t = pick(l, lang); sp = _fsplit(t)
            if sp:
                o.append(r'\needspace{3.5\baselineskip}' + tex(sp[0], hindi) + r':\par\vspace{-2pt}\[' + sp[1][1:-1] + r'\]')
            elif is_pure_math(t):
                o.append(r'\[' + t.strip()[1:-1] + r'\]')
            else:
                o.append(tex(t, hindi) + r'\par\vspace{2.5pt}')
    o.append(r'\end{multicols}\end{document}')
    run_xelatex('\n'.join(o), workdir, f'formula_{lang}', out_pdf)


# ------------------------------------------------------------------ Mind map
def build_mindmap(spec, lang, out_pdf, title, sub, workdir, png=None):
    hindi = lang == 'hi'
    br = spec['mindmap']['branches']; n = len(br)
    nl = (n + 1) // 2; left, right = br[:nl], br[nl:]
    pre = ("\\documentclass[10pt]{article}\n\\usepackage[paperwidth=420mm,paperheight=297mm,margin=6mm]{geometry}\n\\usepackage{amsmath,amssymb}\n" + hindi_preamble() +
           "\\usepackage{xcolor}\n\\usepackage{tikz}\n\\usetikzlibrary{positioning,calc,shapes.geometric}\n\\pagestyle{empty}\n\\setlength{\\parindent}{0pt}\n\\begin{document}\n\\centering\n"
           "\\begin{tikzpicture}[x=1cm,y=1cm]\n")
    o = [pre]
    W, X = 15.4, 4.3
    def place(items, side, offset):
        cnt = len(items); step = min(4.2, 26.5 / max(cnt, 1)); top = (cnt - 1) * step / 2
        for k, b in enumerate(items):
            col = PALETTE[(k + offset) % len(PALETTE)]
            y = top - k * step
            head = tex(pick([b['en'], b['hi']], lang), hindi)
            body = r'\\[1.5pt]'.join(r'$\bullet$\ ' + tex(pick(l, lang), hindi) for l in b['leaves'])
            anchor = 'east' if side < 0 else 'west'; nm = f'b{side}{k}'
            o.append(r'\node[draw=%s!70!black,fill=%s!7,rounded corners=4pt,line width=1.1pt,anchor=%s,text width=%.1fcm,align=left,inner sep=5pt,font=\small] (%s) at (%.1f,%.2f) {\textbf{\color{%s!60!black}\normalsize %s}\\[3pt] %s};'
                     % (col, col, anchor, W, nm, side * X, y, col, head, body))
            o.append(r'\draw[%s!70!black,line width=2.2pt,line cap=round] (0,0) to[out=%d,in=%d] (%s.%s);' % (col, 0 if side > 0 else 180, 180 if side > 0 else 0, nm, 'west' if side > 0 else 'east'))
    place(left, -1, 0); place(right, 1, nl)
    o.append(r'\node[draw=black!70,fill=yellow!25,ellipse,line width=2pt,minimum width=5.2cm,minimum height=2.6cm,align=center,inner sep=4pt] at (0,0) {\bfseries\Large '
             + tex(title, hindi) + r'\\[2pt]\normalsize ' + tex(sub, hindi) + '};')
    o.append('\\end{tikzpicture}\n\\end{document}')
    run_xelatex('\n'.join(o), workdir, f'mindmap_{lang}', out_pdf)
    if png:
        import subprocess
        subprocess.run(['pdftoppm', '-png', '-r', '110', '-singlefile', out_pdf, png[:-4]], check=True)


# ------------------------------------------------------------------ Method flowcharts
def build_flowcharts(spec, lang, out_pdf, workdir):
    hindi = lang == 'hi'
    pre = ("\\documentclass[10pt]{article}\n\\usepackage[a4paper,landscape,margin=7mm]{geometry}\n\\usepackage{amsmath,amssymb}\n" + hindi_preamble() +
           "\\usepackage{xcolor}\n\\usepackage{tikz}\n\\usetikzlibrary{positioning,calc,arrows.meta}\n\\usepackage[export]{adjustbox}\n\\pagestyle{empty}\n\\setlength{\\parindent}{0pt}\n\\begin{document}\n")
    o = [pre]
    YES, NO, OTH = (('हाँ', 'नहीं', 'अन्यथा') if hindi else ('Yes', 'No', 'Otherwise'))
    w = lambda s: ('{\\hindifont ' + s + '}') if hindi else s
    charts = spec['flowcharts']
    for ci, ch in enumerate(charts):
        col = ch.get('color', 'blue'); STEP = 2.35
        title = tex(pick(ch['title'], lang), hindi); start = tex(pick(ch['start'], lang), hindi)
        o.append(r'\begin{center}{\Large\bfseries\color{%s!60!black} %s}\end{center}\vspace{-2mm}' % (col, title))
        o.append(r'\adjustbox{max width=\textwidth,max height=0.88\textheight,center}{')
        o.append(r'\begin{tikzpicture}[>={Stealth[length=3mm]},line width=1pt,'
                 r'dec/.style={draw=%s!70!black,fill=yellow!25,rounded corners=5pt,text width=7.8cm,align=center,inner sep=5pt,font=\normalsize\bfseries},'
                 r'ans/.style={draw=%s!70!black,fill=%s!8,rounded corners=3pt,text width=17.2cm,align=left,inner sep=5pt,font=\normalsize},'
                 r'beg/.style={draw=%s!70!black,fill=%s!25,rounded corners=10pt,text width=9cm,align=center,inner sep=6pt,font=\large\bfseries},'
                 r'lab/.style={font=\scriptsize\bfseries,fill=white,inner sep=1pt}]' % (col, col, col, col, col))
        y = 0.0
        o.append(r'\node[beg] (s) at (0,%.2f) {%s};' % (y, start)); prev = 's'
        for i, st in enumerate(ch['steps']):
            y -= STEP
            q = tex(pick(st['q'], lang), hindi)
            a = r'\\[1pt]'.join(tex(x, hindi) for x in st['a'][1 if hindi else 0])
            o.append(r'\node[dec] (d%d) at (0,%.2f) {%s};' % (i, y, q))
            o.append(r'\node[ans,anchor=west] (a%d) at (5.9,%.2f) {%s};' % (i, y, a))
            o.append(r'\draw[->] (%s.south) -- node[lab] {%s} (d%d.north);' % (prev, '' if i == 0 else w(NO), i))
            o.append(r'\draw[->,%s!70!black] (d%d.east) -- node[lab] {%s} (a%d.west);' % (col, i, w(YES), i))
            prev = f'd{i}'
        y -= STEP
        el = r'\\[1pt]'.join(tex(x, hindi) for x in ch['else'][1 if hindi else 0]) if isinstance(ch['else'][0], list) else tex(pick(ch['else'], lang), hindi)
        o.append(r'\node[beg,fill=white,text width=3.2cm] (e) at (0,%.2f) {%s};' % (y, w(OTH)))
        o.append(r'\node[ans,anchor=west,fill=%s!18] (ae) at (5.9,%.2f) {%s};' % (col, y, el))
        o.append(r'\draw[->] (%s.south) -- node[lab] {%s} (e.north);' % (prev, w(NO)))
        o.append(r'\draw[->,%s!70!black] (e.east) -- (ae.west);' % col)
        o.append(r'\end{tikzpicture}}')
        if ci < len(charts) - 1: o.append(r'\newpage')
    o.append(r'\end{document}')
    run_xelatex('\n'.join(o), workdir, f'flow_{lang}', out_pdf)
