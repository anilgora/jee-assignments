# RUN REPORT - JEE_Main_Question_Bank_01_Integral_Calculus_01

Paper: 20 questions (printed Q1-Q20, numbered 1-20 in the deck), all Indefinite Integration. Q1-Q14 single correct, Q15-Q20 numerical.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks: none printed, so JEE Advanced defaults were used: 4 marks for Single Correct (Q1-14) and 4 for Numerical (Q15-20). Stated in the section dividers. The "Numerical Type" label is used for Q15-Q20 (not marked as 0-9 integer type in the paper).

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.40** (all questions 4 marks).
- Level 1: 2 (Q1, Q4). Level 2: 10 (Q2, Q3, Q5, Q6, Q7, Q8, Q9, Q13, Q17, Q19). Level 3: 6 (Q10, Q11, Q12, Q14, Q16, Q18). Level 4: 2 (Q15, Q20). Levels 0 and 5: none.
- No equivalence-relation questions and no multi-concept one-or-more-correct questions, so no adjustment or floor applies.
- All confidences are Medium; nearest-anchor references are approximate (few integration anchors exist for indefinite integrals).

## Solutions that are `corrected` or `written` (no `written`)
- Q8: PDF working is right (alpha=1, beta=1, gamma=3, answer 4) but its key says (D)=7 - see answer-key problems. Marked corrected because the answer differs from the key.
- Q10: notation only - PDF calls the antiderivative f and writes f'(pi/2)=0, f'(pi/4); should be y and the limit condition. Working and answer (B) right.
- Q11: PDF writes I1 = (2/cos theta) sqrt(tan x cot theta - sin theta); radicand must be tan x cos theta - sin theta. Rest and answer (D) right.
- Q12: PDF's evaluation line has numerator -pi instead of -x^2 = -pi^2/16 (value -pi^2/(4(pi+4))); the by-parts step (x^2 w'/w^2) was written out. Answer (B) right.
- Q18: PDF's second line counts "-3I" twice (-3I - 3 int cosec^3(cosec^2-1)); extra -3I removed. The next lines and answer 1 are right.
- All other solutions are as printed (`pdf`), with short justifications added where terse: Q3 (why exponents summing to 2 allow the substitution), Q15 (algebra of the last step), Q17 (derivative of the log term), Q20 (f(0) used as the limit x->0+ since the formula holds for x>0).

## Answer key problems
- Q8: working gives alpha + gamma/beta = 4. The printed options are (A)3 (B)1 (C)7 (D)7 - none equals 4 - and the key says D. Answer kept as 4 and flagged in the deck. Likely the options were mis-typed (original probably had 4 in place of one 7).
- All other 19 keys agree with my checks (antiderivatives differentiated numerically with mpmath for every question; final values recomputed).

## Alternates and results
- Alternate solutions given for **13 of 20 questions** (one each): Q1, Q4, Q5, Q6, Q7, Q8, Q10, Q13, Q15, Q17, Q18, Q19, Q20. All verified numerically.
- Questions with NO alternate:
  - Q2: the bracket is e^x(f+f') in its only natural form; sub x = sin(theta) does not give an e^x(f+f') pattern, and differentiating the guess is just the same check.
  - Q3: the only workable move is t=(x-11)/(x+15) (exponents sum to 2); other substitutions are the same Mobius map.
  - Q9: t = tan^-1(x^3+x^-3) is forced; any other route (w = x^3+x^-3 first) is the same chain.
  - Q11: splitting into sec^{3/2} and cosec^{3/2} parts and the two radical substitutions are the only route.
  - Q12: integrating x^2 w'/w^2 by parts is the single idea; other routes are rewordings.
  - Q14: t=(x/e)^{2x} (or recognising d/dx (x/e)^{2x}) is one idea in two wordings.
  - Q16: t = 3/x + 1/x^3 is the only clean substitution.
- Modest alternates (valid and verified but close in spirit to the main route): Q1 and Q5 (definite integral instead of fixing C), Q18 (standard reduction formula instead of deriving it), Q15 (sinh substitution vs. sec+tan).
- Useful Result / Pattern given for **all 20 questions**.

## make_ppt.py output
- "Equations: 827 converted to native PowerPoint equations." 121 slides, 20 questions. No warnings and no "could not convert" notes.

## Skipped / assumed / guessed
- The deck was not rendered (no soffice step per the run rules); slide fit was not checked visually.
- Levels are my ratings from the calibrated rubric; nearest anchors are approximate. Chapter names are self-assigned.
- The PDF text layer was garbled for maths; every page was read from images. Q5's question stem (exponent 1/4 in the denominator) was confirmed from a zoomed image.
- Q6: signs of a, b are not determined by the question; the maximum sqrt(a^2+b^2) does not depend on them.
- Options for Q8 are reproduced as printed (C and D both 7).
