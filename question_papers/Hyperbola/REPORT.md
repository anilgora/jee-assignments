# Hyperbola: generation report

Blueprint: `qp_blueprints/Hyperbola.xlsx`. There is no `Hyperbola_config.xlsx`, so the check ran without `--config`.
This scheduled run generated the paper on 19-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy and mpmath were missing for `python3`. They were installed with `python3 -m pip install pandas openpyxl sympy mpmath`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- `build_paper.py --blueprint` passed with **no errors and no warnings**. No script was edited and no check was weakened.
- Page 1 of each of the three PDFs was rendered and checked. The Hindi is shaped and the equations (fractions, square roots) are 2D. This paper has no paragraph question.
- **How the questions were written.** I designed all 18 mechanisms and their numbers myself and checked each answer numerically. Three parallel writers then turned the designs into question files (Q1-6, Q7-12, Q13-18).
- **Checks after writing.** Each writer re-verified its answers with a separate sympy/mpmath script. I then ran the stem review on all 18 questions.
- **Variety.** No hyperbola, ellipse or parabola equation is repeated across questions.

## Blueprint check
- **Pattern:** inferred as **JEE Main**: only Single Correct and Numerical types, nothing above level 3.
- **Paper:** 18 questions: 3 Single Correct (Q1-Q3), then 15 Numerical (Q4-Q18).
- **Reorder (`--reorder`):** the single-correct rows moved to the front. Old -> new:
  421->1, 429->2, 434->3, 417->4, 418->5, 419->6, 420->7, 422->8, 423->9, 424->10, 425->11, 426->12, 427->13, 428->14,
  430->15, 431->16, 432->17, 433->18.
- **Answer Plans:** the blueprint had none, so the script drew all 18:
  Q1 Option C, Q2 Option A, Q3 Option B;
  Q4 positive 2-digit integer, Q5 negative decimal, Q6 negative integer, Q7 positive decimal, Q8 decimal between 0 and 1,
  Q9 positive 3-digit integer, Q10 negative integer, Q11 positive 2-digit integer, Q12 negative decimal, Q13 decimal between 0 and 1,
  Q14 positive 3-digit integer, Q15 positive decimal, Q16 positive decimal, Q17 negative decimal, Q18 positive 2-digit integer.
  Every answer matches its plan; the build checks this.
- **Warnings.** These are recorded, not fixed, because the blueprint is your decision:
  - **Concepts repeated across rows:** this is expected in a one-chapter paper. Each repeat uses a different mechanism.
    - "Basic elements of the standard hyperbola" is in Q4-Q7.
    - "Position of a point wrt a Hyperbola" is in Q9 and Q10.
    - "Tangent and normal for Hyperbola" is in Q1, Q11, Q12 and Q17.
    - "Director circle for Hyperbola" is in Q13 and Q14.
    - "Miscellaneous properties of Hyperbola" is in Q3 and Q18.
  - No cell contains ";". There were no errors. The blueprint file was not edited.

## Answers
Q1 (C) 9(√5−1)/2, Q2 (A) 9, Q3 (B) 16,
Q4 45, Q5 −0.45, Q6 −3, Q7 2.7, Q8 0.25, Q9 112, Q10 −4, Q11 18, Q12 −2.5, Q13 0.5, Q14 120, Q15 2.5, Q16 1.25, Q17 −0.5, Q18 13.

Every answer was computed twice: once by me at design time and once by the writer's own sympy/mpmath script (`_source` does not include these scripts). Where a second route was possible, it was used:
- **Q3:** a dense numerical scan over both branches. The minimum is 16, at the vertex (3, 0).
- **Q8:** a slope scan of both chord lengths. It also finds the cross-branch root m² = 1/44, which the same-branch condition excludes.
- **Q9:** a brute-force lattice count. Columns x = 3…8 contribute 7, 11, 11, 11, 9 and 7 points on each side.
- **Q12:** a full scan of the hyperbola for normals that touch the ellipse. It finds four feet, (±5/2, ±1/2), and only (−5/2, 1/2) is in the second quadrant.
- **Q17:** the reflection was checked by vector reflection about the tangent. The reflected ray points exactly at R.
- **Q18:** the common-tangent equations were solved directly. They give exactly two lines, x ± 3y = 13.
- **Q10, Q11, Q14 and Q15:** root scans and uniqueness checks.

## Originality report
A mechanism was named for each question before it was written, and checked against `known_skeletons.md`. Every question was web-searched (WebSearch, standard mode). No question was found published.
"Ingredient only" means the search found the standard result or technique the question uses, but not the question itself. Novelty cannot be guaranteed; please name any question you recognise.

