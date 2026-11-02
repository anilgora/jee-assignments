"""Shared helpers for the question-paper skill: config loading, label maps, chapter grouping."""
import difflib, os, sys
import pandas as pd

# The six difficulty labels used in input_config.xlsx -> the user's calibrated 0-5 scale
LEVEL_OF = {
    'Easier Than JEE Main Level': 0,
    'JEE Main Level': 1,
    'A little easier than JEE Advanced': 2,
    'Default Difficult': 3,
    'A little more difficult than JEE Advanced': 4,
    'Very difficult than JEE Advanced': 5,
}
_LOWER = {k.lower(): k for k in LEVEL_OF}

# Question-type labels in input_config.xlsx -> internal code used by build_paper.py
TYPE_OF = {
    'single correct type': 'SCQ',
    'one or more than one correct type': 'MCQ',
    'paragraph based two single correct type questions': 'PARA',
    'numerical type': 'Numerical',
    'integer type(0 to 9)': 'INT',
    'matrix match': 'MTC',
}

# Chapters that count as ONE chapter for the same-chapter / cross-chapter rule.
# (Vector and 3D are one chapter. Matrices vs Determinants, and DE / Area vs an integration
# technique, are DIFFERENT chapters, which is already true of the sheet's chapter names.)
SAME_GROUPS = [{'Vector 3D', 'Vector', '3D Geometry', 'Vector and 3D'}]


def canon_level(label):
    """Difficulty label (exact config wording, or a plain level 0-5 / 'Level 3') -> canonical label, or None."""
    t = str(label).strip().lower()
    if t in _LOWER:
        return _LOWER[t]
    import re as _re
    m = _re.fullmatch(r'(?:level\s*)?([0-5])(?:\.0)?', t)
    if m:
        want = int(m.group(1))
        return next(k for k, v in LEVEL_OF.items() if v == want)
    return None


def type_code(label):
    """Question-type label (exact config wording or a common short form) -> code, or None."""
    t = str(label).strip().lower()
    if not t:
        return None
    if t in TYPE_OF:
        return TYPE_OF[t]
    if 'paragraph' in t or 'passage' in t:
        return 'PARA_NUM' if ('numerical' in t or 'numeric' in t) else 'PARA'
    if 'matrix' in t or 'match' in t or t == 'mtc':
        return 'MTC'
    if 'integer' in t or t in ('int',):
        return 'INT'
    if 'numerical' in t or 'numeric' in t:
        return 'Numerical'
    if 'one or more' in t or 'multiple correct' in t or 'multi' in t or t in ('mcq',):
        return 'MCQ'
    if 'single' in t or t in ('scq', 'mcq single'):
        return 'SCQ'
    return None


ADV_ONLY_TYPES = {'MCQ', 'PARA', 'PARA_NUM', 'MTC', 'INT'}


def detect_pattern(cfg):
    """Guess 'main' or 'advanced' from the config. Returns (pattern or None, reasons)."""
    codes = {type_code(t) for t, c in cfg['qtypes'].items() if c > 0}
    levels = [LEVEL_OF[canon_level(d)] for d, c in cfg['difficulties'].items() if c > 0 and canon_level(d)]
    adv_types = sorted(codes & ADV_ONLY_TYPES)
    hard = any(l >= 4 for l in levels)
    if adv_types or hard:
        why = []
        if adv_types: why.append('Advanced-only question types present: ' + ', '.join(adv_types))
        if hard: why.append('questions at level 4-5 present')
        return 'advanced', why
    if codes <= {'SCQ', 'Numerical'}:
        return 'main', ['only Single Correct and Numerical types, no question above level 3']
    return None, ['could not tell']


def same_chapter(a, b):
    if a == b:
        return True
    return any(a in g and b in g for g in SAME_GROUPS)


def load_config(path):
    if not os.path.exists(path):
        sys.exit(f"Cannot find '{path}'.")
    x = lambda s: pd.read_excel(path, sheet_name=s)
    ch = x('Chapters').dropna(subset=['Chapter', 'Count'])
    df = x('Difficulties').dropna(subset=['Difficulty Level', 'Count'])
    qt = x('QTypes').dropna(subset=['Question Type', 'Count'])
    cn = x('Concepts').dropna(subset=['Chapter', 'Concept'])
    strip = lambda s: s.astype(str).str.strip()
    ch['Chapter'] = strip(ch['Chapter']); df['Difficulty Level'] = strip(df['Difficulty Level'])
    qt['Question Type'] = strip(qt['Question Type']); cn['Chapter'] = strip(cn['Chapter']); cn['Concept'] = strip(cn['Concept'])
    cfg = {
        'chapters': dict(zip(ch['Chapter'], ch['Count'].astype(int))),          # order = sheet order
        'difficulties': dict(zip(df['Difficulty Level'], df['Count'].astype(int))),
        'qtypes': dict(zip(qt['Question Type'], qt['Count'].astype(int))),
        'concepts': {c: g['Concept'].tolist() for c, g in cn.groupby('Chapter', sort=False)},
    }
    return cfg


