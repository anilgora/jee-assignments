---
name: "jee-question-paper"
description: Generate a complete JEE Mathematics question paper (JEE Main or JEE Advanced pattern) from the user's input_config.xlsx - first a reviewable blueprint Excel with natural-synergy concept pairing (20% single / 40% same-chapter / 40% different-chapter for JEE Main; two or three linked concepts for JEE Advanced), then, after the user approves the blueprint, every question one by one with English and Hindi text, a shortened verified solution, and a difficulty rating on the user's calibrated 0-5 scale. Delivers the Master Question Paper Word file, a questions PDF and a questions-with-solutions PDF (2D equations) and an internal difficulty Excel. Use whenever the user uploads or mentions input_config.xlsx, a question paper blueprint, "generate the question paper", "make a JEE Main / Advanced paper", a PRT / RPT / mock paper from a concept list, or asks to continue from an approved Question_Paper_Blueprint.xlsx, or uploads a blueprint directly (with or without input_config.xlsx) and asks for the paper.
---

# JEE question paper generator

## Two ways in
**A. From `input_config.xlsx`** (no blueprint yet): Part 1 (blueprint, then the mandatory stop for review), then Part 2.
**B. From a blueprint the user supplies directly** (their own Excel, an edited one, or one from an earlier session), with or without `input_config.xlsx`: skip Part 1
and the review stop (the user has already decided the blueprint) and go straight to Part 2, step 4. Run the check **without** `--config` when there is no config
(`python scripts/make_blueprint.py check --blueprint <file> --reorder --json /home/claude/work/blueprint.json`); the pattern is inferred (`--pattern auto`).
Column names are read leniently (Sr No, Chapter, Concept1, Concept 2, Concept 3, Q Type, Difficulty Level, Answer Plan, paper name; question types such as
"Numerical" or "SCQ" and difficulty as a label or a plain 0-5 level are accepted). A row may list **any number of concepts** (2, 3, 4 or more): as columns `Concept 1`, `Concept 2`, `Concept 3`, `Concept 4`, ..., or in one `Concepts` column with **one concept per line** of the cell. Concept names contain `;`, `,` and `|` themselves, so cells are never split on those characters; if the reader warns that a cell contains `;`, ask the user whether it is one concept or several (with `input_config.xlsx` supplied, a `;` list is split automatically when every piece is a concept in the Concepts sheet). Only Chapter, a concept, Q Type and Difficulty Level are required. Without a config the
script cannot check that concepts exist in the Concepts sheet or that counts match a config; it still checks types, difficulties, concept counts per pattern, repeated concepts and
pairs, the Advanced rules it can see, and the answer plan. What it does, and what to tell the user in one short message before writing questions:
- **Pattern** inferred and why (ask only if it says it cannot tell).
- **Order:** if the rows are not in the required type order, `--reorder` applies it and prints old->new numbers; report the mapping. (Omit `--reorder` only if the user wants their own order kept.)
- **Answer Plan:** missing plans are drawn at random and listed; the user may override them.
- **Warnings** (for example too few three-concept questions) are reported, not fixed: the blueprint is the user's decision. Errors (unknown type or difficulty, empty Concept1) must be resolved first.
If the blueprint has no paper name, the file name is used. Then continue with Part 2 exactly as usual (steps 4 to 7).

Replaces the user's old pipeline (Excel_Generation_v3 script, then the Gemini script Question_Generation_v2).
Claude does both parts. The process has a **mandatory stop after the blueprint**: the user reviews and edits it.

**Inputs:** `input_config.xlsx` (sheets Chapters, Difficulties, QTypes, Concepts), the paper name (the old
blueprint used "CD PRT 04 Paper 01"), optionally the **blueprints of earlier papers of the same phase, oldest first** (their
concepts are avoided; if the order is unclear, ask), and the pattern. The pattern (`main` or `advanced`) is inferred from the config by
`plan_slots.py` unless the user states it: Advanced if the config has MCQ, Integer, Matrix Match or Paragraph
types or any question at level 4-5; Main if it has only Single Correct and Numerical types and nothing above
level 3. If the user's words (paper name, phase) contradict the inference, or the config is ambiguous, ask.
After the blueprint is approved: the edited `Question_Paper_Blueprint.xlsx`.

