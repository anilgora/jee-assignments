# Function: generation report

Blueprint: `qp_blueprints/Function.xlsx`. There is no `Function_config.xlsx`, so the check ran without `--config`.
This scheduled run generated the paper on 18/19-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy and mpmath were missing for `python3`. They were installed with `python3 -m pip install pandas openpyxl sympy mpmath`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- The build (`build_paper.py --blueprint`) passed on the first full run with **no errors and no warnings**. No script was edited and no check was weakened.
- Page 1 of each of the three PDFs, and the page with the piecewise questions Q15-Q16, were rendered and checked. The Hindi is shaped and the equations (fractions, cases blocks, limits) are 2D. This paper has no paragraph question.
- The questions were written in five parallel batches (Q1-8, Q9-16, Q17-24, Q25-31, Q32-37). A shared registry of mechanisms and functions kept the batches from reusing a function or setup. All batches followed the same skill references. Each answer was then re-checked by hand during the final review.

## Blueprint check
- **Pattern:** inferred as **JEE Main**: only Single Correct and Numerical types, nothing above level 3.
- **Paper:** 37 questions: 4 Single Correct (Q1-Q4), then 33 Numerical (Q5-Q37).
- **Reorder (`--reorder`):** the single-correct rows moved to the front. Old -> new:
  451->1, 454->2, 476->3, 484->4, 452->5, 453->6, 455->7, 456->8, 457->9, 458->10, 459->11, 460->12, 461->13, 462->14, 463->15,
  464->16, 465->17, 466->18, 467->19, 468->20, 469->21, 470->22, 471->23, 472->24, 473->25, 474->26, 475->27, 477->28, 478->29,
  479->30, 480->31, 481->32, 482->33, 483->34, 485->35, 486->36, 487->37.
- **Answer Plans:** the blueprint had none, so the script drew all 37:
  Q1 Option C, Q2 Option A, Q3 Option B, Q4 Option D;
  Q5 positive 2-digit integer, Q6 negative decimal, Q7 negative integer, Q8 positive decimal, Q9 decimal between 0 and 1,
  Q10 positive 3-digit integer, Q11 negative integer, Q12 positive 2-digit integer, Q13 negative decimal, Q14 decimal between 0 and 1,
  Q15 positive 3-digit integer, Q16 positive decimal, Q17 positive decimal, Q18 negative decimal, Q19 positive 2-digit integer,
  Q20 positive 3-digit integer, Q21 negative integer, Q22 decimal between 0 and 1, Q23 negative integer, Q24 negative decimal,
  Q25 positive 3-digit integer, Q26 decimal between 0 and 1, Q27 positive decimal, Q28 positive 2-digit integer, Q29 positive decimal,
  Q30 negative decimal, Q31 negative integer, Q32 positive 2-digit integer, Q33 decimal between 0 and 1, Q34 positive 3-digit integer,
  Q35 positive 2-digit integer, Q36 positive decimal, Q37 decimal between 0 and 1.
  Every answer matches its plan; the build checks this.
- **Warnings.** These are recorded, not fixed, because the blueprint is your decision:
  - **Cells containing ";":** sheet rows 6, 7, 8, 29, 30, 31, 36 and 37. With no config, each was kept as **one** concept, as instructed.
    These are concepts such as "Definition of a function; vertical line test; identical functions" and "Even and odd functions; decomposition into even and odd parts", which read as single concepts.
  - **More than two concepts in a Main row:**
    - Q2 has four concepts: Cauchy equation, one-one test, inverse and f = f⁻¹.
    - Q10, Q23, Q24 and Q32 have three each.
    - All were kept, and every concept is used. `concept_use` in each `_source/qNN.json` says where.
  - **Concepts repeated across rows:** this is expected in a one-chapter paper. Each repeat uses a different mechanism. For example:
    - "Periodic functions: fundamental period" is in Q4 and Q30-Q34.
    - "Inverse of a function" is in Q2, Q3 and Q27-Q29.
    - "Cauchy's Functional Equations" is in Q1, Q2, Q5 and Q6.
  - There were no errors. The blueprint file was not edited.

## Answers
Q1 (C) 56, Q2 (A), Q3 (B) 12/5, Q4 (D) 12,
Q5 36, Q6 -0.75, Q7 -2, Q8 4.5, Q9 0.5, Q10 125, Q11 -11, Q12 16, Q13 -3.75, Q14 0.25, Q15 249, Q16 1.45, Q17 1.5, Q18 -3.5,
Q19 54, Q20 140, Q21 -6, Q22 0.75, Q23 -48, Q24 -31.5, Q25 876, Q26 0.25, Q27 3.75, Q28 33, Q29 3.2, Q30 -1.25, Q31 -54, Q32 26,
Q33 0.75, Q34 360, Q35 30, Q36 2.4, Q37 0.8.

