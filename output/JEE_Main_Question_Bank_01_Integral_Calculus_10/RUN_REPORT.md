# RUN REPORT - JEE_Main_Question_Bank_01_Integral_Calculus_10

Paper: 11 questions (printed Q181-Q191), deck numbers 1-11, all Area Under Curve, all numerical-value answers. 84 slides.

## Difficulty
- Marks-weighted difficulty index (adjusted levels): **2.45** (108 / 44 marks; all questions 4 marks). No equivalence-relation adjustment or MCQ floor applied.
- Questions per level: Level 1: 1 (Q4) | Level 2: 4 (Q2, Q8, Q9, Q11) | Level 3: 6 (Q1, Q3, Q5, Q6, Q7, Q10) | Levels 0, 4, 5: none.
- Medium-confidence ratings: Q1, Q3, Q5, Q6, Q7, Q8, Q10, Q11.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): +4 for every question (all numerical type), JEE Advanced default; stated on the section divider.

## Solutions whose source is corrected or written
- Q8 (printed 188) - corrected: the PDF writes the trapezoid term as 1/2(3/2+1/2) x 2 (= 2); its next line and the answer use 1. The factor should be 1 (height 1). Also made explicit why the line x+y=2 bounds the region for x>=1. Answer 17 unchanged.
- Q9 (printed 189) - corrected: the antiderivative bracket of the integral of (1-x^2) is printed with limits b and 1 instead of 0 and -1 (value 2/3 is right for -1..0); and the remark about "infinitely many parabolas" is replaced by the fact that y=p(x) is a unique quadratic. Answer 16 unchanged.
- All other questions are `pdf` (working verified). Small additions without changing the PDF's method: Q1 (intersection points, explicit evaluation of each integral and the cancelling surds), Q3 (angle renamed phi to avoid clashing with the question's alpha), Q5 (explicit AM-GM equality), Q6 (explicit derivative factorisation and the k -> -k symmetry), Q7 (reading the inequalities), Q10 (why the broken-path area equals the three triangle terms).
- No question was `written`.

## Answer key
All 11 printed answers were checked (numerical integration or grid-area counting for every question, plus exact derivations) and are correct: 119, 304, 171, 164, 7, 8, 5, 17, 16, 16, 42. No key errors.
- Q6: k = 0 gives no bounded region (area tends to 0, a minimum); the maximum is at k = +-2 as in the PDF.

## Alternates
Alternate solutions given for **all 11 questions**, each checked numerically/exactly: Q1 horizontal slicing; Q2 parabola-segment formula (36 - 32/3); Q3 half-disc minus sector and triangle; Q4 trapezoid minus the sliver; Q5 Archimedes (segment = 4/3 of inscribed triangle, O cannot beat the apex); Q6 general formula 1/(6(alpha+beta)^2) with AM-GM; Q7 line-parabola area minus a quarter-disc segment (2/3 - (pi/4 - 1/2)); Q8 triangle minus the part above f; Q9 vertical strips between the lower arc and the parabola; Q10 parabola-above-tangent gap 2(x-1)^2 (2/3 - 2/5); Q11 triangle plus parabola segment minus the eighth-disc.
Honest note: Q2, Q4 and Q8 alternates are "complement" versions of the main idea (area = bigger piece minus piece), the weakest in terms of novelty; still different decompositions.

### Questions with NO alternate
None.

## Useful Result / Pattern
Every one of the 11 questions has a `useful_results` slide (4-5 bullets each).

## make_ppt.py warnings
None. The build printed no warnings and no "could not convert" notes; 499 equations converted to native PowerPoint equations; 84 slides. Slides were not rendered or opened in PowerPoint here (no soffice rendering in this environment).

## Skipped / assumed / guessed
- Concepts and levels self-assigned; levels are judgement against the calibrated anchors (cited per question in the ratings file). This is a Main-level bank, so levels sit at 1-3.
- Question types taken from the answer format (all numerical, including Q184 whose stem ends with a colon); marks assumed 4.
- The PDF text layer was garbled, so all pages were read from page images (100 dpi); Q8's "x 2" was confirmed on a 200 dpi crop.
