# RUN REPORT - JEE_Main_Question_Bank_01_Differential_Calculus_03

Paper: 20 questions (printed Q41-Q60, numbered 1-20 in the deck). Content is Functions (the page header says "Differential Calculus").

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks: none printed in the paper, so JEE Advanced defaults were used: 4 marks for every question (Single Correct Q1-Q19, Numerical Q20). This is stated in the section dividers.

## Difficulty
- Marks-weighted difficulty index (adjusted): **1.60** (all questions 4 marks).
- Levels: 1 : 8 questions (Q2, Q6, Q7, Q10, Q11, Q12, Q14, Q20); 2 : 12 questions (Q1, Q3, Q4, Q5, Q8, Q9, Q13, Q15, Q16, Q17, Q18, Q19). No level 3-5.
- No equivalence-relation or multi-correct questions, so neither adjustment applies.
- Medium-confidence ratings: Q4, Q5, Q8, Q13, Q15, Q16, Q17, Q19. No low-confidence ratings.

## Solutions that are `corrected` or `written`
- Q5 (printed 45) - **written**: the PDF has only a rough sketch and "2 Solutions"; a full case-wise solution (roots x = -2 and x = 0) was written and checked numerically.
- Q8 (printed 48) - corrected: the PDF states f(x) = 1 - x^2 with no derivation. Added the proof (f-1)(f(1/x)-1)=1, so f = 1 +/- x^2, and the codomain picks the minus sign. Answer 6 unchanged.
- Q13 (printed 53) - corrected: the PDF's condition (1) reads -3 <= g(x) < 0; f's first branch needs -1 <= g(x) < 0. Conclusion and answer unchanged.
- Small additions inside `pdf` solutions (not errors): Q1 gets the algebra 8y^2 = 119 showing the circle and ellipse meet at 4 points (the PDF only has a figure); Q3 gets the intermediate 2 sin6x cos6x; Q16 shows the sum value; Q19 adds the check that the other terms stay in [-8, 8].

## Answer key problems
None found. All 20 keys agree with my checks (brute force for Q1, Q2, Q9, Q10, Q19, Q18; numerical sums for Q4 and Q7; numerical checks for Q3, Q5, Q17).

## Paper misprint
- Q16 (printed 56): option (B) reads "B subset C, A != B" but no set C exists in the question (probably B subset A). Printed as given; the answer (A) is not affected.

## Alternates and results
- Alternate solutions given for 16 of 20 questions.
- No alternate for: Q10 (the only count is the 4 ordered pairs then 5P3; any other route is the same count reworded), Q12 (the two counter-examples are the whole argument), Q19 (the condition is a recurrence fixing everything from f(1); no different route exists), Q20 (choose the one input in 1..98, times 4; a generating-function version would be padding).
- Useful Result / Pattern given for all 20 questions.
- Modest alternates (valid and verified but weaker, a different route rather than a deep new idea): Q3 (product-to-sum instead of triple-angle), Q4 and Q7 (reverse-sum / odd-about-centre viewpoint), Q13 (range of g first, then f), Q16 (decimal 0.333... plus log base 3).

## make_ppt.py output
- "Equations: 711 converted to native PowerPoint equations." No "could not convert" warnings.
- Note for Q20: only 3 solution bullets, because the PDF's complete working is three steps. Harmless; left as is.

## Skipped / assumed / guessed
- The deck was not rendered (no soffice step per the run rules); slide fit was not checked visually.
- Levels are my own ratings from the calibrated rubric; the paper is JEE Main level, so everything is level 1-2 on the Advanced scale.
- Chapter name "Function" used in the ratings file; the paper's header says Differential Calculus.
