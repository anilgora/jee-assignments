# Parabola: generation report

Blueprint: `qp_blueprints/Parabola.xlsx`. There is no `Parabola_config.xlsx`, so the check ran without `--config`.
This scheduled run made the paper on 19-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy and mpmath were missing for `python3` (Python 3.11). I installed them with `python3 -m pip install pandas openpyxl sympy mpmath`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- `build_paper.py --blueprint` passed on the first build with **no errors and no warnings**. No script was edited and no check was weakened.
- I rendered and looked at page 1 of each of the three PDFs and page 13 of the full-solutions PDF (Q13). The Hindi is shaped and the fractions display in 2D. This paper has no paragraph question.

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the blueprint has only Single Correct and Numerical types and nothing above level 3.
- **Paper:** 20 questions: 3 Single Correct (Q1-Q3), then 17 Numerical (Q4-Q20).
- **Reorder (`--reorder`), old -> new:** 376->1, 380->2, 384->3, 371->4, 372->5, 373->6, 374->7, 375->8, 377->9, 378->10, 379->11, 381->12, 382->13, 383->14, 385->15, 386->16, 387->17, 388->18, 389->19, 390->20.
- **Answer Plans:** the blueprint had none, so the script drew all 20. Every answer matches its plan; the build checks this.
  - Q1 Option C, Q2 Option A, Q3 Option B, Q4 positive 2-digit integer, Q5 negative decimal, Q6 negative integer, Q7 positive decimal, Q8 decimal between 0 and 1, Q9 positive 3-digit integer, Q10 negative integer, Q11 positive 2-digit integer, Q12 negative decimal, Q13 decimal between 0 and 1, Q14 positive 3-digit integer, Q15 positive decimal, Q16 positive decimal, Q17 negative decimal, Q18 positive 2-digit integer, Q19 positive 3-digit integer, Q20 negative integer.
- **Cells containing ";":** none.
- **Warnings.** These are recorded, not fixed, because the blueprint is your decision. There were no errors, and the blueprint file was not edited.
  - Concepts repeated across rows (each use has a different mechanism):
    - "Basic elements of the standard parabola: focus, directrix, axis, latus rectum": Q4, Q5, Q6, Q7.
    - "Area of a parabolic segment (Archimedes' 2/3 result)": Q4, Q9.
    - "Tangent to the parabola: point, slope and parametric forms": Q2, Q11, Q12, Q13, Q19.
    - "Normal to the parabola: point, slope and parametric forms": Q3, Q14.
    - "Normals to Parabola: Maximum of 3 co-normal points, ...": Q15, Q16.

## Answers
| Q | Type | Answer |
|---|---|---|
| 1 | SCQ | (C) -2/3 |
| 2 | SCQ | (A) 12√5 |
| 3 | SCQ | (B) 25 |
| 4 | Numerical | 72 |
| 5 | Numerical | -1.50 |
| 6 | Numerical | -6 |
| 7 | Numerical | 9.50 |
| 8 | Numerical | 0.75 |
| 9 | Numerical | 192 |
| 10 | Numerical | -2 |
| 11 | Numerical | 90 |
| 12 | Numerical | -0.75 |
| 13 | Numerical | 0.60 |
| 14 | Numerical | 180 |
| 15 | Numerical | 10.50 |
| 16 | Numerical | 8.75 |
| 17 | Numerical | -0.50 |
| 18 | Numerical | 80 |
| 19 | Numerical | 250 |
| 20 | Numerical | -4 |

Every answer is exact. None needs rounding.

