# Run report — SHEET AREA UNDER CURVE_FCopy JA

Paper: `papers/SHEET AREA UNDER CURVE_FCopy JA.pdf` (24 pages, "Exercise J-A", 22 questions: JEE Advanced previous-year area questions 2012–2026; Q19–20 share one stem, Q21–22 share one stem). The text layer lost the maths symbols, so every page was read as an image. Hindi translations were left out (English deck).

Files: `…_Analysis.pptx` (150 slides), `…_content.json`, `…_ratings.json`, `…_difficulty.xlsx`.

## Blueprint and marks
- **No blueprint was used** (`blueprints/` has no file for this paper). **Concepts self-assigned (no blueprint) - please review.**
- The paper prints no marks. Assumed (stated on the section divider): **4 marks** for single-correct (Q2, Q3, Q6, Q10, Q11, Q12, Q16, Q17), one-or-more-correct (Q1, Q7, Q8, Q14, Q18) and numerical/integer-type answers (Q4, Q9, Q13, Q15, Q19–Q22); **3 marks** for the matching question (Q5). Q19–Q22 are question-stem parts with a numerical answer, treated as numerical (4 marks).

## Difficulty (jee-advanced-difficulty-calibrated)
- Marks-weighted difficulty index (adjusted): **2.68** (total 87 marks). It is a chapter sheet of official questions, so there is no expected distribution; 2.68 sits inside the official Advanced range 2.59–3.21.
- Questions per level: Level 1 — 1 (Q9); Level 2 — 8 (Q2, Q6, Q7, Q10, Q19, Q20, Q21, Q22); Level 3 — 10 (Q1, Q3, Q4, Q5, Q8, Q11, Q12, Q13, Q16, Q17); Level 4 — 3 (Q14, Q15, Q18); Levels 0 and 5 — none.
- Many questions are official Advanced questions already in the anchor bank; their levels follow the user's own ratings (Q12 = 2021-P1-Q2 L3, Q14 = 2023-P1-Q3 L4, Q15 = 2023-P1-Q9 L4, Q16 = 2024-P2-Q2 L3, Q17 = 2025-P2-Q2 L3, Q18 = 2025-P2-Q6 L4, Q19 = 2026-P2-Q15 L2, Q20 = 2026-P2-Q16 L2, Q22 = 2026-P2-Q18 L2; Q21 follows the similar 2026-P2-Q17 L2). Q1–Q11 and Q13 are rated by me (not in the bank).
- No equivalence-relation adjustment; the multi-concept MCQ floor (2.5) was flagged for Q1, Q8, Q14, Q18 but never binds (all are already ≥ 3).
- Confidence Low for Q5 (four unrelated items in one matching question); Medium for Q1, Q3, Q4, Q6, Q8, Q11, Q13.
- Excel built with `build_report.py`; `recalc.py` was skipped (no `/mnt/skills`), so formula cells have no cached values until opened in Excel.

## Solutions: corrected / written (none were `written`)
- **Q1 — corrected (omissions):** the PDF's key is ABD but it never shows (A) (added: $1-\frac1e>\frac1e$) and does not justify "curve lies above the chord" in the trapezium bound (added concavity argument). Answer unchanged.
- **Q5 — corrected:** (B)'s first line is mis-typed in the PDF and the rejection of the factor $\sin X+2\sin Y$ is missing; added that $X+Y=\pi-Z$ in (A) and wrote out the $\alpha=1$ integral in (D). All matches unchanged (A-PRS, B-P, C-PQ, D-ST).
- **Q7 — corrected (omissions):** options (A) and (C) are never checked in the PDF; added. Answer BD unchanged.
- **Q8 — corrected:** the PDF's integrating-factor algebra is garbled (writes $ye^{-2x}$ where $ye^{-x}$ is meant and drops $e^{-2x}$ factors); rewritten cleanly. ODE, $f=1-x$ and answer BC unchanged.
- **Q10 — corrected (assumption stated):** as printed (no sign restriction on $x$) the region also contains $x\le-1$ where $xy\le8$ holds automatically, giving infinite area. The PDF silently uses the first quadrant; I stated this. Key $16\ln2-\frac{14}3$ is right for that region.
- **Q14 — corrected:** the PDF dismisses (D) with "remaining coloured part of (C)" and gives (A) only as "true when $h=\frac34$"; replaced by explicit arguments (a bound $G_b\le\frac16$ for (A), sign changes at both ends for (D)). Answer BCD unchanged.
- **Q18 — corrected:** the PDF writes $h-k^2<0$ for the chord to be real; the correct condition is $h-k^2>0$ (mid-point lies inside the parabola; the final locus has $h-k^2=1$). Answer AC unchanged.
- All other questions — `pdf`: checked step by step and reproduced. Minor notation slips fixed silently in Q4 (missing $t$ in the integrand of $F$), Q13 (written "$12x^2+38x-6x-19$", it is $12x^2+32x-19$) and Q22 (the PDF writes "$\theta=8\times\dots$" where $\alpha$ is meant).

## Answer key
Every answer was checked by computation (numerical integration, symbolic differentiation, Monte-Carlo for Q6 and Q22, sign checks for Q14). No wrong key found: Q1 ABD, Q2 B, Q3 D, Q4 3, Q5 A-PRS B-P C-PQ D-ST, Q6 C, Q7 BD, Q8 BC, Q9 4, Q10 C, Q11 A, Q12 A, Q13 6, Q14 BCD, Q15 8, Q16 B, Q17 B, Q18 AC, Q19 11, Q20 2.5, Q21 7.5, Q22 0.75 are all correct. (The Q10 key assumes the first-quadrant region, see above.)

## Alternate solutions and useful results
- **Alternates: 20 of 22 questions** (all except Q11 and Q20). Each verified against the answer, numerically where possible. Examples: Q2 $2\min(\sin x,\cos x)$ + symmetry; Q3 test function $e^{x-1/2}$ eliminates three options; Q5 shortcuts per item; Q6 horizontal strips; Q7 sign changes instead of solving; Q8 guess $f=1-x$ and prove uniqueness; Q10 one integral in $y$; Q13 subtract $(g-f)^+$ from the tent; Q14 identity $R_a-G_b=G_a-R_b=\frac12-h$; Q15 three triangles of height $n$, bases sum to 1; Q18 $t_1,t_2$ parametrisation; Q19 unit circle meets $u+v=1$; Q21 angle between normals; Q22 elliptic-sector area $\frac{ab}2\Delta\varphi$.
- **Questions with NO alternate (2), one line each:**
  - Q11 — the only variant is rewriting in $\cosh/\sinh$ (same integral, same intersection condition); not a different method.
  - Q20 — the only route is finding an antiderivative of $e^{-x}(\sin x+\cos x-1)$ and adding absolute changes between roots; any other route (e.g. integrating by parts twice) is the same computation.
- **Useful results given for all 22 questions.**

## make_ppt.py warnings and notes
- No warnings. Two harmless notes: "Q5: very long question - font reduced to 20 pt" and "Q14: very long question - font reduced to 20 pt" (kept; question text is long by nature). No "could not convert" messages: 1059 equations converted to native PowerPoint equations.
- Rendering/thumbnails were skipped (no soffice/`/mnt/skills`); the deck was not visually inspected.

## Skipped / assumed / guessed
- Concepts self-assigned; marks assumed as above; Q19–Q22 shared stems are repeated on each of their question slides.
- Q4 type label: Numerical (the PDF's answer is the integer 3; no marks or digit-range printed).
- Hindi text of the PDF omitted.
