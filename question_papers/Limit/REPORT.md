# Limit: generation report

Blueprint: `qp_blueprints/Limit.xlsx`. There is no `Limit_config.xlsx`, so the check ran without `--config`.
This scheduled run generated the paper on 19-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy and mpmath were missing for `python3`. I installed them with `python3 -m pip install pandas openpyxl sympy mpmath`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- `build_paper.py --blueprint` passed with **no errors and no warnings**. No script was edited and no check was weakened.
- I rendered page 1 of each of the three PDFs and looked at it, plus page 3 (Q3 and Q4: nested function, binomial coefficients) and page 8 (Q14 and Q15: a limit-defined function and a `cases` block) of the questions PDF. The Hindi is shaped, and the equations (fractions, limits, binomials, piecewise definitions) are 2D. This paper has no paragraph question.
- **How the answers were checked.** I designed every mechanism and its numbers myself. Each answer was then checked independently with mpmath, sympy or numpy (scripts in a scratch folder, not kept):
  - high-precision evaluation close to the limit point, from both sides where it matters (Q1, Q2, Q6, Q7, Q9, Q14, Q16, Q17);
  - large-n or large-x evaluation (Q4, Q5, Q8, Q10, Q11, Q23);
  - sympy series or limits (Q3, Q18, Q20, Q21);
  - root finding (Q22);
  - a direct check of continuity and jumps (Q12, Q15);
  - a numerical running maximum and kink scans (Q13, Q19).

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the blueprint has only Single Correct and Numerical types and nothing above level 3.
- **Paper:** 23 questions: 6 Single Correct (Q1-Q6), then 17 Numerical (Q7-Q23).
- **Reorder (`--reorder`), old -> new:** 502->1, 503->2, 504->3, 508->4, 515->5, 522->6, 505->7, 506->8, 507->9, 509->10, 510->11, 511->12, 512->13, 513->14, 514->15, 516->16, 517->17, 518->18, 519->19, 520->20, 521->21, 523->22, 524->23.
- **Answer Plans:** the blueprint had none, so the script drew all 23:
  Q1 Option C, Q2 Option A, Q3 Option B, Q4 Option D, Q5 Option A, Q6 Option B; Q7 negative integer, Q8 positive 2-digit integer,
  Q9 negative decimal, Q10 decimal between 0 and 1, Q11 positive 3-digit integer, Q12 positive decimal, Q13 positive decimal,
  Q14 negative decimal, Q15 positive 2-digit integer, Q16 positive 3-digit integer, Q17 negative integer, Q18 decimal between 0 and 1,
  Q19 negative integer, Q20 negative decimal, Q21 positive 3-digit integer, Q22 decimal between 0 and 1, Q23 positive decimal.
  Every answer matches its plan; the build checks this.
- **Cells containing ";"** (rows 5 and 14 of the sheet: "Limits at infinity; dominant term and rational function behaviour"). There was no config, so following your rule each cell was **kept as one concept**. Both questions using it (Q5, Q8) treat it as one concept.
- **Warnings.** These are recorded, not fixed, because the blueprint is your decision:
  - **Three concepts in a Main row:** Q3 (old 504) and Q10 (old 509). Both questions use all three concepts.
  - **Concepts repeated across rows.** Each repeat uses a different mechanism:
    - "Evaluation of limit involving trigonometric functions": Q1, Q2, Q3.
    - "Evaluation of limit using expansion": Q1, Q3, Q18.
    - "Taylor / Maclaurin Series Expansion ...": Q3, Q18.
    - "Evaluation of limit involving algebraic functions": Q7, Q8, Q21.
    - "Limits at infinity; dominant term ...": Q5, Q8.
    - "one raise to infinity form": Q4, Q9, Q10.
    - "Evaluation of limit involving exponential and logarithmic functions": Q9, Q10.
    - "Sandwich Theorem": Q5, Q10, Q23.
    - "Evaluation of limit involving GIF and fractional part": Q11, Q12.
    - "Evaluation of limit involving non uniformly defined functions": Q14, Q15.
    - "Functions defined by a limit ...": Q14, Q19.
    - "Limits of composite functions": Q16, Q17.
    - "Limits of composite functions and the substitution pitfall": Q6, Q17.
    - "Determining unknown constants from a given limit value": Q20, Q21.
    - "Miscellaneous concepts on Limit": Q22, Q23.
  - There were no errors. The blueprint file was not edited.

