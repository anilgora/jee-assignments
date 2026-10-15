# Run report - SHEET_SOLUTION_OF_TRIANGLE_FCopy_C2

Paper: Exercise C-II (Solution of Triangle), 31 questions, 115 marks (assumed). Deck: 210 slides.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.51** (no equivalence-relation or multi-correct adjustment applies).
- Questions per level: L1 = 3, L2 = 12, L3 = 13, L4 = 3, L5 = 0. Ratings are my own application of the calibrated rubric; the only close anchors are the 2021-P1-Q18 cot-ratio question (L2) and the 2023 Solution-of-Triangle stem (L4/L5), so confidence is Medium for several (Q3, Q6, Q8, Q12, Q18, Q29, Q31) and Low for Q30.

## Blueprint / concepts / marks
- No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
- Marks assumed (none printed): Numerical and Subjective questions 4 marks (Q1-22), Paragraph single-correct 3 marks (Q23-28), Matching 3 marks (Q29-31). Stated in the section dividers.
- Types assumed: Numerical = single numeric answer (Q2, 3, 6, 8, 9, 10, 13, 18, 19); Subjective = prove / find / determine (Q1, 4, 5, 7, 11, 12, 14-17, 20-22); paragraphs Q23-25 and Q26-28; matching Q29-31. Q12 (answer 7*pi*R/12) was treated as Subjective.

## Solutions with solution_source "corrected" (18)
- Q1: PDF stops after the cosine-rule formulas; values and the ratio 7:19:25 never shown. Added.
- Q2: PDF has cos A = (5 - a^2)/3; denominator 2bc = 4. Corrected (a^2 = 3, answer 9 unchanged).
- Q3: PDF has C = 9*pi/7; correct C = 4*pi/7.
- Q6: PDF has sin(B/2) where sin(A/2) is meant; steps written out in clean form.
- Q9: PDF writes q/sin(theta1) = 2R for triangle ABD; the side opposite theta1 is BD = p.
- Q11: PDF assumes AB parallel to DC (not given) and labels an angle 30 deg; finds one arrangement only. Rewritten with the given data (3 and 2 in either order); the PDF's trapezoid is the alternate.
- Q12: PDF has 45R^2/64 for 49R^2/64, "angle BDC" for angle CBD, and "r" for R in the final arc.
- Q13: two garbled lines (2cos^2 = a/5, "= A/K") cleaned up.
- Q14: PDF proves only (i) => (ii); the steps for (ii) and (iii) start from A = B and the implication (iii) => (i) is missing. Complete chain written.
- Q15: PDF ends at the third sides; area step added.
- Q16: PDF has B2 = 2nR^2 tan(2*pi/n); correct is tan(pi/2n).
- Q17: PDF uses the inradius formula instead of the exradius to the hypotenuse; rewritten. PDF's final angles and b/c = 2 + sqrt3 are right.
- Q18: PDF has (r-9)(r-9) for (r-4)(r-9) and "6r^2 = 72r + 66 = 0"; corrected, r = 11 unchanged.
- Q19: PDF takes A directly above P without saying so; answer 3 holds for every position (checked numerically; proved in the alternate).
- Q20: PDF stops at 7/(4R^2) = 1 - 6/(8R^3); cubic solved, values of (a), (b) added.
- Q21: PDF stops before the Heron step and the equality case; added.
- Q29: (A) factor 2 missing and cos A = 1 used; see also the answer-key note below.
- Q30: (B) wrong direction of monotonicity (see key note); (C) rewritten as the radical-axis argument.

## Solutions with solution_source "written" (1)
- Q22: the PDF gives only the hint I_n = (n/2) sin(2*pi/n), O_n = n tan(pi/n). Full proof written. The identity needs n >= 4 (false for n = 3), which the question does not state.

## Answer key problems
- **Q29 (B)**: key B -> Q (9*3^(1/3), about 12.98) is only the A.M.-G.M. bound, not the least value of k: equality needs equal tangents t with 3t = t^3 = 9, impossible. Q.M.-A.M. already gives k >= 27 and the true minimum is about 36.39 (not in Column II). Kept as keyed in the answer line, flagged in the note and the alternate.
- **Q30 (B)**: key B -> P ("r >= 1") is wrong; the correct relation is r <= 1 (equality iff r1 = r2). No option states it. Kept as keyed in the answer line, flagged.
- All other keys re-derived and checked numerically (Q3, Q6, Q8, Q9, Q12, Q13, Q17, Q18, Q19 for several positions of A, Q20 incl. existence of the triangle, Q31).

## Alternate solutions
Alternates (different technique or viewpoint, verified) for 29 of 31 questions: Q1-24, 26, 28-31.
Questions with NO alternate (2):
- Q25: each fraction is 2 by one observation (c sin B = b sin C = x); no other route exists.
- Q27: O is the midpoint of AC, triangle BOC is equilateral, inradius is side/(2*sqrt3); other formulas are the same step.
Borderline alternates (different viewpoint, similar arithmetic): Q11 (isosceles-trapezoid configuration - verifies rather than derives), Q14 (all three conditions equivalent to A = B), Q18 (Heron form r^2(x+y+z) = xyz, same quadratic), Q20 (only part (b)), Q23 (area instead of sine rule), Q29 (item-wise tools).

## Useful Result / Pattern
All 31 questions have useful_results (3-4 bullets each).

## make_ppt.py warnings
- "Q28: only 3 solution bullets" - split into 4 bullets and rebuilt. No warnings remain.
- No "could not convert" warnings; 1261 equations converted to native equations.

## Skipped / assumed / guessed
- Concepts, marks and question types are assumed as above; the paper's figures were read from page images, the diagrams themselves are not reproduced in the deck (the question text names the circles/points instead; Q18 describes the figure's radii 1, 4, 9 at A, B, C).
- Column I/II of the matching questions are in the question text (no separate options), as in earlier decks.
- No recalc.py, thumbnails or rendering; the deck was not opened in PowerPoint here. The xlsx has live formulas without cached values.
