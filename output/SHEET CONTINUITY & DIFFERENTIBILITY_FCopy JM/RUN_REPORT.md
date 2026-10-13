# Run report — SHEET CONTINUITY & DIFFERENTIBILITY_FCopy JM

Paper: `papers/SHEET CONTINUITY & DIFFERENTIBILITY_FCopy JM.pdf` (22 pages, Exercise J-M, 26 JEE Main questions: 17 single-correct and 9 numerical, interleaved in the paper's order).

Files in this folder: `…_Analysis.pptx` (165 slides), `…_content.json`, `…_ratings.json`, `…_difficulty.xlsx`.

## Blueprint and marks
- **No blueprint was used** (`blueprints/` has no file for this paper). **Concepts self-assigned (no blueprint) - please review.**
- The paper prints no marking scheme. Marks assumed (JEE Advanced defaults, as instructed): **4 marks for every single-correct question and 4 for every numerical question.** This is stated on every section divider. The paper's questions alternate between the two types, so the deck has 8 short section dividers.

## Difficulty (jee-advanced-difficulty-calibrated)
- Marks-weighted difficulty index (adjusted): **2.15** (all questions carry 4 marks, so it equals the mean level). This is a JEE Main chapter sheet, so it sits below the official JEE Advanced range (2.59–3.21), as expected.
- Questions per level: Level 1 — 2 (Q1, Q15); Level 2 — 18 (Q2–Q7, Q11–Q14, Q16, Q17, Q19–Q22, Q24, Q26); Level 3 — 6 (Q8, Q9, Q10, Q18, Q23, Q25); Levels 0, 4, 5 — none.
- No equivalence-relation adjustment and no multi-correct floor applied (no such questions).
- `recalc.py` was skipped (no `/mnt/skills`), so the workbook's formula cells have no cached values until it is opened in Excel.

## Solutions: corrected / written (none were `written`)
- **Q2 — corrected:** the PDF's line "lim 4cos4x/(6cos6x) = e^{2/3}" drops the factor cos6x/cos4x (the ratio shown alone equals −2/3, not 2/3). Both factors are now shown; the value 2/3 and the final answer 10 were right.
- **Q13 — corrected:** the PDF writes "f(x) < 0 ⇒ f(x) is decreasing"; it must read f'(x) < 0 (f itself is positive).
- **Q19 — corrected:** the PDF's rewritten f(x) shows the middle piece as ax² instead of ax² + 2b. Its later continuity equation 4a + 2b = 1/2 already uses the correct form, so only the display was wrong.
- All other questions — `pdf`. The working was checked step by step and reproduced. Small additions that do not change the PDF's method: Q5 (added the left limit at 0), Q8 (the PDF only quotes the 2p−1 formula; I added two lines of explanation), Q16 (added the missing differentiability check at x = 0), Q21 (added the last step a² = 1152 and the rationalisation line).

## Answer key
- **Q2:** the printed key says "Drop". The exponent in the question is typeset as a fraction (cot 6x over e^{cot 4x}); the printed solution (and the original JEE Main Jan 2023 question) read it as e^{cot6x / cot4x}, which gives **(B) 10**. I used that reading and wrote it in the question text. Read literally, the right-hand limit would be 0 and μ = 0 would make ln μ undefined.
- Every other printed answer was checked numerically or symbolically (Python / sympy) and is correct: Q1 A, Q3 A, Q4 3, Q5 D, Q6 D, Q7 D, Q8 25, Q9 309, Q10 4, Q11 2, Q12 A, Q13 A, Q14 B, Q15 D, Q16 A, Q17 C, Q18 2890, Q19 15, Q20 D, Q21 A (a² = 1152), Q22 D, Q23 D, Q24 B, Q25 17, Q26 81.
- Typo in the paper: option (B) of Q5 is labelled "(2)"; treated as (B).

## Alternate solutions and useful results
- **Alternates: 22 of 26 questions** (all except Q10, Q12, Q20, Q26). Each was verified against the answer.
- Questions with NO alternate:
  - **Q10:** after rewriting f piece by piece, the only route is one-sided limits and slopes at −1, 0, 1 (graph or table); no different idea exists.
  - **Q12:** the continuity condition reads off directly (−a/b = 2 = b); no different technique exists.
  - **Q20:** two standard trigonometric limits; any other route (series, L'Hopital) is the same computation reworded.
  - **Q26:** the left limit uses tan 8x / tan 7x → 0 and the right limit is the standard 1^∞ limit; no genuinely different method.
- Alternates that are weaker in originality (for review): **Q5, Q11, Q23, Q25** use a "jump ledger" (sum of signed jumps of the greatest-integer parts). It is a different viewpoint from computing three limits per point, but closely related to the main solution. **Q8** derives the 2p−1 count by sweeping horizontal lines (the PDF only quotes the formula).
- **Useful Result / Pattern: all 26 questions** have 4 bullets each; formulas were checked on numerical cases.

## make_ppt.py warnings
- Build output: "Equations: 897 converted to native PowerPoint equations. Saved … (165 slides, 26 questions)". No "could not convert" notes.
- One note on the first build: "Q8: only 3 solution bullets". The PDF's solution is three lines long; I added one explanatory bullet (4 bullets now) and the note disappeared.

## Skipped, assumed or guessed
- Skipped (not available in this environment): `recalc.py`, thumbnails and soffice rendering, and visual inspection of the rendered slides.
- Figures in the PDF (graphs for Q10, Q11, Q14–Q17) are not reproduced; the solutions describe the same facts in words.
- The Hindi translations in the PDF were left out.
- Q4, Q8–Q11, Q18, Q19, Q25, Q26 are labelled "Numerical Type" (the paper gives blank-answer questions without printing a digit range).
- Levels and concepts are my calibrated judgement; confidence is Medium for all questions except Q1, Q15, Q20 (High). Details are in the Excel workbook.