## Answers
Q1 (C) 2/3, Q2 (A) 2/√3, Q3 (B) 1/81, Q4 (D) e^(−1/2), Q5 (A) −1/2, Q6 (B) 3/2; Q7 −4, Q8 24, Q9 −1.50, Q10 0.25, Q11 200, Q12 8.50,
Q13 20.25, Q14 −0.50, Q15 33, Q16 190, Q17 −6, Q18 0.25, Q19 −2, Q20 −0.25, Q21 216, Q22 0.60, Q23 2.25.

## Originality report
I named a mechanism for each question before writing it, and checked it against `known_skeletons.md`. Every question was web-searched (WebSearch, standard mode). The labels in the "Web check" column mean:
- **not found:** the search found nothing that matches the question.
- **ingredient only:** the search found the standard fact or problem family the question rests on, but not this question.
- **found: redesigned:** the first design was too close to a published problem and was replaced before the question was written.

Novelty cannot be guaranteed; please name any question you recognise.

| Q | Mechanism | Web check |
|---|---|---|
| 1 | Unit circle, central angle θ. Compares the segment area with the excess of the tangent path PT + TQ over the chord PQ. Both are of order θ³, giving 2/3. | not found |
| 2 | 2cos2x − 1 = cos3x / cos x (the 3A formula written through the 2A formula), so the 0·∞ product with tan3x collapses to sin3x / cos x | not found |
| 3 | N(t) = t − tan t applied twice. Each application cubes the order and multiplies by −1/3, so N(N(x)) ~ x⁹/81. L'Hôpital is out of reach. | **found: redesigned.** The first design was tan(tan x) minus a fourfold sine, over x − sin x. It used the same additive cubic-coefficient idea as JEE Main 2025 (7 April, shift 2), (tan(tan x) − sin(sin x))/(tan x − sin x), so I replaced it before writing. |
| 4 | The 1^∞ base is the ratio of consecutive central binomial coefficients divided by 4, which equals (2n+1)/(2n+2) | not found |
| 5 | The second-order term n(Sₙ − 1) of Σ n/(n² + k). It reduces to −Σ k/(n² + k), which is then squeezed. | ingredient only (Σ k/(n² + k) → 1/2 is a standard sandwich) |
| 6 | One outer f, two inner functions both tending to 0. [cos x] is identically 0 near 0, so f(0) is used; sin x never equals 0, so the limit of f is used. | ingredient only (the general composite-limit warning) |
| 7 | Square root plus cube root vanishing together at x = 1, against the cube root of 9 − x | not found |
| 8 | x(QM − HM) for the numbers x and x + 8, split through the arithmetic mean: 8 + 16 = 24 | not found |
| 9 | 1^∞ with base 2ln(1+x)/(e^{2x} − 1) = 1 − 3x/2 + …; the logarithmic and exponential deviations add | ingredient only (the standard expansions) |
| 10 | (mean of e^{k³/n⁴})ⁿ, a sum with no closed form. e^t is squeezed between 1 + t and 1 + t + t², and the sum of cubes gives λ = 1/4. | not found |
| 11 | √(n² + 40n) sits just below the integer n + 20, so its fractional part tends to 1. The rate 200/n is the answer. | not found |
| 12 | [x](x − a) + [2x](x − b) continuous on (5/4, 9/4). This forces zero jumps at 3/2 and at the double jump 2; then the left limit at 3 is asked. | not found |
| 13 | Running maximum g(x) = max f on [0, x] of a cubic. The corner is where f regains its local maximum value (double-root factorisation), measured by a symmetric difference quotient. | ingredient only. JEE Main has running-max questions (for example g(x) = max{t³ − 6t² + 9t − 3}) that ask for the number of non-differentiable points. Here the regain point and a slope combination are asked instead. |
| 14 | f from an xⁿ limit is ln x for x > 1 and √x − 1 for x < 1. f(1+h)f(1−h)/h² takes one branch of each kind on both sides, so the limit exists although f has a corner. | not found |
| 15 | A line replaces x⁴ − 8x² + 4x on (−c, c). Differentiability at both junctions forces the double tangent y = 4x − 16, giving c = 2. | not found |
| 16 | f(x) = (x²⁰ − 1)/(x − 1). f∘f is undefined at 0 (f(0) = 1), yet (f(f(x)) − 20)/x → 190. | ingredient only (chain rule / geometric sum) |
| 17 | g(y) = (y⁶ − 1)/\|y + 1\| has no limit at −1, but f(x) + 1 = (x − 1)² > 0 picks the right-hand limit | not found |
| 18 | A function times its own inverse agrees with x² up to x⁴. The ratio of the sin·sin⁻¹ and tan·tan⁻¹ defects is (1/18)/(2/9). | not found |
| 19 | The halving functional equation plus continuity at 0 gives f = x² − 1. Then g = lim(1 + \|f\|ⁿ)^{1/n} = max{1, \|f\|}. Corners at ±√2; x = 0 is a trap (\|f\| = 1 there tangentially). | not found |
| 20 | A finite limit of ((1 + ax)eˣ − 1 − bx)/x³ forces two vanishing coefficients | ingredient only (the finite-limit-constants family) |
| 21 | A cube root and a square root must agree to first order; the second-order mismatch −b²/8 = −18 | ingredient only (the same family) |
| 22 | xₙ + … + xₙⁿ = 3/2. The closed form 5xₙ − 3 = 2xₙ^{n+1} and the bound xₙ ≤ x₂ < 1 give 3/5. | ingredient only (x + … + xⁿ = 1 → 1/2 is a known exercise; this changes the constant and the bounding step) |
| 23 | The n-th root of Σ(1 + k/2n)^{2n} is governed by the largest term, (9/4)ⁿ. The term-wise limit e^k is a trap. | not found |

