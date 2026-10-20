# Trigonometric_Ratio: generation report

Blueprint: `qp_blueprints/Trigonometric_Ratio.xlsx`. There is no `Trigonometric_Ratio_config.xlsx`, so the check ran without `--config`.
This scheduled run made the paper on 20-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy, mpmath and python-docx were missing for `python3`. I installed them with `python3 -m pip install ...` (plain `pip` installs into a different Python).
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- `build_paper.py --blueprint` passed on the first build with **no errors and no warnings**. No script was edited and no check was weakened.
- I rendered page 1 of each of the three PDFs and page 4 of the questions PDF and looked at them. The Hindi is shaped and the equations are 2D. This paper has no paragraph question.

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the blueprint has only Single Correct and Numerical types and nothing above level 3.
- **Paper:** 24 questions (blueprint Sr No 679-702): 3 Single Correct (Q1-Q3), then 21 Numerical (Q4-Q24).
- **Reorder (`--reorder`):** old Sr No -> new Q:
  689->1, 690->2, 694->3, 679->4, 680->5, 681->6, 682->7, 683->8, 684->9, 685->10, 686->11, 687->12, 688->13, 691->14, 692->15, 693->16, 695->17, 696->18, 697->19, 698->20, 699->21, 700->22, 701->23, 702->24.
- **Answer Plans:** the blueprint had none, so the script drew all 24. Every answer matches its plan (the build checks this).
  - SCQ: Q1 C, Q2 A, Q3 B.
  - Numerical: Q4 positive 2-digit integer; Q5 negative decimal; Q6 negative integer; Q7 positive decimal; Q8 decimal between 0 and 1; Q9 positive 3-digit integer; Q10 negative integer; Q11 positive 2-digit integer; Q12 negative decimal; Q13 decimal between 0 and 1; Q14 positive 3-digit integer; Q15 positive decimal; Q16 positive decimal; Q17 negative decimal; Q18 positive 2-digit integer; Q19 positive 3-digit integer; Q20 negative integer; Q21 decimal between 0 and 1; Q22 negative integer; Q23 negative decimal; Q24 positive 3-digit integer.
- **Cells containing ";":** rows 2, 4, 17 and 18 (as numbered by the check). No config, so each cell was kept as **one** concept. They are "Trigonometric ratios of allied angles; signs in the four quadrants" and "Range of a.sin(x) + b.cos(x); maximum and minimum", which read as single concepts.
- **Warnings** (recorded, not fixed; the blueprint was not edited; no errors):
  - Q2 and Q6 list 3 concepts, unusual for the Main pattern. Both kept; each question uses all three.
  - Concepts repeat across rows, as expected in a one-chapter paper (sum-to-product Q1/Q2/Q13/Q21; telescoping Q1/Q2/Q22; measurement Q4/Q5/Q6; allied angles Q5/Q7; compound angles Q3/Q6/Q8/Q9/Q24; multiple angles Q6/Q9/Q10/Q11/Q15; half angle Q11/Q12; non-standard angles Q14/Q15; A+B+C = pi Q3/Q16; range of a sin + b cos Q17/Q18; constrained max/min Q18/Q19; AP series Q2/Q20/Q21; elimination Q23/Q24). Every use has its own mechanism; no setup is reused.

## Answers
| Q | Type | Answer | Level (target) |
|---|---|---|---|
| 1 | SCQ | (C) | 3 (3) |
| 2 | SCQ | (A) | 3 (3) |
| 3 | SCQ | (B) | 2 (2) |
| 4 | Num | 18 | 2 (2) |
| 5 | Num | -0.9 | 2 (2) |
| 6 | Num | -117 | 3 (3) |
| 7 | Num | 1.4 | 2 (2) |
| 8 | Num | 0.6 | 2 (2) |
| 9 | Num | 192 | 3 (3) |
| 10 | Num | -5 | 2 (2) |
| 11 | Num | 75 | 3 (3) |
| 12 | Num | -0.2 | 2 (2) |
| 13 | Num | 0.28 | 2 (2) |
| 14 | Num | 112 | 2 (2) |
| 15 | Num | 3.2 | 2 (2) |
| 16 | Num | 7.25 | 2 (2) |
| 17 | Num | -4.5 | 2 (2) |
| 18 | Num | 13 | 2 (2) |
| 19 | Num | 120 | 2 (2) |
| 20 | Num | -5 | 2 (2) |
| 21 | Num | 0.75 | 2 (2) |
| 22 | Num | -7 | 2 (2) |
| 23 | Num | -0.6 | 2 (2) |
| 24 | Num | 576 | 3 (3) |

