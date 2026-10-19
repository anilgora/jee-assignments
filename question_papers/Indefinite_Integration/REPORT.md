# Indefinite_Integration: generation report

Blueprint: `qp_blueprints/Indefinite_Integration.xlsx`. There is no `Indefinite_Integration_config.xlsx`, so the check ran without `--config`.
This scheduled run generated the paper on 19-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy and mpmath were missing for `python3`. I installed them with `python3 -m pip install pandas openpyxl sympy mpmath`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- `build_paper.py --blueprint` passed with **no errors and no warnings**. No script was edited and no check was weakened.
  - The first build attempt failed in xelatex because the title in `meta.json` contained an underscore. I changed the title to "Indefinite Integration"; file names keep the underscore.
- I rendered page 1 of each of the three PDFs and looked at it, plus the page with Q15 (a displayed formula followed by Hindi text). The Hindi is shaped, and the equations (fractions, roots, integrals, limits) are 2D. This paper has no paragraph question.
- **How the questions were written.** I designed every mechanism and its numbers myself. Each answer was checked with sympy/mpmath before the files were written (scripts in `/tmp`, not kept). Where possible a second route was used as well: numerical quadrature, an ODE solver, or a numerical maximum scan.

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the blueprint has only Single Correct and Numerical types and nothing above level 3.
- **Paper:** 18 questions: 6 Single Correct (Q1-Q6), then 12 Numerical (Q7-Q18).
- **Reorder (`--reorder`), old -> new:** 574->1, 577->2, 579->3, 584->4, 585->5, 586->6, 571->7, 572->8, 573->9, 575->10, 576->11, 578->12,
  580->13, 581->14, 582->15, 583->16, 587->17, 588->18.
- **Answer Plans:** the blueprint had none, so the script drew all 18:
  Q1 Option C, Q2 Option A, Q3 Option B, Q4 Option D, Q5 Option A, Q6 Option B;
  Q7 negative integer, Q8 positive 2-digit integer, Q9 negative decimal, Q10 decimal between 0 and 1, Q11 positive 3-digit integer,
  Q12 positive decimal, Q13 positive decimal, Q14 negative decimal, Q15 positive 2-digit integer, Q16 positive 3-digit integer,
  Q17 negative integer, Q18 decimal between 0 and 1.
  Every answer matches its plan; the build checks this.
- **Warnings.** These are recorded, not fixed, because the blueprint is your decision:
  - **`;` in a cell.** Three concept cells contain ";": original rows 1, 5 and 18 (new Q7, Q10, Q18). They are "General vs particular solution; verifying a solution", "Linear differential equation in y; integrating factor" and "Exact differential equations; integrating factors by inspection". No config was supplied, so each cell was kept as **one** concept. Each reads as a single concept name.
  - **Concepts repeated across rows.** Each repeat uses a different mechanism:
    - "Integration of trigonometric functions": Q2 and Q4.
    - "Integrals of the form int dx/(ax^2+bx+c) and int dx/sqrt(ax^2+bx+c)": Q3, Q6, Q13 and Q14.
    - "Variable separable equations": Q1, Q8 and Q13.
    - "Integration by parts": Q1 and Q11.
    - "t = tan(x/2) for a sin x + b cos x + c": Q15 and Q16.
    - "Integration of rational functions": Q12 and Q17.
  - There were no errors. The blueprint file was not edited.

## Answers
Q1 (C) e^(1/4), Q2 (A) 3√3/64, Q3 (B) ln 2 + π/4, Q4 (D) tan⁻¹7 + ln(5/√2), Q5 (A) (1 + ln 2)/2, Q6 (B) 1 − √3 + ½ ln(1 + 2/√3),
Q7 −9, Q8 14, Q9 −22.50, Q10 0.50, Q11 169, Q12 4.50, Q13 1.50, Q14 −1.75, Q15 25, Q16 120, Q17 −5, Q18 0.25.

Second routes used:
- **Q2 and Q4:** dense numerical maximum scans.
- **Q6, Q14, Q15 and Q16:** mpmath quadrature of the given F′.
- **Q13 and Q18:** mpmath ODE solver from the initial point. Q18 gives y(1.5) = 0.25 on the branch with 0 < y < 1.
- **Q15:** checked that the ratio equation has exactly one root, s = 1/2.
- **Q17:** sign of f on each side of x = 1.

## Originality report
I named a mechanism for each question before writing it, and checked it against `known_skeletons.md`. Every question was web-searched (WebSearch, standard mode). No question was found published.

"Ingredient only" means the search found the standard integral or technique the question uses (often a textbook antiderivative), but not the question built on it. Because this is a one-chapter paper, many rows rest on a standard integral by design. Novelty cannot be guaranteed; please name any question you recognise.

