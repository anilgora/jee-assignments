# Trigonometric_Equation: generation report

Blueprint: `qp_blueprints/Trigonometric_Equation.xlsx`. There is no `Trigonometric_Equation_config.xlsx`, so the check ran without `--config`.
This scheduled run made the paper on 19-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy, mpmath and python-docx were missing for `python3`. I installed them with `python3 -m pip install pandas openpyxl sympy mpmath python-docx`. (Plain `pip` installs into a different Python, so it did not help.)
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- `build_paper.py --blueprint` passed on the first build with **no errors and no warnings**. No script was edited and no check was weakened.
- I rendered page 1 of each of the three PDFs (and page 2 of the questions PDF) and looked at them. The Hindi is shaped and the equations are typeset in 2D. This paper has no paragraph question.

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the blueprint has only Single Correct and Numerical types and nothing above level 3.
- **Paper:** 18 questions (blueprint Sr No 703-720): 4 Single Correct (Q1-Q4), then 14 Numerical (Q5-Q18).
- **Reorder (`--reorder`):** the rows were not in type order, so they were renumbered (old Sr No -> new Q):
  705->1, 707->2, 718->3, 719->4, 703->5, 704->6, 706->7, 708->8, 709->9, 710->10, 711->11, 712->12, 713->13, 714->14, 715->15, 716->16, 717->17, 720->18.
- **Answer Plans:** the blueprint had none, so the script drew all 18. Every answer matches its plan, and the build checks this.
  - SCQ: Q1 C, Q2 A, Q3 B, Q4 D.
  - Numerical: Q5 positive 2-digit integer; Q6 negative decimal; Q7 negative integer; Q8 positive decimal; Q9 decimal between 0 and 1; Q10 positive 3-digit integer; Q11 negative integer; Q12 positive 2-digit integer; Q13 negative decimal; Q14 decimal between 0 and 1; Q15 positive 3-digit integer; Q16 positive decimal; Q17 positive decimal; Q18 negative decimal.
- **Cells containing ";":** rows 7, 8, 9 and 13 as numbered by the check. There is no config, so each cell was kept as **one** concept, as the run instructions say. They are "Solution by squaring; rejection of extraneous roots" and "Domain restrictions from log, root and denominator; rejecting solutions", which read as single concepts.
- **Warnings.** Recorded, not fixed; the blueprint was not edited. There were no errors.
  - Q6 and Q10 list 3 concepts, unusual for the Main pattern. Both were kept, and each question uses all three.
  - Concepts repeat across rows, as expected in a one-chapter paper: "Trigonometric inequalities" (Q3, Q4); "Principal solution vs general solution" (Q1, Q5); "General solution of sin(x) = k, ..." (Q5, Q6); "Solution by factorisation" (Q6, Q7); "Solution of a.sin(x) + b.cos(x) = c" (Q6, Q7, Q18); "Solution by substitution" (Q2, Q8); "Solution by squaring; ..." (Q9, Q10); "Domain restrictions from log, root and denominator; ..." (Q9, Q10, Q11); "Number of solutions in a given interval" (Q10, Q12); "Number of solutions by graphical intersection" (Q12, Q13); "Equations solvable only by boundedness" (Q14, Q15); "Miscellaneous trigonometric equations" (Q16, Q17); "Half-angle substitution t = tan(x/2)" (Q8, Q17). Every use has its own mechanism and no equation is reused.

## Answers
| Q | Type | Answer | Level (target) |
|---|---|---|---|
| 1 | SCQ | (C) | 2 (2) |
| 2 | SCQ | (A) | 2 (2) |
| 3 | SCQ | (B) | 2 (2) |
| 4 | SCQ | (D) | 3 (3) |
| 5 | Num | 18 | 3 (3) |
| 6 | Num | -0.96 | 3 (3) |
| 7 | Num | -7 | 2 (2) |
| 8 | Num | 1.2 | 2 (2) |
| 9 | Num | 0.25 | 3 (3) |
| 10 | Num | 150 | 3 (3) |
| 11 | Num | -2 | 3 (3) |
| 12 | Num | 12 | 2 (2) |
| 13 | Num | -2.5 | 3 (3) |
| 14 | Num | 0.75 | 2 (2) |
| 15 | Num | 125 | 3 (3) |
| 16 | Num | 1.5 | 2 (2) |
| 17 | Num | 3.8 | 3 (3) |
| 18 | Num | -0.28 | 2 (2) |