def check_config(cfg):
    """Return (errors, warnings) for an input_config."""
    errs, warns = [], []
    tot = {k: sum(cfg[k].values()) for k in ('chapters', 'difficulties', 'qtypes')}
    if len(set(tot.values())) != 1:
        errs.append(f'Totals differ: chapters={tot["chapters"]}, difficulties={tot["difficulties"]}, question types={tot["qtypes"]}. All three must be equal.')
    for d in cfg['difficulties']:
        if canon_level(d) is None:
            errs.append(f'Unknown difficulty label "{d}". Known: {list(LEVEL_OF)}')
    for t in cfg['qtypes']:
        if type_code(t) is None:
            errs.append(f'Unsupported question type "{t}". Known: {list(TYPE_OF)}')
    for c in cfg['chapters']:
        if c not in cfg['concepts']:
            errs.append(f'Chapter "{c}" has no rows in the Concepts sheet.')
    return errs, warns


def suggest(name, options):
    m = difflib.get_close_matches(name, options, n=3, cutoff=0.5)
    return f' Did you mean: {m}?' if m else ''


def _concept_cols(df):
    return [c for c in df.columns if str(c).replace(' ', '').lower() in ('concept1', 'concept2', 'concept3')]


def used_concepts(paths):
    """Concepts used in earlier blueprints -> (file name, rank). Rank 0 is the earliest use.
    Pass the blueprints OLDEST FIRST; within a file the row order (Sr No) counts."""
    used, rank = {}, 0
    for p in paths or []:
        df = pd.read_excel(p).fillna('')
        cols = _concept_cols(df)
        for _, row in df.iterrows():
            for col in cols:
                v = str(row[col]).strip()
                if v and v not in used:
                    used[v] = (os.path.basename(p), rank)
                    rank += 1
    return used


def used_pairs(paths):
    """Concept sets (2 or more concepts) used together in earlier blueprints."""
    pairs = {}
    for p in paths or []:
        df = pd.read_excel(p).fillna('')
        cols = _concept_cols(df)
        for _, row in df.iterrows():
            cs = frozenset(str(row[c]).strip() for c in cols if str(row[c]).strip())
            if len(cs) >= 2:
                pairs.setdefault(cs, os.path.basename(p))
    return pairs


# ------------------------------------------------------------------ answer planning
# The answer of every question is PLANNED before the question is written, so that answers cannot drift to
# "A", "ABC/ABCD" or single digits (the habit of the old Gemini script). The plan is shown in the blueprint
# (column "Answer Plan") and checked against each question's solution when the paper is built.
import itertools, random as _random, re as _re

NUM_STYLES = ['positive 2-digit integer', 'positive 3-digit integer', 'negative integer',
              'positive decimal', 'negative decimal', 'decimal between 0 and 1']
# {A,B,C} and {A,B,C,D} are left out of the random pool: they were the old Gemini habit. Set them by hand in the blueprint if wanted.
_SUBSETS = [list(c) for r in (1, 2, 3, 4) for c in itertools.combinations('ABCD', r) if ''.join(c) not in ('ABC', 'ABCD')]


def make_answer_plans(type_codes, rnd):
    """type_codes: question type codes in paper order. Returns one plan string per question."""
    letters = []
    need = sum({'SCQ': 1, 'MTC': 1, 'PARA': 2}.get(t, 0) for t in type_codes)
    while len(letters) < need:
        b = list('ABCD'); rnd.shuffle(b); letters += b
    subsets = list(_SUBSETS); rnd.shuffle(subsets)
    digits = []
    styles = []
    def next_digit():
        nonlocal digits
        if not digits:
            digits = list(range(10)); rnd.shuffle(digits)
        return digits.pop()
    def next_style():
        nonlocal styles
        if not styles:
            styles = list(NUM_STYLES); rnd.shuffle(styles)
        return styles.pop()
    li = si = 0
    out = []
    for t in type_codes:
        if t in ('SCQ', 'MTC'):
            out.append(f'Option {letters[li]}'); li += 1
        elif t == 'PARA':
            out.append(f'Q1: Option {letters[li]}; Q2: Option {letters[li + 1]}'); li += 2
        elif t == 'MCQ':
            s = subsets[si % len(subsets)]; si += 1
            out.append('Options ' + ', '.join(s))
        elif t == 'INT':
            out.append(f'Integer {next_digit()}')
        elif t == 'Numerical':
            out.append(next_style())
        elif t == 'PARA_NUM':
            out.append(f'Q1: {next_style()}; Q2: {next_style()}')
        else:
            out.append('')
    return out