Questions with a standard ingredient: Q5, Q6, Q9, Q13, Q16, Q20, Q21, Q22. **Q22 is the closest to a known problem.** If you want it fully fresh, it is the first one to replace.

## Difficulty
- **Level distribution:** level 2 × 14 (Q1, Q2, Q4, Q6, Q7, Q8, Q9, Q11, Q16, Q17, Q20, Q21, Q22, Q23) and level 3 × 9 (Q3, Q5, Q10, Q12, Q13, Q14, Q15, Q18, Q19).
- Every question is rated **at its target level**; none is one level off.
- **Weighted index:** about 2.40 (SCQ 3 marks, Numerical 4), from `build_paper.py`. No equivalence-relation or MCQ adjustments apply.
- **Consistency pass:** I sorted the questions by level and compared the borderline ones.
  - Q11 (L2, "the fractional part tends to 1" trap) and Q8 (L2, split through the arithmetic mean) are the heaviest of the L2 questions.
  - Q12 (L3, two GIF jump conditions) and Q14 (L3, branch swap) are the lightest of the L3 questions.
  - All four are placed with Medium confidence.

## Problems found while verifying
- **Q3:** redesigned after the web check (see the originality table). The final version was checked with sympy: N(N(x)) = x⁹/81 + 2x¹¹/135 + ….
- **Q6:** the definition of [t] was first placed after "is equal to". During the stem review I moved it into the opening sentence.
- **Q17:** the first numerator, y⁴ − 1, gave −4, the same answer as Q7. I changed it to y⁶ − 1, which gives −6.
- **Q22:** the first constant, 1/3, gave 0.25, which repeated Q10 and Q18. I changed it to 3/2, which gives 0.60. The stem now says n ≥ 2, because for n = 1 the root is 3/2 > 1.
- **Q21:** without "positive", (a, b) = (−18, −12) would also satisfy the condition. The stem states that a and b are positive.

## Rows whose concepts were hard to combine naturally
- **Q19** ("functions defined by a limit" + "continuity of a function defined by a functional equation"): the two concepts have no natural meeting point. I chained them: the functional equation produces f, and the n-th-root limit then builds g from f. It reads as one situation, but the link is a chain rather than a single idea.
- **Q20** (single concept, "determining unknown constants"): the family is very standard. The mechanism has the unknown multiplying eˣ, but the question remains close in style to the familiar finite-limit exercises.

The Hindi is my own translation; please review the specialised terms (for example वर्ग-माध्य-मूल for root mean square and हरात्मक माध्य for harmonic mean in Q8).
The stem review is a self-check; an independent reader may still find things.
