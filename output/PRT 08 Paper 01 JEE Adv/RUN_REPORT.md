# Run report: PRT 08 Paper 01 JEE Adv

## Inputs
- Paper: `papers/PRT 08 Paper 01 JEE Adv.pdf` (16 pages, no text layer; read from page images, with solutions printed). 17 maths questions; the paper restarts numbering in each section (SCQ 1-4, MCQ 5-8, paragraph with two questions, integer 1-4, numerical 1-3); deck numbering is continuous 1-17.
- Blueprint: none. **Concepts self-assigned (no blueprint) - please review.**
- Marks are not printed; JEE Advanced defaults assumed and stated in the section dividers: single correct 4 (Q1-4), one-or-more correct 4 (Q5-8), paragraph 3 (Q9-10), integer 4 (Q11-14), numerical 4 (Q15-17). Total 66.
- Types: Q11-14 shown as Integer (0-9) (answers 4, 8, 3, 2); Q15-17 as Numerical (answers 3, 4, 60; 60 is outside 0-9).

## Difficulty (calibrated skill; no equivalence-relation questions)
- Marks-weighted difficulty index (adjusted): **2.91** (inside the official Advanced range 2.59-3.21).
- Questions per level (integer level): L2 = 5 (Q7, Q11, Q15, Q16, Q17); L3 = 9 (Q1, Q2, Q4, Q5, Q8, Q9, Q10, Q12, Q14); L4 = 3 (Q3, Q6, Q13); L0, L1, L5 = 0.
- Multi-correct floor (2.5) applied to Q7 (level 2 -> 2.5). Q5, Q6, Q8 are multi-concept but already above the floor.
- Confidence is Medium on most rows (High on Q7, Q11, Q16, Q17). No Low.

## Solutions whose source is corrected or written
- **Q4 (corrected):** the PDF writes `2 int_0^inf 1/(1+u^2) du/sqrt2 = sqrt2 [tan^-1 u]`, skipping a substitution; after u = tan x the integrand is 1/(1+2u^2) and the value pi/sqrt2 needs tan^-1(sqrt2 u). Value and answer unchanged. Strictness of the bounds on J also stated.
- **Q6 (corrected):** for statement (C) the PDF shows a unique root of 8c^3-8c-7=0 in (1,2) but never excludes (0,1), which "unique c in (0,2)" needs. Added: f'(x) = -pi sin(pi x) < 0 on (0,1). Answer unchanged.
- All other questions: `pdf` (every step re-derived; final answers checked symbolically/numerically). Small gaps filled without changing the method: Q2 (the point 4+sqrt2 where g regains the value 4 is derived; the PDF only lists f piecewise), Q7 (the PDF does not justify x^2+cos x > 0; added), Q8 (the g''' step written out with the corrected combined form).

## Answer key check
- All 17 printed answers match my independent computation (Q1 B, Q2 B, Q3 A, Q4 A, Q5 ABCD, Q6 ABCD, Q7 ABC, Q8 ACD, Q9 B, Q10 C, then 4, 8, 3, 2, 3, 4, 60). No key looks wrong.
- Q5 (C): the midpoint locus 25(x^2+y^2)-12x-16y=0 passes through the origin, but the origin itself is never attained (it is a limit as P goes to infinity); the key treats the statement as true and so do I.
- Option text of Q2 (A), "16/3", was read from a page image.

## Alternates and useful results
- Alternate solutions were written for all 17 questions (Q1-Q17).
- Genuinely different methods: Q1 (midpoint theorem on the right trapezoid O1P1P2O2), Q3 (bound-then-attain argument with an explicit circle), Q4 (elimination by size plus period mean), Q5 (pole-polar and inversion), Q7 (pairing identity for even h), Q8 (derivatives in the variable s=g(y)), Q11 (power-series coefficients), Q13 (integration by parts), Q16 (direction vectors).
- Modest alternates (a different viewpoint or toolset on the same core idea rather than a wholly different technique): Q2 (graph view of the running maximum), Q6 (local expansion at the join), Q9 (second-derivative parametric formula), Q10 (parameter s = t^2+1), Q12 (power-mean limit; the first half is shared with the main solution), Q14 (adapted coordinates and T=0), Q15 (graphical envelope view), Q17 (minimise the power as a quadratic in x).
- No question was left without an alternate.
- Every question 1-17 has useful_results.
- Numerical checks done: Q1 C3 contains all four contact points, chord 7; Q2 numerical one-sided slopes of the running maximum; Q3 min of the power over k; Q4 numerical integral 4499.48 inside the interval (A); Q5 fixed point, locus and minimum chord; Q6 limits, one-sided second derivatives, root and critical points; Q7 numerical f(1), f(pi); Q8 g', g'', g''', D, D' (sympy); Q9 parametric derivatives (sympy); Q10 x(sqrt(e-1)) = 1/e; Q11 series coefficients (a,b)=(1,2); Q12 limit; Q13 antiderivative check and g'(1/2); Q15 numerical slopes; Q16 angle; Q17 minimum power 144.

## make_ppt.py output
- "875 equations converted to native PowerPoint equations", 128 slides, 17 questions. Only note: "Q5: very long question - font reduced to 22 pt" (harmless, kept). No "could not convert" notes, no warnings.

## Skipped / assumed / guessed
- No rendering or thumbnail check of the slides was possible (no soffice); only the script's own checks.
- Concept names, chapters, levels and nearest anchors assigned by me; anchors for Q1, Q3, Q13 are only loosely comparable.
- Question wording was transcribed from the solutions pages (the paper has no separate question section).
- Python environment: system PIL was broken; fixed with `pip install --force-reinstall pillow` (not part of the repo).
