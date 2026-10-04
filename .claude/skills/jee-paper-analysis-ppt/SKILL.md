---
name: jee-paper-analysis-ppt
description: Turn a JEE maths question paper plus its blueprint / concept Excel into the user's "Paper Analysis" PowerPoint - title slide, one question slide per question (question, type and marks, concepts, calibrated difficulty level), condensed solution slides with the correct answer, a difficulty table and the marks-weighted difficulty index. Produces a content JSON (maths as LaTeX in $...$) and a Python script the user runs from their terminal to build the deck. Use whenever the user uploads a test paper (PRT, RPT, mock, JEE Advanced/Main style) with a blueprint or concept list and asks for the paper analysis PPT, analysis deck, question-wise slides, or "make the PPT for this paper" - even if they do not mention the script.
---

# JEE Paper Analysis PPT

Build the user's standard paper-analysis deck. The work splits in two:

1. **In this conversation (you):** read the paper and the blueprint, rate every question with
   the calibrated difficulty skill, write the question text, concepts, answer and condensed
   solution, and save them as one content JSON.
2. **On the user's computer (them):** one command builds the deck from that JSON:
   ```
   python make_ppt.py <Paper>_content.json
   ```
   Every `$...$` becomes a **native PowerPoint equation** (converted LaTeX -> Office Math via
   pandoc, which `pip install pypandoc_binary` bundles). In PowerPoint each equation can be
   switched to LaTeX, edited, and switched back to 2-D (Equation tab -> LaTeX + Linear, then
   Professional). `--equations latex` keeps the old behaviour (plain `$...$` text for an external
   converter). If pandoc is missing, the script falls back to plain LaTeX text and says so.

Always deliver: the content JSON, the built `.pptx` (build it here too, so they can look at it
immediately) and `make_ppt.py`.

## Files in this skill

- `scripts/make_ppt.py` - the deck builder (needs only `python-pptx`). Style and colours copy
  the user's sample deck, with all body text at 24 pt; do not change them per paper. Every text
  box also carries dark default text properties, so equations inserted later by the user's
  LaTeX converter inherit dark text instead of turning white.
- `references/content_schema.md` - the JSON schema, the exact type labels, the LaTeX rules,
  the concepts rule and the solution-writing rules. **Read it before writing any JSON.**
- `references/example_PRT_06_Paper_01_content.json` - a complete, user-approved example.

- `references/test_matrix_content.json` - regression sample with matrices, determinants and `cases`. After any change to the
  equation code, build it and open the result in PowerPoint: there must be no "repair" prompt and no empty slide.

## Workflow

### 1. Read the inputs

- **Question paper (PDF):** follow the file-reading / pdf-reading skills. These papers usually
  include answers and solutions. Many are printed from web pages: the text layer may lose
  superscripts, fractions and minus signs, so rasterize pages and read them whenever the maths
  in the extracted text looks garbled. Use only the Mathematics section.
- **Blueprint / concept Excel:** one row per question with Q No, Chapter, Concept1, Concept 2,
  Q Type (other columns may exist). **Ignore its Difficulty Level column** - the level always
  comes from step 2.
- Number the questions continuously 1..N even when the paper restarts numbering per section,
  and check the paper's question count against the blueprint's rows.

### 2. Rate difficulty with the calibrated skill

Use the **jee-advanced-difficulty-calibrated** skill: read its SKILL.md, `references/rubric.md`
and `references/anchors.md`, and rate every question exactly as it says. That includes the
equivalence-relation adjustment (+0.5) and the 2.5 floor for multi-concept
one-or-more-correct questions. The `level` in the JSON is the skill's **adjusted level**.

If that skill is not available in this session, say so and ask the user for the levels instead
of improvising a scale.

Offer the calibrated skill's Excel report as well if the user wants the detailed justifications.

### 3. Write the content JSON

Follow `references/content_schema.md`:

- Question text transcribed faithfully, maths as `$...$` LaTeX, options in `options`, passage in
  `paragraph`.
- Concepts from the blueprint using the user's rule: same chapter -> one summarised concept;
  different chapters -> both.
- A one-sentence `key_idea` for every question: the decisive step, phrased so students can reuse
  it (it becomes the amber strip at the top of the first solution slide).
- 5-6 condensed solution bullets per question, every question with a solution and an answer.
- Verify every answer by solving the question yourself. If the paper's key disagrees with your
  solution, keep the correct answer and report it to the user.