## How the answers were checked
Every answer was recomputed with sympy, exactly, and checked again by an independent numerical or direct route:
- Q1: minimum of x_Q(t) on a grid of 600,001 points (-0.6666667 at t = ±1.414), and the sympy intersection at t = √2.
- Q2: the circle meets the parabola only at x = 12 (x = -48 rejected), and there the radius slope equals the tangent slope.
- Q3: brute-force nearest point on a fine grid gives (4, 4) at distance 11.1803 = 5√5.
- Q4: rotated-frame integral (72), plus a grid count of the region (71.99).
- Q6: sympy solution of the system; the root x = -1/3 gives no real point.
- Q9: numerical minimisation of the segment area over the chord slope (minimum 192.0 at m = 1).
- Q10: the integer members found by direct evaluation at each integer.
- Q12: direct integration of the region between the two tangents and the arc (500).
- Q13: sympy solve of both tangency conditions in (α, θ) gives only α = 5.
- Q15: the three normals at the feet t = (1 ± √17)/2 and t = -1 all pass through (21/2, 6).
- Q16: numerical root counts at h = 8.74 (one root) and h = 8.76 (three roots).
- Q19: the reflected direction, computed as a vector, points at the focus. The second reflection is parallel to the axis. N = (21, 6), and the shoelace area is 250.
- Q5, Q7, Q8, Q11, Q14, Q17, Q18, Q20: exact sympy checks of each step: intersections, factorisations and tangency discriminants equal to 0.

## Originality report
Every question was built on a named mechanism and checked against `known_skeletons.md`. Each mechanism was then web-searched (WebSearch was available in this run). Perfect novelty cannot be guaranteed. If you recognise a question, tell me which one.

| Q | Mechanism | Web check | Standard ingredient |
|---|---|---|---|
| 1 | The line from the ellipse vertex A(-2,0) through a parabola point meets the ellipse again. tan(θ/2) of Q equals twice the slope, which is bounded by AM-GM over the parabola parameter. | not found | eccentric angle, AM-GM |
| 2 | A circle centred on the axis behind the vertex cuts the parabola orthogonally exactly where the parabola's tangent passes through the centre. | found: redesigned (see below) | parametric tangent |
| 3 | Nearest point to a point on the directrix. The normal cubic t³+3t-14 has one real root. The triangle with the focus. | ingredient only ("shortest distance by normals") | normal through a point |
| 4 | A tilted parabola given by focus and directrix, cut by a line parallel to the directrix. Only two distances matter, then Archimedes. | not found | Archimedes 2/3 |
| 5 | A parabola built from an ellipse (vertex at its centre, focus at a focus). PS1 - PS2 uses both focal-distance properties. | not found | focal distances |
| 6 | A hyperbola fixed by e and the distance between its directrices. The parabola uses one focus and the other directrix. One root is spurious and the symmetric points are counted twice. | not found | hyperbola elements |
| 7 | A circle on the vertex-to-latus-rectum-end segment as diameter. Product of its y-intercepts (power of O). | not found | diametric circle |
| 8 | A vertical-axis parabola through three special points of a shifted ellipse. Symmetry makes the minor-axis end the vertex. | not found | shifted forms |
| 9 | Least-area chord through an interior point. Area = (y2-y1)³/72 is minimised, giving the chord bisected at A. | not found | chord with midpoint, Archimedes |
| 10 | A point on a line, inside the ellipse and outside the parabola. The set is two intervals, with a gap that removes 0. | ingredient only ("range of λ for a point inside a conic" is a common type) | S1 sign tests |
| 11 | Common tangent of y²=24x and y=x³ (s⁵ = -1), then the meet-again point on the cubic. | not found | c = a/m |
| 12 | Area between the parabola and the tangents at the ends of a focal chord, a²|Δt|³/6, used in reverse to find the slope. | not found | tangent triangle, t1t2 = -1 (skeleton ingredients used only as steps) |
| 13 | The tangent and the normal at the same point of an ellipse both touch the parabola. That point is forced onto the directrix, so the directrix is a latus-rectum line of the ellipse. | found: redesigned (see below) | perpendicular tangents meet on the directrix |
| 14 | The normal at a cubic's inflection point is a parabola normal (t = 1/2). Follow it to the meet-again point and take triangle OPQ. | not found | t' = -t - 2/t (skeleton, used only as a step) |
| 15 | The tangents at two co-normal feet meet at a given T. T fixes t1t2 and t1+t2, and Vieta on the co-normal cubic then gives N. | ingredient only (the tangent-triangle-of-co-normal-feet configuration is published, asking for the centroid) | co-normal cubic |
| 16 | Points (h, h-2) on a line through (2a, 0). Three distinct roots of t³ - ut - u ⇔ u²(1 - 4u/27) < 0. | ingredient only ("points on the axis with three normals" is standard) | cubic root analysis |
| 17 | A point fixed by perpendicular tangents (on the directrix) and by the direction of its chord of contact. | not found | director circle = directrix |
| 18 | A point whose polar for the ellipse touches the parabola and whose polar for the parabola touches the ellipse. A spurious root is rejected. | ingredient only ("locus of the pole of a tangent" exercises) | tangency conditions |
| 19 | A ray reflected twice in a parabolic mirror. PQ is a focal chord, so the tangents and normals at P and Q form a rectangle. | not found | reflection property |
| 20 | A parabola touches an ellipse along a common normal. The parabola's constant subnormal is set equal to the ellipse's e²x1 normal intercept. | found: redesigned (see below) | subnormal = 2a, normal intercept e²x1 |