**Outputs (in `/mnt/user-data/outputs`):** Blueprint xlsx (part 1); then two Word files in Master Question Paper format
(LaTeX in `$...$`): `<name>_Shortened_Solutions.docx` and `<name>_Full_Solutions.docx`; three PDFs with 2D equations and
Hindi: `<name>_Questions_EN_HI.pdf`, `<name>_Questions_and_Shortened_Solutions.pdf`, `<name>_Questions_and_Full_Solutions.pdf`
(English and Hindi question, then the solution); and `<name>_difficulty.xlsx` (internal). No HTML files. Levels never
appear in Word or PDF files.

**Question order (fixed by `plan_slots.py`, checked on the blueprint):** JEE Main = Single Correct, then Numerical.
JEE Advanced = Single Correct, One-or-more Correct, Paragraph, Matrix Match, Integer, Numerical. Question numbers in the blueprint,
the picks and the files follow this order.

Scripts are in `scripts/` (run with the skill folder as base). Read the references as indicated:
`references/synergy_guide.md` (part 1), `references/question_rules.md` (part 2). Work in `/home/claude/work`.

## Part 1: blueprint

### 1. Validate and plan the slots
```bash
python scripts/plan_slots.py /mnt/user-data/uploads/input_config.xlsx /home/claude/work \
    [--pattern main|advanced] [--exclude oldest_blueprint.xlsx ... newest_blueprint.xlsx]
```
Stops with a message if the Chapters, Difficulties and QTypes totals differ, a label is unknown, or a chapter has
no concepts. Otherwise writes `slots.json` (chapter, type, difficulty, target level per question,
shuffled as before) and `chapter_concepts.json` (the concepts still available), prints the inferred pattern with
its reasons and the pairing targets (Main: e.g. 3 / 6 / 7 for 16 questions; Advanced: every question 2-3 concepts,
at least two questions with three concepts, at least 40% of questions mixing chapters). A Paragraph question is one slot. Use `--seed N` to reproduce a plan.
With `--exclude`, concepts used in the earlier blueprints leave the fresh pool, `chapter_concepts.json` lists only the
fresh ones, and the script prints how many are left per chapter. **Reuse rule (user's instruction):** use fresh concepts
first. When a chapter has none left, reuse the concepts used **earliest** (`reuse_order.json`, earliest first). If a chapter
has more questions than concepts, a concept may be used more than once in the paper. In every reuse case try not to
repeat a concept combination (pair) used before or elsewhere in this paper; vary the partner concept.

### 2. Choose concepts (your judgement, see `synergy_guide.md`)
Read `chapter_concepts.json`. For each slot choose Concept 1 (main concept, from the slot's chapter, important in
JEE), then Concept 2 (and 3 for Advanced) with a **natural link**, using only chapters of the Chapters sheet.
Main: match the pairing type to the slot (easy L1/INT slots suit single-concept; hard slots rarely do).
Advanced: every question has two or three concepts, **at least two questions have three** (best placed on L3+ slots or
MCQ / Paragraph types) and at least 40% of questions must mix chapters. Write `picks.json`:
```json
[{"sr": 1, "concept1": "exact text from the sheet", "concept2": "..." , "concept3": null, "link": "why they link"}]
```
`sr` is the question number printed by `plan_slots.py` (already in paper order).
Copy concept text exactly from the sheet (the script lists close matches when it differs).
```bash
python scripts/make_blueprint.py build --config /mnt/user-data/uploads/input_config.xlsx --workdir /home/claude/work \
    --picks /home/claude/work/picks.json --paper-name "<paper name>" --out /mnt/user-data/outputs/Question_Paper_Blueprint.xlsx \
    [--exclude oldest_blueprint.xlsx ... newest_blueprint.xlsx]
```
It refuses to write on any error: unknown or misplaced concept; a concept reused within the paper or from an earlier paper
of the phase while its chapter still has fresh ones; partner chapter not in the sheet; three concepts in a Main paper;
in an Advanced paper a single-concept question, fewer than two three-concept questions, or less than 40% chapter mixing.
It warns about the Main mix being more than 1 off target, allowed reuse (earliest-used first) and repeated concept
combinations: remove a repeated combination when an alternative exists, otherwise mention it in the reply.
Columns: Sr No, Chapter, Concept1, Concept 2, Concept 3, Chapter of Concept 2, Chapter of Concept 3,
Pairing Type, Link Note, Q Type, Difficulty Level, **Answer Plan**, Word File and Folder name.

**Answer Plan (answers are planned before any question is written).** `plan_slots.py` draws it at random so answers
cannot drift to "A", "ABC / ABCD" or single digits (the old Gemini habit): single-correct, matrix-match and paragraph
parts get balanced letters A-D; multi-correct gets a random set (A,B,C and A,B,C,D are left out of the pool; the user can
type them in by hand); Integer gets a digit 0-9 (no repeats); Numerical (and paragraph-numerical) parts get a
varied style: positive 2-digit integer, positive 3-digit integer, negative integer, positive decimal, negative decimal
or decimal between 0 and 1 (two decimal places). Format in the sheet: `Option C`, `Options B, D`, `Q1: Option A; Q2: Option C`,
`Integer 7`, `negative decimal`. The user may edit the plan during blueprint review.

### 3. Present the blueprint and STOP
`present_files` the blueprint. Reply briefly: the pairing mix achieved, any chapter without a natural partner,
and a note that Link Note says why each pair works. Then **wait**. Do not generate questions until the user
returns the blueprint (or says to go on).

## Part 2: questions

### 4. Re-read the approved blueprint (or the directly supplied one)
```bash
python scripts/make_blueprint.py check --config .../input_config.xlsx --blueprint <edited.xlsx> --pattern <main|advanced> --json /home/claude/work/blueprint.json [--exclude oldest ... newest]
```
The user's edits are the truth. Concepts, difficulty or type changed by hand are accepted; the check prints
warnings (counts differ from the config, mix off target) and errors (concept missing from the sheet). Report
warnings in one line and carry on; stop only on errors. Generate from `blueprint.json`.

### 5. Write the questions one at a time
Read `references/originality_guide.md` and `references/known_skeletons.md` first: **every question must be brand new**, built on a new
mechanism, never a known problem with new numbers. Then `references/style_guide.md` (authentic JEE Advanced phrasing; rigorous, precise, objective language), `references/question_rules.md`
and the calibrated skill in full first:
`/mnt/skills/plugins/jee-advanced-difficulty-calibrated/` (`SKILL.md`, `references/rubric.md`, `references/anchors.md`).
For each blueprint row, in order:
0. **Name the mechanism** (originality guide, ways 1-5) and run the provenance check before writing the stem. If the one-line summary matches `known_skeletons.md`, change the mechanism.
1. Design an original question that needs **every** concept of the row, however many it lists (never trim a row to two or three). If one concept cannot be made natural, keep it, build the mechanism around it, and say in the reply which row was hard; never drop a concept silently. Record, per question, `blueprint_concepts` (copied exactly from blueprint.json) and `concept_use` (one line per concept: where the solution needs it); the build refuses a question that does not account for each concept. The question with Concept 1 as the main idea, at the
   row's type and target level, phrased as in `style_guide.md`. Define objects by a natural property (a geometric
   condition, a functional equation, an area), not by an arbitrary hint.
