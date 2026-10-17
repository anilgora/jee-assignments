#!/usr/bin/env python3
"""Render the whole chapter kit from a chapter spec.

Usage:
  python render_kit.py --spec chapter_spec.json --qmap question_map.json --qindex question_index.json --out OUTDIR
Optional: --workdir DIR (LaTeX scratch), --only quick,notes,formula,mindmap,flow,excel

Produces (EN and HI, each file separate):
  <Slug>_Quick_Review_<batch>_<EN|HI>.docx/.pdf   graded + practice map, one per batch (native 2D Word equations)
  <Slug>_Short_Notes_<EN|HI>.docx/.pdf
  <Slug>_Formula_Sheet_<EN|HI>.docx/.pdf          two columns
  <Slug>_Mind_Map_<EN|HI>.pdf  (+ .png)
  <Slug>_Method_Flowcharts_<EN|HI>.pdf
  <Slug>_Question_Mapping.xlsx, REPORT.md
"""
import argparse, os, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit_common import pick
import kit_grading as G, kit_docx as D, kit_pdf as PDF
from omml import Math


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--spec', required=True); ap.add_argument('--qmap', required=True); ap.add_argument('--qindex', required=True)
    ap.add_argument('--out', required=True); ap.add_argument('--workdir', default=None); ap.add_argument('--only', default='quick,notes,formula,mindmap,flow,excel')
    a = ap.parse_args()
    only = set(a.only.split(','))
    os.makedirs(a.out, exist_ok=True)
    work = a.workdir or tempfile.mkdtemp(prefix='kit_')
    spec, qmap, qidx = G.load(a.spec, a.qmap, a.qindex)
    ch = spec['chapter']; slug = ch['slug']
    problems = G.validate(spec, qmap, qidx)
    for p in problems: print('WARNING:', p)
    fatal = [p for p in problems if 'unknown item id' in p or 'unresolved xref' in p or 'duplicate' in p]
    if fatal: sys.exit('Fix these before rendering:\n' + '\n'.join(fatal))
    G.numbering(spec)
    ctxs = {b: G.batch_context(spec, qmap, qidx, b) for b in spec['batches']}
    for b, c in ctxs.items(): print(f"batch {b}: graded questions {c['ngraded']}, High threshold {c['hi']}")

    # one pandoc call for every equation that appears in a Word file
    texts = []
    for part in ('quick_review', 'notes', 'formula'):
        for sec in spec[part]['sections']:
            texts += [sec['en'], sec['hi']]
    for sec in spec['quick_review']['sections']:
        for it in sec['items']:
            texts += [pick(it['q'], 'en'), pick(it['q'], 'hi')]
            for l in it['a']: texts += [pick(l, 'en'), pick(l, 'hi')]
    for s in spec['notes']['sections']:
        for k, ls in s['blocks']:
            for l in ls: texts += [pick(l, 'en'), pick(l, 'hi')]
    for s in spec['formula']['sections']:
        for l in s['lines']: texts += [pick(l, 'en'), pick(l, 'hi')]
    import re
    texts = [re.sub(r'\{#\d+\}', '0', t) for t in texts]
    M = Math(texts)
    print('equations converted to native Word equations:', len(M.map))

    LANGS = {'en': 'EN', 'hi': 'HI'}
    for lang, L in LANGS.items():
        ce, chn = ch['en'], ch['hi']; name = ce if lang == 'en' else chn
        if 'quick' in only:
            for b, ctx in ctxs.items():
                title = (f"JEE Mathematics: Quick Review with Grading and Practice Map - {ce} (Batch {b})" if lang == 'en'
                         else f"JEE गणित: त्वरित पुनरावृत्ति (श्रेणी तथा अभ्यास मानचित्र सहित) - {chn} (बैच {b})")
                if ctx.get('dpp_only'):    # DPP-only chapter: no batch in the title
                    title = (f"JEE Mathematics: Quick Review with Grading and Practice Map - {ce}" if lang == 'en'
                             else f"JEE गणित: त्वरित पुनरावृत्ति (श्रेणी तथा अभ्यास मानचित्र सहित) - {chn}")
                base = os.path.join(a.out, f'{slug}_Quick_Review_{b}_{L}')
                D.build_quick_review(spec, ctx, lang, M, base + '.docx', {'en': title, 'hi': title})
                PDF.build_quick_review(spec, ctx, lang, base + '.pdf', title, work, b)
        if 'notes' in only:
            title = f'{ce}: Short Notes' if lang == 'en' else f'{chn}: संक्षिप्त नोट्स'
            base = os.path.join(a.out, f'{slug}_Short_Notes_{L}')
            D.build_notes(spec, lang, M, base + '.docx', title); PDF.build_notes(spec, lang, base + '.pdf', title, work)
        if 'formula' in only:
            title = f'{ce}: Formula Sheet' if lang == 'en' else f'{chn}: सूत्र-पत्र'
            base = os.path.join(a.out, f'{slug}_Formula_Sheet_{L}')
            D.build_formula(spec, lang, M, base + '.docx', title); PDF.build_formula(spec, lang, base + '.pdf', title, work)
        if 'mindmap' in only:
            base = os.path.join(a.out, f'{slug}_Mind_Map_{L}')
            PDF.build_mindmap(spec, lang, base + '.pdf', name, 'Mind map' if lang == 'en' else 'माइंड मैप', work, base + '.png')
        if 'flow' in only:
            PDF.build_flowcharts(spec, lang, os.path.join(a.out, f'{slug}_Method_Flowcharts_{L}.pdf'), work)
    if 'excel' in only:
        xl = os.path.join(a.out, f'{slug}_Question_Mapping.xlsx')
        G.build_excel(spec, qmap, qidx, ctxs, xl)
        rc = '/mnt/skills/public/xlsx/scripts/recalc.py'          # fills the cached formula values (best effort)
        if os.path.exists(rc):
            import subprocess
            subprocess.run([sys.executable, rc, xl, '90'], capture_output=True, text=True)
    G.build_report(spec, qmap, qidx, ctxs, problems, os.path.join(a.out, 'REPORT.md'))
    print('done ->', a.out)


if __name__ == '__main__':
    main()
