#!/usr/bin/env python3
"""Build every deliverable of a full question paper (one JSON file per question, or one set JSON).

Usage:
    python build_paper.py PAPER_DIR_or_set.json OUTDIR [--name Short_Name] [--no-excel]

PAPER_DIR holds meta.json ({"title": ..., "date": ...}) and q01.json, q02.json, ... (one question each,
same fields as a question in set.json plus "target_level" from the blueprint). Types: SCQ, MCQ, INT,
Numerical, MTC (matrix match, four options), PARA (paragraph + two single-correct questions: give
"parts": [rating1, rating2] instead of one rating; the English/Hindi text holds the paragraph and both
questions with options; the solution holds two sub-solutions).

Every question has TWO solutions: "solution" (shortened, user-approved level of detail) and "solution_full"
(normal, complete step-by-step). Optional "answer_plan" (copied from the blueprint) is checked against both.

Outputs (in OUTDIR):
    <name>_Shortened_Solutions.docx          Master format with the shortened solutions, maths as LaTeX $...$
    <name>_Full_Solutions.docx               Master format with the full solutions
    <name>_Questions_EN_HI.pdf               questions only, English + Hindi, 2D equations
    <name>_Questions_and_Shortened_Solutions.pdf   English + Hindi question, shortened solution
    <name>_Questions_and_Full_Solutions.pdf  English + Hindi question, full solution
    <name>_difficulty.xlsx                   internal difficulty report (calibrated skill), levels never appear elsewhere

set.json schema: see references/set_schema.md. The question list order is the order in every file.
The script appends the standard "Only one option is correct." style line itself, from "type".
"""
import argparse, json, os, re, subprocess, sys, shutil, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import check_answers, extract_answers, parse_plan, classify_number

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)
FONTS = os.path.join(SKILL, 'assets', 'fonts')
BUILD_MASTER = os.path.join(HERE, 'build_master.py')
PARAS = ('PARA', 'PARA_NUM')


def part_marks(q):
    return q.get('marks', {'PARA': 3, 'PARA_NUM': 2}.get(q['type'], 0) or INSTR[q['type']][2])


RATING_KEYS = ('level', 'key_step', 'justification', 'nearest_anchor', 'confidence')
CALIB_CANDIDATES = [
    '/mnt/skills/plugins/jee-advanced-difficulty-calibrated/scripts/build_report.py',
    os.path.join(SKILL, '..', 'jee-advanced-difficulty-calibrated', 'scripts', 'build_report.py'),
]
RECALC = '/mnt/skills/public/xlsx/scripts/recalc.py'

INSTR = {  # type -> (English, Hindi, default marks)
    'SCQ': ('Only one option is correct.', 'केवल एक विकल्प सही है।', 3),
    'MTC': ('Only one option is correct.', 'केवल एक विकल्प सही है।', 3),
    'PARA': ('Each of the two questions has only one correct option.', 'प्रत्येक प्रश्न में केवल एक विकल्प सही है।', 6),
    'PARA_NUM': ('Each of the two questions has a numerical answer, correct up to the 2nd decimal digit.', 'प्रत्येक प्रश्न का उत्तर एक संख्यात्मक मान है (दशमलव के दूसरे अंक तक सही)।', 4),
    'MCQ': ('One or more options is(are) correct.', 'एक या अधिक विकल्प सही हो सकते हैं।', 4),
    'INT': ('The answer is a non-negative integer.', 'उत्तर एक अऋणात्मक पूर्णांक है।', 4),
    'Numerical': ('The answer is a numerical value, correct up to the 2nd decimal digit.',
                  'उत्तर एक संख्यात्मक मान है (दशमलव के दूसरे अंक तक सही)।', 4),
}
OPT = re.compile(r'^\(([A-D])\)\s')
ANS = re.compile(r'^(\*\*)?(Correct Options?|Final Answer)( for Question \d)?: ')
CAL_TYPE = {'SCQ': 'SCQ', 'MCQ': 'MCQ', 'INT': 'INT', 'Numerical': 'Numerical', 'MTC': 'MTC SCQ', 'PARA': 'Para SCQ', 'PARA_NUM': 'Q Stem'}


