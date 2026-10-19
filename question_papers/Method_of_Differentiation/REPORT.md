# Method_of_Differentiation: generation report

Blueprint: `qp_blueprints/Method_of_Differentiation.xlsx`. There is no `Method_of_Differentiation_config.xlsx`, so the check ran without `--config`.
This scheduled run made the paper on 19-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy and mpmath were missing for `python3` (Python 3.11). I installed them with `python3 -m pip install pandas openpyxl sympy mpmath`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- The first build stopped in xelatex because the paper title in `meta.json` contained underscores. I changed the title to "Method of Differentiation", as the earlier papers do. File names still use underscores.
- After that, `build_paper.py --blueprint` passed with **no errors and one warning** (Q1 is rated one level below its target; see below). No script was edited and no check was weakened.
- I rendered and looked at page 1 of each of the three PDFs and page 4 of the questions PDF (the Q7 determinant). The Hindi is shaped, and fractions, limits and the 3x3 determinant display in 2D. This paper has no paragraph question.

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the blueprint has only Single Correct and Numerical types and nothing above level 3.
- **Paper:** 10 questions: 2 Single Correct (Q1-Q2), then 8 Numerical (Q3-Q10).
- **Reorder (`--reorder`), old -> new:** 541->1, 543->2, 539->3, 540->4, 542->5, 544->6, 545->7, 546->8, 547->9, 548->10.
- **Answer Plans:** the blueprint had none, so the script drew all 10. Every answer matches its plan; the build checks this.
  - Q1 Option C, Q2 Option A, Q3 positive 2-digit integer, Q4 negative decimal, Q5 negative integer, Q6 positive decimal, Q7 decimal between 0 and 1, Q8 positive 3-digit integer, Q9 negative integer, Q10 positive 2-digit integer.
- **Cells containing ";":** none.
- **Warnings.** These are recorded, not fixed, because the blueprint is your decision. There were no errors, and the blueprint file was not edited.
  - Q4 lists 3 concepts (the Main pattern normally has at most two). All three are used.
  - Concepts repeated across rows (each use has a different mechanism):
    - "Parametric Differentiation": Q1, Q2.
    - "Logarithmic Differentiation": Q3, Q4.
    - "Differentiation of Implicit functions": Q4, Q5.
    - "Higher order derivatives": Q2, Q6.
    - "L'Hospital Rule": Q8, Q9.
    - "Evaluation of limit involving exponential and logarithmic functions": Q3, Q10.

## Answers
| Q | Type | Answer |
|---|---|---|
| 1 | SCQ | (C) e^3(1+e^2)/2 |
| 2 | SCQ | (A) -1/27 |
| 3 | Numerical | 24 |
| 4 | Numerical | -0.60 |
| 5 | Numerical | -6 |
| 6 | Numerical | 5.50 |
| 7 | Numerical | 0.50 |
| 8 | Numerical | 175 |
| 9 | Numerical | -60 |
| 10 | Numerical | 20 |

Every answer is exact. None needs rounding.

## How the answers were checked
I designed every mechanism and its numbers myself. Each answer was then recomputed with sympy (exact) and checked again by an independent numerical route with mpmath:
- Q1: sympy solve of the tangency condition (t = e only), then the normal and the area.
- Q2: the third derivative of y(x) at x = 4, computed numerically by inverting x = t^3 + 3t: -0.0370370 = -1/27.
- Q3: sympy limit, and direct evaluation at x = 2 + 10^-8: 24.0000045.
- Q4: implicit derivative with sympy, and a numerical solution of the implicit relation with a central difference: -0.5999999.
- Q5: exact polynomial factorisation at both steps. R = (2, -3) lies on the curve.
- Q6: the ninth and eleventh derivatives with sympy. The roots (11 ± √11)/4 are simple and sum to 11/2.
- Q7: symbolic and numerical derivative of the full determinant at 0: 0.5.
- Q8: sympy limit: 175.
- Q9: sympy series gives a = 3, b = -2, L = -1/20. A 40-digit evaluation at x = 10^-3 gives -0.04999997.
- Q10: sympy limit of log L gives 20. High-precision values at x = 10^-20 and x = 10^-100 (20.035 and 20.007) approach 20 slowly, as the log terms predict.

## Originality report
Every question was built on a named mechanism, checked against `known_skeletons.md`, and web-searched (WebSearch was available in this run). Perfect novelty cannot be guaranteed. If you recognise a question, tell me which one.

