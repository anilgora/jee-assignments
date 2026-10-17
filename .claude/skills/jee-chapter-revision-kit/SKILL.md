---
name: jee-chapter-revision-kit
description: Build the full revision kit for ONE JEE Mathematics chapter - a graded Quick Review (with a practice map of sheet / DPP / JEE Main Question Bank questions) for batch XII and for batch XIII, short notes, a two-column formula sheet, a mind map and method flowcharts, each in English and Hindi, Word files with native 2D equations plus PDFs. Works interactively or as an unattended scheduled routine (no questions asked). The chapter's Quick Review prompt list comes from the all-chapters master Quick Review saved with this skill, so only the chapter name and that chapter's sheets are needed. Use whenever the user names a JEE maths chapter and supplies or points to its theory sheet, XII / XIII exercise sheets (J-I, J-II, J-M, J-A, Challenger), DPP or JEE Main question bank and asks for the quick review, revision kit, short notes, formula sheet, mind map or flowcharts - or when a scheduled routine says to run the chapter kit for a named chapter.
---

# JEE chapter revision kit

Claude does the thinking (read the material, write the content, map the questions); the scripts in `scripts/` do all file production.
A finished worked example (Quadratic Equation) is in `examples/quadratic_equation/`. **Never stop to ask the user in routine mode** - decide, and list every uncertain decision in `REPORT.md`.

## What one run produces (per chapter)

| Product | Files |
|---|---|
| Quick Review, graded + practice map, one per batch | `<Slug>_Quick_Review_<XII|XIII>_<EN|HI>.docx` + `.pdf` |
| Short notes (no worked examples, tight spacing, all key points) | `<Slug>_Short_Notes_<EN|HI>.docx` + `.pdf` |
| Formula sheet, two columns | `<Slug>_Formula_Sheet_<EN|HI>.docx` + `.pdf` |
| Mind map / method flowcharts | `<Slug>_Mind_Map_<EN|HI>.pdf` (+ png), `<Slug>_Method_Flowcharts_<EN|HI>.pdf` - PDF only |
| Internal | `<Slug>_Question_Mapping.xlsx`, `REPORT.md`, `hindi_glossary_additions.md` |

English and Hindi are separate files. Colour is fine. Word files carry native 2D equations (never LaTeX text). No ungraded Quick Review. The grade is coloured text (High / Medium / Low), no symbols.
One chapter per run (the question mapping alone covers 300+ questions).

## Where things live (routine layout - ask the user once if theirs differs)

```
jee-inputs/quick_review_all_chapters.pdf     master Quick Review (scan) - only needed when it changed or a chapter is missing from the saved index
jee-inputs/master_index.json                 optional: overrides references/master_index.json
jee-inputs/hindi_glossary.md                 optional: overrides/extends references/hindi_glossary.md
chapters/<Chapter_Name>/                     theory sheet, XII sheet, XIII sheet, DPP (optional), Question Bank (optional)  - identify files by content/name (XII, XIII, DPP, QB)
chapters/<Chapter_Name>/kit/                 outputs of this run
```
The skill cannot be re-saved by a routine: everything that changes between runs (master index, glossary additions) is written to the repo, never into the skill folder.

## Routine procedure

0. **Tools.** `python scripts/check_tools.py`. If it fails, write `RUN_FAILED.md` (what is missing, how to install) in the output folder and stop.
1. **Chapter + inputs.** Chapter name from the run prompt (else the next `chapters/*` folder without `kit/`). Required there: theory sheet, XII sheet, XIII sheet. DPP / QB optional (skip that part). Anything required missing -> `RUN_FAILED.md`.
2. **Prompt list.** `python scripts/chapter_prompts.py <index> "<Chapter>" --out WORK [--pdf master.pdf]` (index = `jee-inputs/master_index.json` if present, else `references/master_index.json`).
   Chapter not in the index and the master PDF is present -> `python scripts/split_master.py --pdf master.pdf --out WORK/master_index.json --workdir WORK/ocr --time-budget 240`
   (resumable: repeat until it exits 0; ~4 s/page), re-proof the chapter, and write the new index + `.review.md` to `jee-inputs/`. No PDF either -> `RUN_FAILED.md`.
   The OCR text is reliable for plain words only; **math-heavy prompts must be read from the page image** (`--pdf` renders the chapter pages; the index gives the page range). Keep the master's wording and numbering.