def split_math(s):
    return re.split(r'(\$\$.+?\$\$|\$[^$]*\$)', s)


def outside_math(s):
    return ''.join(p for p in split_math(s) if not (p.startswith('$') and len(p) > 1))


SYLLABUS_BAD = re.compile(r'\\?\b(sinh|cosh|tanh|sech|csch|coth)\b|\\(sinh|cosh|tanh|sech|csch|coth)|asymptot', re.I)
STYLE_BAD = re.compile(r'(?:^|[.?!:]\s+)(Find|Calculate|Compute|Determine|Evaluate|Solve|Show that|Prove|What is|What are)\b')


KNOWN_SKELETONS = [
    (r'\\tan\^\{-1\}\(x\+1\)\s*\+\s*\\tan\^\{-1\}\(x-1\)', 'tan^-1(x+1)+tan^-1(x-1) equation (published JEE Main problem)'),
    (r'x=\\sec\\theta.*y=\\tan\\theta', 'x = sec, y = tan parametric second derivative'),
    (r'\\left\|\\sin\\pi x\\right\|\+\\left\|\\cos', 'period of |sin| + |cos|'),
    (r'\\dfrac\{x\\sin x\}\{1\+\\cos\^\{?2\}?x\}', 'king-rule integral of x sin x/(1+cos^2 x)'),
    (r'\(\\cos x\)\^\{1/x\^\{?2\}?\}', '(cos x)^(1/x^2) limit'),
    (r'\\tan\^\{-1\}\\left\(\\dfrac\{\\sqrt\{1\+x\^\{?2\}?\}-1\}\{x\}\\right\)', 'tan^-1((sqrt(1+x^2)-1)/x) simplification'),
]


def stem_lines_for_domain(q):
    return [l for l in q.get('english', []) if not re.match(r'^\([A-D]\)\s', l)]


