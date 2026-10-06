# RUN REPORT - JEE_Main_Question_Bank_01_Integral_Calculus_03

Paper: 20 questions (printed Q41-Q60, numbered 1-20 in the deck), all Definite Integration, all single correct.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks: none printed, so the run rules' defaults were used: 4 marks for every Single Correct question (Q1-Q20). Stated in the section divider.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.50** (all questions 4 marks).
- Level 2: 10 (Q1, Q2, Q4, Q5, Q6, Q7, Q11, Q13, Q14, Q15). Level 3: 10 (Q3, Q8, Q9, Q10, Q12, Q16, Q17, Q18, Q19, Q20). Levels 0, 1, 4, 5: none.
- No equivalence-relation questions and no multi-concept one-or-more-correct questions, so no adjustment or floor applies.
- Confidences are mostly Medium (nearest anchors are approximate); Q6 is Low (no close anchor for the inverse-trig simplification).

## Solutions that are `corrected` or `written` (no `written`)
- Q3 (PDF Q43): the by-parts line shows the inner integral with a minus sign in front of $\frac1{21k}\int(1-x^k)^{21}dx$ (should be plus; the minus belongs to $I_{21}=I_{20}-\ldots$), and the PDF jumps to $k=7$ without using $147I_{20}=148I_{21}$. Written out; result unchanged.
- Q6 (PDF Q46): the PDF takes the integrand as $\cos2\theta$ (it is $\cos(\pi-2\theta)=-\cos2\theta$) and writes $-2\cos2\theta\sin2\theta=+\sin4\theta$ (it is $-\sin4\theta$). The two sign slips cancel; answer $-\frac14$ right.
- Q12 (PDF Q52): partial-fraction numerator printed as $(x^2-1)-(x^2+\frac13)$; must be $(x^2+1)-(x^2+\frac13)=\frac23$. Answer right.
- Q13 (PDF Q53): the denominator after the second L'Hopital step drops a factor 2 ($2e^{x^2}+4x^2e^{x^2}$, not $e^{x^2}+2x^2e^{x^2}$); as printed the first limit would be $\frac12$ and the total $\frac34$, not the $\frac12$ it states. Answer 2 right.
- Q19 (PDF Q59): $g'(x)$ is printed as $x^{-x^2}(2x)$ (should be $x e^{-x^2}\cdot2x$) and the last line shows $-e^{(\log_e9)^{-1}+1}$ instead of $1-e^{-\log_e9}$. Notation slips; answer 8 right.
- Q20 (PDF Q60): limits of $t=2x-1$ given as $\pm\frac12$; they are $\pm1$. Value 0 unaffected.
- All other solutions are as printed (`pdf`), with small additions where the PDF is terse (Q8: check that $I_2\ne0$; Q9 and Q12: final steps spelled out; Q15 and Q10: intermediate evaluations).

## Answer key problems
None. All 20 keys agree with my checks: every integral and limit was recomputed numerically with mpmath (Q45 and Q51 as limits at $x=\frac\pi2+10^{-4}$ and via the exact formulas), and Q43, Q54, Q56, Q57, Q58 were also checked by exact arithmetic/hand.

## Alternates and results
- Alternate solutions given for **16 of 20 questions** (one each): Q2-Q9, Q11-Q13, Q15, Q17-Q20 (numbered as in the deck). All were checked numerically or symbolically.
- Questions with NO alternate:
  - Q1: the only route is the substitution $x^{10}=t$ to the Beta integral; the Gamma-function formula is the same substitution in general form.
  - Q10: the only route is pairing $x$ with $-x$ in each term and integrating by parts; no different technique exists.
  - Q14: the three linear equations in $a,b,c$ can only be solved by elimination; no genuinely different method.
  - Q16: recognising $\left(\frac{f'^3}3+f'\right)'$ is the same idea as the substitution $z=f'$.
- Modest alternates (valid but close in spirit to the main route): Q15 (geometric reading of the pieces), Q19 (combine integrands instead of differentiating), Q11 and Q13 (asymptotic linearisation instead of L'Hopital).
- Useful Result / Pattern given for **all 20 questions**.

## make_ppt.py output
- "Equations: 808 converted to native PowerPoint equations." 117 slides, 20 questions. No warnings and no "could not convert" notes.

## Skipped / assumed / guessed
- The deck was not rendered (no soffice step per run rules); slide fit was not checked visually.
- Levels, concept names and chapter names are my own, from the calibrated rubric; nearest anchors are approximate.
- The PDF text layer is garbled for maths; every page was read from images.
- Q6: the simplification $2\cot^{-1}\tan\theta=\pi-2\theta$ is valid for $\theta\in(0,\frac\pi2)$, which covers $x\in(-1,1)$.