Every answer was recomputed with sympy or mpmath, separately from the hand solution, and also by a second route:
- **Brute-force enumeration:**
  - Q1 checked all 4^10 maps.
  - Q23 and Q25 were checked by direct enumeration of functions between the finite sets.
- **Dense numerical grids:**
  - Q9, Q12, Q13, Q14, Q15, Q16, Q21 and Q36.
  - Q26: the points where it is not differentiable were confirmed by one-sided difference quotients.
- **Numerical period scans** found no smaller period for Q4, Q32, Q34 and Q35.
- **High-precision checks:**
  - Q6: the Riemann-sum limit.
  - Q29: the area, using the numerical inverse.
  - Q27: f(f(x)) = x was solved, all nine roots.
- All decimal answers are exact to two places; none is rounded.
- Every answer was also re-derived by hand during the final review.

## Originality report
A mechanism was named for each question before it was written, and checked against `known_skeletons.md`. Every question was web-searched (WebSearch, standard mode). No question was found published.
"Ingredient only" means the search found the standard result or technique the question uses, but not the question itself. Novelty cannot be guaranteed; please name any question you recognise.

| Q | Mechanism | Web check |
|---|---|---|
| 1 | Log-type Cauchy equation on the truncated set {1,...,10} with codomain {0,1,2,3}; the truncation decides which constraints exist; count = 56 | not found |
| 2 | f(xy)=f(x)+f(y), f'(1)=2 gives 2 ln x; h = x²−3x+2 ln x is increasing and onto, so h = h⁻¹ reduces to h(x) = x, root located by IVT | not found |
| 3 | tan of the angle at which y=f meets y=f⁻¹ (on y=x, reciprocal slopes), f = x³+2x−2 | ingredient only |
| 4 | Period of sin(cos(πx/2)) + cos(sin(2πx/3)); the trap is treating both composites as having period π | not found |
| 5 | f(x+y)=f(x)f(y), continuous at 0; the base is fixed by the tangent-line inequality f(x) ≥ 1+2x | not found |
| 6 | Log Cauchy equation fixed by a limit at 1, then a weighted Riemann sum giving 3∫x ln x | ingredient only |
| 7 | 2f(x) + f(1/(1−x)) = 6x solved on the 3-cycle −1 → 1/2 → 2 | ingredient only (the cycle substitution is a known technique) |
| 8 | log(A/B) vs log A − log B: the length of the set where they are not identical | ingredient only |
| 9 | The relation x = 2[y]+3{y}−a{y}² is a function of x only when it is monotone inside each block (a ≤ 3/2) and the blocks do not overlap (a ≥ 1) | not found |
| 10 | The set where two radical expressions are identical excludes the AM-GM point, so the minimum of x+2500/x moves to the boundary | ingredient only |
| 11 | Domain of √(([x]+6)([x]−1)/log_{1/2}(|x|−3)); the denominator changes sign at |x| = 4 | ingredient only |
| 12 | Range of [6x/(1+x²)] and the points where its limit fails; the trap is the touching points x = ±1, where the limit exists | not found (a first design, [x²]−[x]², was dropped after the search showed it is a past JEE function) |
| 13 | Least value of max{f(|x|), slanting line}; the minimum sits at a crossing on the left arc | not found |
| 14 | lim((4|x|)ⁿ + |x−5|ⁿ)^{1/n} = max of two moduli; range, then the reciprocal | ingredient only |
| 15 | f∘g where the inner g skips a band of f's domain, so the composite's range has a gap | not found |
| 16 | Unknown in the left piece fixed by existence of the limit at the junction, then the range of the piecewise function | ingredient only |
| 17 | Domain of (f+g)/(f−g); the extraneous root of √(2x+3) = x must not be removed | not found |
| 18 | f/g + g/f removes the zeros of both functions; the radical's end point becomes open | not found |
| 19 | Ordered point maps (stretch, reflection, translation) of y = x²; triangle formed by the vertex and the x-intercepts | not found |
| 20 | g = |f(|x|)| with f obtained from |x| by transformations; area between the W graph and y = 6 | not found |
| 21 | Integers missing from the range of [1/({x}−1/4)] | not found |
| 22 | Least a for which 2x²−3|x−a| is one-one on [0,∞) (moving kink vs turning point) | not found |
| 23 | Functions A→B with no fixed point on B: a one-one restriction to B vs onto; p − q | not found |
| 24 | Exactly one real root of 2x³+6x²+λx+27 = 0: a larger set than the one-one range λ ≥ 6; boundary from f = f′ = 0 | not found |
| 25 | f(1) < f(2) combined with the onto/into split by swap symmetry | not found |
| 26 | Composite of piecewise functions: crossing the outer jump vs touching it vs an inner jump that heals | not found |
| 27 | A decreasing cubic conjugate to u ↦ −4u³; f = f⁻¹ has a 2-cycle off y = x | ingredient only |
| 28 | f + 2f⁻¹ = 3x for a polynomial f; substituting x = f(t) and counting degrees forces f to be linear | not found |
| 29 | Two loops between the odd cubic (x³+x)/5 and its inverse, by symmetry about y = x | ingredient only |
| 30 | Odd part of a periodic function given through {x/3} | not found |
| 31 | (x+1)f(x) odd gives E = −xO; a symmetric integral gives E | not found |
| 32 | Even and odd parts with periods 6 and 8; f(x)f(−x) = g²−h² has period 12, less than f's 24 | ingredient only |
| 33 | f(x+1) = (f(x)−3)/(f(x)+1): the map has order 3, so period 3, and the map must be run backwards | ingredient only (a published problem of the same family, a Möbius-type recurrence asking for the period, exists; this one differs in cycle length and asks for a value) |
| 34 | sin²(x°) + |cos θ_x|, with θ_x from an arc of a circle of radius 40/π; the period in degrees is 360 | ingredient only |
| 35 | Compound-angle collapse to 3 sin(πx/10) sin(πx/30); true period 30, not the LCM 60 | ingredient only |
| 36 | 15x(x²+1)/(4x⁴+17x²+4) → 15u/(4u²+9) on |u| ≥ 2; the AM-GM point lies outside | ingredient only |
| 37 | Least value of x + a/x on [1,2] is 9/5; the critical point lies outside the interval (trap answer 0.81) | ingredient only |