I recomputed every answer in Python with sympy/mpmath, separately from the written solutions, mostly by a fine numerical root scan of the original equation (not of the simplified form):
- Q1: the sum of principal roots for λ = -2.5, -4 and -10 (always 5π).
- Q2, Q6, Q7, Q8, Q13, Q17: all roots found numerically in the stated interval and the asked quantity evaluated from them; Q6's factorisation also checked with sympy.
- Q3, Q4: measure of the solution set by sampling 2,000,000 points (π and π/3).
- Q5, Q10, Q12, Q15: roots counted directly (18, 150, 12, 125). For Q10 a scan of one period of 3x shows the only roots of the root form are π/2 (rejected by sec) and 11π/6. For Q15 a scan of a 4π period shows the maximum 3 is reached only at π/3.
- Q9: the squared equation and each root's domain checked. Q11: every candidate tested against the domain. Q14: the minimum of LHS − RHS over a grid is 0, reached only at 0.75. Q16: sympy confirms that sin 3x/sin x + cos 3x/cos x − 4 cos 2x = 0. Q18: the tangency 3 sin x + 4 cos x ≤ 5 checked.

## Level distribution and index
- Level 2: 9 questions (Q1, Q2, Q3, Q7, Q8, Q12, Q14, Q16, Q18). Level 3: 9 questions (Q4, Q5, Q6, Q9, Q10, Q11, Q13, Q15, Q17).
- Marks-weighted index (SCQ 3 marks, Numerical 4 marks): **2.51**. No question involves equivalence relations, and there is no MCQ, so neither adjustment applies.
- **No question is one level off its target.** Every rated level equals the blueprint level.
- **Consistency pass.** I sorted the questions by level and compared neighbours.
  - Q9 (log with base cos x, then squaring) is the easiest Level 3 and is borderline 2/3. I rated it with **Low** confidence. If you see it as 2, the index drops to about 2.46.
  - Q12 (an endpoint root at a crest) is the hardest Level 2.
  - The anchor bank has no trigonometric-equation chapter as such; ratings lean on 2026-P1-Q14 (L3), 2023-P1-Q8 (L2), 2023-P2-Q3 and 2025-P2-Q3 (L3). Most are Medium confidence.

## Originality report
I web-checked every question with web search, searching its distinctive structure in words and symbols. Perfect novelty cannot be guaranteed, so please tell me if you recognise any question.

