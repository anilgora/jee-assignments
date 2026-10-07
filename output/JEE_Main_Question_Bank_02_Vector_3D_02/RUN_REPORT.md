# Run report - JEE_Main_Question_Bank_02_Vector_3D_02

**Difficulty index (marks-weighted, adjusted): 2.25** (20 questions x 4 marks; no equivalence-relation or multi-correct adjustments apply).
Levels: L1 = 3 (Q7, Q13, Q14), L2 = 9 (Q1, Q2, Q4, Q5, Q8, Q10, Q11, Q16, Q20), L3 = 8 (Q3, Q6, Q9, Q12, Q15, Q17, Q18, Q19), L0/L4/L5 = 0.
Deck numbering Q1-Q20 = paper Q21-Q40 (the PDF starts at question 21).

**Blueprint:** none was available. Concepts self-assigned (no blueprint) - please review.
Marks assumed: the paper prints no marks; JEE Advanced default of 4 per question used for all 20 (single-correct Q1-Q14 and the "Integer type" Q15-Q20), no negative marking assumed; stated on the section dividers.
Q15-Q20 are headed "Integer type" in the paper but have answers 0.8, 15, 5, 7, 3501, 288 (not 0-9), so they are labelled "Numerical Type".

## Questions with solution_source = corrected (answers unchanged)
- Q1 (paper 21): PDF repeats the "Intersection of (1) & (2)" block under the heading "(1) & (3) B" (stray duplicate); removed and the elimination written out.
- Q2 (paper 22): PDF argues |a| < 3/10 hence |a| < 3 max|a_i| - does not follow; replaced by a_i^2 <= m^2 => |a|^2 <= 3m^2. Strict "<" in the PDF vs "<=" in the statement also fixed.
- Q3 (paper 23): PDF has 3(a-2)^2 = 8x3(a^2+2) (extra factor 3; next line is the right quadratic) and "b >= -8" (correct range from |a-b|<=10 with a=-2 is -12 <= b <= 8).
- Q10 (paper 30): PDF writes a = lambda|n2 x n2| (should be n1 x n2), a.b = lambda|0+4+2| (should be 6 lambda); also computes n2 from i-j, i-k while the stem says i-j, j-k (same plane).
- Q14 (paper 34): PDF writes (a2 . a1) in the shortest-distance numerator; it must be (a2 - a1).
- No question needed solution_source = written; all others are `pdf`.

## Answer key
All 20 keys verified correct (hand computation plus sympy for Q3, Q6, Q9, Q12, Q15, Q18, Q19, Q20 and the quadratics/determinants in Q5, Q9, Q11, Q12).

## Alternates and results
- Alternate solutions given for 19 of 20 questions (all except Q19).
- No alternate: Q19 - the only route is "minimum of u.(v x w) is at u antiparallel to v x w, then project on i"; other routes (Lagrange multipliers, Cauchy-Schwarz) are the same step reworded.
- useful_results given for all 20 questions.
- Alternates checked: Q1 affine signed distance (-23/3, -1/3 -> -4); Q2 cube geometry test a=(.05,.05,.05); Q3 same quadratic 5a^2+12a+4 via |n x p|; Q4 OT.(0,2,1)=0 so 171; Q5 combination x=11/5, y=-1/5, z=2; Q6 (20+a^2)^3-6912a = (a-2)^2(positive quartic); Q7 symmetric roots 2, -1; Q8 explicit example b=(0,0,1), c=(1,-2,0); Q9 factor argument D=4abc (sympy); Q10 common vector (0,1,-1); Q11 min 5 sqrt(3/2); Q12 minors -18a+54, 3-3b; Q13 alpha*beta = 1; Q14 12/5; Q15 t = 5/9 -> lambda = 4/5; Q16 mu = 1/28; Q17 r/R = 1/4; Q18 same quadratic 5b^2+18b+9; Q20 foot (-3/7,-9/7,6/7).

## make_ppt.py warnings
First build printed two "could not convert" notes for Q20's last results bullet; they were caused by a shell-quoting slip in my edit (text corrupted). Fixed the text and rebuilt: no warnings. 821 equations converted, 129 slides.

## Skipped / assumed / guessed
- No visual rendering of the deck (no soffice/thumbnails); build-only check.
- Levels are my calibrated judgement (no blueprint difficulty column); nearest anchors cited are approximate.
- Hindi text in the PDF was ignored; only the English statements were used.
- Q1 alternate (affine signed distance) is a modest variation on the primary; kept as it avoids computing the mid-point.
