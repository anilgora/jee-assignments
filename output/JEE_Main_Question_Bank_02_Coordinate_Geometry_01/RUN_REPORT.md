# RUN REPORT - JEE_Main_Question_Bank_02_Coordinate_Geometry_01

Paper: 20 questions (printed 1-20, numbered 1-20), all single-correct with four options (coordinate geometry: circles, parabola, ellipse, straight line). Read from the PDF text layer plus page images for garbled symbols. 132 slides, 878 native equations.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.15** (4 marks each; computed by hand as 43/20; no equivalence-relation questions, no multi-correct questions, so no adjustments; workbook formulas not recalculated - recalc.py unavailable).
- Questions per level: Level 1: 3 (Q1, Q8, Q12) | Level 2: 11 (Q2, Q3, Q4, Q5, Q9, Q10, Q11, Q14, Q17, Q18, Q19) | Level 3: 6 (Q6, Q7, Q13, Q15, Q16, Q20). No Level 0, 4 or 5.
- Confidence: High for most; Medium for Q5, Q6, Q7, Q13, Q15, Q16, Q17, Q20 (JEE Main bank, anchors point in different directions).

## Blueprint
No blueprint used. **Concepts self-assigned (no blueprint) - please review.** Marks assumed (none printed): 4 marks for every Single Correct question (JEE Advanced default), 0 otherwise; stated on the section divider.

## Solutions whose source is corrected or written
- Q4 - corrected: PDF line "x/(3p) + y/(2p) = 1" is wrong; it should be x/(2p) + y/(2p/sqrt3) = 1 (the next PDF line a=2p, b=2p/sqrt3 and the answer are right).
- Q13 - corrected: typos in the PDF working: the common root is printed as "x^2 = -sqrt(c)/sqrt(a)" (should be x = -sqrt(c)/sqrt(a)), and "b = sqrt(ae)" should be b = sqrt(ac). Logic and answer unchanged.
- Q17 - corrected: PDF prints the tangent as "3x - xy = 7"; it should be 3x - 4y = 7 (its later working already uses 3x - 4y - 7). Answer unchanged.
- Q12 - written: the PDF gives the answer (C) but no working; a complete solution was written (centre (3,-4), r = 8 sqrt2, vertices (3+-8, -4+-8), nearest (-5,4) at sqrt41).
- All other questions: source pdf (steps reproduced; where the PDF compresses a step - e.g. Q6's elimination of m, Q2's checks, Q16's option test, Q10's check of the other options - the step was expanded into separate bullets).

## Answer key
All 20 keys verified by computation (hand derivation plus numeric checks in Python): 1 D, 2 C, 3 A, 4 D, 5 A, 6 D, 7 C, 8 C, 9 C, 10 A, 11 A, 12 C, 13 B, 14 D, 15 C, 16 B, 17 B, 18 A, 19 C, 20 B. No key looks wrong. (Option texts in the PDF are partly garbled in the text layer; I read them from page images.)

## Alternates
Given for all 20 questions. Methods: Q1 radical axis + perpendicular diagonals; Q2 power of a point; Q3 parametric points (centroid alone fixes P, Q); Q4 right-triangle angles (OBA = 60 degrees); Q5 median to hypotenuse; Q6 circumcentre as unknown mid-point with tangency c*m=a; Q7 parametric tangent + Vieta; Q8 coordinates (centre (h,0)); Q9 homogenisation; Q10 test options with the focal-sum property; Q11 mid-line of a trapezoid (centre distance); Q12 dot-product sign choice; Q13 G.P. as a, ar, ar^2; Q14 no-parameter + similar triangles; Q15 constant 1/OP^2 + 1/OR^2; Q16 focal polar form; Q17 line of centres; Q18 tangent parallel to the chord; Q19 complex-number rotation; Q20 subtangent + tangent lengths.
- Lighter variants (shares the setup with the main solution but a different final technique): Q8 (coordinates versus half-chord geometry), Q12 (vector sign choice versus listing four vertices), Q13 (a, ar, ar^2 parametrisation), Q14. These were kept because the closing step is genuinely different, but they are the weakest alternates - review if you want only fully independent methods.

## Questions with NO alternate
None - every question has an alternate.

## Useful Result / Pattern
Given for all 20 questions.

## make_ppt.py warnings
None (only the equation count and the save line). No "could not convert" notes.

## Skipped / assumed
- Thumbnails/rendering, soffice and recalc.py skipped (not available); the xlsx has live formulas without cached values.
- Marks assumed as above; levels are my own ratings with the calibrated skill, nearest anchors cited in the ratings JSON.
- The PDF has no figure-based information that I could not read; Q19's PDF figure was used only to confirm B(-t,t), C(t,-t).
