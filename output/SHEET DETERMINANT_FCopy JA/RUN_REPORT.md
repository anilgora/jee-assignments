# Run report — SHEET DETERMINANT_FCopy JA

Paper: `papers/SHEET DETERMINANT_FCopy JA.pdf` (11 pages, "Exercise J - A", 7 questions: Q1 SCQ, Q2 integer, Q3 MCQ, Q4 integer, Q5 MCQ, Q6–Q7 matching). The text layer drops many symbols (≠, Greek letters, determinants), so the maths was read from page images. Hindi text left out (English deck).

Files: `…_Analysis.pptx` (57 slides), `…_content.json`, `…_ratings.json`, `…_difficulty.xlsx`.

## Blueprint and marks
- **No blueprint was used. Concepts self-assigned (no blueprint) - please review.**
- No marks printed. Assumed (JEE Advanced defaults, also stated on the section dividers): **4 marks** for Q1 (single correct), Q2 and Q4 (integer), Q3 and Q5 (one or more correct); **3 marks** for Q6 and Q7 (matching). Total 26.

## Difficulty (jee-advanced-difficulty-calibrated)
- Marks-weighted difficulty index (adjusted): **2.81** (73 / 26 marks).
- Questions per level: Level 2 — 2 (Q1, Q5); Level 3 — 4 (Q2, Q3, Q4, Q7); Level 4 — 1 (Q6); Levels 0, 1, 5 — none.
- No equivalence-relation adjustment; no multi-correct floor (Q3 and Q5 each involve one concept only). Confidence Medium for Q2, Q3, Q4, Q6; High for Q1, Q5, Q7. `recalc.py` skipped (no `/mnt/skills`), so formula cells in the Excel file have no cached values until it is opened in Excel.

## Solutions: corrected / written
- **None.** All 7 are `pdf`: every step was re-derived and the final answers checked with sympy (determinants, factorisations, linear systems for all parameter cases).
- The PDF is terse in places; I expanded steps the PDF only states, keeping its method: Q1 (evaluation of both determinants and the link of the Statement-2 determinant with Δy, which the PDF only asserts), Q2 (check of the x=0 solutions and rejection of sin3θ=0), Q3 (row/column results and the division by 2), Q4 (cyclic column move, quadratic factorisation), Q5 (one line per option), Q6 (derivation of a=d from each ratio), Q7 (why z≠0 for γ≠28 and why y=−2 when α=1).

## Answer key
All keys are correct: Q1 A, Q2 3, Q3 BC (α = 0 is also a root of the equation but is not an option), Q4 2, Q5 BCD, Q6 B, Q7 A. In Q6 the printed solution's "I → P, Q, R, T / IV → P, Q, R, T" is consistent with key (B) (Q and R are among the true statements; option (B) is the only one with all four assignments true).

## Alternate solutions and useful results
- **Alternates: all 7 questions** (Q1–Q7), each verified symbolically or numerically: Q1 linear dependency of left sides (row3 = 2·row1 + row2); Q2 elimination of xyz sin3θ giving tan3θ=1 with no case split; Q3 factorisation of the matrix of squares into two Vandermonde-type matrices (−4 × 2α³); Q4 plain row reduction (R2−2R1, R3−3R1); Q5 adding the equations; Q6 equation (3) = (a−d)(1) + d(2); Q7 substitution reducing to (2β−7α+3)z = 2(γ−28).
- **Questions with NO alternate:** none.
- **useful_results given for every question (Q1–Q7).** General formulas checked: det[(xᵢ+yⱼ)²] = −2·V(x)·V(y) and det[a, a², 1+a³] = V·(1+abc) were verified symbolically.

## make_ppt.py output
- `note: Q1: very long question - font reduced to 22 pt.`; `Q6` and `Q7`: font reduced to 20 pt (long statement text with lists). Harmless; resolved by the script itself.
- No "could not convert" warnings: all 338 equations became native PowerPoint equations.

## Skipped / assumed / guessed
- Concepts, question types and marks assumed as above. Question types: Q2 "all possible values of θ" and Q4 "total number of distinct x" are integer answers (0–9), so labelled Integer Type(0 to 9).
- Level ratings for Q2–Q4 and Q6 are judgement calls (Medium confidence). Slides were not rendered visually (no soffice).
