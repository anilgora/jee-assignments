# Run report: PRT 09 Paper 02 JEE Adv

## Inputs
- Paper: `papers/PRT 09 Paper 02 JEE Adv.pdf` (15 pages, scanned, no text layer; read from page images, solutions printed). 17 maths questions: Q1-4 single correct, Q5-8 one-or-more correct, Q9-10 paragraph (one shared stem), then 7 numerical answers (paper numbering restarts: Q1-4 and Q1-3), deck numbering continuous 1-17.
- Blueprint: none. **Concepts self-assigned (no blueprint) - please review.**
- Marks are not printed; JEE Advanced defaults assumed and stated in the section dividers: single correct 4 (Q1-4), one-or-more correct 4 (Q5-8), paragraph 3 (Q9-10), integer 4 (Q11-14), numerical 4 (Q15-17). Total 66.
- Type assumption: the PDF has no section headers (title says "I0,P,Q"). Q11-14 are shown as "Integer Type(0 to 9)" and Q15-17 as "Numerical Type" (all seven answers are single digits: 5, 4, 7, 2, 3, 6, 2); the split follows the paper's numbering restart.

## Difficulty (calibrated skill; no equivalence-relation questions; MCQ floor 2.5 set on Q5, Q6, Q8 but all already at or above it)
- Marks-weighted difficulty index (adjusted): **2.71** (179 / 66), inside the official Advanced range 2.59-3.21.
- Questions per level: L1 = 1 (Q13); L2 = 5 (Q7, Q9, Q12, Q16, Q17); L3 = 9 (Q1, Q2, Q3, Q4, Q6, Q8, Q10, Q11, Q15); L4 = 2 (Q5, Q14); L0, L5 = 0.
- Confidence Medium except Q7, Q12, Q13, Q17 (High). No Low.
- The xlsx has live formulas without cached values (recalc.py is not available here); open it in Excel to see the computed values.

## Solutions whose source is corrected or written
- **Q6 - corrected.** The PDF's own working gives the area in (D) as 5/3 - 2/pi (exactly the value in option D) but the key omits D. Correct answer is (A, C, D). Added the missing verdicts for (B) (area is 4/pi + 2/3, not 4/pi + 1/3) and (D).
- All other questions: `pdf`. Small gaps filled without changing the method: Q3 (the algebra for g(x) is shown in full, the PDF's "constant k" step shown); Q5 (verdict wording for each option); Q7 (named the property used for each statement).

## Answer key check
- **Q6: the key (A, C) looks wrong; correct is (A, C, D)** (see above; numerically: area for (D) = 1.0300 = 5/3 - 2/pi).
- All other printed answers match my independent computation (sympy / numerical): Q1 A, Q2 B, Q3 A, Q4 A, Q5 A,B,D (checked by random sampling of 200k admissible points), Q7 A,B,C,D, Q8 B,C,D, Q9 C, Q10 B, then 5, 4, 7, 2, 3, 6, 2.
- Q1 option (B) was read from a low-resolution page as e^{-(pi+1)/4}; it is a distractor and does not affect the answer.

## Alternates and useful results
- Alternate solutions were written for all 17 questions.
- Genuinely different methods: Q1 (gradient field of the family), Q2 (guess-and-verify antiderivative + focal-chord length), Q3 (circle through fixed normal-point argument + x = sin(theta) integral), Q4 (coefficient of y equals derivative of coefficient of y', no integrating factor), Q5 (factorisation (s-6)(s+3)^2 and position tests instead of calculus), Q6 (odd-symmetry of the outer pieces), Q8 (v as the independent variable with t = -ln(1-v)), Q9 (area = 1/2 PQ.ST with ST = 2a/sin theta), Q10 (diameter form of the circle), Q11 (cosh form and tanh), Q12 (affine map to the circle), Q13 (triangle + Archimedes segment), Q14 (reduce to ln(1+x) >= rational function, k = 2 is the classical inequality, second-order expansion for necessity), Q16 (sin^4 + cos^4 = (3 + cos 4t)/4, full periods cancel exactly), Q17 (split and integrate by parts).
- Modest alternates (a different technique but close to the main idea): Q7 (pairing x with -x and power reduction instead of the king / 2a-x properties), Q15 (x = sin(theta) and 3A1 + 12A2 = 3(A1 + A2) + 9A2; the first half of the solution is the same).
- **No question without an alternate.**
- Every question 1-17 has useful_results.
- Numerical/symbolic checks: Q1 (orthogonality product = -1), Q2 (antiderivative, limit, chord length), Q3 (integral), Q4 (ODE substitution residual 0), Q5 (sampling for A-D, closed forms for G, centre, H), Q6 (three areas and integral), Q7 (integral), Q8 (derivatives symbolic), Q9/Q10 (area 32, intercept 4 sqrt 13), Q11 (ODE integrated numerically, k = 5), Q12 (integral and chord formula), Q13, Q14 (f minimum for k = 1.9, 1.99, 2, 2.5; f''(0) and series symbolic), Q15, Q16 (sum equals 6 exactly for n = 4, 6, 10), Q17 (integrals). Q17 companion integral e^x(1+sin x)/(1+cos x) was checked by hand (derivative of e^x tan(x/2)).

## make_ppt.py output
- "926 equations converted to native PowerPoint equations", 141 slides, 17 questions. No warnings; two notes only: Q3 and Q5 questions are long so the font was reduced to 22 pt (harmless). No "could not convert" notes.
- First run crashed because one answer string had an unescaped LaTeX backslash (a form-feed character); fixed in the content file.

## Skipped / assumed / guessed
- No rendering or thumbnail check of the slides was possible (no soffice); only the script's own checks.
- Concept names, chapters, levels and nearest anchors assigned by me; anchors are only loosely comparable for several rows.
- The PDF's wording "Queen's property" was written as the 2a - x property.
- Python environment: system PIL was broken; fixed with `pip install --ignore-installed pillow` (not part of the repo); sympy and scipy installed for checks.
