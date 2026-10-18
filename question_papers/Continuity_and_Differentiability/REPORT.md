# Continuity_and_Differentiability: generation report

Blueprint: `qp_blueprints/Continuity_and_Differentiability.xlsx`. There is no `Continuity_and_Differentiability_config.xlsx`, so the check ran without `--config`.
This scheduled run generated the paper on 18-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy and mpmath were missing for `python3`; installed with `python3 -m pip install pandas openpyxl sympy mpmath`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- The paper title in `meta.json` is "Continuity and Differentiability" (no underscores); file names use `Continuity_and_Differentiability`.
- `build_paper.py` passed on the first run with no errors and no warnings. No script was edited.
- Page 1 of each of the three PDFs (and page 2 of the questions PDF, which has the case-defined functions) was rendered and checked: Hindi shaped, equations in 2D, display formulas readable.

## Blueprint check
- **Pattern:** inferred as **JEE Main** (only Single Correct and Numerical types, nothing above level 3). The paper name comes from the file name.
- **Paper:** 14 questions: 1 Single Correct, then 13 Numerical.
- **Reorder (`--reorder`):** the single-correct row moved to the front. Old -> new:
  534->1, 525->2, 526->3, 527->4, 528->5, 529->6, 530->7, 531->8, 532->9, 533->10, 535->11, 536->12, 537->13, 538->14.
- **Answer Plans:** the blueprint had none, so the script drew all 14:
  Q1 Option C, Q2 positive 2-digit integer, Q3 negative decimal, Q4 negative integer, Q5 positive decimal, Q6 decimal between 0 and 1,
  Q7 positive 3-digit integer, Q8 negative integer, Q9 positive 2-digit integer, Q10 negative decimal, Q11 decimal between 0 and 1,
  Q12 positive 3-digit integer, Q13 positive decimal, Q14 positive decimal. Every answer matches its plan (the build checks this).
- **Warnings (recorded, not fixed; the blueprint is yours):**
  - Q4 (old 527) lists three concepts; the Main pattern normally has at most two. Kept, and all three are used.
  - Concepts repeated across rows (expected in a one-chapter paper; each repeat uses a different mechanism): "Continuity and Differentiability of functions" (Q1, Q2, Q3, Q4, Q14); "...involving GIF and fractional part" (Q2, Q4); "...involving max min operators" (Q4, Q5); "...involving non uniformly defined functions" (Q5, Q6); "Intermediate Value theorem" (Q8, Q9); "Types of discontinuity" (Q8, Q10); "Determination of functions using differentiability" (Q1, Q11); "...involving sin(1/x) or cos(1/x)" (Q12, Q13).
  - No cell contained ";". No errors. The blueprint file was not edited.

## Answers
Q1 (C) -7, Q2 58, Q3 -0.30, Q4 -4, Q5 2.50, Q6 0.50, Q7 210, Q8 -14, Q9 21, Q10 -0.50, Q11 0.25, Q12 190, Q13 3.50, Q14 3.20.
Each was recomputed with code separately from the hand solution: Q1 by checking which monic cubics fit; Q2 by numeric one-sided limits and derivatives at all 49 integers; Q3 with a bisection inverse and difference quotients (h = 1e-12); Q4 and Q5 by fine grid scans for non-smooth points; Q6 by solving the full sympy system (two solutions; the stem excludes the one that is differentiable at -1); Q7 by checking the closed form satisfies the equation; Q8 by factorisation and a range scan; Q9 by counting sign changes for n = 1..10; Q10 with sympy one-sided limits; Q11 by series inversion and numeric third derivatives on both sides; Q12 by enumeration; Q13 by direct counting at a = 1e-3, 1e-4, 1e-5; Q14 with sympy and numeric difference quotients.

## Difficulty
- Level distribution: **7 questions at level 2 (Q1, Q6, Q7, Q8, Q10, Q12, Q14) and 7 at level 3 (Q2, Q3, Q4, Q5, Q9, Q11, Q13)**. Every question is rated at its target level; none is one level off.
- Marks-weighted index: **2.51** (no equivalence-relation or multi-correct adjustments apply). This is a Main-pattern chapter paper, so it is not expected to fall in the Advanced range of 2.6-3.2.
- Borderline ratings (Medium confidence):
  - Q1 (2): could be read as 1; the reverse deduction (a root without a corner must be repeated) plus the sign of p keeps it at 2.
  - Q6 (2): the rational/irrational tangency condition for differentiability is less practised; it could be read as 3.
  - Q4 (3) and Q13 (3): long casework (Q4) and an accumulating count (Q13) could be read as 4.
- Consistency pass: the hardest level-2 questions (Q6, Q14) were read next to the easiest level-3 ones (Q5, Q13), and the order was kept.