Every answer was recomputed in Python (mpmath at 40 digits, sympy), separately from the written solutions: direct evaluation of the sums (Q1, Q2, Q9, Q14, Q15, Q20, Q21, Q22), reconstruction of the configuration (Q3 triangle angles, Q4 sector and incircle, Q5 blade positions, Q6 arc and chord, Q8 and Q13 angle pairs, Q12, Q23 with an explicit theta), grid search for the extrema (Q17 minimum, Q18 maximum over the triangle, Q19 brute force over x, y), and sympy simplification of the eliminant in Q24.

## Level distribution and index
- Level 2: 18 questions. Level 3: 6 questions (Q1, Q2, Q6, Q9, Q11, Q24).
- Marks-weighted index (SCQ 3 marks, Numerical 4 marks): **2.24**. No equivalence relations and no MCQ, so neither adjustment applies. (This is a JEE Main pattern chapter test; the blueprint itself targets 18 level-2 and 6 level-3 rows, so the index follows the blueprint.)
- **No question is one level off its target.**
- **Consistency pass** (sorted by level, neighbours compared):
  - Q11 (nested radical on the interval where cos 2theta < 0) is the weakest Level 3; rated with **Low** confidence. If you see it as 2, the index drops to about 2.20.
  - Q22 (tan-product telescoping over multiples of pi/7) and Q20 (pairwise cosine sum) are the hardest Level 2s; either could be read as 3.
  - The anchor bank has few Trigonometric Ratio items; ratings lean on 2024-P1-Q3 (L3), 2025-P2-Q15 (L4), 2026-P1-Q4 (L2), 2021-P1-Q18 (L2).

## Originality report
Every question was web-checked with web search on its distinctive structure. Perfect novelty cannot be guaranteed; please tell me if you recognise any question.

