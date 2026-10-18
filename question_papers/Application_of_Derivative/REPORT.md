# Application_of_Derivative: generation report

Blueprint: `qp_blueprints/Application_of_Derivative.xlsx` (no `_config.xlsx`, so the check ran without `--config`).
Generated 18-Oct-2026 by the scheduled run, skill `jee-question-paper` way B (blueprint supplied directly).

## Blueprint check
- **Pattern:** inferred **JEE Main** (only Single Correct and Numerical types, nothing above level 3). Paper name taken from the file name.
- **Paper:** 22 questions, 4 Single Correct (Q1-Q4) then 18 Numerical (Q5-Q22). This is the blueprint's own mix, kept as given.
- **Reorder (`--reorder`)**, old Sr No -> new Q:
  551->1, 558->2, 560->3, 563->4, 549->5, 550->6, 552->7, 553->8, 554->9, 555->10, 556->11, 557->12, 559->13, 561->14, 562->15, 564->16, 565->17, 566->18, 567->19, 568->20, 569->21, 570->22.
- **Answer Plans:** the blueprint had none, so all 22 were drawn at random by the script:
  Q1 Option C, Q2 Option A, Q3 Option B, Q4 Option D, Q5 positive 2-digit integer, Q6 negative decimal, Q7 negative integer, Q8 positive decimal, Q9 decimal between 0 and 1, Q10 positive 3-digit integer, Q11 negative integer, Q12 positive 2-digit integer, Q13 negative decimal, Q14 decimal between 0 and 1, Q15 positive 3-digit integer, Q16 positive decimal, Q17 positive decimal, Q18 negative decimal, Q19 positive 2-digit integer, Q20 positive 3-digit integer, Q21 negative integer, Q22 decimal between 0 and 1. Every answer matches its plan (the build checks this).
- **Warnings (recorded, not fixed; the blueprint is yours):**
  - The cell in file row 20 (old Sr 568, new Q20) contains ";": "Bounded functions; greatest and least values". No config was supplied, so it was kept as **one concept**.
  - Q14 (old 561) lists **4 concepts** although the Main pattern normally has at most two. All four were used.
  - Concepts repeated within the paper: "Approximation and errors using differentials" (Q2, Q3), "Tangent or normal drawn through an external point" (Q1, Q6), "Common tangent/normal between two curves" (Q6, Q7, Q11), "Minimum distance between two curves" (Q9, Q10), "Length of tangent, subtangent, normal and subnormal" (Q5, Q12), "Rate measure and related rates" (Q2, Q13), "Proving inequalities using monotonicity" (Q4, Q16), "Rolle's theorem and its application" (Q17, Q18), "LMVT and its application" (Q17, Q19), "One-one vs many-one ..." (Q15, Q19), "Absolute (Global) Maxima & Minima on Closed Intervals" (Q14, Q20). Each repeat uses a different mechanism and a different function.
- No errors. The blueprint file was not edited.

## Originality report (per question)
Mechanism named before writing; provenance check against `known_skeletons.md`; web search done for every question (standard mode).
"not found" = no similar problem found; "ingredient only" = only the standard ingredient or method came up, not this construction.

