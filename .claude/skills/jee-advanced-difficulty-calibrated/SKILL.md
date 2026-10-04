---
name: jee-advanced-difficulty-calibrated
description: Rate JEE / JEE Advanced mathematics questions on the user's own 0-5 difficulty scale, calibrated against their ratings of 172 official JEE Advanced questions (2021-2026), and produce an Excel report with question-wise levels, justifications, the level distribution and the marks-weighted difficulty index compared with official papers, applying the user's rules for equivalence relations (+0.5) and multi-concept multi-correct questions (floor 2.5). Use this whenever the user uploads a question paper, mock test, assignment, DPP or question bank with maths questions and asks how hard it is, what level each question is, for a difficulty index, or how it compares with JEE Advanced - including casual phrasings like "rate this paper", "difficulty of this mock", "tag levels", "is this Advanced standard". Prefer this calibrated evaluator over any generic JEE difficulty skill whenever the user wants ratings that match their own standard.
---

# JEE Advanced Difficulty Evaluator - calibrated to the user's scale

Rate each maths question on the user's 0-5 scale and deliver an Excel report plus a short chat
summary. The scale is the user's own, learned from their ratings of every maths question in the
official JEE Advanced 2021, 2023, 2024, 2025 and 2026 papers. The goal is to predict the level
*the user* would give, not a generic difficulty.

## Files in this skill

- `references/rubric.md` - the calibrated rubric: what each level means for this user, the six
  deciding factors in order of weight, the decision procedure, quirks, reference statistics.
  **Read it in full before rating the first question.**
- `references/anchors.md` - the 172 rated official questions grouped by level, one line each.
  Use it for every question to find the nearest comparable anchors.
- `references/anchors.csv` - the same data, for computations.
- `scripts/build_report.py` - builds the Excel report from a ratings JSON.

## Workflow

### 1. Read the file properly

Maths PDFs often have broken text layers. Check first:

```bash
pdfinfo paper.pdf
pdffonts paper.pdf                       # empty table = scanned; rasterize
pdftotext -f 1 -l 1 -layout paper.pdf - | head -40
```

If symbols come out garbled (common for matrices, integrals, fractions), rasterize those pages
(`pdftoppm -jpeg -r 150 -f N -l N paper.pdf /tmp/pg`) and read the images. Full JEE papers
contain Physics and Chemistry too - rate only the Mathematics questions, and locate the maths
section by its heading rather than assuming it comes first.

### 2. Build the question list

For each maths question record: paper label, printed number, type, chapter and full marks.

- **Type** uses the anchor vocabulary: `SCQ`, `MCQ` (one or more correct), `Numerical`,
  `INT` (integer), `MTC SCQ` (matching), `Q Stem` (question-stem / paragraph numerical parts),
  `Para SCQ` (paragraph single-correct). Rate each part of a stem or paragraph separately.
- **Chapter** uses the chapter names that appear in `anchors.md` where possible, so anchors match.
- **Equivalence-relation flag** (`eq_relation`): true when the key step involves equivalence
  relations or equivalence classes.
- **Multi-concept flag** (`multi_concept`): for MCQs, true when the statements draw on two or more
  distinct concepts. See `rubric.md` section 9 for both flags.
- **Marks** come from the section header. If none are printed, use JEE Advanced defaults
  (SCQ 3, MCQ 4, Numerical/INT 4, MTC 3, Q Stem 2, Para SCQ 3) and say so in the chat reply.

### 3. Solve, then rate

Each question gets an integer **level** (0-5) on the user's scale; question format is part of
that judgement (`rubric.md` F5), exactly as in the user's own ratings. The script then applies the
user's two rules (`rubric.md` section 9) to get the adjusted level: +0.5 when the key step involves
equivalence relations or classes, and a floor of 2.5 for one-or-more-correct questions that involve
several concepts. Do not raise the integer level for the equivalence-relation topic itself - the
adjustment carries it.

Solve every question fully before rating it: the level depends on the route a strong student
would realistically take, and you cannot judge that without doing it. Then follow the decision
procedure in `rubric.md` section 5:

1. Name the key step.
2. Find 2-3 nearest anchors in `anchors.md` (same chapter, then same kind of demand).
3. Place the question relative to them and check factors F1-F6.

The two mistakes this skill exists to prevent:

- **Rating by your own ease.** Almost everything is easy for a model. The previous rubric ran
  0.56 levels too low on the 2026 blind test for exactly this reason. Judge the reference
  student in `rubric.md` section 1.
- **Ignoring idea availability.** A short solution built on an idea students rarely meet
  (Mobius maps, orthogonal matrices, a hidden Leibniz expansion) is high on this scale - often 4,
  sometimes 5 - regardless of question format.

Write the justification while the reasoning is fresh. Name the specific thing that sets the
level, and cite the nearest anchor with its level, e.g. "Same bounded-distribution counting as
2026-P1-Q11 (L3), plus an extra restriction that forces inclusion-exclusion over two conditions."
Vague lines like "moderately difficult" are useless to the user.

### 4. Consistency pass

Before writing the report, sort the questions by level and read neighbours side by side:
the hardest Level 2 next to the easiest Level 3, and so on. Move anything that reads the same as
the level above or below. For a full paper in the Advanced pattern, compare the weighted index
with the official range in `rubric.md` section 7 (about 2.6-3.2); if yours falls well outside it,
re-check the extremes before accepting it. For assignments and DPPs, report the spread as it is -
there is no expected distribution.

### 5. Build the Excel report

Write the ratings to JSON (schema at the top of `scripts/build_report.py`), then:

```bash
python scripts/build_report.py ratings.json /mnt/user-data/outputs/<name>_difficulty.xlsx
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/<name>_difficulty.xlsx
```

The rules default to +0.5 (equivalence relations) and a 2.5 floor (multi-concept MCQ). If the
user asks for different values, add `"topic_adjustment"` / `"mcq_multi_concept_floor"` at the top of
the JSON. The Reference sheet shows the user's official-paper ratings as given - they already
include these effects. The recalc step fills in the formula results (skip it if that script is not available). The
workbook has three sheets: `Evaluation` (one row per question: level, equivalence adjustment,
MCQ floor, adjusted level), `Summary` (level distribution; weighted index adjusted and unadjusted,
per paper and overall, as live formulas) and `Reference` (the user's own indices for official
papers 2021-2026 next to this paper's adjusted index). Present the file to the user.

### 6. Chat reply

Keep it short: the level distribution, the adjusted marks-weighted difficulty index (per paper
and overall), how it compares with the official years, which questions carry the
equivalence-relation adjustment or the MCQ floor, and any questions rated with Low confidence.
Do not repeat the whole table - it is in the workbook.

## When the user supplies their own ratings

If the user sends their levels for a paper you rated, compare question by question: exact
matches, within-one matches, mean bias, and every gap of two or more with the likely reason.
Then offer to append their ratings to `anchors.csv` / `anchors.md` and add a line to the
calibration history in `rubric.md` - every new rated paper makes the skill closer to their
standard. Never overwrite existing anchors; the user's historical ratings are the ground truth.
