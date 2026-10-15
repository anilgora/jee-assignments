# Run report - SHEET_SEQUENCE_&_PROGRESSION_FCopy_C2

Paper: Exercise C-II (Sequence & Progression), 35 questions, 128 marks (assumed). Deck: 226 slides.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.83** (no equivalence-relation or multi-correct adjustment applied; none applies).
- Questions per level: L1 = 2, L2 = 9, L3 = 19, L4 = 5, L5 = 0. Ratings are my own application of the calibrated rubric (only one close Sequence & Progression anchor exists, so most comparisons are cross-chapter).

## Blueprint / concepts / marks
- No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
- Marks assumed (none printed in the paper; JEE Advanced defaults): Numerical and Subjective questions 4 marks (Q1-23), Paragraph single-correct 3 marks (Q24-33), Matching 3 marks (Q34-35). Stated in the section dividers.
- Types: Q1-5, 7, 11, 12, 16, 19, 20, 22 numerical (answers such as 200 or 11/15 are not 0-9 integers); Q6, 8-10, 13-15, 17, 18, 21, 23 subjective (prove / find); paragraphs Q24-25, Q26-28, Q29-30, Q31-33; matching Q34-35.

## Solutions with solution_source "corrected" (6)
- Q3: PDF treats $1000x^6-1=0$ (i.e. $x^6=1/1000$) as giving roots. For real $x$ that means $10x^2=1$, excluded when the G.P. was summed (such $x$ give $3x\ne0$). Real roots come only from $20x^2+x-2=0$. Answer 200 unchanged.
- Q6: PDF compares with $27x^3-27x^2+9x-1$ without the scale factor; given cubic is $a=27k,\ b=k$, least $a+b=28$ at $k=1$. Added. Answer unchanged.
- Q17: PDF's discriminant condition is written wrongly ($y^2+3y-1\ge0$; correct is $(3-y)(3y-1)\ge0$) and its conclusion has closed ends $[1/3,1)\cup(1,3]$, contradicting the statement. Ends $y=1/3,3$ correspond to $r=\mp1$ (non-distinct numbers) and are excluded.
- Q20: PDF takes $S_1=1/0!=1$ and gives the $k=2$ term the value 0 ($4-6+2$); correct $S_1=0$ (first term 0, ratio 1) and the $k=2$ term is $|-1|\cdot1=1$. The two slips cancel; answer 3 unchanged.
- Q21: PDF applies A.M.-G.M. to three terms with exponent 1/2; it must be 1/3. Product of terms is $(a^ab^bc^c)^2=1$ so the conclusion is unchanged.
- Q34: PDF gets last term of 1000th group as 500501 (is 500500, option S) and middle of 501st group as $125251+249=125500$ (is $125251+250=125501$).

## Solutions with solution_source "written" (0)
None; the PDF had a working for every question.

## Answer key problems
- Q34 (B): exact middle number of the 501st group is **125501**, which is not in Column II; the key's B-P (125500) is only the nearest listed value (same slip as in the PDF working). The deck says so in the answer line.
- All other answers were re-derived and checked numerically (series sums, roots, Q9, Q12, Q16, Q20, Q34 with exact fractions / sympy). Q20 key 3 is right.

## Alternate solutions
Alternates (different technique or viewpoint, verified) for 29 of 35 questions: Q1-12, 14-19, 21-24, 26, 27, 29, 31, 33, 34, 35.
Questions with NO alternate (6):
- Q13: only route is the G.P. sum $y=2\log_2x$ and the two A.P. sums; other bookkeeping (sum over $k$) is the same step.
- Q20: only route is $S_k$ closed form, modulus by sign, telescoping with factorials.
- Q25: single step ($A^2=1/(\alpha-\beta)^2$) after Q24.
- Q28: direct A.M.-G.M.; other proofs are proofs of A.M.-G.M. itself.
- Q30: one substitution $a_{21}=41a_1$.
- Q32: factorisation of $3r^2+2r-1$ is the only route.
Borderline alternates (different viewpoint, similar arithmetic): Q4 (forward/backward sum), Q11 (block-scaling view), Q26 and Q27 (calculus / Lagrange instead of A.M.-G.M.), Q31 (elimination with $n=1,2$), Q34 (triangular numbers), Q35 (block-sum A.P. and H.M. view).

## Useful Result / Pattern
All 35 questions have useful_results (2-4 bullets each).

## make_ppt.py warnings
- "Q30: only 3 solution bullets" - the PDF's working is two lines; split into 4 bullets and rebuilt. No warnings remain.
- No "could not convert" warnings; 1276 equations converted to native equations.

## Skipped / assumed / guessed
- Concepts, marks and question types (Numerical vs Subjective) are assumed as above.
- Column I/II of the matching questions are in the question text (no separate options), as in earlier decks.
- No recalc.py, thumbnails or rendering; the deck was not opened in PowerPoint here. The xlsx has live formulas without cached values.
- The Q35 key (A-Q, B-S, C-R, D-Q) was checked and is correct.