### 4. Build and check

```bash
pip install python-pptx pypandoc_binary --break-system-packages   # if needed in the sandbox
python scripts/make_ppt.py /mnt/user-data/outputs/<Paper>_content.json -o /mnt/user-data/outputs/<Paper>_Analysis.pptx
```

The script prints notes for anything it could not fit, any missing answer/solution, and any
LaTeX it could not convert or deliberately kept as plain text for PowerPoint-safety (that snippet stays as text; the note gives the reason) - fix the JSON and rebuild. Note that
LibreOffice cannot display Office equations: in a LibreOffice render the boxes show the LaTeX
fallback text instead, which is longer, so judge overflow only on text without much maths or
convert a few equations to check with `pandoc x.docx -t markdown` (round trip). Then render the deck (pptx skill: convert to PDF, rasterize) and look at the
question slides with the longest text and at the closing slides. Check that no text runs outside
its box and that the numbering and answers are right.

### 5. Deliver

Present the JSON, the deck and `scripts/make_ppt.py` (copy it to outputs). In the chat reply give:

- the overall marks-weighted difficulty index and the level spread;
- any question where the paper's answer key looked wrong, or where you were unsure of a level;
- the terminal command, the first time only:
  ```
  pip install python-pptx pypandoc_binary
  python make_ppt.py <Paper>_content.json
  python make_ppt.py <Paper>_content.json -o "My name.pptx" --max-bullets 5
  ```

Ask for the "Marks for AIR" figures only if the user wants that slide; never estimate them.

## Deck structure (what make_ppt.py produces)

1. Title slide (navy): title and subtitle.
1a. A **section divider** (navy) before each section: "Section n", the question type, the
   question range and the marking scheme. Sections come from `sections` in the JSON - fill it from
   the paper's section headers (e.g. "+3 if correct · 0 if unanswered · −1 otherwise") whenever the
   paper prints them; without it the script groups consecutive questions of the same type and marks
   and shows "n marks each".
All body text is **24 pt Arial** (the user's classroom standard; equations get Cambria Math from
the user's converter); the answer box is 28 pt. Borders are a darker grey and level colours run
green -> yellow -> orange -> red, strong enough to survive a projector. Every question and solution
slide carries a **level badge** in the header ("Level 3.5 · 3 Marks", in the level colour), and
solution steps use real bullets with a hanging indent.

2. For each question: a question slide (question box; info box with
   `Type(n Marks)`, `Concept(s) : ...`, `Difficulty Level: Level x(description)`), then solution
   slides (bullets spread evenly, at most 6 per slide, usually 3-5 at 24 pt). The first solution
   slide opens with an amber **Key idea** strip; the last one carries the green `Correct Answer`
   box. If a question is too long to share its slide with the
   info box, the info box moves to the top of the first solution slide; only a question that
   cannot fit a whole slide at 24 pt is reduced (22 or 20 pt) and the script says so.
3. Difficulty table - a native, editable table, up to 5 questions per slide in 24 pt,
   colour-coded by level. Chosen over a pasted picture because it stays sharp and readable in a
   large classroom.
4. Summary slide: the marks-weighted difficulty index in very large type plus the number of
   questions in each band.
4a. **Difficulty Profile**: a native bar chart, one bar per question, height = level, coloured by
   level, so the class sees where the paper got hard.
5. "Marks for AIR" slide, only when `air_marks` is in the JSON.
6. Last slide - comparison table: the difficulty index of JEE Advanced 2021, 2023, 2024, 2025
   and 2026 (the user's own ratings: 2.76, 3.19, 2.59, 3.21, 3.02) with this paper's index as a
   highlighted final row. When the user rates a new official paper, add it with
   `reference_indices` in the JSON (or update `DEFAULT_REFERENCE` in the script).

Default level descriptions (override with `level_labels` in the JSON):

| Level | Description |
|---|---|
| 0, 0.5 | Easier than JEE Main Level |
| 1 | JEE Main Level |
| 1.5 | A little above JEE Main Level |
| 2 | A level below Average JEE Advanced Level |
| 2.5 | A little easier than Average JEE Advanced Level |
| 3, 3.5 | Average JEE Advanced Level |
| 4, 4.5 | A level above Average JEE Advanced Level |
| 5 | Very difficult than JEE Advanced |