| Q | Mechanism | Web check | Standard ingredient |
|---|---|---|---|
| 1 | tan x + cot x = λ (λ < −2) gives sin 2x = 2/λ; the sum of the principal roots is the invariant 5π for every such λ. | ingredient only | tan x + cot x = 2/sin 2x |
| 2 | u = tan x − cot x turns the equation into u(u − 3) = 0; one branch is a quadratic in tan x with roots of opposite sign. | ingredient only | reciprocal substitution |
| 3 | Sign chart of sin x(1 − 2cos x)/cos x on a full period; the total length π is asked. | ingredient only | **yes**: wavy-curve sign analysis (tan x ≥ sin x is a solver example) |
| 4 | System: 1/2 < sin x < 1 together with tan x > cot x, where the sign of tan x reverses the second inequality in the second quadrant. | ingredient only | **yes**: each inequality alone is a routine exercise |
| 5 | tan(π sin x) = 1: the bound on sin x keeps the n = 0 and n = −1 members (sin x = 1/4, −3/4); the count runs over 4.5 periods. | not found | general solution of tan θ = 1 |
| 6 | An expanded equation that is secretly (2 sin x − cos x)(sin x + 2cos x − 2) = 0; the second root is twice the first. | not found | factorisation |
| 7 | Sum-to-product on two pairs gives the factor cos 2x and a sin x + √3 cos x = 1 factor; only one of its roots lies in [−π, 0]. | not found | sum-to-product |
| 8 | 4 sin x − 3 cos x − 3 = tan(x/2) becomes the cubic t³ − 7t + 6 = 0 under t = tan(x/2). | not found | t = tan(x/2) |
| 9 | log base cos x equal to 1/2 creates a root equation; squaring gives cos x = 1/4 or 1/9, and 1/9 fails both the sign check and the log domain. | not found | **yes**: squaring and rejecting roots (as in the classic √(5 − 2 sin x) = 6 sin x − 1) |
| 10 | √(2 − 2 sin 3x) sec 3x = 2: sin 3x = 1 is rejected by sec, and half of sin 3x = −1/2 is extraneous; then 150 roots are counted. | ingredient only | **yes**: the rejection of sin x = 1 by sec appears in the published "tan x + sec x = 2 cos x" |
| 11 | The domain of √(−tan x) + log(4π² − x²) filters the roots of sin 2x + sin x = 0 (keeps tan x = 0 roots and two of four cos x = −1/2 roots). | not found | domain of radical and log |
| 12 | cos(πx) = x²/36 on [−5, 6]: one crossing per unit interval, plus the endpoint x = 6 where the parabola meets a crest. | not found | graphical counting |
| 13 | y = −1/2 against max{sin\|x\|, cos\|x\|} on [−2π, π]: one root on each branch, only on the left; the sum of the roots is asked. | ingredient only | **yes**: a published ALLEN item counts the solutions of max(sin x, cos x) = 1/2 on (−2π, 5π). The \|x\|, the negative level and the sum make this different, but the family is close |
| 14 | 4^{sin²πx} + 4^{cos²πx} ≥ 4 (AM-GM) against 4 − \|4x − 3\| ≤ 4; the equality sets meet only at x = 3/4. | ingredient only | **yes**: the AM-GM minimum of 2^{sin x} + 2^{cos x}-type sums |
| 15 | √3 sin x + cos x + sin(3x/2) = 3: both maxima are reached only on every second member of x = π/3 + 2nπ (a parity condition). | not found | range of a sin x + b cos x |
| 16 | sin 3x/sin x + cos 3x/cos x collapses to 4 cos 2x, so cos 2x = −1/5 and tan² x = 1.5. | ingredient only | **yes**: the related identity sin 3x/sin x − cos 3x/cos x = 2 is a textbook "prove that" |
| 17 | sec x + tan x = (1 + t)/(1 − t) with t = tan(x/2), against 1 + 4t; the roots t = 0, 1/2 are counted in the open interval (−2π, 2π). | ingredient only | **yes**: the identity sec x + tan x = tan(π/4 + x/2) |
| 18 | x − y = π/2 turns 3 sin x − 4 sin y = 5 into 3 sin x + 4 cos x = 5, its maximum, fixing sin x and cos x. | ingredient only | **yes**: "if 3 sin x + 4 cos x = 5 then ..." is a standard item; the system form is the new part |

No search found a near-identical problem, so no question was redesigned after the web check. Q13 is the closest to published material; if you want it further from the ALLEN item, change it.

## Problems found while verifying
- **The web search assistant made errors that I checked and rejected.** In each case my answer stands:
  - Q14: it tested 4 − |x|, not the stem's 4 − |4x − 3|, and concluded there is no solution.
  - Q16: it simplified sin 3x/sin x to 2 + cos 2x. The correct value is 3 − 4 sin² x = 1 + 2cos 2x, and sympy confirms that the sum is 4 cos 2x.
- **Uniqueness and domain conditions added to stems:**
  - Q1: "principal solutions" defined as the solutions in [0, 2π).
  - Q3: x ≠ π/2, 3π/2.
  - Q4 and Q17: the trigonometric functions involved must be defined.
  - Q8: x ≠ π.
  - Q16: x is not a multiple of π/2.
- The stem review is a self-check; an independent reader may still find things.

## Rows whose concepts were hard to combine naturally
- **Q9 (squaring + domain restrictions):** with only cos x in play, the question reduces to a short chain. It is the weakest Level 3 (Low confidence).
- **Q10 (three concepts):** the count in [0, 100π] uses the multiple angle 3x so that the "number of solutions" concept gives a 3-digit answer. The interval is a little large for a natural question.
- **Q11 (domain restrictions + domain of functions):** the two concepts overlap, so the function f is introduced only to supply the domain filter.

The Hindi is my own translation. Please review the specialised terms: मुख्य हल (principal solution), अन्तरालों का सम्मिलन (union of intervals), and असमिका (inequality).
