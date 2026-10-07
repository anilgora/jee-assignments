# RUN REPORT - JEE_Main_Question_Bank_02_Coordinate_Geometry_04

Paper: 17 numerical questions (printed 61-77, numbered 1-17 in the deck; deck n = printed n+60), coordinate geometry (parabola, circle, ellipse, hyperbola, straight line). Read from the PDF text layer plus page images for garbled symbols. 107 slides, 807 native equations.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.12** (4 marks each; 36/17; no equivalence-relation or multi-correct questions, so no adjustments; workbook formulas not recalculated - recalc.py unavailable).
- Questions per level: Level 1: 2 (Q1, Q10) | Level 2: 11 (Q2, Q3, Q5, Q6, Q9, Q11, Q12, Q13, Q15, Q16, Q17) | Level 3: 4 (Q4, Q7, Q8, Q14). No Level 0, 4 or 5.
- Confidence: High for Q1, Q3, Q5, Q6, Q9, Q10, Q12, Q13, Q15; Medium for the rest.

## Blueprint
No blueprint used. **Concepts self-assigned (no blueprint) - please review.** Marks assumed (none printed): 4 marks for every question (all numerical), 0 otherwise; stated on the section divider.

## Solutions whose source is corrected or written
- Q11 (printed 71) - corrected: the PDF reflects the point Q(-1,0) "about l2: x-y+1=0", but Q lies on l2; the mirror must be the bisector l1: 3y-2x=3 (the numbers Q'(-17/13, 6/13), alpha = 7 are those of the reflection in l1). Naming error only; answer 348 correct.
- No question is "written": every question has a PDF solution.
- All others: source pdf. Steps the PDF compresses were expanded into separate bullets: Q2 (tangent meets axis at (-b,0)), Q8 (the PDF checks n+1 = 9, 25, 49 without saying why; the deck adds that e rational forces n+1 to be an odd perfect square), Q12 (the three vertices are solved explicitly), Q13 (the vertices Q, R and the area are written out), Q16 (the PDF's count for a = 4 is lost in the text layer; it is 2, as the figure and total 31 confirm).
- Minor PDF slips left out of the slides (do not change any result): Q6 takes t2 = 3 t1 although the ratio P:Q = 3:1 would give t1 = 3 t2 (the expression is symmetric; noted in the bullet); Q9 figure labels the centre (6,3) but it is (5,3) (noted in Useful Results); Q4 answer was already consistent.

## Answer key
All 17 keys verified by hand and numerically in Python (sympy/numpy): 1 0.5, 2 146, 3 122, 4 144, 5 7, 6 16, 7 1, 8 306, 9 3, 10 24, 11 348, 12 529, 13 10, 14 80, 15 9, 16 31, 17 904.
- **Q17 (printed 77): the key 904 is only the integer part of the true maximum 50625/56 = 904.0178...** The question says "maximum value", so the exact answer is 50625/56. The deck shows "904 (exact maximum 50625/56 ≈ 904.02; key gives the integer part)". Please decide how you want this stated.
- Q14 (printed 74): the PDF (and the deck) assume the square is centred at the origin ("by the symmetry of the curve"); the answer 80 matches the key under that assumption. A non-centred square was not ruled out.
- Q7 (printed 67): the internal-contact circle (r = sqrt2 - 1) is used; the externally tangent circle (r = sqrt2 + 1) contains C and gives no tangent from C (noted in Useful Results).

## Alternates
Given for 16 of the 17 questions (all but Q3), each reaching the same answer (checked numerically): Q1 parametric/sub-tangent; Q2 divisibility (a = c^3/32, power of 2); Q4 evaluation on an admissible equilateral triangle; Q5 normal-aligned distances (|2 - 9cos^2|); Q6 chord of contact + Vieta; Q7 coordinates: distance from centre to line CE; Q8 coprime factors and negative Pell equation; Q9 pole/polar of S; Q10 C midpoint of PQ + Apollonius; Q11 equal directed angles (slope formula); Q12 D from parallels and shoelace area; Q13 sine rule R = a/(2 sin A); Q14 polar form r^2 = 2/|sin 2 theta|; Q15 triangle B1 F B2 equilateral (2b = a); Q16 count by multiplier k; Q17 AM-GM.
- Lighter variants (share the setup with the main solution but the closing technique differs): Q1 (same tangent facts), Q10 (the same right-triangle facts via Apollonius), Q11 (shares the first step beta = -17), Q12 (same vertices). Review if you want only fully independent methods. Q4's alternate assumes the value is the same for every admissible triangle (the question implies it, and the main solution proves it).

## Questions with NO alternate
- Q3 (printed 63): every route (centroid equations, median to the midpoint of BC, vertices on two lines) leads to the same two linear equations in alpha, beta, a; no genuinely different method exists, so none was invented.

## Useful Result / Pattern
Given for all 17 questions.

## make_ppt.py warnings
None (only the equation count and the save line). No "could not convert" notes.

## Skipped / assumed
- No slide rendering or thumbnails (soffice/recalc.py unavailable); the difficulty workbook formulas have no cached values.
- Marks assumed 4 for every question (not printed); no AIR marks slide (none supplied).
- Chapters/concepts self-assigned; Q4 spans two topics (triangle centres, multiple-angle cosine), Q8 hyperbola plus number theory.
