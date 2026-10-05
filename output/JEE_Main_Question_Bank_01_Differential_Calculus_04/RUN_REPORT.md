# RUN REPORT - JEE_Main_Question_Bank_01_Differential_Calculus_04

Paper: 20 questions (printed Q61-Q80, numbered 1-20 in the deck). Q1-10 Functions (Numerical), Q11-20 Inverse Trigonometric Functions (Single Correct).

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks: none printed, so JEE Advanced defaults were used: 4 marks for every question (Numerical Q1-10, Single Correct Q11-20). Stated in the section dividers.

## Difficulty
- Marks-weighted difficulty index (adjusted): **1.75** (all questions 4 marks).
- Level 1: 7 questions (Q3, Q4, Q5, Q11, Q15, Q18, Q20). Level 2: 11 (Q1, Q2, Q6, Q8, Q9, Q10, Q12, Q13, Q14, Q16, Q19). Level 3: 2 (Q7, Q17). No level 0, 4 or 5.
- No equivalence-relation or multi-correct questions, so neither adjustment applies.
- Medium-confidence ratings: Q2, Q7, Q10, Q13, Q16, Q17, Q19.

## Solutions that are `corrected` or `written`
- Q2 (printed 62) - corrected: PDF wrote 1/3 >= [a] >= -3/5; correct bounds are -3/5 < [a] <= 1/5. Conclusion and answer 18 unchanged.
- Q7 (printed 67) - corrected: PDF's "no root in [5,6] since LHS=1 at x=5,6" is not a proof and ignores x<5. Replaced with (x-6)^2>0 on [5,6) and LHS>(x-5)(x-6)>0 for x<5. Answer 9 unchanged.
- Q10 (printed 70) - corrected: PDF jumps from the closed form of f to "2f(2)+f'(2)=119.2^10+1" with no derivative or evaluation; added f(2)=18434, f'(2)=84989 and the check 121857=119*1024+1. Answer 10 unchanged.
- Q16 (printed 76) - corrected: typo in first simplified term (denominator alpha+beta, should be alpha-beta). Answer pi unchanged.
- Q17 (printed 77) - corrected: PDF wrote cos^-1(...)=pi/2+alpha, valid only if pi/2+alpha<=pi; replaced by taking cosines of both sides. Also added the check that alpha=pi/2 (y=-x) is attainable. Answer 0 unchanged.
- Small additions inside `pdf` solutions (not errors): Q1 shows the 4th composition; Q3 gives the induction for f(n)=n and the final floor 1010 (PDF stops at 1010.5); Q4 and Q5 spell out reasoning.

## Answer key problems
None. All 20 keys agree with my checks (brute force for Q2, Q6, Q8, Q9, exact sums for Q10, numerical checks for Q1, Q7, Q13, Q14, Q16, Q17, Q20).

## Alternates and results
- Alternate solutions given for 18 of 20 questions.
- No alternate for: Q4 (list/parametrise four solutions then 4!; any other route is the same count reworded), Q20 (reduction of 5 rad into the two principal ranges is the only route; "a=-b" is the same reduction).
- Useful Result / Pattern given for all 20 questions.
- Modest alternates (valid, verified, but weaker - special-value tests that rely on the options being single-correct): Q11, Q15, Q16, Q19; Q3 (AP average) is also modest.

## make_ppt.py output
- "Equations: 878 converted to native PowerPoint equations." 123 slides. No warnings, no "could not convert".

## Skipped / assumed / guessed
- The deck was not rendered (no soffice step per the run rules); slide fit was not checked visually.
- Levels are my own ratings from the calibrated rubric; the paper is JEE Main level, so everything sits at level 1-3.
- The paper's header says "Differential Calculus"; chapter names "Function" and "Inverse Trigonometric Functions" used in the ratings.
- Q19 alternate (equilateral triple) relies on the question having a single correct option; flagged as a check, not a proof.