| Q | Mechanism | Web check |
|---|---|---|
| 1 | Ratio of the intercept triangles cut off by the tangent and by the normal at the same point; reduces to cos⁴θ = sin²θ, a golden-ratio equation | not found |
| 2 | The chord of contact of a given point, re-read as a chord with an unknown mid-point (T = 0 matched with T = S₁) | ingredient only |
| 3 | 9p₁ + p₂ for the focal perpendiculars on a tangent, with p₁p₂ = b²; the ratio p₂/p₁ is confined to (1, 7], so the AM-GM value 6√7 cannot be reached and the minimum 16 is at the vertex | ingredient only (the product property is standard) |
| 4 | The constant of a shifted hyperbola, fixed by the position of a focus (which also forces a vertical transverse axis); rectangle on the ends of the latera recta | ingredient only (the same polynomial with other constants is a textbook exercise) |
| 5 | An ellipse and a hyperbola with common latera recta: this forces e₁e₂ = 1 for every size | not found (closest: 2026-P2-Q13, where reciprocal eccentricities are given, not derived) |
| 6 | The circle on a latus rectum as diameter; for e = 2 it touches the far branch at its vertex | not found |
| 7 | Focus, oblique directrix and one point give e; then a comes from p = a(e²−1)/e; then the directrix spacing 2a/e | ingredient only |
| 8 | A line through the common focus of a confocal ellipse and hyperbola cuts equal chords from both; the same-branch condition picks between the two roots | not found |
| 9 | Lattice points inside an ellipse and on the focal side of a hyperbola; the curve that limits each column switches from H to E | not found |
| 10 | The position test S₁ > 0 applied along a segment, which becomes the range of a quadratic on a restricted interval with a moving vertex | not found |
| 11 | Normals of a hyperbola that touch a parabola; the tangency condition forces cos θ < 0, so only the far (left) branch contributes | not found |
| 12 | One line that is a tangent to an ellipse and a normal to a hyperbola; the foot of the normal is recovered | not found |
| 13 | Point fixed by perpendicular tangents (director circle) and a given line; the tangent slopes come from the slope quadratic | ingredient only |
| 14 | Double orthoptic condition: the common points of the director circles of an ellipse and a shifted hyperbola, then the area of the kite | not found |
| 15 | The pairs of tangents from one point to an ellipse and to a hyperbola coincide; SS₁ = T² equations compared term by term | not found |
| 16 | Poles of one line with respect to an ellipse and a hyperbola; their separation scales as 1/λ | ingredient only |
| 17 | Point of incidence recovered from a far point on the reflected ray (the line through the other focus), then the tangent's intercept | ingredient only |
| 18 | Ellipse and non-concentric hyperbola with a shared focus; the common tangents come from intersecting the two auxiliary circles | not found |

**Flagged as closest to standard exercises:**
- Q4: shifted hyperbola and latus rectum.
- Q13: director circle with tangent slopes.
- Q16: pole of a line.
- Q2: chord with a given mid-point.

These are the ones to replace if you want stricter originality.

## Difficulty
- Distribution on the calibrated scale: **Level 2: 8, Level 3: 10**. Every question is rated at its target level, so none is one level off.
- **Weighted index: about 2.55.** The paper has no equivalence-relation or multi-correct adjustments. See `Hyperbola_difficulty.xlsx`.
- **Consistency pass.** The hardest level-2 questions (Q10, Q17, Q18) were read beside the easiest level-3 questions (Q5, Q7). No question was moved.
- **Medium confidence:** Q1, Q3, Q5, Q7, Q8, Q10-Q12, Q14, Q15, Q17 and Q18.
  - Q5 and Q7 could be read as level 2.
  - Q18 could be read as level 3 if a student does not use the auxiliary-circle property.

## Problems found while verifying
- **Q3:** the search tool's own working claimed that the minimum is 6b = 6√7, reached by AM-GM. This is wrong: p₂/p₁ never exceeds 7, so equality in AM-GM cannot hold. The true minimum is 16, and 6√7 is kept as the trap option (A).
- **Q2:** one search tool claimed that no tangents can be drawn from (1, ½). This is also wrong: S₁ < 0, and the points of contact (6 ± √10, …) are real and lie on the right branch.
- **Q14:** the first design used the ellipse x²/64 + y²/36 = 1. With that ellipse, the common point (8, 6) is the corner of the rectangle on the axes, where the perpendicular tangents are just x = 8 and y = 6, so the answer could be guessed. The ellipse was changed to x²/75 + y²/25 = 1.
- **Q1:** the first draft wrote "area of" as English text inside the maths, and it appeared in the Hindi as well. The stem now names the areas Δ₁ and Δ₂.
- **Q12:** the solution uses the line-coordinate tangency condition. It shows why the extra algebraic root X = 10/3 is rejected.
- **Q17:** the second intersection of line S′R with H is on the left branch. The stem names the branch in the region x > 0.

## Rows whose concepts were hard to combine naturally
- **Q3 (miscellaneous properties + trigonometric max/min under constraints):**
  - The "trigonometric expression" enters through the parametric form of the perpendicular distances.
  - The constraint is that the eccentric angle keeps p₂/p₁ in (1, 7].
  - The link is real but uses the trigonometry lightly.
- **Q10 (position of a point + range of a quadratic):** natural. The segment makes the restricted interval.

## Notes
- **Hindi.** The Hindi is my own translation, using the terms in `hindi_terms.md`. Please review these specialised terms:
  - नाभिलम्ब (latus rectum)
  - नियता (directrix)
  - ध्रुव / ध्रुवी (pole / polar)
- **Syllabus.** No question or solution uses asymptotes or hyperbolic functions; the build checks this.
- **Stem review.** It is a self-check. An independent reader may still find things.
- **Source files.** `_source/` holds `blueprint.json`, `meta.json` and `q01.json`-`q18.json`, so any question can be edited and the paper rebuilt with `build_paper.py`.
