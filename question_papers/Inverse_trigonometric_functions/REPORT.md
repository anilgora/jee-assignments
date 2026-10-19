# Inverse_trigonometric_functions: generation report

Blueprint: `qp_blueprints/Inverse_trigonometric_functions.xlsx`. There is no `Inverse_trigonometric_functions_config.xlsx`, so the check ran without `--config`.
This scheduled run generated the paper on 19-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy and mpmath were missing for `python3`. I installed them with `python3 -m pip install pandas openpyxl sympy mpmath`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- `build_paper.py --blueprint` passed on the first build with **no errors and no warnings**. No script was edited and no check was weakened.
- I rendered page 1 of each of the three PDFs and looked at it, plus page 4 of the questions PDF (Q6-Q8: an infinite sum and a set in braces). The Hindi is shaped, and the equations (fractions, roots, sums, inverse functions) are 2D. This paper has no paragraph question.
- **How the answers were checked.** I designed every mechanism and its numbers myself. Every answer was checked with mpmath/numpy (scripts in a scratch folder, not kept), using an independent route:
  - dense sign-change scans for root counts and solution sets (Q3, Q7, Q11, Q12 first design, Q14);
  - brute force for integer and pair counts (Q9, Q13: all 2500 pairs at 30 digits);
  - direct high-precision summation or iteration (Q2, Q6, Q8, Q10, Q12);
  - sampling the range or the minimum on a fine grid (Q4, Q5);
  - numerical differentiation at the root (Q11).

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the blueprint has only Single Correct and Numerical types and nothing above level 3.
- **Paper:** 14 questions: 2 Single Correct (Q1-Q2), then 12 Numerical (Q3-Q14).
- **Reorder (`--reorder`), old -> new:** 494->1, 501->2, 488->3, 489->4, 490->5, 491->6, 492->7, 493->8, 495->9, 496->10, 497->11, 498->12, 499->13, 500->14.
- **Answer Plans:** the blueprint had none, so the script drew all 14:
  Q1 Option C, Q2 Option A; Q3 positive 2-digit integer, Q4 negative decimal, Q5 negative integer, Q6 positive decimal,
  Q7 decimal between 0 and 1, Q8 positive 3-digit integer, Q9 negative integer, Q10 positive 2-digit integer, Q11 negative decimal,
  Q12 decimal between 0 and 1, Q13 positive 3-digit integer, Q14 positive decimal.
  Every answer matches its plan; the build checks this.
- **Warnings.** These are recorded, not fixed, because the blueprint is your decision:
  - **Three concepts in a Main row:** Q5 (old 490) and Q6 (old 491) each list 3 concepts. Both questions use all three.
  - **Concepts repeated across rows.** Each repeat uses a different mechanism:
    - "Domain and range of inverse trigonometric functions": Q3, Q4, Q5 and Q6.
    - "Evaluation of inverse trigonometric expression": Q1, Q5 and Q8.
    - "Addition and subtractions of angles involving inverse trigonometric expressions": Q2, Q6, Q10 and Q12.
    - "Summation of series based on ITF": Q2 and Q6.
    - "Graphs of inverse trigonometric functions": Q3 and Q7.
    - "Properties of Inverse trigonometric functions": Q8 and Q9.
    - "Simplification of Inverse trigonometric expressions by trigonometric substitutions": Q5, Q10 and Q11.
    - "ITF Equations": Q13 and Q14.
  - No cell contained ";". There were no errors. The blueprint file was not edited.

## Answers
Q1 (C) π/10, Q2 (A) π − tan⁻¹(9/17), Q3 13, Q4 −0.50, Q5 −2, Q6 1.50, Q7 0.75, Q8 590, Q9 −11, Q10 19, Q11 −0.25, Q12 0.96, Q13 206, Q14 9.25.

## Originality report
I named a mechanism for each question before writing it, and checked it against `known_skeletons.md`. Every question was web-searched (WebSearch, standard mode). The labels in the "Web check" column mean:
- **not found:** the search found nothing that matches the question.
- **ingredient only:** the search found the standard fact or family the question rests on, but not the question built on it.

Novelty cannot be guaranteed; please name any question you recognise.