**Redesigns forced by the originality check:**
- **Q2, first design:** the angle between the parabola and a circle centred at the focus (tan = |t|). It has the same core as JEE Main 2018 (the circle through P and the axis intercepts of the tangent and normal at P is centred at the focus, and asks for tan of angle CPB). Redesigned.
- **Q13, first design:** a line tangent to the parabola and normal to an ellipse, asking for its slope. The search found a published problem with the same core: the tangent to y²=4x at (t²,2t) is the normal to 4x²+5y²=20. Redesigned.
- **Q15, first design:** the area of the triangle formed by the tangents at the three co-normal feet. The same configuration appears in published questions (asking for its centroid). Redesigned.
- **Q20, first design:** the common tangents of an ellipse and a parabola meet the x-axis at (α, 0). This is essentially JEE Advanced 2023 P1 Q2 with new numbers. Redesigned.

Note on the web checks: several search summaries added their own working, and one (Q2) wrongly concluded that no orthogonal circle exists. I re-verified Q2 independently: the radius slope 1/2 equals the parabola's tangent slope at (12, 12).

## Levels
- **Distribution:** level 2: 7 questions (Q2, Q3, Q5, Q7, Q8, Q17, Q20); level 3: 13 questions (Q1, Q4, Q6, Q9-Q16, Q18, Q19).
- **Weighted index:** about **2.66** (SCQ 3 marks, Numerical 4 marks). There is no equivalence-relation adjustment and no MCQ floor in this paper.
- **One level off target:** none. Every question is rated at its blueprint target level (High or Medium confidence).
- The calibrated consistency pass was done. The hardest level-2 questions (Q3, Q17) were read beside the easiest level-3 questions (Q10, Q15). Q10 stays at 3 because of its irrational bounds and the excluded integer, with no options. Q17 stays at 2 because it applies two standard results once each.
- Possible borderline: Q13 (rated 3) could read as 4 if the perpendicular-tangents idea is judged unfamiliar.

## Rows whose concepts were hard to combine naturally
- **Q10** (position w.r.t. parabola + ellipse). Position questions are inherently of the "range of λ" type. The new element is the gap at λ = 0. The ingredient is standard.
- **Q16** (co-normals + roots of a cubic by derivative). The pairing is natural, but "condition for three normals" is a well-known topic. The new element is a line through (2a, 0), which puts the parameter in two coefficients.
- **Q20** (miscellaneous properties of parabola + ellipse). The phrase is broad. I used the constant subnormal of the parabola and the e²x1 normal intercept of the ellipse. A student may also solve it by a discriminant.

## Stem review
`review_stems.py` was run and every English stem was read as a student would read it. The review is recorded in each question's `stem_review` field. Changes made:
- Q7: L is now "in the first quadrant".
- Q8: "upper end" of the minor axis is now stated.
- Q16: the line's name was removed.
- Q1: the vertex exclusion was dropped.

The review is a self-check, so an independent reader may still find something. The Hindi is my own translation; please review the specialised terms.

## Files
- `Parabola_Shortened_Solutions.docx`, `Parabola_Full_Solutions.docx`
- `Parabola_Questions_EN_HI.pdf`, `Parabola_Questions_and_Shortened_Solutions.pdf`, `Parabola_Questions_and_Full_Solutions.pdf`
- `Parabola_difficulty.xlsx` (internal)
- `_source/`: `blueprint.json`, `meta.json`, `q01.json`-`q20.json`, for later fixes and rebuilds.
