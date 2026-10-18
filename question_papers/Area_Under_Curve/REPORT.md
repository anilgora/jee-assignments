# Area_Under_Curve: generation report

Blueprint: `qp_blueprints/Area_Under_Curve.xlsx`. There is no `_config.xlsx`, so the check ran without `--config`.
The scheduled run generated this on 18-Oct-2026 with skill `jee-question-paper`, way B (blueprint supplied directly).

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the blueprint has only Single Correct and Numerical types and nothing above level 3. The paper name comes from the file name.
- **Paper:** 21 questions: 6 Single Correct (Q1-Q6), then 15 Numerical (Q7-Q21). This is the blueprint's own mix, kept as given.
- **Reorder (`--reorder`)**, old Sr No -> new Q:
  661->1, 663->2, 669->3, 672->4, 674->5, 677->6, 658->7, 659->8, 660->9, 662->10, 664->11, 665->12, 666->13, 667->14, 668->15, 670->16, 671->17, 673->18, 675->19, 676->20, 678->21.
- **Answer Plans:** the blueprint had none, so the script drew all 21 at random:
  Q1 Option C, Q2 Option A, Q3 Option B, Q4 Option D, Q5 Option A, Q6 Option B, Q7 negative integer, Q8 positive 2-digit integer, Q9 negative decimal, Q10 decimal between 0 and 1, Q11 positive 3-digit integer, Q12 positive decimal, Q13 positive decimal, Q14 negative decimal, Q15 positive 2-digit integer, Q16 positive 3-digit integer, Q17 negative integer, Q18 decimal between 0 and 1, Q19 negative integer, Q20 negative decimal, Q21 positive 3-digit integer. Every answer matches its plan (the build checks this).
- **Warnings (recorded, not fixed; the blueprint is yours):**
  - The concept cells in file rows 1, 2, 3 and 18 (old Sr 658, 659, 660, 675, i.e. new Q7, Q8, Q9, Q19) contain ";": "Area bounded by a curve and the x-axis; handling sign changes". No config was supplied, so each was kept as **one concept**.
  - Q8 (old 659) lists **4 concepts**, and Q9 (old 660) and Q12 (old 665) list **3**, although the Main pattern normally has at most two. Every listed concept was used.
  - Concepts repeated within the paper (the blueprint is a single-chapter paper): "Area bounded by two curves" (Q1, Q5, Q8, Q9, Q10, Q17), "Area obtained by integrating with respect to y" (Q1, Q2, Q9), "Area bounded by a curve and the x-axis; handling sign changes" (Q7, Q8, Q9, Q19), "Area using symmetry of the region" (Q4, Q8, Q12, Q13, Q14), "Area of a region defined by inequalities" (Q11, Q12, Q13), "Area of regions bounded by modulus curves such as |x| + |y| = a" (Q4, Q12, Q18), "Determining a parameter from a given area" (Q6, Q8), "Area computed after shifting the origin" (Q3, Q15), "Areas involving GIF, fractional part or piecewise curves" (Q19, Q20), "Maximum or minimum of an area expressed in terms of a parameter" (Q6, Q21). Each repeat uses a different mechanism and different curves.
- No errors. The blueprint file was not edited.

## Originality report (per question)
Each mechanism was named before the question was written and checked against `known_skeletons.md`. Every question was also web-searched (standard mode).
"not found" = no similar problem turned up; "ingredient only" = only the standard ingredient or method turned up, not this construction.