| Q | Mechanism | Web check |
|---|---|---|
| 1 | The curve is defined by its tangent's y-intercept, y(1 − x² ln x). This gives the separable equation y′/y = x ln x, solved by parts; at √e the two by-parts terms cancel. | not found |
| 2 | The antiderivative of cos⁴x − a cos²x is required to be periodic, which forces zero mean and a = 3/4. F collapses to ¼ sin x cos³x, and its maximum is asked. | not found |
| 3 | p and q are recovered from the antiderivative's behaviour at infinity: boundedness of F − ln(quadratic) gives p; the limit of F(x) − F(−x) gives q. | ingredient only |
| 4 | Maximum of x + ln(3 sin x + 4 cos x), the antiderivative of (7cos x − sin x)/(3 sin x + 4 cos x), reached at tan x = 7 | ingredient only (the integral itself is a textbook-type exercise) |
| 5 | Euler substitution for 1/(x + √(x² + 2x)), normalised at 0. The finite part at infinity of F − ½ ln x is asked. | not found |
| 6 | Reciprocal substitution for 1/(x²√(x² + x + 1)), normalised at infinity; infinity becomes t = 0 | ingredient only |
| 7 | On ℝ∖{0} the general solution has two independent constants. f(x) + f(−x) = 4 links them, and a single constant contradicts the data. | not found |
| 8 | The curve through the origin is defined by its subnormal MN = 3x√(x² + 9). The sign of yy′ must be argued, then the substitution u = x² + 9. | not found |
| 9 | The antiderivative of x²/√(9 − x²) in the angle variable (half a sector minus a triangle). The angle where it takes a given value is asked in degrees; uniqueness comes from monotonicity. | ingredient only |
| 10 | The rational forcing term of a linear DE is g + g′ with g = x/(1 + x²). The e^x(f + f′) rule solves it, boundedness at −∞ fixes C, and the maximum is asked. | not found |
| 11 | Second antiderivative of e^{5x} sin 12x: the repeating integral twice, constants fixed by decay at −∞, amplitude 1/169 via the 119-120-169 triple | ingredient only |
| 12 | Partial fractions whose coefficients sum to 0, so the antiderivative can be normalised at infinity | ingredient only |
| 13 | Separable DE with a quadratic on each side and arctan coefficients in ratio 1:2; the value needs tan(½ tan⁻¹(4/3)) = ½ | ingredient only |
| 14 | The unknown k in (x² + 1)/(x⁴ + kx² + 1) is recovered from lim F = π, with t = x − 1/x and normalisation at t = 0 | ingredient only (the definite integral 0→∞ appears as a general result) |
| 15 | a and b in 1/(a + b sin²x) are identified by matching two values with the tan(x/2) antiderivative of 1/(5 + 3cos x); the hidden fact is F(x) = G(2x) | ingredient only |
| 16 | The domain is the interval between consecutive roots of sin x + √3 cos x = −1, found via the half-angle quadratic. Its factorisation gives a single log, which is inverted at tan(θ/2) = √3. | ingredient only |
| 17 | A rational antiderivative is required (no log residues), found by undetermined coefficients, plus an extremum at x = 1 | not found |
| 18 | A non-separable DE made of d(xy), d(y/x) and dx, with integrating factor 1/(x²y²) by inspection; the range condition picks the branch | not found (the closest textbook equation is y(1+xy)dx + x(1−xy)dy = 0) |

## Difficulty
- **Level distribution:** level 2 × 6 (Q4, Q6, Q11, Q12, Q13, Q15) and level 3 × 12. Every question is rated **at its target level**; none is one level off.
- **Weighted index:** about 2.67, from `build_paper.py`. No equivalence-relation or MCQ adjustments apply.
- **Consistency pass:** I sorted the questions by level and compared the borderline ones.
  - Q7 (L3, two constants on ℝ∖{0}) is the lightest computation among the L3 questions. It is placed at L3 for idea availability, with Medium confidence.
  - Q15 (L2) is the heaviest of the L2 questions, with Medium confidence.

## Problems found while verifying
- **Q2:** the first design used F′ = cos⁴x − a sin²x. Expanding it gave a cos 2x coefficient that makes the maximum irrational and messy. I changed it to cos⁴x − a cos²x before writing the question; the antiderivative then collapses to ¼ sin x cos³x.
- **Q18:** for a given x, the implicit solution y + 1/y = 13x/3 − x² has two roots. The stem therefore requires f to take values in (0, 1), which removes y = 4. I checked that this branch exists on [1, 3/2].
- **Q9 and Q16:** both answers are angles in degrees. Q9 asks for θ in degrees, which is its measurement-of-angles concept. Q16 asks for 180θ/π, the natural integer for its trigonometric-equation concept.

## Rows whose concepts were hard to combine naturally
- **Q7** ("standard formulae" + "general vs particular solution; verifying a solution"). The integration is elementary, so the general-vs-particular concept carries the question: the two-interval domain and the verification against f(x) + f(−x) = 4.
- **Q9** (trigonometric substitution + measurement of angles). The degree measure enters only as the unit of the answer and through the sector-area reading. The link is real but light.

## Notes
- The Hindi is my own translation. Please review the specialised terms, for example प्रतिअवकलज (antiderivative) in Q17 and विवृत अन्तराल in Q18.
- `_source/` holds `blueprint.json`, `meta.json` and `q01.json`-`q18.json`, so a question can be fixed and the paper rebuilt.
- The stem review is a self-check (`review_stems.py` plus reading each stem). An independent reader may still find things.
