# Ellipse: generation report

Blueprint: `qp_blueprints/Ellipse.xlsx`. There is no `Ellipse_config.xlsx`, so the check ran without `--config`.
This scheduled run generated the paper on 18-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy and mpmath were missing for `python3`. They were installed with `python3 -m pip install pandas openpyxl sympy mpmath`. Plain `pip` installed them for a different Python, 3.13, so `python3 -m pip` was needed.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- The paper title in `meta.json` is "Ellipse", and the file names use `Ellipse`.
- The build passed on the first full run with no errors and no warnings. No script was edited and no check was weakened.
- Page 1 of each of the three PDFs was rendered and checked. The Hindi is shaped correctly and the equations (fractions, subscripts) are 2D. This paper has no paragraph question.

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the paper has only Single Correct and Numerical types and nothing above level 3.
- **Paper:** 26 questions: 5 Single Correct (Q1-Q5), then 21 Numerical (Q6-Q26).
- **Reorder (`--reorder`):** the single-correct rows moved to the front. Old -> new:
  392->1, 398->2, 400->3, 403->4, 411->5, 391->6, 393->7, 394->8, 395->9, 396->10, 397->11, 399->12, 401->13, 402->14, 404->15,
  405->16, 406->17, 407->18, 408->19, 409->20, 410->21, 412->22, 413->23, 414->24, 415->25, 416->26.
- **Answer Plans:** the blueprint had none, so the script drew all 26:
  Q1 Option C, Q2 Option A, Q3 Option B, Q4 Option D, Q5 Option A;
  Q6 negative integer, Q7 positive 2-digit integer, Q8 negative decimal, Q9 decimal between 0 and 1, Q10 positive 3-digit integer,
  Q11 positive decimal, Q12 positive decimal, Q13 negative decimal, Q14 positive 2-digit integer, Q15 positive 3-digit integer,
  Q16 negative integer, Q17 decimal between 0 and 1, Q18 negative integer, Q19 negative decimal, Q20 positive 3-digit integer,
  Q21 decimal between 0 and 1, Q22 positive decimal, Q23 positive 2-digit integer, Q24 positive decimal, Q25 negative decimal,
  Q26 negative integer. Every answer matches its plan; the build checks this.
- **Warnings.** These are recorded, not fixed, because the blueprint is your decision:
  - **Cell containing ";":** the check reported sheet row 9. That is Q12's concept "Range of a.sin(x) + b.cos(x); maximum and minimum". With no config, it was kept as **one** concept, as instructed. It reads as a single concept.
  - **Three concepts in a Main row:** Q13 (parametric coordinates, tangent and normal, chord with given midpoint). It was kept, and all three concepts are used.
  - **Concepts repeated across rows:** this is expected in a one-chapter paper. Each repeat uses a different mechanism. The check listed 23 repeats, for example "Parametric coordinates for Ellipse" in Q2, Q3, Q11, Q12, Q13 and Q26, and "Tangent and normal for Ellipse" in Q11, Q13, Q17 and Q25.
  - There were no errors. The blueprint file was not edited.

## Answers
Q1 (C) 4/5, Q2 (A) -13, Q3 (B) 12√2, Q4 (D) 4√17/5, Q5 (A) 8√2/3,
Q6 -5, Q7 28, Q8 -4.25, Q9 0.9, Q10 300, Q11 6.25, Q12 8.5, Q13 -0.5, Q14 36, Q15 104, Q16 -2, Q17 0.5, Q18 -30, Q19 -2.4,
Q20 144, Q21 0.4, Q22 6.4, Q23 72, Q24 1.75, Q25 -4.5, Q26 -4.

Each answer was recomputed with sympy or mpmath, separately from the hand solution:
- **Brute-force numerical checks:**
  - Q1: the ratio r/d was checked on five focal chords, including the major axis.
  - Q2: 4000 chords parallel to the line were checked.
  - Q3, Q12 and Q14: dense sweeps of the eccentric angle (Q12 and Q14 used 200000 points).
  - Q7: a sweep over a^2 confirmed the minimum 49 at (28, 21).
  - Q15 and Q16: direct enumeration of the integer points.
- **Symbolic recomputation:**
  - Q4, Q5, Q10 and Q21-Q23: the conics were intersected.
  - Q6, Q7 and Q9: the systems for a, b and e were solved.
  - Q13: the tangent slope, the branch and the normal.
  - Q17: a discriminant condition for b.
  - Q19 and Q20: the slopes were checked against c^2 = a^2 m^2 + b^2.
  - Q24: tan θ came from the second-degree part of SS1 = T^2 and also from Vieta.
  - Q25: the reflection was done as a vector reflected in the normal.
  - Q26: the feet of the perpendiculars were computed directly and their dot product formed.
- All decimal answers are exact to two places; none is rounded.

## Originality report
Each mechanism was named before the question was written and checked against `known_skeletons.md`. Every question was also web-searched in standard mode.
No question was found published. "Ingredient only" means the search found the standard result the question uses, not the question.
Novelty cannot be guaranteed. Please name any question you recognise.

