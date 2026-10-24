# Run report: RPT 02 Paper 01 JEE Main

## Inputs
- Paper: `papers/RPT 02 Paper 01 JEE Main.pdf` (19 pages, scanned, no text layer; read from page images, solutions printed). 25 maths questions: 20 single correct (Q1-20) and 5 numerical (paper numbering Q1-5), deck numbering continuous 1-25.
- Blueprint: none. **Concepts self-assigned (no blueprint) - please review.**
- Marks are not printed; JEE Advanced defaults assumed and stated in the section dividers: single correct 4 (Q1-20), numerical 4 (Q21-25). Total 100. Same convention as RPT 01 Paper 01. The five numerical answers (8, 9, 3, 5, 60) are shown as "Numerical Type" because 60 is outside 0-9.

## Difficulty (calibrated skill)
- Marks-weighted difficulty index (adjusted): **2.38** (below the official Advanced range, as expected for a JEE Main paper).
- Questions per adjusted level: L1 = 3 (Q11, 16, 17); L2 = 10 (Q1, 2, 3, 4, 6, 7, 10, 18, 20, 22); L2.5 = 1 (Q19, equivalence-relation +0.5); L3 = 10 (Q5, 8, 9, 13, 14, 15, 21, 23, 24, 25); L4 = 1 (Q12); L0, L5 = 0.
- Q19 carries the equivalence-relation adjustment (counting equivalence relations on a 3-set is part of the key step). No MCQs, so no multi-correct floor.
- Confidence High on Q2, 4, 6, 10, 11, 16, 17, 18, 20, 22; Medium on the rest; no Low.
- The xlsx has live formulas without cached values (recalc.py is not available here); open it in Excel to see computed values.

## Solutions whose source is corrected or written
- **Q12 (corrected):** PDF Case 2 claims at least 4 non-differentiable points for every k not 0. That is false: a direct count gives 4 points for 0<|k|<1 and only 3 for |k|>=1 (e.g. k=2: x = 0, 1, 2+sqrt3). Conclusion S = {0} and answer (C) unchanged (3 > 2); working now proves "at least 3", using the symmetry x -> 2-x (k <-> -k).
- **Q13 (corrected, minor):** two sign slips: for set A (|x|>1) the PDF writes "x <= 2 => x in [2, inf)" (should be x >= 2); for set B (|x|>1) it writes "x >= x+1 => 0 >= 1" (should be x <= x+1 => 0 <= 1). Sets and answer (A) unchanged. A typo "BA = ..." on the last line is dropped.
- **Q25 (corrected, minor):** PDF gives the one-sided slopes of g at x=0 as -1 and +1; correct values are -1/2 and +1/2. Still a corner; N = 3 and the answer 60 unchanged.
- No question is `written`; the other 22 are `pdf`. Small gaps filled without changing the method (still `pdf`): Q2 (explanation of the final count of corners), Q3 (discriminant check), Q8 (explicit region counts), Q20 (y >= 1 because y is in A, while the PDF writes 0 <= 3y <= 23), Q21 (g(x) written piecewise), Q24 (x=1 treated separately from k >= 2).

## Answer key check
- All 25 printed answers match my independent check (hand derivation, numerical evaluation in Python): Q1 C, Q2 B, Q3 B, Q4 D, Q5 B, Q6 B, Q7 A, Q8 B, Q9 D, Q10 B, Q11 B, Q12 C, Q13 A, Q14 D, Q15 A, Q16 C, Q17 A, Q18 C, Q19 B, Q20 B, then 8, 9, 3, 5, 60. No wrong key found.

## Alternates and useful results
- Alternate solutions were written for 21 of 25 questions.
- Genuinely different methods: Q1 (boundary value + test point option elimination), Q2 (additive function h = f - x^2), Q7 (derivative is zero, constant from the limit at 0-), Q9 (evaluate at the end-point x -> 1-), Q10 (quadratic in u = sin^2), Q11 (n(AΔB) = n(A)+n(B)-2n(A∩B)), Q18 (period by sin/cos swap; cos decreasing on [0, pi]), Q21 (rule for f(|x|)), Q23 (L'Hopital four times instead of series), Q25 (direct tangent addition), Q6 (t = sin^2 3x, f = t^2 - t + 1 and its symmetry), Q5 (long division / oblique asymptote), Q16 (directed-graph view), Q22 (test the 11 integers).
- Modest alternates (same core idea, different viewpoint or order): Q3 (monotonic f(x) - x has one root), Q4 (complement counting), Q8 (union = 80 + k, check endpoints), Q12 (shift t = x - 1, mirror symmetry in k), Q13 (single sweep over regions), Q19 (standard limits and Bell recurrence), Q20 (divisibility view).
- **No alternate: Q14.** Every term is handled by the same squeeze/bounding argument; any other route (e.g. x = 1/n) is not equivalent for a continuous limit.
- **No alternate: Q15.** Continuity, the condition alpha > 1 and the IVT are each the only natural tool; option elimination would reuse the same three facts.
- **No alternate: Q17.** The sandwich theorem on sin x cos(1/x) is the single idea; a series expansion would only reword it.
- **No alternate: Q24.** The per-interval smoothness, the left-limit test at each integer and the special case x = 1 have no genuinely different route.
- Every question 1-25 has useful_results.
- Checks done: Q1 formula at x = 0.1, 0.5, 0.7; Q7 value 0 at x = -0.9, -0.5, -0.1; Q9 f = pi, g = pi/2 at x = 0.6, 0.8, 0.99; Q12 corner count by numerical derivative scan for k from -3 to 3 (2 at k=0, 4 for 0<|k|<1, 3 otherwise); Q13 membership test of sample points in B minus A; Q14 limit numerically 0.857143; Q20 fundamental period 24 by search; Q23 numerically 3.0; Q24 one-sided limits and slopes at x = 1..5; Q25 tan S = 0.6. Others by hand.

## make_ppt.py output
- "1091 equations converted to native PowerPoint equations", 165 slides, 25 questions. No warnings, no "could not convert" notes.

## Skipped / assumed / guessed
- No rendering or thumbnail check of the slides was possible (no soffice); only the script's own checks.
- Concept names, chapters, levels and nearest anchors assigned by me; anchors are only loosely comparable for several rows.
- Question text was transcribed from the solutions pages (the paper has no separate question section).
- Python environment: system PIL was broken; fixed with a forced reinstall of Pillow; sympy and numpy installed for checks (not part of the repo).
