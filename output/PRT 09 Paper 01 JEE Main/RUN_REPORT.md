# Run report: PRT 09 Paper 01 JEE Main

## Inputs
- Paper: `papers/PRT 09 Paper 01 JEE Main.pdf` (16 pages, scanned, no text layer; read from page images, solutions printed). 25 maths questions: 20 single correct (Q1-20) and 5 numerical (paper numbering Q1-5), deck numbering continuous 1-25.
- Blueprint: none. **Concepts self-assigned (no blueprint) - please review.**
- Marks are not printed; JEE Advanced defaults assumed and stated in the section dividers: single correct 4 (Q1-20), numerical 4 (Q21-25). Total 100. (Real JEE Main would carry -1 negative marking for SCQ; not printed, so not stated.)
- Type split assumption: the paper has no section headers; Q21-25 (answers 9, 4, 44, 96, 12) are shown as "Numerical Type" (44 and 96 are outside 0-9).

## Difficulty (calibrated skill; no equivalence-relation questions, no MCQs so no floor)
- Marks-weighted difficulty index (adjusted): **2.24** (below the official Advanced range 2.59-3.21, as expected for a JEE Main paper).
- Questions per level: L1 = 3 (Q1, Q3, Q20); L2 = 13 (Q2, Q4, Q6, Q7, Q9, Q11, Q13, Q15, Q18, Q22, Q23, Q24, Q25); L3 = 9 (Q5, Q8, Q10, Q12, Q14, Q16, Q17, Q19, Q21); L0, L4, L5 = 0.
- Confidence Medium on all except Q1, Q3, Q20 (High). No Low.
- The xlsx has live formulas without cached values (recalc.py is not available here); open it in Excel to see the computed values.

## Solutions whose source is corrected or written
- None. Every question is `pdf`: each step was re-derived and every final answer checked (sympy / numerical): all 25 printed answers are right.
- Small gaps filled without changing the method (still `pdf`): Q12 (added the verdicts for (B), (C), (D) with counterexamples, which the PDF omits); Q13 (shown the rearrangement from SS1 = T^2 to the printed quadratic, which the PDF skips); Q14 (stated the regrouping into (x dx + y dy) + sqrt(x^2+y^2)(y dx - x dy) before the polar step); Q2 (stated the range check of the tan^{-1} argument, which the PDF has).

## Answer key check
- All 25 printed answers match my independent computation (Q1 A, Q2 A, Q3 A, Q4 A, Q5 A, Q6 B, Q7 A, Q8 A, Q9 A, Q10 A, Q11 A, Q12 A, Q13 A, Q14 A, Q15 A, Q16 B, Q17 B, Q18 B, Q19 B, Q20 B, then 9, 4, 44, 96, 12). No wrong key found.
- Q12 note: only (A) is forced; the exact value is f''(c) = -3 for some c (second-difference theorem), shown as Alternate 2.

## Alternates and useful results
- Alternate solutions were written for 24 of 25 questions.
- Genuinely different methods: Q1 (Archimedes on the latus rectum), Q3 (normal in slope form), Q4 (option test via point and slope), Q6 (segment formula + reflected lobe), Q7 (equal slopes at contact), Q8 (parametric P = (a sec t, b tan t)), Q9 (split 1/x - x^2/(x^3+1), definite integral), Q10 (direct I.F. x*sqrt(1+x^2)), Q11 (La Hire: pole of x+y=6), Q12 (two alternates: convexity contradiction; second-difference theorem), Q13 (slope-tangency condition), Q15 (closed form floor/2 + {x}^2/2 and g = arctan f), Q17 (Darboux on LMVT slopes), Q18 (direct integration with u = 9^x), Q19 (special positions of P on the axes), Q21 (y = vx), Q22 (rectangle from perpendicular lines), Q23 (Archimedes + reflection), Q24 (AM-GM on the angle form + scaling dV/dt = 3V R'/R), Q25 (direct separation + Archimedes).
- Modest alternates (a different viewpoint on the same core idea): Q2 (common parameter phi = cos^{-1} x), Q5 (u = x^2 + y^2 and the exact differential d(tan^{-1}(y/x)), no polar coordinates), Q14 (exact differentials in Cartesian form instead of polar), Q16 (determinant elimination for order/degree).
- **No alternate: Q20.** g'(x) = 2x f(x^2) and f(4) = f(1) is the only reasonable route; any other route (chain rule on F(x^2)) is the same Leibniz step reworded.
- Every question 1-25 has useful_results.
- Numerical/symbolic checks: Q1 integral; Q2 derivative ratio to 30 digits; Q4 constant and point; Q5, Q10, Q14, Q21 substituted back into the ODE with sympy (residual 0); Q6 three sub-areas; Q8 k = 1/3 and the point P on the hyperbola; Q9 definite integral; Q11, Q13 pair of tangents expanded; Q12 counterexamples and f(0), f(1), f(2); Q15; Q16 f satisfies the ODE; Q18 numeric integral = 30; Q23 area = 44/3; Q25 area = 12. Q3, Q7, Q17, Q19, Q20, Q22, Q24 by hand.

## make_ppt.py output
- "1018 equations converted to native PowerPoint equations", 174 slides, 25 questions. No warnings, no "could not convert" notes.

## Skipped / assumed / guessed
- No rendering or thumbnail check of the slides was possible (no soffice); only the script's own checks.
- Concept names, chapters, levels and nearest anchors assigned by me; anchors are only loosely comparable for several rows.
- Question wording was transcribed from the solutions pages (the paper has no separate question section).
- Python environment: system PIL was broken; fixed with `pip install --force-reinstall pillow` (not part of the repo); sympy installed for checks.
