# RUN REPORT - JEE_Main_Question_Bank_01_Integral_Calculus_04

Paper: 20 questions (printed Q61-Q80, numbered 1-20 in the deck), all Definite Integration; Q1-Q5 single correct, Q6-Q20 numerical value.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks: none printed, so JEE Advanced defaults were used: 4 marks for every Single Correct and Numerical question (Q1-Q20). Stated in the section dividers.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.35** (all questions 4 marks).
- Level 1: 2 (Q1, Q3). Level 2: 10 (Q2, Q4, Q5, Q6, Q9, Q10, Q16, Q17, Q18, Q19). Level 3: 7 (Q7, Q8, Q11, Q12, Q13, Q14, Q20). Level 4: 1 (Q15). Levels 0 and 5: none.
- No equivalence-relation questions and no multi-concept one-or-more-correct questions, so no adjustment or floor applies.
- Confidence is Medium except Q7 and Q13 (Low: no close anchor for the hidden-pattern ODE and recurrence ideas).

## Solutions that are `corrected` or `written` (no `written`)
- Q1 (PDF Q61): last line reads $\frac\pi2+\frac{7\sqrt3}{64}$ (should be $\frac\pi8+\ldots$); one line is printed twice. $a=\frac18$ and the answer are right.
- Q4 (PDF Q64): value at $t=2$ printed as $2\ln\sqrt5+2-\sqrt5$; correct is $2\ln(2+\sqrt5)-\sqrt5$. Final expression right.
- Q6 (PDF Q66): first piece written $(1-\ln2-0)$, dropping the factor 2 of $\int2dx$ (sum would be 1, not $2-\ln2$). Answer 8 right.
- Q7 (PDF Q67): $f(x)=x^{3/4}$ printed; it is $x^{-3/4}$ (later lines use the right one). Answer 112 right.
- Q8 (PDF Q68): the factor $e^{-1}$ is lost in the last lines. $\alpha=64$ right.
- Q12 (PDF Q72): constants in the $\lambda=\cos t\tan x$ substitution wrong ($\lambda^2+\cos^2t$ should be $\lambda^2+\cot^2t$, factor $\tan t$ not $\frac1{\cos t}$); redone with $u=\tan x$. Answer right.
- Q15 (PDF Q75): $\frac1{\sqrt2}(\frac\pi2-\frac\pi4)$ is written as $\frac\pi{\sqrt2}$; it is $\frac\pi{4\sqrt2}$. Also the question prints the second term's numerator as 8; the general term gives $8n$ (used). Answer 32 right.
- All other solutions are as printed (`pdf`), with small additions where the PDF is terse (Q3 chain-rule factor $2t$, Q17 check that the denominator vanishes at $x=3$, Q5 explicit reasoning for $\min$ and $[x-\ln x]$). Q14: the PDF's page layout is garbled; it is read as two separate sums for $[x^2]$ and $[x^2/2]$.

## Answer key problems
None. All 20 keys agree with my checks: every integral and limit was recomputed numerically with mpmath (Q8 as a limit at $t=10^{-9}$, Q15 also as a finite Riemann sum with $n=20000$), and each solution was re-derived by hand.

## Alternates and results
- Alternate solutions given for **15 of 20 questions** (one each): Q1, Q2, Q4, Q6, Q7, Q8, Q10, Q11, Q12, Q13, Q14, Q15, Q18, Q19, Q20. All checked numerically or symbolically.
- Questions with NO alternate:
  - Q3: the only route is differentiating w.r.t. $t$ (equivalently $u=t^2$); no different technique exists.
  - Q5: the answer needs the piecewise reading and two direct integrals; nothing else.
  - Q9: splitting at $\frac\pi{48}$ and $\frac\pi6$ is forced; the $u=4x-\frac\pi{12}$ shift is the same split.
  - Q16: "f odd, then pair $x$ and $-x$" is the only sensible method (using $f'$ even is only a shorter proof of oddness).
  - Q17: only L'Hopital after noticing $\frac00$; no different method.
- Modest alternates (valid but close in spirit to the main route): Q6, Q10 (second part), Q14 and Q19 (layer-cake counting instead of explicit breakpoints), Q18 (shift to $u=x-\frac\pi4$).
- Useful Result / Pattern given for **all 20 questions**.

## make_ppt.py output
- "Equations: 801 converted to native PowerPoint equations." 120 slides, 20 questions. No warnings and no "could not convert" notes.

## Skipped / assumed / guessed
- The deck was not rendered (no soffice step per run rules); slide fit was not checked visually.
- Levels, concept names and chapter names are my own, from the calibrated rubric; nearest anchors are approximate.
- The PDF text layer is garbled for maths; every page was read from images.
- Q5: the question prints $x-[x]$ (read in a 200 dpi zoom); with it $f=e^{x^2}$ on $[0,1)$ and the key (C) is right.
