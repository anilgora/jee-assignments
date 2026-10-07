# RUN REPORT - JEE_Main_Question_Bank_02_Coordinate_Geometry_03

Paper: 20 questions (printed 41-60, numbered 1-20 in the deck; deck n = printed n+40): 7 single-correct (Q1-7) and 13 numerical (Q8-20). Coordinate geometry: straight line, circle, parabola, ellipse, hyperbola. Read from the PDF text layer plus page images for the garbled symbols. 130 slides, 845 native equations.

## Difficulty
- Marks-weighted difficulty index (adjusted): **1.85** (4 marks each; 37/20; no equivalence-relation or multi-correct questions, so no adjustments; workbook formulas not recalculated - recalc.py unavailable).
- Questions per level: Level 1: 6 (Q1, Q2, Q4, Q7, Q9, Q20) | Level 2: 11 (Q3, Q5, Q6, Q8, Q10, Q13, Q14, Q15, Q16, Q17, Q19) | Level 3: 3 (Q11, Q12, Q18). No Level 0, 4 or 5.
- Confidence: High for Q1, Q2, Q4, Q7, Q9, Q20; Medium for the rest (JEE Main bank questions; anchors point in different directions).

## Blueprint
No blueprint used. **Concepts self-assigned (no blueprint) - please review.** Marks assumed (none printed): 4 marks for every question (single-correct and numerical), 0 otherwise; stated on the section dividers.

## Solutions whose source is corrected or written
- Q3 (printed 43) - corrected: the PDF ends with x^2 + 4by + 4b^2 - 4a^2 = 0. With centre (x,y) = (-g,-f), 4bf = -4by, so the locus is x^2 - 4by + 4b^2 - 4a^2 = 0. Sign slip; still a parabola.
- Q7 (printed 47) - corrected: the PDF's angle formulas use the wrong denominators (1+m2m3 in all three) and it gives tan B = -3. Correct: tan A = (m1-m2)/(1+m1m2) = 3, tan C = (m3-m1)/(1+m1m3) = 3, tan B = (m2-m3)/(1+m2m3) = 3/4. Conclusion (A = C, isosceles) unchanged.
- Q14 (printed 54) - corrected: typo "sqrt(13)/2" for cos 30 degrees in the tangent line (should be sqrt(3)/2); later values and the answer 39 are right.
- No question is "written": every question has a PDF solution.
- All other questions: source pdf. Steps the PDF compresses were expanded into separate bullets (Q1 gets the missing "the triangle must be the smaller part" check; Q5 gets the sign of alpha; Q10 the "first two lines are not parallel" remark; Q12 the sign choice for positive intercepts; Q18 the PDF's unjustified "maximum at C(4,4)" is justified by convexity with numerical end-point values). Notation-only fix in Q13: the PDF says "polar of P(2,beta)" where S(alpha,beta) is meant; the deck uses S.

## Answer key
All 20 keys verified by hand and numerically in Python: 1 C, 2 B, 3 B, 4 C, 5 D, 6 D, 7 A, 8 1225, 9 32, 10 32, 11 32, 12 8, 13 11, 14 39, 15 113, 16 4, 17 36, 18 48, 19 216, 20 3. No key is wrong.
- Q11 (printed 51): the y-axis x = 0 is also a common tangent of the two curves (touching both at the origin, so P = Q and PQ = 0); the intended answer 32 uses the non-degenerate tangents. Mentioned in Useful Results.
- Q17 (printed 57): the answer 36 does not depend on whether C is above or below the x-axis (both checked).
- Q8: "positive x-axis" is taken loosely; the normal meets the x-axis at (-1/4, 0) as the PDF does, and the area is unchanged.

## Alternates
Given for 19 of the 20 questions, each reaching the same answer (checked numerically): Q2 centroid divides the median 2:1 (R = 2r); Q3 r^2 = y^2 + (half-chord)^2 = distance to the point; Q4 contact points as centre +/- r times the unit normal; Q5 find theta from the ordinate (no elimination); Q6 rotate AB by 90 degrees; Q7 vertices and side lengths; Q8 right angle at P, legs 7/sin and 7/cos; Q9 translate the line by AB; Q10 explicit intersection point of two lines; Q11 tangent length PQ^2 = PC^2 - r^2; Q12 reflection symmetry in the x-axis (y = x - 3 is common to P and Q); Q13 pole at distance r^2/d along the perpendicular; Q14 slope-form tangent c^2 = a^2m^2 + b^2; Q15 elimination to (alpha - 8)z = beta - 6; Q16 standard hyperbola form and normal intercept on the conjugate axis; Q17 base angle gives B and the slope of BC directly; Q18 calculus (f' = 0 and convexity); Q19 tangent first (c^2 = a^2m^2 - b^2) and d = x_P sqrt(1+m^2); Q20 angle bisector locus.
- Lighter variants (share the setup with the main solution but the closing technique differs): Q4 (contact points vs distance formula), Q9, Q10 and Q20 (same equations reached differently). Review if you want only fully independent methods.

## Questions with NO alternate
- Q1 (printed 41): the only route is "corner triangle has area 2, so alpha*beta = 4, mid-point xy = 1". Viewing it as a rectangle of area half the triangle's, or using the 1/5 fraction directly, is the same computation reworded, so no genuinely different method was invented.

## Useful Result / Pattern
Given for all 20 questions.

## make_ppt.py warnings
None (only the equation count and the save line). No "could not convert" notes.

## Skipped / assumed
- No slide rendering or thumbnails (soffice/recalc.py unavailable); the difficulty workbook formulas have no cached values.
- Marks assumed 4 for every question (not printed); no AIR marks slide (none supplied).
- Chapters/concepts self-assigned; Q15 spans two chapters (family of lines, system of equations).
