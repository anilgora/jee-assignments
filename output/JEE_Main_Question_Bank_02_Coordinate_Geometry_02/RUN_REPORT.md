# RUN REPORT - JEE_Main_Question_Bank_02_Coordinate_Geometry_02

Paper: 20 single-correct questions (printed 21-40, numbered 1-20 in the deck; deck n = printed n+20). Coordinate geometry: circle, parabola, ellipse, hyperbola, straight line. Read from the PDF text layer plus page images for the garbled symbols. 134 slides, 873 native equations.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.20** (4 marks each; 44/20 by hand; no equivalence-relation or multi-correct questions, so no adjustments; workbook formulas not recalculated - recalc.py unavailable).
- Questions per level: Level 1: 3 (Q6, Q8, Q20) | Level 2: 10 (Q1, Q3, Q4, Q11, Q13, Q14, Q15, Q17, Q18, Q19) | Level 3: 7 (Q2, Q5, Q7, Q9, Q10, Q12, Q16). No Level 0, 4 or 5.
- Confidence: High for Q3, Q6, Q8, Q14, Q15, Q17-Q20; Medium for the rest (JEE Main bank, anchors point in different directions).

## Blueprint
No blueprint used. **Concepts self-assigned (no blueprint) - please review.** Marks assumed (none printed): 4 marks for every Single Correct question (JEE Advanced default), 0 otherwise; stated on the section divider.

## Solutions whose source is corrected or written
- Q5 (printed 25) - corrected: the PDF's quadratics are wrong. It prints (+) m^2+11m+4=0 and (-) 7m^2-11m-4=0 with roots m=1 or -4/7. The determinant equals -52m^2 and gives 9m^2+11m+4=0 (no real root) and 15m^2-11m-4=0 (roots 1 and -4/15). m=1 does not satisfy the PDF's printed 7m^2-11m-4=0. Final answer m=1 is right.
- Q4 (printed 24) - corrected: the PDF ends "...we get the answer (B)" although its own working (and the answer line "A/B") shows both (A) and (B) satisfy the conditions (normals at 15 and 75 degrees). Answer given as (A) or (B).
- Q12 (printed 32) - corrected: sign slip "beta - gamma = 2 sqrt(bc)" in step (2) (should be gamma - beta); "(A)+(2)+(3)" means (1)+(3). I also added the reason the smallest circle is the middle one. Result unchanged.
- No question is "written": every question has a PDF solution.
- All other questions: source pdf. Where the PDF compresses a step (Q1, Q18's incentre derivation, Q20's side/diagonal check, Q10's obtuse-angle choice, Q9's side lengths, Q11's notation clash of the letter "a", Q14, Q15, Q7), the step was expanded into separate bullets.

## Answer key
All 20 keys verified by computation (hand derivation plus numeric checks in Python): 1 B, 2 B, 3 A, 4 A/B, 5 B, 6 C, 7 A, 8 B, 9 D, 10 B, 11 B, 12 B, 13 A, 14 D, 15 D, 16 C, 17 A, 18 B, 19 D, 20 A.
- Q11 (printed 31): the key (B) 1 is the sharp bound (a > 1), but a > 1 also implies a > -1, a > 1/2 and a > -1/2, so as worded the question is ambiguous; (B) is the intended answer.
- Q4: the key A/B is correct (two valid lines).
- Q5: option (A) 4/15 is a distractor; the other root of the true quadratic is -4/15 (rejected as m > 0).
- Option texts in the PDF are partly garbled in the text layer; I read them from page images.

## Alternates
Given for 19 of the 20 questions. Methods: Q1 CP via cos(theta)=1-2sin^2(theta/2); Q2 common focus + foot of perpendicular on vertex tangent (rectangle); Q3 parametrise P=(2t,t); Q4 test each option with normal/line-direction cosine; Q5 area ratio CP/CA * CQ/CB; Q6 reflect the tangent instead of the curve; Q7 AH horizontal => BC vertical; Q9 right-triangle inradius; Q10 explicit P, Q and dot product; Q11 constant subnormal; Q12 Descartes' circle theorem with a line; Q13 substitute c=cos(theta); Q14 congruence mod 4; Q15 Vieta on the intersection quadratic; Q16 pole and polar of PQ; Q17 centre O-C parallel to tangents => distance = radius; Q18 right-triangle inradius; Q19 altitude to hypotenuse (1/h^2=1/a^2+1/b^2); Q20 90-degree rotation symmetry.
- Lighter variants (share the setup with the main solution but the closing technique differs): Q10 (explicit points vs homogenisation), Q19 (altitude relation is the same distance as the main formula), Q20 (symmetry vs side/diagonal check), Q3, Q18. Review if you want only fully independent methods.

## Questions with NO alternate
- Q8 (printed 28): the only route is to show (2,2) lies on x/a+y/b=1 given 1/a+1/b=1/2; intersecting with y=x or testing the point are the same step reworded, so no genuinely different method was invented. (A special-member elimination, a=b=4, is mentioned under Useful Results.)

## Useful Result / Pattern
Given for all 20 questions.

## make_ppt.py warnings
None (only the equation count and the save line). No "could not convert" notes.

## Skipped / assumed
- Thumbnails/rendering, soffice and recalc.py skipped (not available); the xlsx has live formulas without cached values.
- Marks assumed as above; levels are my own ratings with the calibrated skill, nearest anchors cited in the ratings JSON.
- Deck numbering is 1-20 although the PDF prints 21-40 (the PDF is the second half of a bank).
