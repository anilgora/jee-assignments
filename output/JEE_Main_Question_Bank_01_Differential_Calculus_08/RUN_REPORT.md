# RUN REPORT - JEE_Main_Question_Bank_01_Differential_Calculus_08

Paper: 20 questions (printed Q141-Q160, numbered 1-20 in the deck). Q1-Q3 methods of differentiation / continuity, Q4-Q6 blank-fill (limit, higher derivatives, simplification), Q7-Q10 tangent and normal, Q11-Q12 blank-fill (distance/extremum, circle in ellipse), Q13-Q20 monotonicity and critical points.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks: none printed, so JEE Advanced defaults were used: 4 marks for every question (Single Correct Q1-3, Q7-10, Q13-20; Numerical Q4-6, Q11-12). Stated in the section dividers. The "Numerical Type" label is used for all blank-fill questions (Q4, Q5, Q6, Q11, Q12) because the paper does not mark them as 0-9 integer type.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.20** (all questions 4 marks).
- Level 1: 2 questions (Q17, Q20). Level 2: 12 (Q1, Q2, Q3, Q4, Q5, Q6, Q8, Q10, Q13, Q14, Q16, Q18). Level 3: 6 (Q7, Q9, Q11, Q12, Q15, Q19). No level 0, 4 or 5.
- No equivalence-relation questions and no multi-concept one-or-more-correct questions, so no adjustment or floor applies.
- Medium/Low-confidence ratings: Q1-Q4, Q7, Q11, Q12, Q15, Q19 (Medium); Q9 (Low - the intended circle is debatable, see below). Nearest-anchor references in the workbook are approximate; the paper is JEE Main level.

## Solutions that are `corrected` or `written` (no `written`)
- Q8 (printed 148) - corrected: PDF writes dV/dt = -81 but multiplies by +1/(4 pi), dropping the minus of d(alpha)/dt. Signs restored: dV/dt = -(r+1)^2 = -81. Answer (D) 256 pi unchanged.
- Q9 (printed 149) - corrected (caution added): PDF takes the circle touching the parabola at its vertex (centre (0,4), r=2) without justification; that circle also crosses the parabola at (+-sqrt3, 3). Added a bullet saying so. Answer (D) kept (see answer-key section).
- Q10 (printed 150) - corrected: PDF's last line "(D) normals" contradicts its own four roots and the key (C); should read "4 normals". Answer (C) unchanged.
- Q15 (printed 155) - corrected: PDF writes "100(a+b+c) = 10(4+8/5-2)"; should be 100(a+b-c) = 100(4+8/5-2) = 360. Also made explicit that f'(3)=0 (not just >= 0) is needed for (2,3) to be the largest interval. Answer (C) unchanged.
- Q19 (printed 159) - corrected: PDF says "Let x = pi/12" before using cos 3x (should be the angle theta; the root is x = cos(pi/12)), and says f' > 0 on [1/2,1] though f'(1/2)=0 (positive for x>1/2, still strictly increasing). Answer (B) unchanged.
- All other solutions were reproduced as printed (`pdf`), with a few justification phrases added (Q1 each determinant spelt out, Q11 why the maximum is at the end (2,0) of the semicircle, Q18 why f is strictly decreasing). Small notational slips (Q3 "= f''(x)" for "f''(x) =", Q16 "F(x)", Q4 "2.2") were written correctly.

## Answer key problems
- **Q9 (printed 149):** key (D) (2,4) corresponds to the circle x^2+(y-4)^2=4 touching the parabola y=6-x^2 at its vertex and the lines at (+-sqrt3,3). Strictly, the circle of MINIMUM area tangent to the lines and to the parabola from inside has centre (0, 3sqrt3-2) and radius (3sqrt3-2)/2 (about 1.598 < 2); none of the four options lies on it (checked numerically). So the question as worded is flawed; (D) is the only answer consistent with the options and is kept. Please review.
- All other 19 keys agree with my checks (sympy / numerical scan for Q1-Q6, Q10-Q12, Q19; by hand for the rest).

## Alternates and results
- Alternate solutions given for **18 of 20 questions** (one each): Q1-Q4, Q7-Q20.
- Questions with NO alternate:
  - Q5 (printed 145): the only route is to differentiate to the constant third derivative and solve the linear system for f'(1), f''(2), f'''(3); any variant (elimination order, matrices) is the same method.
  - Q6 (printed 146): the only route is to factor the cube difference to get y = (x-1) + ..., then differentiate; substituting c = cos x for the trig part is the same chain-rule step, not a different method.
- Modest alternates (valid and verified, but close in spirit to the main route): Q2 (numerical sign/size elimination of options), Q8 (shell principle dV = area x thickness, the same calculus in shorter form), Q4 (log form of the same expansion), Q16 (same two facts in the reverse order).
- Useful Result / Pattern given for **all 20 questions**.

## make_ppt.py output
- "Equations: 703 converted to native PowerPoint equations." 128 slides. No warnings and no "could not convert" in the final build. (An earlier build showed three "could not convert" notes caused by a stray line break I had introduced into the Q14 question text through "\ne"; fixed at the source.)

## Skipped / assumed / guessed
- The deck was not rendered (no soffice step per the run rules); slide fit was not checked visually.
- Levels are my own ratings from the calibrated rubric; the paper is JEE Main level, so everything is at 1-3.
- Chapter names in the ratings are self-assigned (e.g. "Tangent & Normal", "Rate of Change", "Monotonicity").
- The PDF text layer was garbled for maths, so all pages were read from page images at 80 dpi; answers were then recomputed with sympy/numerics.