2. **Verify with code** (sympy/mpmath): answer, well-posedness, every MCQ statement.
3. Rate it with the calibrated rubric (key step, nearest anchors, level). If the rating is not the target level,
   redesign the question (not the rating). One redesign per question; if it still lands one level off with
   Low or Medium confidence, keep it and list it in the reply.
4. **Make the answer equal the Answer Plan** (blueprint.json, `answer_plan`): put the correct option at the planned
   letter; design the MCQ statements so that exactly the planned set is true; hit the planned integer digit or numerical
   style. If the topic makes a style unnatural (an area cannot be negative), ask for a derived quantity such as `8A` or
   `A-10`; never change the plan yourself.
4b. **Web check** (if a search tool is available): search the distinctive structure of the question in words and symbols; if a near-identical problem
   appears, redesign (record `web_check`: `not found`, `ingredient only`, `found: redesigned` or `not available`).
5. Write the Hindi, then **two solutions**: the shortened one (`solution_style.md`) and the full one (`solution_full`,
   see `question_rules.md`), with identical answers.
6. Save `/home/claude/work/paper/qNN.json` (schema at the end of `question_rules.md`; include `target_level`, `answer_plan`, `originality_note` and `web_check`).
   Also keep `/home/claude/work/paper/meta.json`: `{"title": "<paper name>", "date": "<today>"}`.