def parse_plan(text):
    """Plan string -> list of parts: {'kind': 'option', 'letters': [...]} | {'kind': 'int', 'value': n} | {'kind': 'num', 'style': s}."""
    text = str(text or '').strip()
    if not text:
        return []
    parts = []
    for seg in [s.strip() for s in text.split(';') if s.strip()]:
        seg = _re.sub(r'^Q\d:\s*', '', seg)
        m = _re.match(r'^Options?\s+([A-D](?:\s*,\s*[A-D])*)$', seg)
        if m:
            parts.append({'kind': 'option', 'letters': sorted(_re.findall('[A-D]', m.group(1)))}); continue
        m = _re.match(r'^Integer\s+(\d)$', seg)
        if m:
            parts.append({'kind': 'int', 'value': int(m.group(1))}); continue
        if seg in NUM_STYLES:
            parts.append({'kind': 'num', 'style': seg}); continue
        parts.append({'kind': 'bad', 'text': seg})
    return parts


def extract_answers(sol_lines, type_code):
    """Answer strings found in a solution, one per part (letters sorted for options)."""
    ans = []
    for l in sol_lines:
        t = l.replace('**', '').strip()
        m = _re.match(r'^Correct Options?(?: for Question \d)?:\s*(.+)$', t)
        if m:
            ans.append(('option', sorted(_re.findall(r'\(([A-D])\)', m.group(1)))))
            continue
        m = _re.match(r'^Final Answer(?: for Question \d)?:\s*(.+)$', t)
        if m:
            ans.append(('value', m.group(1).strip()))
    if type_code in ('SCQ', 'MTC', 'MCQ', 'INT', 'Numerical'):
        return ans[-1:]
    return ans[-2:]


def classify_number(s):
    """Return (style or None, problem or None) for a numerical answer string."""
    s = str(s).replace('$', '').replace('\\,', '').replace(' ', '')
    try:
        v = float(s)
    except ValueError:
        return None, f'"{s}" is not a plain number'
    frac = s.split('.')[1] if '.' in s else ''
    if len(frac) > 2:
        return None, f'"{s}" has more than two decimal places'
    is_int = abs(v - round(v)) < 1e-9 and (not frac or int(frac) == 0)
    if is_int:
        n = int(round(v))
        if n < 0: return 'negative integer', None
        if 10 <= n <= 99: return 'positive 2-digit integer', None
        if 100 <= n <= 999: return 'positive 3-digit integer', None
        return f'integer {n}', None
    if v < 0: return 'negative decimal', None
    return ('decimal between 0 and 1' if v < 1 else 'positive decimal'), None


def check_answers(plan_text, type_code, sol_lines):
    """Errors (list of str) when a solution's answer does not match the planned answer."""
    parts = parse_plan(plan_text)
    if not parts:
        return []
    got = extract_answers(sol_lines, type_code)
    errs = []
    if len(got) != len(parts):
        return [f'solution has {len(got)} answer line(s), the plan has {len(parts)}']
    for i, (p, (gk, gv)) in enumerate(zip(parts, got), 1):
        tag = f'part {i}: ' if len(parts) > 1 else ''
        if p['kind'] == 'option':
            if gk != 'option' or gv != p['letters']:
                errs.append(f'{tag}answer is {gv if gk == "option" else gv} but the plan says {"".join(p["letters"])}')
        elif p['kind'] == 'int':
            try:
                ok = gk == 'value' and int(float(gv)) == p['value'] and float(gv) == int(float(gv))
            except ValueError:
                ok = False
            if not ok:
                errs.append(f'{tag}answer is {gv} but the plan says integer {p["value"]}')
        elif p['kind'] == 'num':
            if gk != 'value':
                errs.append(f'{tag}expected a numerical answer'); continue
            style, prob = classify_number(gv)
            if prob:
                errs.append(f'{tag}{prob}')
            elif style != p['style']:
                errs.append(f'{tag}answer {gv} is a "{style}" but the plan says "{p["style"]}"')
        else:
            errs.append(f'{tag}cannot read plan "{p.get("text")}"')
    return errs


# ------------------------------------------------------------------ question order (user's instruction, 18-Oct-2026)
# Main:     Single Correct first, then Numerical.
# Advanced: Single Correct, One-or-more Correct, Paragraph, Matrix Match, Integer, Numerical.
ORDER = {
    'main': ['SCQ', 'Numerical', 'INT'],
    'advanced': ['SCQ', 'MCQ', 'PARA', 'PARA_NUM', 'MTC', 'INT', 'Numerical'],
}


def type_rank(code, pattern):
    o = ORDER[pattern]
    return o.index(code) if code in o else len(o)
