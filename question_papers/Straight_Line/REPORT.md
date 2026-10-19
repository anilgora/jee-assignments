# Straight_Line: generation report

Blueprint: `qp_blueprints/Straight_Line.xlsx`. There is no `Straight_Line_config.xlsx`, so the check ran without `--config`.
This scheduled run made the paper on 19-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy, mpmath and python-docx were missing for `python3`. I installed them with `python3 -m pip install pandas openpyxl sympy mpmath python-docx`. (Plain `pip` installs into a different Python, so it did not help.)
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- `build_paper.py --blueprint` passed with **no errors and no warnings**. The first full build gave one PDF warning: a "✓" character in the Q28 solution had no glyph. I replaced it with words and rebuilt. No script was edited and no check was weakened.
- I rendered page 1 of each of the three PDFs and looked at them. The Hindi is shaped and the equations are typeset in 2D. This paper has no paragraph question.

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the blueprint has only Single Correct and Numerical types and nothing above level 3.
- **Paper:** 31 questions (blueprint Sr No 299-329): 7 Single Correct (Q1-Q7), then 24 Numerical (Q8-Q31).
- **Reorder (`--reorder`):** the rows were not in type order, so they were renumbered (old Sr No -> new Q):
  304->1, 309->2, 310->3, 314->4, 317->5, 319->6, 324->7,
  299->8, 300->9, 301->10, 302->11, 303->12, 305->13, 306->14, 307->15, 308->16, 311->17, 312->18, 313->19, 315->20, 316->21, 318->22, 320->23, 321->24, 322->25, 323->26, 325->27, 326->28, 327->29, 328->30, 329->31.
- **Answer Plans:** the blueprint had none, so the script drew all 31. Every answer matches its plan, and the build checks this.
  - SCQ: Q1 C, Q2 A, Q3 B, Q4 D, Q5 A, Q6 B, Q7 D.
  - Numerical: Q8 negative integer; Q9 positive 2-digit integer; Q10 negative decimal; Q11 decimal between 0 and 1; Q12 positive 3-digit integer; Q13 positive decimal; Q14 positive decimal; Q15 negative decimal; Q16 positive 2-digit integer; Q17 positive 3-digit integer; Q18 negative integer; Q19 decimal between 0 and 1; Q20 negative integer; Q21 negative decimal; Q22 positive 3-digit integer; Q23 decimal between 0 and 1; Q24 positive decimal; Q25 positive 2-digit integer; Q26 positive decimal; Q27 negative decimal; Q28 negative integer; Q29 positive 2-digit integer; Q30 decimal between 0 and 1; Q31 positive 3-digit integer.
- **Cells containing ";":** six blueprint rows (rows 3, 8, 15, 16, 28 and 29 as numbered by the check). There is no config, so each cell was kept as **one** concept, as the run instructions say. These are names such as "Image of a line in a line; reflection of a light ray" and "Angle between the lines of a pair; parallel and perpendicular conditions", which read as single concepts.
- **Warnings.** I recorded these and did not fix them, because the blueprint is your decision. There were no errors, and the blueprint file was not edited.
  - Some rows list more than two concepts, which is unusual for the Main pattern: Q9 has 4; Q19, Q24 and Q27 have 3. Each was kept as given, and every question uses all of its concepts.
  - Many concepts repeat across rows, as expected in a single-chapter paper of 31 questions. Examples: "Locus based questions" (Q1, Q9, Q12, Q13); "Four points (centroid, incentre, ...)" (Q9, Q10, Q11); "Angle bisectors" and "Angle Bisector Identification" (Q6, Q23, Q24); "Optimisation on a line" (Q19, Q25, Q26); "Pair of straight lines ... component slopes" and "General second-degree equation ... pair of lines" (Q7, Q27, Q29, Q30). Each use has a different mechanism, and no setup is reused.