Never reuse the same function or setup across questions. Stay inside the JEE syllabus (no hyperbolic functions, no asymptotes;
see `question_rules.md`).
After the last question do the calibrated skill's consistency pass (sort by level, read neighbours), then the **stem review**:
`python scripts/review_stems.py /home/claude/work/paper` prints every stem and its options. Read each English stem as a student seeing it
for the first time: is every symbol and function introduced, is every condition stated, is there one reading of each sentence, is the answer
unique and equal to the Answer Plan, do the options have one form. Fix what you find in the question files, then record the review in each
question's `stem_review` field (what you checked and what you changed). The review is a self-check, so say so in the reply; an independent
reader may still find things.
Edit the qNN.json files in place for any fix.

### 6. Build and check
```bash
python scripts/build_paper.py /home/claude/work/paper /mnt/user-data/outputs --name "<paper_name_underscored>" --blueprint /home/claude/work/blueprint.json
```
It validates everything before building anything (stem phrasing: no "Find/Calculate/Determine..." openers, the required stock phrases for
matrix-match, multi-correct, paragraph and numerical stems, a domain for every function, and a recorded `stem_review` are all **errors** that stop the build;
special characters outside `$...$`, Hindi inside maths, option counts, English vs
Hindi option maths, answer lines, shortened and full solutions agreeing, **answer equal to the Answer Plan**, rating completeness,
rated level vs target: two or more apart is an error, one apart is a warning), builds the two Word files, the three PDFs and
the Excel, and prints the answer spread and the level distribution with the weighted index. Needs `xelatex` (installed here).
Render page 1 of each PDF (`pdftoppm -jpeg -r 60`) and look: Hindi shaped, equations 2D, paragraph block readable.

### 7. Deliver
`present_files` in this order: shortened-solutions Word, full-solutions Word, questions PDF, questions-and-shortened-solutions
PDF, questions-and-full-solutions PDF, difficulty Excel (and the blueprint if it changed).
Short reply: **originality report** (per question: the mechanism, whether it was web-checked, any standard ingredient; never claim novelty you did not check), level distribution and weighted index, questions still one level off target (with reason), anything
you changed from the blueprint (nothing should be), and problems found while verifying. Do not paste questions.

## Things that go wrong
- Choosing a partner concept just to satisfy a percentage. Naturalness beats the 20/40/40 split; say so when it
  costs you a target.
- Hindi options whose maths differs from English (the script warns).
- Writing the question first and letting the answer fall where it falls: plan the answer first.
- Hyperbolic functions or asymptotes in a question or solution (outside the JEE syllabus; the build refuses them).
- Stems that sound like exercises ("Find ...", "Calculate ...", contrived multipliers such as "the value of $8A$"). Rewrite them as JEE Advanced would.
- Solutions written at full length. They should be about 35-45% of a full solution.
- Putting levels, concept names or "link" notes into the Word or PDF files.