## Originality report (per question)
Each mechanism was named before the stem was written and checked against `known_skeletons.md` (none matched; the build's skeleton lint gave no warning). Every question was web-searched (WebSearch, standard mode); no near-identical problem was found.

| Q | Target | Rated | Mechanism | Web check |
|---|---|---|---|---|
| Q1 | 2 | 2 | Reverse problem: the corner of \|p\| at x = 3 and the corner-free root x = 1 determine the cubic p = (x-1)^2(x-3); then f'(0) = -p'(0) (way 5) | not found |
| Q2 | 3 | 3 | {x} times sin(pi x/2) sin(pi x/3): continuity at an integer needs a zero of the product, differentiability a double zero; count by divisibility by 2, 3, 6 (way 2) | not found |
| Q3 | 3 | 3 | Inverse of a continuous decreasing function with a corner: the one-sided derivatives of g are reciprocals of the opposite one-sided derivatives of f (way 4) | not found |
| Q4 | 3 | 3 | max{{x}, \|x\|/4}: crossings at 4n/3 for x > 0 and 4n/5 for x < 0, plus jumps at every integer in (-4,4); sum of points (way 2) | not found |
| Q5 | 3 | 3 | Sliding-window maximum of a piecewise function over [x-1, x]; the only corner is the tie f(x-1) = f(x) at x = 5/2 (way 2) | ingredient only (running max from 0 is a known JEE type) |
| Q6 | 2 | 2 | x^3 on rationals, ax + b on irrationals: continuity points are roots, differentiability points are repeated roots; Vieta fixes a, b (way 5) | ingredient only (rational/irrational continuity) |
| Q7 | 2 | 2 | f(x) = f(x/2)cos(x/2) iterated to a telescoping cosine product; continuity at 0 closes it to f(0) sin x/x (way 1) | ingredient only (halving functional equations, the cosine product) |
| Q8 | 2 | 2 | Existence of the limit forces a removable discontinuity; the limit value -6 is the missing end of the range found by the IVT (way 5) | not found |
| Q9 | 3 | 3 | Family e^x = x^n counted for n = 1..10: parity decides negative roots, n > e decides positive roots (way 5) | ingredient only (e^x = x^2, 2^x = x^2) |
| Q10 | 2 | 2 | The jump type of the discontinuity is the condition that fixes a = b = 1; the sign of x\|x\| splits the one-sided limits (way 5) | not found |
| Q11 | 3 | 3 | Third-order matching at 0 between a cubic and an implicitly defined function y + 6y^3 = x (way 5) | not found |
| Q12 | 2 | 2 | x^m sin(1/x^n): pairs that are differentiable at 0 but have an unbounded derivative, 2 <= m <= n <= 20 (way 2) | ingredient only (x^p sin(1/x) thresholds are textbook) |
| Q13 | 3 | 3 | Corners of \|cos(7 pi/(2x))\| accumulate at 0; a N(a) is squeezed to 7/2 (way 2) | not found |
| Q14 | 2 | 2 | Inner function with a jump, yet f o g is differentiable because f(-1) = f(1) and the slopes compensate (way 4) | not found |

Standard ingredients worth flagging:
- Q12 is the weakest on originality: the family x^p sin(1/x^q) and its thresholds are textbook; only the "band" condition and the pair count are new.
- Q7: the product cos(x/2)cos(x/4)...cos(x/2^n) = sin x/(2^n sin(x/2^n)) is standard; the functional equation built on it was not found.
- Q9: equations like e^x = x^2 are standard; the summed family with parity was not found.
- Q5: running maximum g(x) = max{f(t): 0 <= t <= x} is a known JEE Main type (2021); the fixed-length window was not found.
- Novelty cannot be guaranteed; please flag any question you recognise.

## Problems found while verifying
- Q3: the first draft asked for L + R, which does not test the side swap (the sum is the same either way). It was changed to R - L, where a swapped solution gives +0.30 instead of -0.30, and the left slope was changed from -4 to -2 so the answer is a clean -0.30.
- Q6: the conditions "continuous at -1 and differentiable somewhere" have a second solution (a = 3, b = 2, differentiable at -1 itself). The stem says "differentiable at some point c not equal to -1", which leaves exactly one solution (checked with sympy).
- Q13: the first draft of the shortened solution had wrong bounds for N(a); they were corrected to 7/(2a) - 9/2 <= N(a) < 7/(2a) - 7/2 before the build, matching the full solution and the direct count.
- Q1 originally used the same "C^2 matching of two pieces" idea as Q11; Q1 was redesigned (corners of |p|) so the two determination rows use different mechanisms.

## Rows whose concepts were hard to combine naturally
- Q4 (old 527, three concepts: general, GIF/fractional part, max-min): combined naturally in max{{x}, |x|/4}.
- Q5 (max-min + non-uniformly defined): "non-uniformly defined" was read as piecewise-defined; the max is over a moving window. In Q6 (single concept) it was read as a function defined differently on rationals and irrationals. If your sheet means only one of these readings, please say so.
- Q9: the root-counting concept uses IVT and monotonicity; Rolle's theorem is not needed.

## Notes
- The Hindi is the assistant's own translation; please review specialised terms (उच्छेदी (jump) असांतत्यता for jump discontinuity, भिन्नात्मक भाग is not used: {t} is defined by formula, अपरिबद्ध for unbounded, एकैकी आच्छादी for bijection).
- The stem review is a self-check; an independent reader may still find things.
- `_source/` holds `blueprint.json`, every `qNN.json` and `meta.json`, so a question can be fixed and the paper rebuilt with `build_paper.py`.