## Answers
| Q | Type | Answer | Level (target) |
|---|---|---|---|
| 1 | SCQ | (C) | 2 (2) |
| 2 | SCQ | (A) | 3 (3) |
| 3 | SCQ | (B) | 2 (2) |
| 4 | SCQ | (D) | 2 (2) |
| 5 | SCQ | (A) | 2 (2) |
| 6 | SCQ | (B) | 3 (3) |
| 7 | SCQ | (D) | 2 (2) |
| 8 | Num | -4 | 3 (3) |
| 9 | Num | 12 | 3 (3) |
| 10 | Num | -3.75 | 3 (3) |
| 11 | Num | 0.56 | 3 (3) |
| 12 | Num | 120 | 2 (2) |
| 13 | Num | 22.5 | 3 (3) |
| 14 | Num | 5.5 | 2 (2) |
| 15 | Num | -2.5 | 3 (3) |
| 16 | Num | 10 | 2 (2) |
| 17 | Num | 137 | 2 (2) |
| 18 | Num | -4 | 3 (3) |
| 19 | Num | 0.75 | 3 (3) |
| 20 | Num | -5 | 3 (3) |
| 21 | Num | -0.75 | 3 (3) |
| 22 | Num | 300 | 2 (2) |
| 23 | Num | 0.25 | 3 (3) |
| 24 | Num | 1.5 | 3 (3) |
| 25 | Num | 42 | 3 (3) |
| 26 | Num | 5.25 | 2 (2) |
| 27 | Num | -1.75 | 3 (3) |
| 28 | Num | -7 | 2 (2) |
| 29 | Num | 14 | 3 (3) |
| 30 | Num | 0.25 | 3 (3) |
| 31 | Num | 135 | 2 (2) |

I recomputed every answer in Python with sympy/mpmath, separately from the written solutions. Where possible I also checked it a second way, numerically:
- Q3: sampled the interval length (2.2361 = √5).
- Q9: random sampling of C on the locus (maximum 12.000).
- Q11: computed S, H and both circumradii from coordinates (ratio 0.5600).
- Q12: solved the two circle equations (common points (100,75) and (28,-21)).
- Q17: brute-force lattice count (137).
- Q18: all four slopes found and summed (-4).
- Q19: grid search over P and Q (minimum 10 at P = (2.5,0), Q ≈ (4.86,3.14)).
- Q20: the fixed point (5,-10) checked on three members of the family.
- Q25 and Q26: fine 1-D searches over the line or graph.
- Q27: both (λ, μ) solutions and the OA·OB = 0 check.
- Q29: Δ checked for every k with |k| ≤ 10.
- Q30: the intersection points found and their slopes (±0.7706) compared.

## Level distribution and index
- Level 2: 13 questions (Q1, Q3, Q4, Q5, Q7, Q12, Q14, Q16, Q17, Q22, Q26, Q28, Q31). Level 3: 18 questions (Q2, Q6, Q8, Q9, Q10, Q11, Q13, Q15, Q18, Q19, Q20, Q21, Q23, Q24, Q25, Q27, Q29, Q30).
- Marks-weighted index (SCQ 3 marks, Numerical 4 marks): **2.60**. No question is about equivalence relations, and there is no MCQ, so neither adjustment applies.
- **No question is one level off its target.** Every rated level equals the blueprint level.
- **Consistency pass.** I sorted the questions by level and compared neighbours.
  - Q21 (shift of origin, then the foci) and Q30 (homogenisation with a slope-sum condition) are the easiest Level 3s and are borderline 2/3. I rated them with **Low** confidence.
  - Q17 (a lattice count with 19 rows) is the hardest Level 2, because of its precision risk.
  - The anchor bank has only two Straight Line questions (2021-P1-Q9 and Q10, both question-stem parts), so most ratings lean on circle and conic anchors. Most are Medium confidence.

## Originality report
I web-checked every question with web search, searching its distinctive structure in words and symbols. Perfect novelty cannot be guaranteed, so please tell me if you recognise any question.

