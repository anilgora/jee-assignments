# Run report - JEE_Main_Question_Bank_02_Vector_3D_01

**Difficulty index (marks-weighted, adjusted): 1.95** (20 questions x 4 marks; no equivalence-relation or multi-correct adjustments apply).
Levels: L1 = 5 (Q2, Q5, Q10, Q15, Q18), L2 = 11, L3 = 4 (Q1, Q4, Q11, Q12), L0/L4/L5 = 0.

**Blueprint:** none was available. Concepts self-assigned (no blueprint) - please review.
Marks assumed: the paper prints no marks; JEE Advanced default of 4 per single-correct question used for all 20 (stated on the section divider; no negative marking assumed).

## Questions with solution_source = corrected (PDF solution had slips; answers unchanged)
- Q1: stray extra vector a at the end of b = lambda(-2i-2j+2k); triple-product expansion and the acute-angle check on b were not shown (added).
- Q4: coplanarity determinant had 1 instead of 2 in the first row; also see answer-key note below.
- Q7: PDF writes 5*lambda = 0; the expansion gives -5*lambda = 0 (lambda = 0 unchanged).
- Q8: dot signs missing in (v x w)v and (v x w)w; dot product intended.
- Q11: division by a, b, c without justifying K != 0 (added; otherwise a=b=c=0).
- Q12: (a+b)x(a-b) printed as 2i+10j+6k; correct is -2i+10j+6k (norm unchanged, 140); BAC-CAB step added.
- Q14: normal written as AC = (a,-a,-4) but plane used is ax-ay+4z=0; normal along CA is (a,-a,4).
- Q19: the "reduced determinant" step does not follow from any row/column operation; replaced by direct expansion (same value 34*alpha - 146).
- No question needed solution_source = written; all other questions are `pdf`.

## Answer key
Q4: strictly, the internal bisector of b and c is a = (4,2,4), which matches no option. The key (B) corresponds to the external bisector (along b-hat minus c-hat), a = (1,2,-2). The key is kept (only consistent option) but the stem is loosely worded. All other keys verified correct (checked by hand and with sympy for Q4, Q8, Q9, Q12, Q13, Q19).

## Alternates and results
- Alternate solutions given for 18 of 20 questions (all except Q11 and Q16).
- No alternate: Q11 - the decisive step (the three equal products force 1/a+1/b+1/c = 0 via the cosine sum) is unique; other routes merely recompute the same sum. Q16 - line/plane intersection, distance and sum/product of roots is a single natural path; no genuinely different method.
- useful_results given for all 20 questions.
- Alternates checked: Q1 b=sqrt2(1,1,-1); Q2 x=85/14; Q3 point (12,20,10); Q4 two sign cases; Q5 right-triangle test; Q6 explicit coordinates; Q7 |AP x d|^2/|d|^2=74; Q8 w=(7,-1,1)/6; Q9 x=5/3 or 31/15; Q10 options tested; Q12 (lambda-1=0); Q13 normal (27,30,25); Q14 CD^2=72-6; Q15 numerical quadrilateral; Q17 a x b=-n x b; Q18 option test; Q19 plane normal (15,17,24); Q20 affine combination.

## make_ppt.py warnings
None. 672 equations converted, 113 slides, no "could not convert" messages.

## Skipped / assumed / guessed
- No visual rendering of the deck (no soffice/thumbnails); build-only check.
- Levels are my calibrated judgement (no blueprint difficulty column); nearest anchors cited are approximate.
- Hindi text in the PDF was ignored; only the English statements were used.
