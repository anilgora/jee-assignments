# Run report - JEE_Main_Question_Bank_02_Integral_Calculus_04

Paper: `papers/JEE_Main_Question_Bank_02_Integral_Calculus_04.pdf` (19 pages, Matrix JEE Academy; 20 single-correct questions with printed solutions, English + Hindi). Printed numbers are 61-80; deck numbers are 1-20 (deck Qn = printed Q(n+60)).
Files: `_Analysis.pptx` (127 slides), `_content.json`, `_ratings.json`, `_difficulty.xlsx`, this report.

## Blueprint and marks
- **Concepts self-assigned (no blueprint) - please review.** No blueprint was used.
- No marks printed. Assumed **4 marks per Single Correct question**, no negative marking (stated in the section divider). Total 80 marks.

## Difficulty
- **Marks-weighted difficulty index: 2.25** (equal marks; no equivalence-relation or multi-correct adjustments apply).
- Level 1: 1 (Q7); Level 2: 13 (Q1, Q3, Q4, Q6, Q9, Q10, Q11, Q12, Q14, Q15, Q16, Q17, Q18); Level 3: 6 (Q2, Q5, Q8, Q13, Q19, Q20); Levels 0, 4, 5: none.

## Solutions whose source is corrected
- Q8 (printed 68): PDF has a sign error (dP/dx - Px = +e^{x^2/2}; correct is -e^{x^2/2}) and uses I.F. e^{x^2/2} (correct e^{-x^2/2}); later lines are inconsistent. Working redone; the final value and key (C) are right.
- Q9 (printed 69): PDF differentiates both sides (and writes 4f(x) instead of 4f(x)^3) and concludes lim g = g(2), which assumes g differentiable at 2 (not given). Replaced by the limit definition of (f^4)'(2); answer 18 unchanged.
- Q10 (printed 70): PDF writes area of A = pi*4/2 - 1 (= 2pi-1) but states pi-1; the quarter disc is pi*4/4. Fixed; line-circle intersection step added.
- Q15 (printed 75): PDF typos f = 2x^3 - 19x^2 + ... and f' = 6(x-1)(x+2); correct factor is (x-2). Conclusion unchanged.
- Q16 (printed 76): PDF has tan(x-alpha) in the denominator of step 2 (should be sin); and option (B) is equally valid (see answer key note).
- Kept as `pdf`: Q2 (algebra from equation (1) to a^6-12a^3+4=0 was skipped in the PDF; written out), Q4 (the region is taken in x>0, see below), Q5 (the PDF's move of sin(theta) inside the root holds for sin(theta)>0; stated), Q7 (stray (1-x)^{3/2} typo in the PDF's first line, not copied), Q3, Q17 and Q20 (extra concluding steps added: elimination factorisation, and the final lambda*f(pi/3) step that the PDF omits).

## Solutions whose source is written
- None.

## Answer key
- All 20 keys verified numerically (mpmath/quadrature, differentiation of the closed forms, ODE solutions checked in the equation). All keys are correct as the printed answer, except the notes below.
- **Q16 (printed 76):** key (C) is the direct result, but option (B) (A = x+alpha, B = ln|sin(x-alpha)|) differs from (C) only by the constant 2*alpha*cos(2*alpha), which is absorbed in C, so (B) is equally a correct antiderivative. The deck keeps (C) and says so.
- **Q4 (printed 64):** read literally, for x<0 the condition xy<=8 holds automatically with 1<=y<=x^2, so the region is unbounded. The key (B) corresponds to x>0 (first quadrant), which is the intended region; the solution states this assumption.
- Q5 (printed 65): the antiderivative (1/18)T^{3/2} is valid where sin(theta)>0 (for sin(theta)<0 the sign flips); the key (C) is the intended answer.

## Alternates
- Given for 18 of 20 questions (all except Q12, Q17).
- **No alternate:** Q12 (printed 72): the only route is splitting at 0 and solving the quadratic in e^{-alpha}; reading it as exponential-distribution probabilities gives the same equation reworded. Q17 (printed 77): a linear DE; the only real choice is how to find the I.F. (substitution vs partial fractions), which is the same method.
- Weaker alternates (flagging for review): Q13 (shorter factorisation of the same split), Q16 (a different splitting of the same identity), Q18 (x = tan(theta) is the same linearisation in a new variable), Q3 (guess-and-verify with a uniqueness argument), Q5 (derivative test of the options - an exam technique rather than a derivation).
- Useful results: all 20 questions have `useful_results`.

## make_ppt.py warnings
- None. 920 equations converted to native PowerPoint equations; no "could not convert" notes.
- `build_report.py` ran without warnings.

## Skipped / assumed
- No rendering or thumbnails (no soffice); the deck was not visually inspected. Hindi text not transcribed.
- Concepts and levels are my own judgement (Medium confidence; the rubric's anchors are Advanced-level, so for this Main-level bank I placed questions relative to the lowest anchors).
- Numbering: deck numbers 1-20 differ from printed 61-80; the question text itself does not show printed numbers.