| Q | Mechanism | Web check | Standard ingredient |
|---|---|---|---|
| 1 | On the curve x = t ln t, y = t^2, the point whose tangent passes through O is fixed by a transcendental condition that collapses to ln t = 1. The normal there closes triangle OPN. | not found | tangent/normal equations |
| 2 | dy/dx = 4t/3 because the factor t^2+1 cancels. The question asks for the third parametric derivative at the point where the tangent is parallel to a given line. | not found | parametric d²y/dx² rule |
| 3 | Two "towers" whose bases equal 1 at x = 2, so the derivative of the exponent x^x drops out of the logarithmic derivative. | not found | e^u - 1 ~ u |
| 4 | x^y + 3y^x = 4xy^2 through (1,1), where every log term vanishes. The question asks for d(y^x)/d(x^y). | ingredient only (x^y + y^x = c implicit exercises) | x^y, y^x implicit family |
| 5 | Two successive tangent-meets-again steps on y^2 + y = x^3 - x, with each cubic factored by its double root. | ingredient only (this curve appears in elliptic-curve notes, where the doubling at (0,0) is a group-law example) | tangent-chord construction |
| 6 | Points of inflection of the ninth derivative of x^2 e^{-4x}: Leibniz closed form, then f^(11), then Vieta. | not found | Leibniz n-th derivative |
| 7 | A determinant of unrelated functions that equals the identity at 0, so F'(0) is the sum of the diagonal derivatives. | not found | row-wise derivative rule |
| 8 | Second-order L'Hospital limit of a six-factor product. p''(0) comes from (Σk)^2 - Σk^2. | ingredient only (the first-order version is a known exercise) | L'Hospital |
| 9 | The x and x^3 terms of sin^{-1}x, tan x and sin x cancel for one (a, b). One L'Hospital step, then series to x^4. | ingredient only ("find a, b so that the limit is finite" is a common type) | Maclaurin series |
| 10 | A 0^0 form with exponent 4/ln(tan x). After taking logs, only the orders of vanishing (3 + 2) survive. | not found | standard limits |

**Redesigns forced by the web check:**
- **Q1, attempt 1:** the node of x = t^3 - 3t, y = t^2 + 3. A Cornell calculus worksheet uses the same curve (without the +3) and finds the two tangents at the crossing point. Redesigned.
- **Q1, attempt 2:** a line that is the normal at P and the tangent at Q on x = 3t^2, y = 2t^3. This is a known JEE/forum problem. Redesigned again.
- **Q5, first design:** y^2 = x^3 - x + 1. A Harvard worksheet runs the same first tangent step on that curve. The curve was changed.

## Levels
- **Distribution:** level 2: 3 questions (Q1, Q7, Q8); level 3: 7 questions (Q2-Q6, Q9, Q10).
- **Weighted index:** about **2.71**. There is no equivalence-relation adjustment and no MCQ floor in this paper.
- **One level off target:**
  - **Q1** is rated 2 against a target of 3 (Medium confidence). The two redesigns came from the originality check, and the version that passed is a routine four-step parametric chain: slope, tangency condition, normal, area. I kept it rather than make it artificially harder. Its nearest anchors are 2023-P1-Q7 (L2) and 2026-P2-Q2 (L2).
- Every other question is at its target level (all ratings Medium or High confidence).
- The calibrated consistency pass was done: the hardest level-2 question (Q1) and the easiest level-3 question (Q2) were compared side by side.

## Rows whose concepts were hard to combine naturally
- **Q4** (logarithmic + one function with respect to another + implicit). This is the only three-concept row. It works, but the relation was chosen so that the logs vanish at (1,1), and the x^y / y^x family is a standard ingredient.
- **Q10.** In the "0^0 / ∞^0 via logarithms" form the answer is naturally e^k, so the stem asks for log_e L. This is a normal JEE phrasing, but it is a derived quantity.

## Stem review
`review_stems.py` was run and every English stem was read as a student would read it. The review is recorded in each question's `stem_review` field. It is a self-check, so an independent reader may still find something.

## Files
- `Method_of_Differentiation_Shortened_Solutions.docx`, `Method_of_Differentiation_Full_Solutions.docx`
- `Method_of_Differentiation_Questions_EN_HI.pdf`, `Method_of_Differentiation_Questions_and_Shortened_Solutions.pdf`, `Method_of_Differentiation_Questions_and_Full_Solutions.pdf`
- `Method_of_Differentiation_difficulty.xlsx` (internal)
- `_source/`: `blueprint.json`, `meta.json`, `q01.json`-`q10.json`, for later fixes and rebuilds.
