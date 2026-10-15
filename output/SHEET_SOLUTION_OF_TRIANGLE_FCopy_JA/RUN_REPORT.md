# Run report - SHEET_SOLUTION_OF_TRIANGLE_FCopy_JA

Paper: Exercise J-A (Solution of Triangle), 13 questions (printed as 1-11, 14, 15; the paragraph parts are numbered 12-13 in the deck), 50 marks (assumed). Deck: 98 slides.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.86** (143/50; no equivalence-relation adjustment; Q9 carries the multi-concept flag but its level 3 is already above the 2.5 floor).
- Questions per level: L1 = 1 (Q5), L2 = 3 (Q1, Q3, Q10), L3 = 6 (Q2, Q4, Q6, Q8, Q9, Q11), L4 = 2 (Q7, Q13), L5 = 1 (Q12).
- Q9, Q10, Q12 and Q13 are official JEE Advanced 2021/2023 questions that are in the anchor bank (2021-P2-Q2 L3, 2021-P1-Q18 L2, 2023-P2-Q14 L5, 2023-P2-Q15 L4); the user's own levels were used. Q1-Q8 and Q11 are my application of the rubric; confidence Low for Q11, Medium for Q2, Q4, Q6, Q7, Q8.

## Blueprint / concepts / marks
- No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
- Marks assumed (none printed): single-correct, one-or-more-correct and numerical 4 marks each (Q1-Q11); paragraph-based parts 3 marks each (Q12-Q13). Stated in the section dividers. Types: Q1, Q3 single correct; Q2, Q4, Q6-9, Q11 one or more correct; Q5, Q10 numerical; Q12-13 paragraph numerical.

## Solutions with solution_source "corrected" (5)
- Q3: PDF prints (a^2+b^2-c^2)/2ab = 7/2 (should be -1/2); its last line 3ab/(4c(x+c)) loses a factor 2 (s taken as a+b+c); correct 3ab/(2c(x+c)) = option B.
- Q4: PDF has s-z = k (should be 2k); (D) is never checked in the PDF - added.
- Q6: PDF states angle R = 30 deg from the sine rule (wrong; angle QRP = 120 deg, PR = QR makes it isosceles); (A) never ruled out - added.
- Q9: notation fixes only (PDF writes '=' where '>' is meant in (D); (q-p)/p for (q+r)/p in (C)); the arguments are right.
- Q11: PDF uses RS = 1 without justification; the angle chase (angle QSR = angle SQR = 55 deg) was added.

## Solutions with solution_source "written" (0)
None. Q2, Q7, Q10, Q12, Q13 are "pdf": the PDF working is correct; a few missing justifications (tangent-length setup in Q2, centroid argument in Q7) were added as extra bullets without changing its method.

## Answer key problems
None found. Every key (1 C, 2 BD, 3 B, 4 ACD, 5 6, 6 BCD, 7 ABC, 8 BC, 9 AB, 10 2, 11 AB, 14 1008, 15 0.25) was re-derived and checked numerically (Q7 by coordinates, Q9 by 20,000 random triangles, Q12 by computing the sides and area).

## Alternate solutions
Alternates for 12 of 13 questions: Q1-Q10, Q12, Q13 (cosine-rule numerics; tangent-length/r^2 method; r=(s-c)tan(C/2); tangent lengths with half-angle tangents; trig parametrisation; coordinates (Q6, Q7); sum-to-product half-angle identity; elimination by test triangles; altitude-foot cot formula; angle-only route with area 2R^2 sinA sinB sinC; r = ac/6R).
Questions with NO alternate (1):
- Q11: after the angle chase the only route is the two sine rules (the 'distance of S from PR' view is the same step reworded); no genuinely different method.
Borderline alternates (different viewpoint, similar arithmetic): Q1 (numerical cosine-rule check), Q9 (elimination by counterexamples; (A) and (B) still rest on the same identities), Q13 (short formula route).

## Useful Result / Pattern
All 13 questions have useful_results (3-4 bullets each).

## make_ppt.py warnings
- None printed. 620 equations converted to native equations; no "could not convert" notes.

## Skipped / assumed / guessed
- Concepts, marks and types assumed as above. Figures (Q2, Q3, Q6, Q7, Q11, Q12) were read from page images; the diagrams are not reproduced in the deck.
- PDF lines for Q12 (d^2 = 1/4) were partly garbled in the text layer; I re-derived them (a^2 = 7/4, d^2 = 1/4, area 3*sqrt7/16).
- No recalc.py, thumbnails or rendering; the deck was not opened in PowerPoint. The xlsx has live formulas without cached values.