| Q | Mechanism | Web check | Standard ingredient |
|---|---|---|---|
| 1 | Circle on OP as diameter touches x+y=4, so OP = distance to x+y=8: a parabola with focus O and an oblique axis. | not found | focus-directrix definition |
| 2 | Two parallel tangents (one not normalised) give r and the mid-parallel; an x-chord gives two circles; "meets the y-axis" picks one. | ingredient only | chord length 2√(r²−d²) |
| 3 | Line x + t y = t²: the side test becomes a product of two quadratics in t; the two intervals have total length √5. | not found | side-of-line sign test |
| 4 | A plane mirror locates the second focus; the reflection property is used backwards to find the contact point; e = 3/5. | ingredient only | **yes**: the reflection property of the ellipse |
| 5 | The rotation angle is recovered from a point whose coordinates swap, (2,3) -> (3,2); then the line y = x is transformed. | not found | rotation formulas |
| 6 | Four centres of radius-7 circles touching two lines; acute-bisector identification plus a side condition picks one; the options are the four candidates. | not found | acute-bisector sign test |
| 7 | Δ = 0 gives two values of α; the intersection on the y-axis selects one; then the area with the x-axis. | not found | pair-of-lines condition |
| 8 | The harmonic pair's ratio is fixed by the diametric circle passing through O (OP·OQ = 0, i.e. λ = OA/OB). | ingredient only | **yes**: the Apollonius circle |
| 9 | The bisector feet D, E at a moving vertex are fixed harmonic conjugates; the centroid traces a circle; maximum area of DEG. | not found | bisector theorem |
| 10 | The pair is fixed by an angle of π/4 with h > 0; then the orthocentre of the triangle with x + 3y + 2 = 0. | **found: redesigned** (see below) | **yes**: orthocentre of a pair-and-line triangle is a standard exercise type |
| 11 | R(HBC)/R(SBC) = 2cos A, a hidden invariant that collapses a heavy coordinate computation. | ingredient only | R(HBC) = R |
| 12 | Midpoint locus (circle on OP) and feet locus (circle on PQ) share the chord P to the foot of P on OQ. | not found | both loci are standard |
| 13 | Tangent to an oblique line plus a fixed x-chord: d₁² − d₂² = const, always a rectangular hyperbola. | ingredient only | **yes**: the axis-parallel version x² − y² = c² is standard |
| 14 | L is the mirror image of L₂ in L₁: the pair angle tan θ = 1/7 feeds the angle equation; the root m = 2 is excluded. | not found | angle formulas |
| 15 | The cutting angle π/3 becomes d = r cos(π/3); it chooses between two slopes from a 45° condition. | not found | angle between two lines |
| 16 | A ray point in parametric form, equidistant from its start and from a line: a linear equation in r. | not found | parametric form |
| 17 | Lattice count in the strip 12 < 3x + 4y < 62 (far side of the line, distance < 10), positive coordinates. | not found | none beyond the definitions |
| 18 | Variable mirror y = mx; the image circle touches the x-axis; two quadratics in m; Vieta sum −4. | not found | image formula |
| 19 | Two-mirror shortest path (x-axis, then x + y = 8); the last leg is the image line; slope 3/4. | **found: redesigned** (see below) | **yes**: reflection method for PA + PB |
| 20 | Circles through O and the chord cut by a pencil of lines all pass through the fixed point (5,−10). | not found | S + tL family; power of a point |
| 21 | The new origin is fixed by "no X term and no constant" (a vertex of the ellipse); the sign of the Y coefficient selects it; slope to a focus. | not found | shifting of origin |
| 22 | 23x² + 72xy + 2y² = 1250 with tan 2θ = 24/7: 50X² − 25Y² = 1250; (2c)² = 300. | not found | **yes**: rotation to remove xy is a textbook routine (new coefficients) |
| 23 | All circles touching three lines (incircle and three excircles); ratio of the smallest to the largest radius. | ingredient only | in/exradius formulas |
| 24 | A non-homogeneous pair: shift to the intersection, apply the pair-bisector formula, identify the acute bisector. | not found | pair-bisector formula |
| 25 | The PA + PB minimiser is the contact point of the confocal ellipse; b² from 2a = √58 (or b² = d_A d_B). | ingredient only | **yes**: reflect A to minimise PA + PB (known skeleton, used as a step) |
| 26 | Reflection minimisation on the V-graph y = \|x−2\|: each ray separately, then compare. | not found | **yes**: reflect to minimise PA + PB (used as a step) |
| 27 | Unknown λ, μ fixed by Δ = 0 and the homogenised right angle at O; the quadrant of the vertex selects the solution. | ingredient only | **yes**: "x + y = k meets a pair, ∠AOB = 90°" exercises exist |
| 28 | Perpendicular pair with one bisector through (1,2): the bisector formula used backwards. | ingredient only | **yes**: both formulas are textbook |
| 29 | Count the integers k with \|k\| ≤ 10 giving a hyperbola, removing the degenerate k = 3, −7 (Δ = 0). | not found | h² − ab classification |
| 30 | Homogenisation with a chord through (0,2); the slopes of OA and OB sum to zero, so the xy coefficient vanishes. | not found | homogenisation |
| 31 | The third side is recovered from the given centroid (8,9); area 135. | ingredient only | **yes**: the centroid formula for a pair-and-line triangle (used inversely) |