| Q | Type | Target | Rated | Mechanism | Web check |
|---|---|---|---|---|---|
| Q1 | SCQ | 2 | 2 | two mirror-image logarithmic curves closing a region with the x-axis, where integrating in y turns the region into strips of width 4 - 2^(y+1) (way 5) | not found |
| Q2 | SCQ | 2 | 2 | a curve given only implicitly (y^3 + 3y = 2x) that is a function of y, cut by the chord from O to the point with abscissa 7 (way 5) | not found |
| Q3 | SCQ | 2 | 2 | a curve given as a general second-degree equation xy - 2x - 3y + 2 = 0 that becomes XY = 4 after shifting the origin to (3,2), cut by a line that becomes X + Y = 5 (way 5) | ingredient only |
| Q4 | SCQ | 2 | 2 | the square |x| + |y| <= 2 with the inside of the four-armed parabola region |y| < x^2 removed (way 5) | not found |
| Q5 | SCQ | 2 | 2 | the first step of Archimedes' exhaustion asked as an area question - the leftover between a parabolic segment and its greatest inscribed triangle (way 1, one step of the iteration) | ingredient only |
| Q6 | SCQ | 3 | 3 | one family of chords through an interior point read twice - its least area fixes m0, and a given area fixes the pair m1, m2 symmetric about m0 (way 3: a family fixed by two conditions) | ingredient only |
| Q7 | Numerical | 3 | 3 | the accumulation function g of f is minimised exactly at the end of the region under the axis, so the least value of g equals minus the given area (way 4, hidden link between the signed integral and the area) | not found |
| Q8 | Numerical | 3 | 3 | the parameter of an odd cubic is fixed by a total (unsigned) area across a sign change, and then the area against a line through the origin is read by central symmetry (way 5) | not found |
| Q9 | Numerical | 3 | 3 | the two regions cut off by sin^-1 x and cos^-1 x against the y-axis and against x = 1 compared through their difference, which is the signed integral of the difference (way 5) | ingredient only |
| Q10 | Numerical | 2 | 2 | a line crossing the corner of |x^2 - 2| so that the region between them straddles the point x = sqrt2 where the modulus changes form (way 5) | not found |
| Q11 | Numerical | 2 | 2 | a region squeezed between the W-shaped curve y = x^2 - 2|x| and the V-shaped line pair y = 2|x| + 12 (way 5) | not found |
| Q12 | Numerical | 3 | 3 | the region between the square |x| + |y| = 4 and the curve |x| + |y| + |xy| = 4, which factorises as (1+|x|)(1+|y|) = 5 (way 4, a hidden factorisation) | not found |
| Q13 | Numerical | 3 | 3 | the region common to the insides of two congruent parabolas that are mirror images in y = x, with four corners (two on y = x, two on x + y = -1); the surds of the second pair cancel (way 4, a hidden symmetry) | not found |
| Q14 | Numerical | 2 | 2 | the area between a cubic and its mirror image in the y-axis, which depends only on the odd part of the cubic (way 4, the even part cancels) | not found |
| Q15 | Numerical | 2 | 2 | a general cubic and a line through its point of inflection become an odd cubic and a line through the origin after the shift (way 4, hidden symmetry) | not found |
| Q16 | Numerical | 2 | 2 | a one-parameter family of odd increasing cubics whose fixed points are 0 and +-sqrt k, so that the area with the inverse is linear in k (way 5) | not found |
| Q17 | Numerical | 3 | 3 | a tangent of one parabola (x^2 = -3y) used as a chord of another parabola (y = x^2), with the cut-off area fixing the point of contact (way 5) | not found |
| Q18 | Numerical | 3 | 3 | the square |x| + |y| <= 1 with the double hump |y| < |f(|x|)| removed, where the humps reach the square's sides at (+-1/2, +-1/2) and cover the corners beyond (way 5) | not found |
| Q19 | Numerical | 2 | 2 | the sawtooth with growing amplitude f(x) = [x]{x}, whose pieces flip below the axis for negative x, with the lower limit recovered from a total area (way 5) | not found |
| Q20 | Numerical | 3 | 3 | a region between two step curves y = [x]^2 and y = 3 - 2[x], whose x-range is found exactly like the domain of a GIF function, and whose heights 4 - (n+1)^2 are symmetric so the bisector is x = -1/2 (way 4, hidden symmetry) | not found |
| Q21 | Numerical | 3 | 3 | the area between y = x^3 and a moving tangent over a fixed strip [0,6], a cubic function of the contact point whose minimum is at the midpoint and whose maximum on [1,5] is at an end point (way 2, a function defined by a construction) | not found |
Standard ingredients worth flagging:
- Q3: area between xy = c and a line.
- Q5: Archimedes' quadrature itself. The segment is 4/3 of the greatest inscribed triangle, which is the blueprint concept.
- Q6: a line through a fixed interior point cutting the least area from a parabola.
- Q9: the region between sin^-1 x, cos^-1 x and an axis.
- Q16: the area between a function and its inverse is twice the area with y = x.
- Q21: the least area between a curve and a tangent over a strip occurs at the midpoint.