def lint(q, tag):
    """(errors, warnings) for syllabus words and non-JEE phrasing in one question."""
    errs, warns = [], []
    for part in ('english', 'hindi', 'solution', 'solution_full'):
        for l in q.get(part, []):
            if SYLLABUS_BAD.search(l):
                errs.append(f'{tag} {part}: hyperbolic function or asymptote (outside the JEE syllabus): {l[:70]}')
    for pat, what in KNOWN_SKELETONS:
        if re.search(pat, ' '.join(q.get('english', [])).replace(' ', '')) or re.search(pat, ' '.join(q.get('english', []))):
            warns.append(f'{tag}: matches a known skeleton ({what}); see references/known_skeletons.md')
    bc = q.get('blueprint_concepts') or []
    cu = q.get('concept_use') or {}
    if not bc:
        errs.append(f'{tag}: blueprint_concepts missing (copy the row\'s concepts from blueprint.json) and concept_use (one line per concept: where the solution needs it)')
    else:
        missing = [c for c in bc if c not in cu]
        extra = [c for c in cu if c not in bc]
        short = [c for c in bc if c in cu and len(str(cu[c]).strip()) < 15]
        if missing:
            errs.append(f'{tag}: concept(s) from the blueprint not used or not accounted for: {missing}. Every concept of the row must be needed in the question; add it to the question or explain its role in concept_use')
        if extra:
            errs.append(f'{tag}: concept_use lists concept(s) that are not in the blueprint row: {extra}')
        if short:
            errs.append(f'{tag}: concept_use for {short} is too short; say where the solution needs that concept')
    rev = q.get('stem_review', '')
    if len(rev.strip()) < 40:
        errs.append(f'{tag}: stem_review missing or too short; run scripts/review_stems.py, read each stem as a student would, and record what you checked (symbols defined, conditions complete, one reading, answer unique)')
    note = q.get('originality_note', '')
    if len(note.strip()) < 60:
        errs.append(f'{tag}: originality_note missing or too short (needs: New / Closest known / Different because; see references/originality_guide.md)')
    if q.get('web_check') not in ('not found', 'ingredient only', 'not available', 'not checked', 'found: redesigned'):
        warns.append(f'{tag}: web_check should be one of: not found / ingredient only / not checked / not available')
    # every function introduced in the stem needs a domain (and codomain): "Let $f:\\mathbb{R}\\to\\mathbb{R}$ ...", "defined on ...", "for x > 0"
    plain = ' '.join(stem_lines_for_domain(q))
    for m in re.finditer(r'[Ll]et\s+(.{1,60}?)\s+(?:be|denote)\s+(?:the\s+|a\s+|an\s+|two\s+)?(?:[A-Za-z\- ]{0,40}?)functions?\b', plain):
        seg = m.group(1)
        names = sorted({n for tok in re.findall(r'\$([^$]*)\$', seg) for n in re.findall(r'(?<![A-Za-z\\])([A-Za-z])(?![A-Za-z(])', tok.split(':')[0])})
        has_colon = ':' in seg
        has_words = re.search(r'defined\s+(on|for)|on\s+the\s+interval|for\s+(all\s+)?(real\s+)?\$[a-z]', plain)
        if names and not (has_colon or has_words):
            errs.append(f'{tag}: function(s) {", ".join(names)} introduced without a domain; write "Let $f:\\mathbb{{R}}\\to\\mathbb{{R}}$ be ..." or "defined on ..." (see references/style_guide.md)')
    if q.get('web_check') == 'not checked':
        warns.append(f'{tag}: originality not web-checked')
    t = q.get('type')
    stem = [l for l in q.get('english', []) if not re.match(r'^\([A-D]\)\s', l)]
    text = ' '.join(stem)
    for m in STYLE_BAD.finditer(re.sub(r'\$[^$]*\$', '', text)):
        errs.append(f'{tag}: stem uses "{m.group(1)}"; JEE Advanced phrases it as "Then the value of ... is" (see references/style_guide.md)')
    if t == 'MTC' and 'Match each entry in List-I to the correct entry in List-II' not in text:
        errs.append(f'{tag}: matrix-match stem should say "Match each entry in List-I to the correct entry in List-II and choose the correct option."')
    if t == 'MCQ' and not (re.search(r'statement', text, re.I) and re.search(r'TRUE|correct', text)):
        errs.append(f'{tag}: multi-correct stem should end "which of the following statements is(are) TRUE?" (or "correct")')
    if t in ('PARA', 'PARA_NUM') and not (q.get('english') and q['english'][0].startswith('**Paragraph')):
        errs.append(f'{tag}: paragraph block should start with "**Paragraph for Questions 1 and 2:**"')
    if t == 'Numerical' and '______' not in text:
        errs.append(f'{tag}: numerical stem must end with a blank "______"')
    return errs, warns


def ratings_of(q):
    """List of rating dicts for a question: one for most types, two for PARA."""
    if q.get('type') in PARAS:
        return q.get('parts') or []
    return [q]