| Q | Mechanism | Web check | Standard ingredient |
|---|---|---|---|
| 1 | Invariant: the circle on any focal chord has radius / (distance of centre from directrix) = e | ingredient only | Parabola analogue (the circle touches the directrix) |
| 2 | The direction of parallel chords fixes α+β; then minimise OP·OQ = 10cos(α-β) - 3 | ingredient only | Sum of eccentric angles is constant for parallel chords |
| 3 | Weighted intercepts 2·OA + 3·OB become 6(sec + cosec); AM-GM applied twice | not found | Tangent intercepts |
| 4 | Chord through a vertex whose midpoint lies on y = x (T = S1 through the vertex) | not found | Chord with a given midpoint |
| 5 | The external point is found from a condition on its own chord of contact | not found | Chord of contact |
| 6 | Ellipse rebuilt from a latus rectum and a line through the centre; the other directrix | not found | Elements of a shifted ellipse |
| 7 | Least AB over ellipses through (4,3): multiply by the constraint, AM-GM, then the foci | ingredient only | Cauchy/AM-GM under a constraint |
| 8 | Focus chosen by distance to the origin, paired with its own directrix | ingredient only | Completing squares (routine L2) |
| 9 | Focus, oblique directrix and major-axis length; e from a quadratic; vertex on the oblique axis | ingredient only | Focus-directrix distance |
| 10 | Parabola and ellipse with a common focus: the common points lie on one line, u = 15 | ingredient only | Common-focus intersection trick |
| 11 | Iteration: each normal's foot gives the next abscissa, so the abscissae form a GP with ratio e^2 | ingredient only | CG = e^2·CN |
| 12 | SP + PM becomes linear in cos and sin through SP = a - ex; range of A cos + B sin | ingredient only | Focal distance a - ex |
| 13 | Tangent parallel to a chord given only by its midpoint; branch choice; then the normal | not found | T = S1, parametric tangent |
| 14 | Base chord given by eccentric angles; far-arc maximum (the near-arc point gives 12, not 36) | ingredient only | Chord formula in eccentric angles |
| 15 | Lattice points between an ellipse and its own auxiliary circle | not found | Position of a point (S1 sign) |
| 16 | The position test is hidden in a focus-directrix inequality PS < e·PN | not found | PS^2 - e^2 PN^2 = (1 - e^2) a^2 S1 |
| 17 | The tangent to y = 2/(1+x^2) also touches an ellipse with unknown b | ingredient only | c^2 = a^2 m^2 + b^2 |
| 18 | Uniqueness of a point on a line, using the director circle as a set | ingredient only | Director circle |
| 19 | Point fixed on a ray by the perpendicular-tangent condition; sum of slopes by Vieta | ingredient only | Director circle, slope quadratic |
| 20 | Triangle cut off on the x-axis by the two tangents from a point | ingredient only | Tangency condition |
| 21 | Midpoint on a diameter (from the slope), intersected with a second line | ingredient only | Diameter of parallel chords |
| 22 | On the polar of an interior Q, the point whose chord of contact is bisected at Q | ingredient only | Pole-polar reciprocity (La Hire) |
| 23 | Both y-intercepts read from SS1 = T^2 cut by x = 0 | ingredient only | Joint equation of the tangent pair |
| 24 | Angle between the tangents from the second-degree part of SS1 = T^2, checked by Vieta | ingredient only | **Standard skeleton with new numbers** |
| 25 | Light path from a focus via the end of the minor axis, through the other focus, then the tangent at the second point | ingredient only | Reflection property |
| 26 | OU·OV for the feet of the focal perpendiculars, via the auxiliary circle | ingredient only | Feet lie on the auxiliary circle |

**Flagged:** Q24 is a routine application of a standard exercise (the angle between the tangents from a point) with new numbers. The level-2, two-concept row ("pair of tangents" plus "tangents from an external point") left little room for anything else.
Q8, Q18 and Q21 are also close to routine; they are level-2 single-concept or near-single-concept rows. If you want stricter originality on such rows, these four are the ones to replace.

**Q4 was tightened after the web check.** The search tool's working pointed out that the major axis is also a chord through (2,0) with its midpoint (the origin) on y = x. "In the first quadrant" was added to the stem so that the chord is unique.

## Difficulty
- Distribution on the calibrated scale: **Level 2: 16, Level 3: 10.** Every question is at its target level, and none is one level off.
- **Weighted index: about 2.38.** There are no equivalence-relation or multi-correct adjustments in this paper. See `Ellipse_difficulty.xlsx`.
- **Consistency pass:**
  - The easiest level-3 questions are Q19 (director circle, then Vieta), Q13 (three standard steps with a branch choice) and Q6 (rebuilding the ellipse from its elements). These could be read as level 2. Their confidence is Medium.
  - The hardest level-2 questions are Q10 (common-focus intersection), Q15 (two-condition lattice count) and Q16 (hidden ellipse). These could be read as level 3.
  - No question was moved.

## Problems found while verifying
- Q4: the chord was not unique (see above). Fixed in the stem before the build.
- Q10 and Q16: two lines of the shortened solutions were rewritten before the build, because they were garbled or clumsy. The answers did not change.
- Q15: the search tool's own count was 106, because it included the boundary of the auxiliary circle. The stem says "strictly", and the direct enumeration gives 104.
- The search tool's summaries sometimes misread the questions (for example, the reciprocal ratio in Q1). Those summaries were ignored; the code checks decide.

## Rows whose concepts were hard to combine naturally
- **Q13 (parametric, tangent and normal, chord with given midpoint):** the three concepts are chained, not fused. The midpoint chord fixes a direction, the parametric tangent gives the point, and the normal gives the answer. It reads as one situation, but the link is sequential.
- **Q10 (ellipse and parabola, focus-directrix with a general axis):** the two curves were given a common focus and parallel oblique directrices, so that both definitions are genuinely needed.

## Notes
- The Hindi is my own translation, using the terms in `hindi_terms.md`. Please review the specialised terms: नाभिलम्ब (latus rectum), नियता (directrix), उत्केन्द्र कोण (eccentric angle), सहायक वृत्त (auxiliary circle), ध्रुवीय रेखा (polar) and स्पर्श जीवा (chord of contact).
- The stem review is a self-check. An independent reader may still find things.
- `_source/` holds `blueprint.json` and `q01.json`-`q26.json` plus `meta.json`, so any question can be edited and the paper rebuilt with `build_paper.py`.
