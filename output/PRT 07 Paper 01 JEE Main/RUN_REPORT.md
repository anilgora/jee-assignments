# Run report: PRT 07 Paper 01 JEE Main

## Inputs
- Paper: `papers/PRT 07 Paper 01 JEE Main.pdf` (15 pages, scanned image PDF with solutions printed, no text layer; read from page images). 25 maths questions: Q1-20 single correct, Q21-25 numerical (the paper restarts numbering at 1 for the numerical part; deck numbering is continuous 1-25).
- Blueprint: none. **Concepts self-assigned (no blueprint) - please review.**
- Marks are not printed, so JEE Advanced defaults were assumed and stated in the section dividers: single correct 4 each (Q1-20), numerical 4 each (Q21-25). Total 100. (The real JEE Main marking of -1 for wrong answers is not printed, so it is not shown.)
- Types: Q21-25 are shown as Numerical (answers 2, 1, 10, 5, 0.6 - the last is not an integer 0-9).

## Difficulty (calibrated skill; no equivalence-relation questions, no multi-correct questions)
- Marks-weighted difficulty index: **1.16** (far below the official Advanced range 2.59-3.21, as expected for a JEE Main paper).
- Questions per level: L0 = 6 (Q2, Q7, Q9, Q10, Q13, Q14); L1 = 10 (Q3, Q5, Q6, Q8, Q11, Q15, Q16, Q17, Q19, Q20); L2 = 8 (Q1, Q4, Q12, Q18, Q22, Q23, Q24, Q25); L3 = 1 (Q21); L4 = 0; L5 = 0.
- Medium/Low confidence is marked in the Excel; Q21 (Low) is the one most worth a second look.

## Solutions whose source is corrected or written
- **Q18 (corrected):** the PDF stops after finding x1 = R/sqrt2 and gives key (D) without doing the Lagrange part. Added: chord slope sqrt2 R, solving A'(c) = sqrt2 R gives c = (R/4) sqrt(7 - sqrt17) ~ 0.424R, which matches none of R/2, R/(2 sqrt2), R/4. Key (D) is correct.
- **Q21 (corrected):** the PDF proves only "at least 2 distinct roots" and gives 2 as the minimum. A minimum also needs an example with exactly 2 roots; added f(x) = 1 - 3x (g has exactly one root near -0.338, checked numerically). Answer 2 is correct.
- All other questions: `pdf` (every step re-derived; final answers confirmed with sympy or by hand). Small gaps filled without changing the method: Q5 (the image-formula substitution was skipped in the PDF), Q10 (the PDF never states "x = 2" at the end), Q13 (the PDF is a figure only; the "right angle at A, so H = A" reasoning was written out), Q22 (the solving for new coordinates of A and B was skipped).

## Answer key check
- Q25: the key reads "0.6, 1". 0.6 is correct (6/10); the stray "1" is unexplained (perhaps a duplicate or a typo). Answer shown: 0.6.
- No other key looks wrong (Q1-24 all match my computed answers).

## Alternates and useful results
- Alternate solutions were written for Q1-Q16 and Q18-Q25 (24 of 25).
- Q17 has no alternate: the only way to evaluate the limit is one-sided analysis of [x] and {x} near 0; any other route is the same argument reworded, so none was invented.
- Modest alternates (a different viewpoint of the same idea rather than a wholly different technique): Q2 (step-deviation), Q10 (sign pattern of f'), Q20 (gradient normals), Q5 (the geometric method printed in the PDF itself), Q9 (half-angle form), Q16 (completing the square). The rest are genuinely different methods (e.g. Q1 homothety from the meeting point of the tangents, Q6 complex series, Q8 elimination by domain and sign, Q19 reciprocal substitution, Q23 reflection map, Q24 circle through O with AB as diameter).
- Every question 1-25 has useful_results.

## make_ppt.py output
- No warnings: "880 equations converted to native PowerPoint equations", 150 slides, 25 questions. No "could not convert" notes.

## Skipped / assumed / guessed
- No rendering or thumbnail check of the slides was possible (no soffice); only the script's own checks were used.
- Concept names, chapters and levels were assigned by me; anchors for Q4, Q22 and Q25 are only loosely comparable.
- Python environment: the system PIL was broken; fixed with `pip install --force-reinstall pillow` (not part of the repo).
