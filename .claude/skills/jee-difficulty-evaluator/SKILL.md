---
name: jee-difficulty-evaluator
description: Rate the difficulty of JEE / JEE Advanced mathematics questions on a 0-5 scale and produce a question-wise Excel report with justifications. Use this whenever the user uploads an assignment, question bank, DPP, practice sheet, test paper, or worksheet (PDF, DOCX, or images) containing maths questions and asks about difficulty, level, grading, tagging, calibration, or "which level is this" - and also whenever they ask to classify questions as JEE Main vs JEE Advanced vs Olympiad level, to check whether a paper is balanced, or to produce a blueprint/Excel of an existing paper. Trigger even if the user does not say the word "difficulty" - phrases like "how hard are these", "tag these questions", "analyse this DPP", or "make a blueprint from this paper" all belong here.
---

# JEE Mathematics Difficulty Evaluator

Grade each question in an assignment on a 6-point difficulty scale (Level 0 to Level 5) and
deliver an Excel workbook with one row per question, containing the level, the reasoning behind
it, and the topic tags.

The scale is not generic. It mirrors the levels used by the user's own question-generation
prompt, so the output can be fed straight back into that pipeline as a blueprint.

## The one thing that goes wrong most often

**Calibrate against a strong Class 11/12 student preparing for JEE Advanced - never against your
own ability.** Almost every question in these assignments is trivial for a language model. If you
rate by how hard it felt to you, everything lands on Level 0-1 and the report is worthless.

The reference student is: knows the full JEE syllabus, has solved a few thousand problems, is
strong but not exceptional, and is working under exam pressure with roughly 3 minutes per mark.
Ask "would *that* student solve this cleanly in the expected time, or stall?" That is the whole
judgement.

## Workflow

### Step 1 - Inventory the file

Never assume the PDF has clean text. Maths PDFs are frequently image-based or use custom font
encodings that produce garbage on extraction.

```bash
pdfinfo assignment.pdf        # page count, size
pdffonts assignment.pdf       # empty table = scanned/raster, text extraction will fail
pdftotext -f 1 -l 1 -layout assignment.pdf - | head -40   # is the text sane?
```

Decide the reading mode:
- **Clean text layer** - extract with `pdftotext -layout` and work from the text. Still rasterize
  any page containing a diagram, matrix, or determinant, because those flatten badly.
- **Garbled or no text layer** - rasterize every page and read the images:
  ```bash
  pdftoppm -jpeg -r 150 assignment.pdf /tmp/pg
  ls /tmp/pg-*.jpg
  ```
  Then view each image. At 150 DPI a page costs roughly 1,600 tokens, so for long assignments
  work in batches of about 10 pages, rating as you go rather than loading everything first.

If the input is DOCX or images instead of PDF, adapt - the rating logic is unchanged.

### Step 2 - Segment into questions

Build a list of questions before rating anything. Watch for:

- **Paragraph / comprehension blocks** - one passage feeding two or three questions. Record the
  passage once and rate each sub-question separately, since they usually differ in difficulty.
  Reference them as `Q12(i)`, `Q12(ii)`.
- **Matrix match** - a single question, however many rows it has.
- **Assertion-Reason** - map onto Single Correct Type.
- **Solutions section** - usually at the end. Pair each solution back to its question; the
  solution is evidence, not a separate item.

Record for each: the printed question number, the page it appears on, and the question type using
the exact strings in `references/taxonomy.md`.

### Step 3 - Read the solution, but do not trust its length

The provided solution tells you which route the author intended, and often reveals a trap. It is
weak evidence of difficulty by itself:

- A three-line solution can hide one brilliant substitution that most students never find. That
  is a *hard* question with a short solution.
- A two-page solution may be pure grinding with no insight at all. That is a Level 3 at most, not
  a Level 5.

**Always rate against the shortest correct route a well-prepared student would realistically
find**, not the route the author printed. If the printed solution is clearly clumsier than the
obvious approach, say so in the justification.

### Step 4 - Score the five dimensions

