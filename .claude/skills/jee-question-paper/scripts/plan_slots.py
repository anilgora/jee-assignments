#!/usr/bin/env python3
"""Step 1. Validate input_config.xlsx and create the question slots (chapter, type, difficulty).

Usage:  python plan_slots.py input_config.xlsx WORKDIR [--pattern main|advanced|auto] [--seed N] [--exclude PREV_BLUEPRINT.xlsx ...]

--pattern auto (default) infers the pattern from the config (see common.detect_pattern) and prints why.
--exclude lists blueprints of earlier papers of the same phase, OLDEST FIRST. Their concepts are taken out of the
fresh pool; when a chapter runs out, concepts are reused earliest-used first (reuse_order.json).

Writes WORKDIR/slots.json and WORKDIR/chapter_concepts.json (concepts of the paper's chapters only)
and prints the pairing targets. Questions are ordered by type: Main = Single Correct then Numerical; Advanced = Single Correct, One-or-more Correct,
Paragraph, Matrix Match, Integer, Numerical. Each question also gets a planned answer (option letter, option set, integer digit or numerical style) so answers
cannot drift to A / ABC / single digits. Concept choice is NOT done here: Claude picks natural-synergy
concepts (see references/synergy_guide.md) and passes them to make_blueprint.py.
"""
import argparse, json, math, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('config'); ap.add_argument('workdir')
    ap.add_argument('--pattern', choices=['main', 'advanced', 'auto'], default='auto')
    ap.add_argument('--exclude', nargs='*', default=[], help='earlier blueprints of the same phase')
    ap.add_argument('--seed', type=int, default=None)
    a = ap.parse_args()
    cfg = load_config(a.config)
    errs, _ = check_config(cfg)
    if errs:
        sys.exit('ERROR in input_config:\n  ' + '\n  '.join(errs))
    pattern = a.pattern
    if pattern == 'auto':
        pattern, why = detect_pattern(cfg)
        if pattern is None:
            sys.exit('Cannot tell Main from Advanced from this config (' + '; '.join(why) + '). Ask the user and rerun with --pattern.')
        print(f'Pattern inferred: {pattern.upper()} ({"; ".join(why)}). Confirm with the user if the paper name or phase says otherwise.')
    a.pattern = pattern
    used = used_concepts(a.exclude)
    rnd = random.Random(a.seed)
    n = sum(cfg['chapters'].values())
    chs, dfs, qts = [], [], []
    for k, c in cfg['chapters'].items(): chs += [k] * c
    for k, c in cfg['difficulties'].items(): dfs += [canon_level(k)] * c
    for k, c in cfg['qtypes'].items(): qts += [k] * c
    for l in (chs, dfs, qts): rnd.shuffle(l)
    slots = [{'sr': i + 1, 'chapter': chs[i], 'q_type': qts[i], 'type_code': type_code(qts[i]),
              'difficulty': dfs[i], 'target_level': LEVEL_OF[dfs[i]]} for i in range(n)]
    # question order by pattern (stable: the shuffle decides the order inside each type)
    slots.sort(key=lambda s: type_rank(s['type_code'], a.pattern))
    for i, s in enumerate(slots, 1):
        s['sr'] = i
    plans = make_answer_plans([s['type_code'] for s in slots], rnd)
    for s, p in zip(slots, plans):
        s['answer_plan'] = p
    os.makedirs(a.workdir, exist_ok=True)
    plan = {'pattern': a.pattern, 'n': n, 'slots': slots, 'excluded_sources': a.exclude}
    if a.pattern == 'main':
        s = round(0.2 * n); sm = round(0.4 * n); plan['targets'] = {'single': s, 'same_chapter': sm, 'cross_chapter': n - s - sm}
    else:
        plan['targets'] = {'min_cross_chapter': math.ceil(0.4 * n), 'min_concepts_per_question': 2, 'min_three_concept_questions': 2}
    json.dump(plan, open(os.path.join(a.workdir, 'slots.json'), 'w'), indent=1)
    avail = {c: [x for x in cfg['concepts'][c] if x not in used] for c in cfg['chapters']}
    json.dump(avail, open(os.path.join(a.workdir, 'chapter_concepts.json'), 'w'), indent=1, ensure_ascii=False)
    reuse = {c: sorted([x for x in cfg['concepts'][c] if x in used], key=lambda x: used[x][1]) for c in cfg['chapters']}
    json.dump(reuse, open(os.path.join(a.workdir, 'reuse_order.json'), 'w'), indent=1, ensure_ascii=False)
    print(f'{n} questions | pattern: {a.pattern}')
    if a.pattern == 'main':
        t = plan['targets']
        print(f"Pairing targets (judgement allowed, +-1 each): single {t['single']}, same chapter {t['same_chapter']}, different chapters {t['cross_chapter']}")
    else:
        t = plan['targets']
        print(f"Advanced: every question has 2-3 concepts; at least {t['min_three_concept_questions']} questions have three; at least {t['min_cross_chapter']} of {n} mix different chapters")
    for c, q in cfg['chapters'].items():
        left, total = len(avail[c]), len(cfg['concepts'][c])
        note = ''
        if left < q:
            note = '  <-- fewer fresh concepts than questions: reuse earliest-used first (reuse_order.json); avoid repeating a pair'
        elif left < 2 * q:
            note = '  <-- running low'
        if used or note:
            print(f'  {c}: {left} of {total} concepts fresh ({q} questions as main chapter){note}')
    if used:
        print(f'{len(used)} concepts were used in earlier papers of this phase and are out of the fresh pool.')
    print('Chapters in this paper (partners for cross-chapter pairs come only from these):', list(cfg['chapters']))
    for s in slots:
        print(f"  {s['sr']:>2}. {s['chapter']:<28} {s['type_code']:<9} L{s['target_level']}  {s['difficulty']:<42} answer: {s['answer_plan']}")


if __name__ == '__main__':
    main()
