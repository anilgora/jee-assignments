# RUN REPORT - JEE_Main_Question_Bank_01_Vector_3D_02

Paper: 20 single-correct questions (Vector 3D). The PDF prints them as Q21-Q40; the deck numbers them 1-20 (deck Q1 = printed Q21, ..., deck Q20 = printed Q40).

## Difficulty
- Marks-weighted difficulty index (adjusted levels): **2.15** (43 / 20 questions, 4 marks each). No equivalence-relation adjustment or MCQ floor applied (all single correct).
- Questions per level: Level 0: none | Level 1: 2 (Q7, Q8) | Level 2: 13 (Q1-6, 9, 11, 13, 16, 17, 18, 20) | Level 3: 5 (Q10, 12, 14, 15, 19) | Levels 4 and 5: none.
- Low-confidence ratings: Q10 and Q12. This is a JEE Main-style bank, so the index sits below the JEE Advanced range.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed in the paper): JEE Advanced default for single-correct = 4 each (+4 correct, 0 otherwise, stated on the section divider).

## Solutions whose source is corrected or written
- Q10 (printed 30) - corrected (gap): the PDF writes the three component equations and then jumps to `|5a-11b-8g| = 25` with no working. Added the substitution showing lambda and the multiplier cancel (`-25`). The PDF also uses mu for the multiplier along L3, clashing with L2's parameter; renamed to t. Answer 25 unchanged.
- Q12 (printed 32) - corrected (gap, no wrong number): the PDF calls the root of `36a^2-36a+1=0` "C" (it is the x-component a), writes b with a bare "-+" sign, and carries only one root to the final vector. Added the sign pairing and showed that the other root gives a vector not among the options. Answer (3) unchanged.
- Q17 (printed 37) - corrected: equation (1) is printed `3 = k(-3 + 3*lambda)`; the sum is `2+6-15+3-2+3*lambda = -6 + 3*lambda` (its next line uses `k = 3/(-6+3 lambda)`, so (1) is a typo). Answer 25 unchanged.
- No question is `written`; all others are `pdf` (working verified; trivial notation tidied). Q21/Q29 intermediate lines (`x^2-4x+4+y^2+9 = ...` for Q9) were checked and are correct as printed.

## Answer key
All 20 printed answers were checked by independent computation (sympy / hand check) and none looks wrong. Q1 (printed Q21): with p,q,r equal to i,j,k the data are not geometrically consistent (circumcentre is not (3/8)(1,1,1)), so p,q,r must be general (non-orthonormal) vectors; the Euler-line working and the key (3) are valid for linearly independent p,q,r.

## Alternates
Alternate solutions given for 16 of 20 questions: Q2-Q13, Q16, Q18, Q19, Q20. Each was verified numerically or symbolically and reaches the same answer. Notes:
- Q13's alternate (determinant for the triple product, linear in x) is only a different route for the last step; x itself is found the same way.
- Q16's alternate (direction cosine l = sin(phi) cos(theta), d = OP sin(psi)) is close to the PDF route but uses a distinct viewpoint.
- Q5's alternate (expanding with s = a+b) is a different organisation of the algebra rather than a different idea.

### Questions with NO alternate
- Q1: Euler line 2:1 and Sylvester's relation (H = A+B+C-2O) are the same equation; the orthogonal/dot-product route is impossible without knowing p.q etc.
- Q14: `|c|sin(alpha) = 2/3` is forced by `|a| = |b||c| sin(alpha)`; any picture (distance of c from line of b) gives the same minimisation of 4/(9 sin^2 alpha).
- Q15: every route reduces to `|c|^2 - 12|c| + 30 = 0` (law of cosines or squaring); no different method.
- Q17: eliminating k is the whole problem; squaring `a.s = 3|s|` is the same equation.

## Useful Result / Pattern
Every one of the 20 questions has a `useful_results` slide.

## make_ppt.py warnings
- None. 827 equations converted to native PowerPoint equations; no "could not convert" notes. 123 slides.

## Skipped / assumed / guessed
- Concepts and levels are self-assigned (nearest anchors cited per question in the ratings file).
- Slides were not rendered or checked visually (no soffice rendering in this environment); the PDF was read from page images (text layer is garbled).
- Marks assumed 4 per question (not printed in the paper).
- Q12 option (4): its k-component was read as +(1/2+2sqrt2/3); either way the second root does not match it, so the key (3) is unique.
