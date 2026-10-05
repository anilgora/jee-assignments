# RUN REPORT - JEE_Main_Question_Bank_01_Differential_Calculus_05

Paper: 20 questions (printed Q81-Q100, numbered 1-20 in the deck). Q1-9 Inverse Trigonometric Functions (Q6-9 integer answers), Q10-20 Limits (Q16 functional equation, Q17 determinant limit, Q19 circle, all via limits).

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks: none printed, so JEE Advanced defaults were used: 4 marks for every question (Single Correct Q1-2, 4-5, 10-20; One-or-more-correct Q3; Integer Q6-9). Stated in the section dividers.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.15** (all questions 4 marks).
- Level 1: 2 questions (Q8, Q17). Level 2: 13 (Q1, Q3, Q6, Q9, Q10, Q11, Q12, Q13, Q15, Q16, Q18, Q19, Q20). Level 3: 5 (Q2, Q4, Q5, Q7, Q14). No level 0, 4 or 5.
- No equivalence-relation questions; Q3 is one-or-more-correct but single-concept, so no 2.5 floor applies.
- Medium-confidence ratings: Q2, Q3, Q4, Q5, Q7, Q9, Q13, Q14, Q15.

## Solutions that are `corrected` or `written` (no `written`)
- Q3 (printed 83) - corrected: PDF labels the results "Option 3"/"Option 1" (original exam numbering); here they are (A) and (B). Added a bullet showing (C), (D) are wrong. Answer (A, B) unchanged.
- Q5 (printed 85) - corrected: the PDF's working (S empty, sum 0) is right but its answer key says C (-2pi/3). Correct answer is **(A) 0**.
- Q7 (printed 87) - corrected: no wrong value; PDF jumps from the sine equation to x^3-2x-1=0 and rejects roots with just "false". Added the domain [-1,0], the squaring step and the reasons for rejecting x=-1 and (1+sqrt5)/2. Answer 5 unchanged.
- Q10 (printed 90) - corrected: PDF solves -3a/4=3 as a=4 (should be a=-4) then writes beta+gamma-alpha=7 (inconsistent with a=4); also "x->10" typo. Answer 7 (A) unchanged.
- Q11 (printed 91) - corrected: typo b=-3/4 (should be 3/4, as the PDF's own b=1+a gives). Answer 1/2 unchanged.
- Q18 (printed 98) - corrected: PDF's general numerator term (r-1)(r-2)(n-r) does not match the given terms (r^2-r)(n-r); the denominator's minus sign was lost. Leading coefficient 1/12 and answer 1/3 unchanged.
- Q19 (printed 99) - corrected: typos "2c^2y" (should be 5c^2y) in the second line and "3c+12" (should be 3c+2) in the limit for k. Answer (C) unchanged.
- Other solutions were reproduced as printed (`pdf`); Q2, Q4 etc. have only added justification phrases.

## Answer key problems
- **Q5 (printed 85): the key says C but the correct answer is (A) 0.** The equation has no solution in [-1/2, 1/2] (|LHS - pi| >= pi/3 on the whole interval, checked numerically), so S is empty and the sum is 0 - which is also what the PDF's own working concludes.
- All other 19 keys agree with my checks (numerical / symbolic with sympy for Q1-2, 7, 10-13, 15, 17-20; direct for others).

## Alternates and results
- Alternate solutions given for **all 20 questions** (one each).
- No question without an alternate.
- Modest alternates (valid and verified but close in spirit to the main route): Q1 (factor common surd), Q8 (range view of the same identity), Q10 (third-derivative matching), Q13 (substitution x=t^6 then equivalents), Q20 (series of (1+t)^(1/t)).
- Useful Result / Pattern given for all 20 questions.

## make_ppt.py output
- "Equations: 835 converted to native PowerPoint equations." 133 slides. No warnings and no "could not convert".

## Skipped / assumed / guessed
- The deck was not rendered (no soffice step per the run rules); slide fit was not checked visually.
- Levels are my own ratings from the calibrated rubric; the paper is JEE Main level, so everything sits at level 1-3. Nearest-anchor references in the ratings workbook are approximate.
- Integer type (0 to 9) label chosen for Q6-9 because their answers 3, 5, 0, 4 fit; the paper itself prints no type.
- Chapter names in the ratings: "Inverse Trigonometric Functions", "Limits", "Functions", "Matrices and Determinants", "Straight Lines and Circles" (self-assigned).
- The "correct reading" of the typos in Q19 was checked against a zoomed page image.