| Q | Mechanism | Web check |
|---|---|---|
| 1 | α = −(1+√5)/4 is −cos 36° = −sin 54°, and 2α² − 1 is cos 72° = sin 18°. Both principal-value traps act together: sin⁻¹ of −cos 36°, and cos⁻¹(2x² − 1) ≠ 2cos⁻¹x for negative x. | not found |
| 2 | The term 4k/(k⁴ − k² + 4) is a difference of arctangents of consecutive triangular numbers. S₂ + S₃ = tan⁻¹3 + tan⁻¹6 then needs the +π correction. | ingredient only. A paper on arctangent sums gives the infinite sum of this family, Σ tan⁻¹(2ak/(k⁴ − k² + a²)) = π/2. The question asks for finite partial sums and their addition instead. |
| 3 | 2 sin⁻¹(sin x) = cos⁻¹(x/20). The domain sets the window [−20, 20], and the range [0, π] removes the negative half-waves. This leaves 2 roots per hump plus 1 in a partial hump. | not found |
| 4 | The range of sin⁻¹([x]/2) − cos⁻¹({x}) is a union of five shifted copies of (0, π/2]. Whether each end is open or closed comes from the fractional part never reaching 1. | not found |
| 5 | The domain of sin⁻¹(x(3 − x²)/2) comes from the factorisations (x−1)²(x+2) and (x+1)²(x−2). Then x = 2 sin t gives sin 3t, and the minimum of F sits at the domain end point. | not found |
| 6 | A telescoping cot⁻¹ series with step 3 whose first argument is negative (−1/3). The range (0, π) of cot⁻¹ decides the answer; writing cot⁻¹x = tan⁻¹(1/x) gives −0.5. | not found |
| 7 | The total length of the set where cos⁻¹(cos x) < 3 tan⁻¹(tan x) on one period, read from the tent graph and the sawtooth graph | not found |
| 8 | Σ cos⁻¹(sin 40k°) for k = 1..7, via cos⁻¹ = π/2 − sin⁻¹ and seven quadrant reductions, with an incomplete cancellation | not found |
| 9 | cot⁻¹(cot n) = tan⁻¹(tan n) exactly when n mod π lies in (0, π/2). The two principal ranges are not symmetric, so n and −n behave oppositely and the sum over 1 ≤ \|n\| ≤ 10 is −11. | not found |
| 10 | x = cos θ turns the two inverse cosines into cos(θ ∓ π/3). Their sum is 2π/3, then 2θ, then 4π/3. A 19-point sample reads off all three pieces. | not found |
| 11 | The point x₀ is defined by u(x₀) = v(x₀). Finding it needs the branch u = π − 2φ, which gives x₀ = cos 72°, and the same branch fixes the sign of dv/du. | ingredient only (differentiating sin⁻¹(2x√(1−x²)) piecewise is standard) |
| 12 | The recurrence x_{n+1} = (4x_n + 3√(1−x_n²))/5 is the rotation θ → θ + sin⁻¹(3/5), folded back by the principal range of sin⁻¹. It becomes 2-periodic, so x₁₀₀ = sin 2φ = 24/25. | not found |
| 13 | tan⁻¹(1/m) + tan⁻¹(1/n) ≥ tan⁻¹(1/2) over a 50 × 50 grid reduces to (m−2)(n−2) ≤ 5, plus the trivial rows m ≤ 2 or n ≤ 2. The equality case (3,7), (7,3) is the boundary. | ingredient only (the identity tan⁻¹(1/3) + tan⁻¹(1/7) = tan⁻¹(1/2) and the related Diophantine equation are known) |
| 14 | sin(2tan⁻¹x) = cos(2tan⁻¹(2x/3)) is solved via the general solution of cos A = cos B. The member −3π/4 of the family α + β = π/4 − kπ gives the second root x = −3. | not found |

**Redesigned after the web check:** the first design for row Q12 was sin⁻¹x − cos⁻¹x = sin⁻¹((x − 2)/5). The search found a published equation of the same form, sin⁻¹x − cos⁻¹x = sin⁻¹(3x − 2), so I replaced it with the iteration above before writing the question.

## Difficulty
- **Level distribution:** level 2 × 7 (Q1, Q2, Q7, Q8, Q9, Q10, Q13) and level 3 × 7 (Q3, Q4, Q5, Q6, Q11, Q12, Q14). Every question is rated **at its target level**; none is one level off.
- **Weighted index:** about 2.52, from `build_paper.py`. No equivalence-relation or MCQ adjustments apply.
- **Consistency pass:** I sorted the questions by level and compared the borderline ones.
  - Q13 (L2, grid count) and Q2 (L2, triangular-number telescoping) are the heaviest of the L2 questions.
  - Q4 (L3, range as a union of five intervals) is the lightest of the L3 questions.
  - All three are placed with Medium confidence.

## Problems found while verifying
- **Q2:** one early distractor, π/2 + tan⁻¹(9/17), equals π − tan⁻¹(17/9), which was another option. I replaced it with 3π/4.
- **Q11:** the first plan asked for du/dv, which is −4 (an integer, not the planned negative decimal). I asked for dv/du = −0.25 instead. The stem says x₀ is in (−1, 1) because x = 1 also satisfies u = v.
- **Q12:** redesigned after the web check (see above).
- **Shared ingredients:** the chapter has only four composite functions (sin⁻¹(sin x), cos⁻¹(cos x), tan⁻¹(tan x), cot⁻¹(cot x)), so some appear in more than one question. Each question uses them in a different setup:
  - Q3: sin⁻¹(sin x) against cos⁻¹(x/20).
  - Q7: cos⁻¹(cos x) against tan⁻¹(tan x).
  - Q8: discrete reductions of sin⁻¹(sin θ).
  - Q9: cot⁻¹(cot n) against tan⁻¹(tan n) at integers.

## Rows whose concepts were hard to combine naturally
- **Q8** ("Evaluation" + "Properties"). Both concepts are close to each other. The property cos⁻¹y = π/2 − sin⁻¹y carries the question, and the quadrant reductions are the evaluation part.
- **Q12** ("Addition of ITF" + "Compound angles"). The ITF addition appears only in the solution, as the sin⁻¹a + sin⁻¹b rule with the a² + b² > 1 case. The stem is a pure recurrence; a student who iterates by hand reaches the same 2-cycle without inverse functions.

## Notes
- The Hindi is my own translation. Please review the specialised terms, for example परिसर (range) in Q4 and "u के सापेक्ष v का अवकलज" in Q11.
- `_source/` holds `blueprint.json`, `meta.json` and `q01.json`-`q14.json`, so a question can be fixed and the paper rebuilt.
- The stem review is a self-check (`review_stems.py` plus reading each stem). An independent reader may still find things.