## Problems found while verifying
- **Q10 redesigned after the web check.** The first design fixed h in 6x² + 2hxy − y² = 0, which gives the pair 6x² + xy − y² = 0. That exact pair appears in a published problem: the orthocentre of the triangle formed by x + 3y = 10 and 6x² + xy − y² = 0 (Zigya / Getmarks). I replaced it with 3x² + 2hxy + 2y² = 0 (h > 0, so h = 7/2) and the line x + 3y + 2 = 0. I chose the line so that no angle is a right angle, so the orthocentre is not a vertex.
- **Q19 redesigned after the web check.** The first design reflected in the x-axis and in y = x. That is the same pair of mirrors as Putnam 1998 (the minimum perimeter PQ + QR + RP with Q on the x-axis and R on y = x). I replaced the second mirror with x + y = 8 and used the points A(1,2), B(2,1).
- **The web search assistant made three errors that I checked and rejected.** In each case my answer stands:
  - Q18: it reported that one case has no real slopes. In fact both quadratics have a negative product of roots, so all four slopes are real; the code confirms this.
  - Q24: it reported the acute bisector as 2x − 6y + 7 = 0. It had not made the constants positive before the sign test. The lines have slopes 7 and −1, the acute angle is 53.13°, and its bisector has slope −3.
  - Q29: it stated that infinitely many k work. The stem restricts to |k| ≤ 10.
- **Uniqueness conditions added to stems:**
  - Q1: P ≠ O.
  - Q2: "meets the y-axis".
  - Q5: an anticlockwise rotation.
  - Q14: "different from L₂".
  - Q15: the angle between a line and a circle is defined.
  - Q16: P lies on the ray.
  - Q20: λ = 4 is excluded, since that line passes through O.
  - Q21: the sign of the Y coefficient.
  - Q27: the vertex lies in the fourth quadrant.
  - Q29: a pair of lines is not counted as a hyperbola.
- The stem review is a self-check; an independent reader may still find things.

## Rows whose concepts were hard to combine naturally
- **Q9 (four concepts: harmonic conjugate + triangle centre + area + locus):** all four are used in one chain. The bisector feet are harmonic conjugates, C's locus is the circle on DE, the centroid's locus is scaled from it, and the area of DEG is maximised. The centroid is the least natural ingredient.
- **Q21 (shifting of origin + shifted ellipse):** shifting to the centre is too routine, so the new origin is fixed at a vertex. The final question (the slope from the new origin to a focus) is a little artificial.
- **Q17 (position + distance):** the natural combination is a lattice count. It is mechanical rather than conceptual.
- **Q11 (four points + circumradius):** the circumcentre appears in both concepts. I used the orthocentre as well, so that "four points" contributes something separate.

The Hindi is my own translation. Please review the specialised terms: प्रसंवादी संयुग्मी (harmonic conjugate), नाभिलम्ब (latus rectum), लम्बकेन्द्र (orthocentre), परित्रिज्या (circumradius), and प्रतिबिम्ब (image).
