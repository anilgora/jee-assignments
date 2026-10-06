# RUN REPORT - JEE_Main_Question_Bank_01_Integral_Calculus_09

Paper: 20 questions (printed Q161-Q180), deck numbers 1-20, all Area Under Curve. Q1-14 single correct (4 options), Q15-20 numerical value. 134 slides.

## Difficulty
- Marks-weighted difficulty index (adjusted levels): **2.35** (188 / 80 marks; all questions 4 marks). No equivalence-relation adjustment or MCQ floor applied.
- Questions per level: Level 1: 2 (Q7, Q12) | Level 2: 9 (Q1, 3, 5, 6, 8, 10, 11, 13, 20) | Level 3: 9 (Q2, 4, 9, 14, 15, 16, 17, 18, 19) | Levels 0, 4, 5: none.
- Lowest-confidence (Medium) ratings: Q2, Q4, Q6, Q9, Q14, Q15, Q16, Q17.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): +4 for every question (single correct and numerical), JEE Advanced default; stated on the section dividers.

## Solutions whose source is corrected or written
- Q5 (printed 165) - corrected: the PDF gives the second intersection as (-2, 4); it is (-2, -4) (its own graph shows this). Integral and answer 4/3 unchanged.
- Q9 (printed 169) - corrected: the PDF's "Case (i) y>0" uses f<0 and x in (1,2) U (3,4). For y>0 the condition is f>0, i.e. x in (0,1) U (2,3); (1,2) U (3,4) is the y<0 case. The four-strip integral and answer 32/3 unchanged.
- Q15 (printed 175) - corrected: the last antiderivative bracket (for the integral of sqrt(y)) has limits 0 to 4 instead of 2 to 4, and the line "80sqrt2/3 - 16 = 40sqrt2/3 - 16" is false. Correct: A = 40sqrt2/3 - 16 = 80sqrt2/6 - 16, alpha = 6, beta = 16. Answer 22 unchanged.
- Q16 (printed 176) - corrected: the PDF gets 12 from 1/2*2*2 + 1/2*3*3 + 1/2*1*11, treating curved pieces as triangles (true areas on [0,3] and [3,4] are 14/3 and 16/3, not 9/2 and 11/2; errors +-1/6 cancel). Replaced by exact integrals; answer 12 unchanged.
- All other questions are `pdf` (working verified). Small additions without changing the PDF's method: Q1 (rejecting x = -1), Q2 (rectangle sides), Q4/Q14 (why the negative root gives no enclosed region), Q8, Q10, Q11, Q12, Q17 (why the bounded piece is below the axis; triangle spelled out), Q19 (evaluation of the arcsin bracket; PDF's alpha/beta renamed b/c to match the question).
- No question was `written`.

## Answer key
All 20 printed answers were checked (numerical integration for all, plus exact derivations) and are correct. No key errors.
- Q4 (printed 164) and Q14 (printed 174) are the same question with the same solution; both kept as separate deck questions (numbers 4 and 14), with different alternate solutions.
- Q17 (printed 177): taken literally, the set {0<=9x<=y^2, y>=3x-6} has an unbounded piece above the x-axis (touching the lower piece only at the origin). The PDF's answer 15 uses the bounded piece below the axis (A = 5/2); that reading was followed and stated in the solution.

## Alternates
Alternate solutions given for **19 of 20 questions** (all except Q7), each checked numerically (areas by numerical integration; Q14's Simpson computation and Q19's segment-plus-triangle decomposition by direct evaluation). Methods used: Archimedes/parabola-chord formula (Q2, Q3, Q5, Q8, Q9, Q18), different slicing (Q1, Q11, Q15, Q17), polygon minus curve (Q6), trapezoid plus log (Q10), factorisation and shift (Q12), reflection symmetry (Q13, Q20), max = f + (g-f)^+ (Q16), golden-ratio reduction (Q4), Simpson's rule (Q14), circular segment plus triangle (Q19). Closer relatives of the main method (stated honestly): Q1 (x-slicing with a trigonometric substitution is heavier than the main solution), Q9 (same integral reinterpreted as half of a known region), Q20 (relies on the same symmetry idea as Q13).

### Questions with NO alternate
- Q7 (printed 167): the area is the single integral of 1/x - a/x^2 over [1,2]; any other route (differentiating in a, substitution u = 1/x) is the same antiderivative reworded, so none was given.

## Useful Result / Pattern
Every one of the 20 questions has a `useful_results` slide (4 bullets each).

## make_ppt.py warnings
None. The build printed no warnings and no "could not convert" notes; 815 equations converted to native PowerPoint equations; 134 slides. Slides were not rendered or opened in PowerPoint here (no soffice rendering in this environment).

## Skipped / assumed / guessed
- Concepts and levels self-assigned; levels are judgement against the calibrated anchors (cited per question in the ratings file). This is a Main-level bank, so levels sit at 1-3.
- Question types "Single Correct Type" / "Numerical Type" taken from the answer format (four options vs blank); marks assumed 4.
- The PDF text layer was garbled, so all pages were read from page images (100 dpi); Q15's integral limits were confirmed on a 220 dpi crop.