Read `references/rubric.md` in full before rating the first question. It carries the dimension
definitions, the level descriptors, the composite-to-level mapping, and worked anchor examples.

In short: score C (conceptual depth), L (concept linkage), M (manipulation load), I (insight
required) and T (traps and precision) from 1 to 5 each, estimate solve time, then map to a level.
The override rules in the rubric matter - especially that heavy algebra alone never reaches
Level 5, and that Level 5 requires genuine Olympiad-grade insight.

Write the justification as you rate, while the reasoning is fresh. A justification must name the
specific thing that sets the level - the actual concepts that had to be combined, the actual trap,
the actual key step. Vague lines like "requires good understanding of the topic" are useless to
someone reviewing the paper.

Good: "Needs the student to recognise that the given functional equation forces f to be periodic
with period 4, then apply that to collapse the definite integral. Single insight, routine algebra
afterwards - the recognition is the whole difficulty."

Bad: "This is a moderately difficult question on functions and integration."

### Step 5 - Calibration pass over the whole set

Rating questions one at a time causes drift and clustering. Before writing the Excel, review the
full list together:

1. **Check the spread.** A typical coaching assignment spans Levels 1-4. If more than about 60%
   of questions landed on a single level, you were probably anchoring - re-examine that group and
   separate the genuinely routine from the genuinely demanding.
2. **Sort by level and sanity-check the boundaries.** Read the hardest Level 2 next to the easiest
   Level 3. If they feel identical, move one.
3. **Watch for Level 5 inflation.** Level 5 is RMO/INMO territory. In a normal coaching
   assignment it should be rare or absent. If several questions landed there, most are probably
   Level 4.
4. **Watch for Level 0/1 deflation.** Conversely, if nothing is below Level 3, check whether you
   have been rating by your own ease rather than the student's.

State the distribution to the user in the chat reply so they can see the shape at a glance.

### Step 6 - Build the Excel

Write the ratings to a JSON file, then run the bundled script:

```bash
python scripts/build_report.py ratings.json output.xlsx
```

The exact JSON schema is documented at the top of `scripts/build_report.py` - read it before
writing the file. The script produces three sheets:

| Sheet | Purpose |
|---|---|
| `Evaluation` | One row per question: level, dimension scores, estimated time, justification, key step, confidence |
| `Summary` | Level distribution and chapter distribution, computed with live formulas |
| `Blueprint` | The same questions in the exact column layout of `Question_Paper_Blueprint.xlsx`, ready to feed back into the generation script |

The `Check` column in `Evaluation` flags any row where the assigned level differs from what the
dimension scores imply by more than one level. Investigate every flag before delivering - either
the scores or the level is wrong. A deliberate override is fine, but explain it in the
justification.

Because `Summary` contains formulas, recalculate before delivering, otherwise the counts read as
blank in Excel and pandas:

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py output.xlsx
```

Then save the workbook to the outputs directory and present it.

## Reply alongside the file

Keep the chat reply short. Give the level distribution, name the two or three questions that are
the biggest outliers in either direction, and flag anything the user should look at - a
mis-tagged chapter, a question whose printed solution looks wrong, a paper that is heavily
lopsided. The detail lives in the spreadsheet; the reply is the executive view.

## Handling uncertainty

Set `confidence` to `Medium` or `Low` and say why, rather than guessing silently:

- The question is cropped, blurred, or a diagram is unreadable.
- The solution is missing and the question is ambiguous.
- The printed answer appears wrong, which changes what the question is really asking.

Never silently drop a question you could not read. Include the row with `Low` confidence and a
justification saying what was unreadable, so the user knows to check it manually.

## Reference files

- `references/rubric.md` - the scoring rubric, level descriptors, mapping table, and anchor
  examples. Read before rating.
- `references/taxonomy.md` - exact question-type strings, difficulty-level label strings, and
  chapter naming conventions used by the user's generation pipeline. Read before writing the
  Excel so the Blueprint sheet drops straight into the existing script.
- `scripts/build_report.py` - JSON to Excel builder, with the input schema in its docstring.