| Q | Mechanism | Web check | Standard ingredient |
|---|---|---|---|
| 1 | Denominator cos 1 + cos(2k-1) is 2 cos k cos(k-1) after sum-to-product; then tan-difference telescoping to (1/2) cosec 1. | ingredient only | **yes**: sum of 1/(cos k cos(k+1)) for k = 0..44 is published; here the product is hidden |
| 2 | Reciprocals of the partial sums S_n of an AP sine series telescope as cot 3n - cot(3n+3). | not found | 1/(sin a sin b) = (cot a - cot b)/sin(b-a) |
| 3 | Triangle fixed by A - B = pi/4 and tan C = 3; tan A tan B from cos(A-B), cos(A+B), then the A+B+C = pi tan identity. | not found | tan A + tan B + tan C = tan A tan B tan C |
| 4 | Sector known only by arc length and area; recover r and the radian angle, then the incircle of the 60 degree sector. | not found | incircle of a 60 degree sector |
| 5 | Three-blade fan: arc 19.05 pi m at radius 0.9 m is ten turns plus 210 degrees; the 120 degree offsets place the tips in different quadrants. | not found | arc = r theta, allied angles |
| 6 | Arcs l and 2l with only chord AB known; angle from the chord, then cos(theta + 2theta). | not found | chord = 2r sin(theta/2) |
| 7 | Sum of cos(theta + k pi/2) for k = 1..2026: period-4 cancellation, remainder sign fixed by the third quadrant. | not found | allied angles |
| 8 | cos(alpha-beta)/cos(alpha+beta) = (1+p)/(1-p) from tan sum and tan(alpha+beta); sign from the obtuse alpha+beta. | not found | tan(A+B) |
| 9 | 40, 80, 160 degrees as roots of cos 3theta = -1/2; cube power sum of the reciprocal cubic gives 192. | ingredient only | **yes**: sec^2 20 + sec^2 40 + sec^2 80 = 36 and sec 40 + sec 80 - sec 20 = 6 are known; the cube version was not found |
| 10 | tan 3theta/tan theta depends only on cos 2theta: (1+2cos2theta)/(2cos2theta-1) = -5. | not found | triple angle |
| 11 | sqrt(2 + sqrt(2 + 2cos 4theta)) on (pi/4, pi/2) equals 2 sin theta, not 2 cos theta; then sqrt(2+sqrt3) = 2cos 15 gives 75. | ingredient only | **yes**: "simplify sqrt(2 + sqrt(2 + 2cos 4theta)) = 2 cos theta" is a published textbook item. The sign case and the reverse decoding are the new part. **Closest to published material**; replace it if you want more distance. |
| 12 | sin(theta/2) + cos(theta/2) with theta/2 beyond 3pi/4: the squared route gives +-1/5, the quadrant gives the sign. | not found | half-angle signs |
| 13 | alpha - beta = 2pi/3 makes cos alpha + cos beta = cos((alpha+beta)/2). | not found | sum-to-product |
| 14 | cosec 18 and sec 36 are sqrt5 +- 1; fourth-power sum 112. | not found | values of sin 18, cos 36 |
| 15 | sin 36 sin 72 = 2(1 - cos^2 36)cos 36 = sqrt5/4. | not found | double angle, cos 36 |
| 16 | Sum of cosec^2 of a triangle's angles from the sum of cotangents via sum cot A cot B = 1. | not found | **yes**: the identity sum cot A cot B = 1 is standard |
| 17 | cos x(3 sin x - 4 cos x) = (3/2) sin 2x - 2 cos 2x - 2, amplitude 5/2. | not found | range of a sin + b cos |
| 18 | C = 60 degrees: 7 sin A + 8 sin B = 11 sin A + 4 sqrt3 cos A, amplitude 13, maximiser inside the triangle. | not found | range of a sin + b cos |
| 19 | sin x + sin y = 1 bounds x - y via 2 + 2cos(x-y) = 1 + (cos x + cos y)^2. | not found | sum-of-squares trick |
| 20 | Pairwise cosine sum over 11 of 12 equally spaced directions via |sum|^2, the AP sums giving P = -1, Q = 0. | not found | **yes**: the n = 3 version (sum cos(a-b) = -3/2) is a classic; the non-closing AP is new |
| 21 | Three cosine products sixty degrees apart add to the constant 3/4 (product-to-sum remainders form a vanishing AP sum); asked at pi/7. | not found | product-to-sum |
| 22 | Tan-product telescoping over k pi/7; tan(6pi/7) = -tan(pi/7) kills the irrational part: -7. | ingredient only | **yes**: the telescoping identity is a coaching staple, and a different (cyclic) 2pi/7 identity with value -7 is published |
| 23 | x = cos/(1+sin), y = sin/(1+cos) satisfy x + y + xy = 1. | not found | elimination |
| 24 | x = 5cos(theta+alpha), y = 5cos(theta-alpha), tan alpha = 3/4: eliminant 25x^2 - 14xy + 25y^2 = 576. | ingredient only | **yes**: the general eliminant for x = a cos(theta-alpha), y = b cos(theta-beta) is a textbook result; here the numbers must be carried to the reduced integer form |

No search found a near-identical problem, so no question was redesigned after the web check.

## Problems found while verifying
- **The web search assistant made errors that I checked and rejected.** In each case my answer stands:
  - Q18: it reported the maximiser A = 72.6 degrees. Recomputed: tan A = 11/(4 sqrt3) gives A = 57.8 degrees (still inside the triangle, so the maximum 13 is attained).
  - Q7: it assumed theta in the first quadrant and got -1.4. The stem states sin theta < 0, so theta is in the third quadrant and the answer is 1.4.
- **Uniqueness conditions added to stems:** Q5 (order and sense of the blades), Q6 (l less than half the circumference), Q19 (0 <= y <= x <= pi), Q24 (integers with no common factor, p > 0).
- Q11: 15 degrees also satisfies the radical equation; the interval (pi/4, pi/2) excludes it, which is the point of the question.
- The stem review is a self-check; an independent reader may still find things.

## Rows whose concepts were hard to combine naturally
- **Q20 and Q22 (AP series alone, telescoping alone, negative integer):** sums of cosines over AP with standard angles only give 0, +-1/2, +-1; a search over all multiples of 15 degrees found no natural sum <= -2. I used a pairwise-difference sum (Q20) and a tan-product sum whose end terms cancel (Q22) to reach a negative integer naturally.
- **Q9 (compound + multiple angles, 3-digit integer):** the compound angle enters only through cos 3theta = cos(2theta + theta); the question is driven by the triple-angle cubic.
- **Q11 (multiple + half angle, 2-digit integer):** the answer is a degree measure (75); Q19 is also a degree measure (120).

The Hindi is my own translation. Please review the specialised terms: त्रिज्यखण्ड (sector), पंखुड़ी (blade), विलोपन (elimination), डिग्री माप (degree measure).