def validate(d):
    errs, warns = [], []
    qs = d.get('questions', [])
    if not qs:
        errs.append('no questions')
    for i, q in enumerate(qs, 1):
        tag = f'Q{i:02d}'
        t = q.get('type')
        for k in ('type', 'english', 'hindi', 'solution', 'solution_full'):
            if k not in q or q[k] in ('', None, []):
                errs.append(f'{tag}: missing "{k}"')
        if t not in INSTR:
            errs.append(f'{tag}: type must be one of {list(INSTR)}')
        rs = ratings_of(q)
        if t in PARAS and len(rs) != 2:
            errs.append(f'{tag}: {t} needs "parts" with exactly two rating objects')
        for j, r in enumerate(rs, 1):
            rt = tag + (f' part {j}' if t in PARAS else '')
            for k in RATING_KEYS:
                if k not in r or r[k] in ('', None, []):
                    errs.append(f'{rt}: missing "{k}"')
            if not isinstance(r.get('level'), int) or not 0 <= r.get('level', -1) <= 5:
                errs.append(f'{rt}: level must be an integer 0-5')
            elif q.get('target_level') is not None:
                gap = abs(r['level'] - q['target_level'])
                if gap >= 2:
                    errs.append(f'{rt}: rated level {r["level"]} but blueprint target is {q["target_level"]} - redesign the question')
                elif gap == 1:
                    warns.append(f'{rt}: rated level {r["level"]}, target {q["target_level"]} (one off: redesign once unless the rating is borderline)')
        for part in ('english', 'hindi', 'solution', 'solution_full'):
            for l in q.get(part, []):
                o = re.sub(r'\*\*', '', outside_math(l)).replace('______', '')
                if re.search(r'[%&#_^{}\\]', o):
                    errs.append(f'{tag} {part}: special character outside $...$ in: {l[:60]}')
                if l.count('$') % 2:
                    errs.append(f'{tag} {part}: odd number of $ in: {l[:60]}')
                if any(re.search(r'[\u0900-\u097F]', m) for m in split_math(l) if m.startswith('$')):
                    errs.append(f'{tag} {part}: Devanagari inside $...$ (the PDF font cannot draw it); move the Hindi word outside the maths: {l[:60]}')
        need = {'SCQ': 4, 'MCQ': 4, 'MTC': 4, 'PARA': 8}.get(t)
        if need:
            eo = [l for l in q.get('english', []) if OPT.match(l)]
            ho = [l for l in q.get('hindi', []) if OPT.match(l)]
            if len(eo) != need or len(ho) != need:
                errs.append(f'{tag}: {t} needs exactly {need} option lines "(A) ..." in English and in Hindi (found {len(eo)} / {len(ho)})')
            else:
                for a_, b_ in zip(eo, ho):
                    ma = [p for p in split_math(a_) if p.startswith('$')]
                    mb = [p for p in split_math(b_) if p.startswith('$')]
                    if sorted(ma) != sorted(mb):
                        warns.append(f'{tag}: option {a_[:3]} differs between English and Hindi')
        le, lw = lint(q, tag)
        errs += le
        warns += lw
        sol = [l for l in q.get('solution', []) if l]
        if not sol or not ANS.match(sol[-1]):
            errs.append(f'{tag}: solution must end with "Correct Option: (X)", "Correct Options: (X), (Y)" or "Final Answer: ..."')
        if t == 'PARA' and sum(1 for l in sol if re.match(r'^\*\*Correct Option for Question \d: \(', l)) != 2:
            errs.append(f'{tag}: PARA solution needs two lines "**Correct Option for Question 1: (X)**" and "...Question 2: (Y)**"')
        if t == 'PARA_NUM':
            if sum(1 for l in sol if re.match(r'^\*\*Final Answer for Question \d: ', l)) != 2:
                errs.append(f'{tag}: PARA_NUM solution needs two lines "**Final Answer for Question 1: x**" and "...Question 2: y**"')
            if any(OPT.match(l) for l in q.get('english', []) + q.get('hindi', [])):
                errs.append(f'{tag}: PARA_NUM questions have no options')
        full = [l for l in q.get('solution_full', []) if l]
        if full and not ANS.match(full[-1]):
            errs.append(f'{tag}solution_full must end with its answer line, like the shortened solution')
        if sol and full and extract_answers(sol, t) != extract_answers(full, t):
            errs.append(f'{tag}shortened and full solutions give different answers: {extract_answers(sol, t)} vs {extract_answers(full, t)}')
        if q.get('answer_plan'):
            for e in check_answers(q['answer_plan'], t, sol):
                errs.append(f'{tag}answer plan "{q["answer_plan"]}": {e}')
        else:
            warns.append(f'{tag}no answer_plan given; answer not checked against the plan')
        if not re.search(r'[\u0900-\u097F]', ' '.join(q.get('hindi', []))):
            errs.append(f'{tag}: Hindi text has no Devanagari')
        for part in ('english', 'hindi'):
            if any(ANS.match(l) for l in q.get(part, [])):
                errs.append(f'{tag}: answer line found inside the {part} question text')
    return errs, warns