**Flagged as closest to standard exercises:**
- Q7: the 3-cycle substitution is a known technique.
- Q33: the same family as a known Möbius-recurrence period problem.
- Q37: x + a/x on an interval is a standard exercise.
- Q8, Q17 and Q18: routine domain work.

These are the ones to replace if you want stricter originality.

## Difficulty
- Distribution on the calibrated scale: **Level 2: 10, Level 3: 27**. Every question is rated at its target level, so none is one level off.
- **Weighted index: about 2.73.** The paper has no equivalence-relation or multi-correct adjustments. See `Function_difficulty.xlsx`.
- **Consistency pass.** These were read side by side with their neighbours; no question was moved.
  - **Level 3 that could be read as level 2:**
    - Q8: sign scheme only; Low confidence.
    - Q11, Q16, Q22 and Q37: Medium confidence.
  - **Level 2 at the top of the level:** Q26 (several traps) and Q20.

## Problems found while verifying
- **Q12:** the first design was a known past-JEE function. It was replaced before writing.
- **Q31:** the first draft gave f(x) − f(−x) directly, which made it a two-line substitution, too easy for level 3. The second condition is now a symmetric integral.
- **Q28:** the relation alone allows f = x and every f = 2x + b. The condition f(1) = 7 in the stem is what makes f unique.
- **Q21 and Q24:** the search tool's own working was wrong (it claimed 1 is missing from Q21's range and gave about −31.49 for Q24). The code checks and hand checks confirm −6 and −31.5.
- **Wording changes for the build's lint.** Q11, Q15, Q23, Q25, Q27 and Q29 were reworded so that the domain lint did not take a set or a count for a function without a domain. The meaning did not change, and each change is recorded in that question's `stem_review`.

## Rows whose concepts were hard to combine naturally
- **Q2 (four concepts):** the Cauchy equation, the one-one test, the inverse and f = f⁻¹ are chained in sequence: the equation gives f, f gives h, monotonicity of h gives h⁻¹, and the reduction to h(x) = x gives the root. It reads as one situation, but the link is sequential. The answer is an option-statement ("exactly one solution, in (3,4)") because the root is not a closed form.
- **Q34 (fundamental period with degree/radian measure):** the angle-measure concept enters through the conversion of degrees and arc length. It is natural, but light.

## Notes
- The Hindi is my own translation, using the terms in `hindi_terms.md`. Please review these specialised terms:
  - एकैकी / आच्छादक (one-one / onto)
  - प्रतिलोम फलन (inverse function)
  - मूल आवर्तकाल (fundamental period)
  - सम / विषम फलन (even / odd function)
- The stem review is a self-check. An independent reader may still find things.
- `_source/` holds `blueprint.json`, `meta.json` and `q01.json`-`q37.json`, so any question can be edited and the paper rebuilt with `build_paper.py`.