**Q13 was redesigned after the web check.** The first design, the area of x^2 + y^2 <= 2|x| + 2|y|, is a rescaling of the published AMC 10B 2016 #21 problem (x^2 + y^2 = |x| + |y|). It was replaced by the region y >= x^2 - 2, x >= y^2 - 2, which is symmetric about y = x.

Complete novelty cannot be guaranteed. If you recognise any question, say which one.

## Difficulty (calibrated 0-5 scale)
- Distribution: **Level 2: 11 questions** (Q1-Q5, Q10, Q11, Q14, Q15, Q16, Q19); **Level 3: 10 questions** (Q6, Q7, Q8, Q9, Q12, Q13, Q17, Q18, Q20, Q21).
- Every rated level equals its blueprint target, so no question is one level off.
- Marks-weighted index: **2.50** (SCQ 3 marks, Numerical 4 marks; no equivalence-relation or MCQ-floor adjustment applies). This is a JEE Main paper, so there is no official range to compare it with.
- Consistency pass (questions sorted by level, neighbours compared): the borderline pair is Q14 (L2: f(x) - f(-x) is twice the odd part, area k^2) and Q17 (L3: the tangent of one parabola used as a chord of another, then a cube root). Both were kept at their targets. Q7, Q17, Q20 and Q21 were rated L3 with Medium confidence; each could be read as a strong L2.

## Problems found while verifying (all fixed before the build)
- Q13: replaced after the web check (see above). A draft of the full solution had an arithmetic slip in the surd simplification ((beta+1)^3 = 2 beta + 3); it is corrected.
- Q9: the full solution's check line was rewritten. It was garbled, though the answer was correct.
- Q15 and Q16: the first versions gave answers 32 and 144, the same values as Q8 and Q11. The constants were changed (line y = 7x - 14, area 50; area 50, so k = 200) so that the answer key has no repeats.
- Q6: the first condition ("area is 2 sqrt 2 times the least area") was replaced by the cleaner A(m1) = A(m2) = 32/3.
- Every answer was recomputed with sympy/mpmath independently of the hand solution: numerical quadrature on the region for every question, root-finding for the inverse function (Q16) and the implicit curve (Q2), and a grid search for the extremes (Q7, Q21).
- The web-search tool's own summaries sometimes contained wrong arithmetic (for example it gave 5 for Q13). Those numbers were ignored; the code checks decide.

## Rows whose concepts were hard to combine naturally
- Q8 (four concepts in one Main numerical): combined as "the area across a sign change fixes a, then the odd symmetry gives the area with a line". All four concepts are needed, but the parameter step is light.
- Q9 ("sign changes" together with "integrate with respect to y"): the sign change is that of sin^-1 x - cos^-1 x, not of a curve against the x-axis. A1 - A2 is its signed integral. This reading of the concept is a little loose.
- Q20 ("domain and range of GIF functions"): used as solving [x]^2 + 2[x] - 3 <= 0 for the x-range of the region, the same step as finding the domain of sqrt(3 - 2[x] - [x]^2). The "range" side is not used.
- Q14: "Property for odd and even functions" appears as the cancellation of the even part and the evenness of |odd|. It is natural but quick.

## Stem review
`review_stems.py` was run, and each stem was read as a student would read it. Changes: Q6 condition, Q13 replaced, and Q15/Q16 constants. This is a self-check; an independent reader may still find things.

## Notes
- Several numerical answers are rounded values ("correct up to the 2nd decimal"): Q9 -0.43 (pi/2 - 2), Q10 0.73, Q12 15.81 (48 - 20 ln 5), Q13 7.67 (23/3), Q18 0.83 (5/6). None is close to a rounding boundary.
- The Hindi is the assistant's own translation. Please check the specialised terms (for example भुज / कोटि for abscissa / ordinate, आलेख for graph).
- `recalc.py` (the xlsx formula recalculation) is not available in this environment. The Excel summary uses live formulas that compute when the file is opened.
- `_source/` holds `blueprint.json`, `meta.json` and `q01.json` ... `q21.json`. To fix a question, edit it and rerun `build_paper.py` with `--blueprint _source/blueprint.json`.