| Q | Type | Target | Rated | Mechanism | Web check |
|---|---|---|---|---|---|
| Q1 | SCQ | 3 | 3 | points of a parabola classified by the number of tangents they send to a cubic (way 5: the point turns out to be where the parabola meets the cubic) | not found |
| Q2 | SCQ | 2 | 2 | a related-rate of the area of a rectangle whose vertex slides on a circle, fed into a differential (linear-in-time) estimate (way 5) | not found |
| Q3 | SCQ | 3 | 3 | error propagation from a measured viewing angle back to the observer's distance, with two positions giving the same angle (way 5) | ingredient only |
| Q4 | SCQ | 2 | 2 | one always-increasing function f(x)=x+ln(x^2-2x+2) generates four close numerical bounds on e at x = 1/3, -1/3, 1/2, -1/2 (way 5) | not found |
| Q5 | Numerical | 2 | 2 | the normal condition through a point on the y-axis fixes P, then the triangle PTG is read off from subtangent plus subnormal (way 5) | ingredient only |
| Q6 | Numerical | 2 | 2 | the two tangents from a point to one parabola are required to touch a second parabola; the hidden invariant is that the second parabola is the point reflection of the first in that point (way 4) | not found |
| Q7 | Numerical | 2 | 2 | common normal of two parabolas that are reflections of each other in y = -x, solved through the slope form of one and the parametric form of the other; uniqueness needs a quintic factorisation (way 5) | ingredient only |
| Q8 | Numerical | 2 | 2 | tangent at one parameter re-meeting a cubic parametric curve, then the normal at the second point (way 1, one step of a tangent chain) | not found |
| Q9 | Numerical | 2 | 2 | two opposite parabolas that are point-symmetric about (3/4, 0); the common normal is found through equal slopes and the minimum is justified by two parallel separating tangents (way 4) | ingredient only |
| Q10 | Numerical | 2 | 2 | circle-parabola distance reduced to centre-parabola distance, with the case split alpha <= 6 (vertex nearest) versus alpha > 6 and a sign condition removing alpha = -42 (way 5) | ingredient only |
| Q11 | Numerical | 2 | 2 | orthogonal intersection of two coaxial-direction parabolas fixes the second one, whose common tangents with the first turn out to be perpendicular (way 3: a family fixed by two conditions) | not found |
| Q12 | Numerical | 3 | 3 | a curve defined by a geometric equality between its subtangent and the radius of the circle through O and P centred on the x-axis (way 5), which turns into the homogeneous equation y' = 2xy/(x^2+y^2) with a rectangular-hyperbola family | ingredient only |
| Q13 | Numerical | 3 | 3 | a sector kept at constant area while its angle shrinks at a rate given in degrees (way 5); the perimeter rate needs the radian conversion, the constraint and two chained rates | not found |
| Q14 | Numerical | 3 | 3 | the max-min of a sliding window, g(t) = min of x/(1+x^2) on [t, t+1], maximised over t (way 2: a function defined by a construction) | not found |
| Q15 | Numerical | 3 | 3 | counting coefficient pairs for which a cubic is one-one on the half-line [0, infinity), where the condition splits by the position of the vertex of f' (way 5) | ingredient only |
| Q16 | Numerical | 3 | 3 | best exponents in a two-sided power bound for log(1+x), where the upper exponent is decided at x -> 0 by the series but the lower exponent is decided at x -> infinity, not by the series (way 4: two different regimes) | found: redesigned |
| Q17 | Numerical | 2 | 2 | Rolle's theorem fixes the parameter of f(x) = x + k/x, and the LMVT point on a second interval comes out as the geometric mean of its end points (way 5) | ingredient only |
| Q18 | Numerical | 3 | 3 | the roots of P' + 2P are located by Rolle on e^{2x}P and the missing fourth root by the IVT, so that 'sum of real roots' equals the Vieta sum (way 5) | not found |
| Q19 | Numerical | 3 | 3 | integer pairs (a,b) for which ax + b sin x is simultaneously one-one and 6-Lipschitz, the Lipschitz part being exactly the LMVT bound |f'| <= 6 (way 5) | not found |
| Q20 | Numerical | 3 | 3 | range of a cubic composed with a bounded rational function, where the bounded inner range [-4,4] becomes the closed interval on which the cubic's absolute extrema are taken (way 5) | ingredient only |
| Q21 | Numerical | 2 | 2 | cones with a fixed external vertex over the parallel sections of a sphere, parametrised by the plane constant d in coordinates (way 5) | ingredient only |
| Q22 | Numerical | 3 | 3 | the maximum of a quartic and its mirror image is F(-|x|), so the inflection points come from the left half of F, not the right (way 2: a function defined by a max construction) | not found |
Standard ingredients worth flagging: Q3 (angle subtended by a segment), Q5 (triangle of tangent, normal and x-axis), Q9/Q10 (common-normal method for distance), Q12 (circles through O centred on the x-axis), Q15 (one-one cubic condition a^2 <= 3b), Q17 (LMVT for 1/x gives the geometric mean), Q20 (range of x/(1+x^2)), Q21 (the classic cone-in-sphere optimisation, here with the vertex outside the sphere).
**Q16 was redesigned after the web check:** the first design (least lambda for which (1+3/x)^(x+lambda) is decreasing) is a rescaling of a published result, (1+1/x)^(x+a) is decreasing iff a >= 1/2, so it was replaced by the two-sided bound x/(1+x)^alpha <= ln(1+x) <= x/(1+x)^beta.
Complete novelty cannot be guaranteed. If you recognise any question, tell me which one.

## Difficulty (calibrated 0-5 scale)
- Distribution: **Level 2: 11 questions** (Q2, Q4-Q11, Q17, Q21); **Level 3: 11 questions** (Q1, Q3, Q12-Q16, Q18-Q20, Q22).
- Every rated level equals its blueprint target, so no question is one level off.
- Marks-weighted index **2.50** (SCQ 3 marks, Numerical 4 marks; no equivalence-relation or MCQ-floor adjustments apply). This is a JEE Main paper, so there is no official range to compare it with.
- Consistency pass (sorted by level, neighbours compared): the borderline pair is Q11 (L2: orthogonality, then the common-tangent discriminant, with surds) and Q20 (L3: the bounded inner function gives the interval, then closed-interval extrema). Both kept at their targets, Medium confidence.

## Problems found while verifying (all fixed before the build)
- Q10: the web check showed that alpha = -42 also gives minimum distance 40 (the vertex is then the nearest point). Added "alpha > 0" to the stem.
- Q16: replaced after the web check (see above). Also tightened the full solution's alpha < 0 case.
- Q2: the full solution's comparison value was corrected to the exact area after 0.1 s (about 47.25).
- Every answer was recomputed with sympy/mpmath/numpy (brute-force grids for Q9, Q14, Q15, Q19, Q20, Q22 and root-finding for Q3, Q18).

## Rows whose concepts were hard to combine naturally
- Q14 (four maxima/minima concepts in one Main numerical): combined through a sliding-window function g(t) = least value of x/(1+x^2) on [t, t+1]. All four concepts are needed, but the "second derivative test" part is light (it only classifies x = +-1).
- Q18 (Rolle + IVT): Rolle on e^{2x}P gives three roots and the IVT gives the fourth. Natural, but the Vieta finish is quick once all four roots are known to be real.
- Q4 (always increasing + inequalities): a student who knows e to 3 decimals could check the options numerically. The bounds were chosen within 2% of e, so the check takes effort.

## Stem review
`review_stems.py` was run and each stem was read as a student would read it. Changes: Q2 wording, Q10 condition alpha > 0, Q1 dropped a superfluous condition. This is a self-check; an independent reader may still find things.

## Notes
- The Hindi is the assistant's own translation. Please check the specialised terms (for example अधःस्पर्शी for subtangent, नति-परिवर्तन बिन्दु for point of inflection).
- `recalc.py` (the xlsx formula recalculation) is not available in this environment. The Excel summary uses live formulas that compute when the file is opened.
- `_source/` holds `blueprint.json` and `q01.json` ... `q22.json` plus `meta.json`. To fix a question, edit it and rerun `build_paper.py` with `--blueprint _source/blueprint.json`.