3. **Index the questions:** `python scripts/extract_questions.py --reference-sheet XII.pdf --batch XII=XII.pdf --batch XIII=XIII.pdf [--dpp DPP.pdf] [--qb QB.pdf] --out question_index.json`; check counts against the sheets' contents pages.
   `python scripts/detect_overlaps.py question_index.json` -> QB questions equal to a batch's JM go into `qb_overlap`. XII is the reference for every exercise except J-M; XIII is used only for its J-M.
4. **Baseline Quick Review** from the master prompts (one item per prompt, same headings, `o` = master number). Rephrase only ambiguous prompts (tag `rephrased`). Short model answer from the theory sheet (EN + HI): 1-3 lines + one `Ex:` line; verify every example with sympy.
5. **Map every question** (all sheet exercises incl. Challenger, both J-M sets, JA, DPP, QB) to item ids - rules in `references/authoring_guide.md`.
6. **Coverage check** (exclude Challenger): a concept needed by non-Challenger questions that no item covers is a candidate new item.
   **Cross-chapter rule: if the concept is already covered in ANY chapter of the master Quick Review (as a heading or prompt), do not add it here.** Check every candidate with
   `python scripts/search_master.py <index> "keyword" "other keywords"` (try synonyms); only add when nothing matches. Candidates not added go into REPORT.md as "covered in <chapter> / <heading>", and the questions that needed them are mapped to the nearest existing item or `-`.
   Added items: tag `added`, ids `N1...`, under the matching heading else Miscellaneous.
7. **Companion content** in the spec (EN + HI): short notes, formula sheet, mind map, flowcharts. Hindi per `references/hindi_glossary.md`.
8. **Write** `chapter_spec.json`, `question_map.json`, `question_index.json` (`references/spec_schema.md`).
9. **Render:** `python scripts/render_kit.py --spec ... --qmap ... --qindex ... --out chapters/<Chapter>/kit --workdir WORK`; fix every WARNING; `python scripts/verify_outputs.py <out> <Slug> XII,XIII`;
   `python /mnt/skills/public/docx/scripts/office/validate.py <docx>` when that script exists. Rasterise a few pages of each product and look at them (Word equations do not preview in LibreOffice - trust the verifier).
10. **Report** = `REPORT.md` (written by the renderer) + your additions: added / rephrased items with source questions, candidates dropped because another chapter covers them, graded counts and High thresholds per batch, High items, unmapped questions,
    overlaps counted once, new Hindi terms (also to `hindi_glossary_additions.md`), source errors found, and every uncertain decision.

## Fixed rules

- **Grading:** graded = the batch's J-M + J-A + QB (QB questions equal to the batch's JM count once). J-I, J-II, DPP, Challenger are mapped but not graded; Challenger is not used for coverage. A question counts for its main item and every "other" item.
  High = count >= max(2, round(0.091 x graded questions)); Medium = 1 up to High; Low = 0 (means only "not tested in these questions").
- **Practice map** at the end of every Quick Review item: main-concept questions and also-used questions, grouped Sheet / DPP / Question Bank, with the batch's own J-M.
- **Short notes:** no worked examples; keep all key points; Formulas box, Key points, Steps, Watch out (only what the topic needs).
- **Hindi:** write it yourself with the glossary; same formulas; no English words outside math except JM, JA, DPP, QB, H.P. and similar; never Hindi inside `\text{}`.
- Every formula and example comes from the user's sheets or is verified. Do not invent.

## Limits to state honestly

Mapping is judgement (figure questions and garbled stems are the weak spots). Master prompts with math can differ slightly from the printed wording unless read from the image.
Word equations are pandoc-converted OMML (schema-valid; previewable only in Word).