def with_instruction(q):
    en, hi, _ = INSTR[q['type']]
    en = q.get('instruction_en', en)
    hi = q.get('instruction_hi', hi)
    return q['english'] + ['', en], q['hindi'] + ['', hi]


# ---------------------------------------------------------------- Word
def build_docx(d, path, tmp, key='solution', suffix=''):
    items = []
    for i, q in enumerate(d['questions'], 1):
        e, h = with_instruction(q)
        items.append({'number': f'{i:02d}', 'english': e, 'hindi': h, 'solution': q[key]})
    mj = os.path.join(tmp, 'master.json')
    json.dump({'title': d['title'] + suffix, 'questions': items}, open(mj, 'w', encoding='utf-8'), ensure_ascii=False)
    subprocess.run([sys.executable, BUILD_MASTER, mj, path], check=True)


# ---------------------------------------------------------------- PDF (XeLaTeX)
PRE = r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=2.2cm]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{fontspec}
\newfontfamily\hindifont[Script=Devanagari,Path=%s/,Extension=.ttf,BoldFont=NotoSansDevanagari-Bold]{NotoSansDevanagari}
\usepackage{titlesec}
\usepackage{xcolor}
\usepackage{needspace}
\titleformat{\section}{\large\bfseries}{}{0pt}{}[\vspace{-2pt}\hrule]
\titlespacing*{\section}{0pt}{16pt}{8pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\newcommand{\blank}{\underline{\hspace{1.6cm}}}
\newcommand{\lab}[1]{\par\vspace{6pt}{\small\bfseries\color{black!70}#1}\par\vspace{3pt}}
\begin{document}
'''


def tex_line(l):
    l = re.sub(r'\*\*(.+?)\*\*', lambda m: '@@B@@' + m.group(1) + '@@E@@', l)
    l = l.replace('______', '@@BLANK@@')
    l = l.replace('@@BLANK@@', r'\blank{}')
    return l.replace('@@B@@', r'\textbf{').replace('@@E@@', '}')


def hwrap(t):
    out = []
    for p in split_math(t):
        if p.startswith('$') and len(p) > 1:
            out.append(p)
        else:
            out.append(re.sub(r'[\u0900-\u097F]+(?:[ ,.:;\-\u0964]+[\u0900-\u097F]+)*',
                              lambda m: '{\\hindifont ' + m.group(0) + '}', p))
    return ''.join(out)


def para(lines, hindi=False):
    s = []
    for l in lines:
        if l == '':
            s.append(r'\vspace{5pt}')
            continue
        if l.strip() == '---':
            s.append(r'\vspace{3pt}\hrule\vspace{5pt}')
            continue
        t = tex_line(l)
        if hindi:
            t = hwrap(t)
        if OPT.match(l):
            s.append(r'\hspace{1.2em}' + t + r'\par\vspace{2pt}')
        elif ANS.match(l):
            s.append(r'\vspace{2pt}\textbf{' + t + r'}\par')
        else:
            s.append(t + r'\par\vspace{3pt}')
    return '\n'.join(s)


def write_tex(d, fn, mode, title):
    out = [PRE % FONTS.replace('\\', '/'), r'{\Large\bfseries ' + title + r'\par}\vspace{4pt}\hrule\vspace{6pt}']
    for i, q in enumerate(d['questions'], 1):
        e, h = with_instruction(q)
        out.append(r'\needspace{%d\baselineskip}' % (20 if mode == 'q' else 6))
        out.append(r'\section*{Question %02d}' % i)
        if mode == 'q':
            out += [r'\lab{English}', para(e), r'\lab{{\hindifont हिन्दी}}', para(h, True)]
        else:
            key = 'solution_full' if mode == 'qs_full' else 'solution'
            out += [r'\lab{English}', para(e), r'\lab{{\hindifont हिन्दी}}', para(h, True), r'\lab{Solution}', para(q[key])]
        out.append(r'\vspace{6pt}')
    out.append(r'\end{document}')
    open(fn, 'w', encoding='utf-8').write('\n'.join(out))


def build_pdf(d, path, mode, title, tmp):
    base = os.path.join(tmp, mode)
    write_tex(d, base + '.tex', mode, title)
    r = subprocess.run(['xelatex', '-interaction=nonstopmode', '-halt-on-error', '-output-directory', tmp, base + '.tex'],
                       capture_output=True, text=True)
    log = open(base + '.log', encoding='utf-8', errors='ignore').read() if os.path.exists(base + '.log') else r.stdout
    if r.returncode != 0 or not os.path.exists(base + '.pdf'):
        print(log[-2500:])
        sys.exit(f'xelatex failed for {mode}; see the log above (usually a bad LaTeX command inside $...$)')
    miss = re.findall(r'Missing character: (.*)', log)
    if miss:
        print('WARNING: missing glyphs in PDF:', sorted(set(miss))[:8])
    shutil.copy(base + '.pdf', path)


# ---------------------------------------------------------------- Excel (calibrated skill)
def build_excel(d, path, tmp):
    script = next((p for p in CALIB_CANDIDATES if os.path.exists(p)), None)
    if not script:
        print('NOTE: jee-advanced-difficulty-calibrated skill not found; Excel report skipped.')
        return False
    rows = []
    for i, q in enumerate(d['questions'], 1):
        rs = ratings_of(q)
        for j, r in enumerate(rs, 1):
            marks = r.get('marks', part_marks(q))
            rows.append({'sr_no': len(rows) + 1, 'paper': '', 'q_ref': f'Q{i:02d}' + (f'({"i" * j})' if q['type'] in PARAS else ''),
                         'type': CAL_TYPE[q['type']], 'chapter': q.get('chapter', d.get('concept', '')), 'marks': marks,
                         'level': r['level'], 'eq_relation': bool(r.get('eq_relation', q.get('eq_relation', False))),
                         'multi_concept': bool(r.get('multi_concept', q.get('multi_concept', False))),
                         'key_step': r['key_step'], 'justification': r['justification'],
                         'nearest_anchor': r['nearest_anchor'], 'confidence': r['confidence']})
    rj = os.path.join(tmp, 'ratings.json')
    json.dump({'source': d.get('title', 'practice set'), 'evaluated_on': d.get('date', ''), 'questions': rows},
              open(rj, 'w', encoding='utf-8'), indent=1)
    subprocess.run([sys.executable, script, rj, path], check=True)
    if os.path.exists(RECALC):
        subprocess.run([sys.executable, RECALC, path], capture_output=True)
    return True


def answer_report(d):
    """Print how the answers are spread, and warn when they look like the old Gemini habits."""
    from collections import Counter
    letters, mcq, nums = Counter(), [], []
    for q in d['questions']:
        t = q['type']
        for kind, v in extract_answers(q['solution'], t):
            if kind == 'option':
                if t == 'MCQ': mcq.append(''.join(v))
                else: letters[v[0]] += 1
            elif t in ('Numerical', 'PARA_NUM'):
                nums.append(v)
    print('Answers: single-correct letters', dict(sorted(letters.items())), '| multi-correct sets', mcq, '| numerical', nums)
    n = sum(letters.values())
    if n >= 4 and letters.get('A', 0) / n > 0.4:
        print('WARN too many single-correct answers are (A):', dict(letters))
    if len(mcq) >= 2 and sum(1 for m in mcq if m in ('ABC', 'ABCD')) / len(mcq) > 0.5:
        print('WARN multi-correct answers lean to ABC / ABCD:', mcq)
    if len(nums) >= 3:
        styles = {classify_number(x)[0] for x in nums}
        if len(styles) < 2:
            print('WARN numerical answers all look alike:', nums)


def summary(d):
    from collections import Counter
    rows = []
    for q in d['questions']:
        for r in ratings_of(q):
            marks = r.get('marks', part_marks(q))
            multi = bool(r.get('multi_concept', q.get('multi_concept', False)))
            rows.append((r['level'], marks, q['type'], 2.5 if q['type'] == 'MCQ' and multi else 0))
    cnt = Counter(l for l, _, _, _ in rows)
    tm = sum(m for _, m, _, _ in rows)
    wi = sum(m * max(l, fl) for l, m, _, fl in rows) / tm
    print('Levels:', dict(sorted(cnt.items())), '| formats:', dict(Counter(q['type'] for q in d['questions'])), f'| weighted index ~{wi:.2f} (before the equivalence-relation +0.5)')


def load_paper(path):
    """A set.json file, or a directory with meta.json + q*.json."""
    if os.path.isdir(path):
        meta = json.load(open(os.path.join(path, 'meta.json'), encoding='utf-8')) if os.path.exists(os.path.join(path, 'meta.json')) else {}
        files = sorted(f for f in os.listdir(path) if re.match(r'q\d+\.json$', f))
        meta['questions'] = [json.load(open(os.path.join(path, f), encoding='utf-8')) for f in files]
        return meta
    return json.load(open(path, encoding='utf-8'))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('set_json', help='paper directory (meta.json + q*.json) or a set.json file')
    ap.add_argument('outdir')
    ap.add_argument('--name', default=None)
    ap.add_argument('--no-excel', action='store_true')
    ap.add_argument('--blueprint', default=None, help='blueprint.json from make_blueprint.py check; every question must carry that row\'s concepts')
    a = ap.parse_args()
    d = load_paper(a.set_json)
    d.setdefault('title', 'JEE Mathematics Practice Paper')
    errs, warns = validate(d)
    if a.blueprint:
        bp = json.load(open(a.blueprint, encoding='utf-8'))
        if len(bp) != len(d['questions']):
            errs.append(f'blueprint has {len(bp)} questions but the paper has {len(d["questions"])}')
        for i, (row, q) in enumerate(zip(bp, d['questions']), 1):
            if list(q.get('blueprint_concepts') or []) != list(row['concepts']):
                errs.append(f'Q{i:02d}: blueprint_concepts {q.get("blueprint_concepts")} differ from the blueprint row {row["concepts"]}')
            if q.get('type') and row.get('type_code') and q['type'] != row['type_code']:
                errs.append(f'Q{i:02d}: question type {q["type"]} differs from the blueprint type {row["type_code"]}')
    else:
        warns.append('no --blueprint given: concepts were not cross-checked against the blueprint')
    for w in warns:
        print('WARN', w)
    if errs:
        print('\n'.join('ERROR ' + e for e in errs))
        sys.exit(f'{len(errs)} problem(s) in the set file; fix them and rerun (nothing was built)')
    name = a.name or re.sub(r'[^A-Za-z0-9]+', '_', d.get('title', 'Question_Paper')).strip('_')
    os.makedirs(a.outdir, exist_ok=True)
    tmp = tempfile.mkdtemp()
    build_docx(d, os.path.join(a.outdir, f'{name}_Shortened_Solutions.docx'), tmp, 'solution', ' - Shortened Solutions')
    build_docx(d, os.path.join(a.outdir, f'{name}_Full_Solutions.docx'), tmp, 'solution_full', ' - Full Solutions')
    build_pdf(d, os.path.join(a.outdir, f'{name}_Questions_EN_HI.pdf'), 'q', d['title'] + ': Questions', tmp)
    build_pdf(d, os.path.join(a.outdir, f'{name}_Questions_and_Shortened_Solutions.pdf'), 'qs_short',
              d['title'] + ': Questions and Shortened Solutions', tmp)
    build_pdf(d, os.path.join(a.outdir, f'{name}_Questions_and_Full_Solutions.pdf'), 'qs_full',
              d['title'] + ': Questions and Full Solutions', tmp)
    answer_report(d)
    if not a.no_excel:
        build_excel(d, os.path.join(a.outdir, f'{name}_difficulty.xlsx'), tmp)
    summary(d)
    print('Done ->', a.outdir)


if __name__ == '__main__':
    main()
