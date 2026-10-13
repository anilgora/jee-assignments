# Run report — SHEET AREA UNDER CURVE_FCopy C2

Paper: `papers/SHEET AREA UNDER CURVE_FCopy C2.pdf` (37 pages, "Exercise C-II", 31 questions: Q1–21 subjective/integer, Q22–28 comprehension (two paragraphs), Q29–31 match-the-column). The text layer lost all maths symbols, so every page was read as an image. Hindi translations were left out (English deck).

Files: `…_Analysis.pptx` (195 slides), `…_content.json`, `…_ratings.json`, `…_difficulty.xlsx`.

## Blueprint and marks
- **No blueprint was used** (`blueprints/` has no file for this paper). **Concepts self-assigned (no blueprint) - please review.**
- The paper prints no marks. Assumed (JEE Advanced defaults), stated on the section dividers: **4 marks** for Q1–21 (subjective / integer), **3 marks** for Q22–28 (paragraph single-correct) and **3 marks** for Q29–31 (matching).
- Q1–21 are labelled "Numerical Type" where the answer is a single number and "Subjective Type" otherwise (find / show / prove); both carry 4 marks.

## Difficulty (jee-advanced-difficulty-calibrated)
- Marks-weighted difficulty index (adjusted): **2.58** (below the official Advanced range 2.59–3.21 only marginally; as expected for a chapter sheet).
- Questions per level: Level 1 — 4 (Q1, Q8, Q22, Q27); Level 2 — 11 (Q2, Q3, Q7, Q9, Q12, Q21, Q23, Q24, Q26, Q28, Q29); Level 3 — 11 (Q4, Q5, Q6, Q10, Q11, Q14, Q15, Q16, Q20, Q25, Q31); Level 4 — 5 (Q13, Q17, Q18, Q19, Q30); Levels 0 and 5 — none.
- No equivalence-relation adjustment and no multi-correct floor (no such questions).
- Confidence Low for Q6 (ill-posed wording); Medium for most others; High for the easy ones.
- Excel built with `build_report.py`; `recalc.py` was skipped (no `/mnt/skills`), so formula cells have no cached values until opened in Excel.

## Solutions: corrected / written (none were `written`)
- **Q6 — corrected:** PDF working is right, but the question says "minimum of |a|+|b|+|c|" and never says a, b, c are rational. For real a, b, c the representation is not unique (true real minimum would be Area/π³ ≈ 0.0253). The key 1 assumes rational a, b, c; this is now stated in the solution.
- **Q8 — corrected:** the PDF replaces the denominator t·sin t² by t³ before L'Hôpital without comment; added the factor t²/sin t² → 1. Answer unchanged.
- **Q13 — corrected:** PDF omits the case 0 < a ≤ 1/2 (region contains the asymptote x = 1/2, area infinite). Added. Answer a = 8 or (2/5)(6 − √21) unchanged (both checked numerically).
- **Q15 — corrected:** PDF differentiates √(m²−4m+4c) as (2m−4)/√(…) (missing the factor ½). Does not change m = 2; replaced by A = D^{3/2}/6, dA/dm = (m−2)√D/2.
- **Q17 — corrected:** PDF stops after α = π/3 and never computes the second part (ratio). Added the area above and below y = 1 (U = 1, L = √3/2, ratio 2 : √3, checked numerically).
- **Q18 — corrected (working wrong, key right):** PDF's area function "√(1−a²) − sin⁻¹a + π/4" is wrong (gives A(0) = 1 + π/4) and its derivative gives a = −1/2, outside [0,1]. Correct: A(a) = (1−a)√(1−a²) + sin⁻¹a − π/4, A′ = a(2a−1)/√(1−a²). Key (min at a = 1/2, (3√3−π)/12; local max 1 − π/4 at a = 0; maximum π/4 at a = 1) is right.
- **Q19 — corrected:** the differentiation step (Leibniz, d/dα of the area equation) is missing; the PDF writes the differentiated equation as if it were the original. Added.
- **Q23 — corrected:** PDF's dy/dx has a stray factor 2 (unused) and its decimal 2.266 should be 2.268; option (B) 2.27 unchanged.
- **Q25 — corrected:** PDF applies L'Hôpital in h, which needs continuity of f′ at 0 (not given). Replaced by splitting e^x(f(h)−f(0))/h + f(x)(e^h−1)/h. Result f = xeˣ unchanged.
- **Q29 — corrected:** in (B) the PDF's antiderivative has 11/4·x² instead of 11/2·x²; its printed values 9/4, 1/4, 1/4 are right, so the answer 11/4 stands.
- **Q30 — corrected (omissions):** (C) lower limit (sin x)^cos x → 0 as x → 0⁺ not evaluated; (D) ends at y ≤ 2 ln 4 without linking to option S = 2 ln 6. Both completed.
- All other questions — `pdf`: checked step by step and reproduced (Q20's printed split of the integrand was suspected wrong but verified correct and kept).

## Answer key
Every answer was checked by computation (numerical integration / ODE solving). No wrong key letter or value found. Notes: Q6 key (1) assumes rational coefficients; Q18 and Q29(B) have wrong *working* with right keys (above). Q16 is a proof (no numerical answer printed).

## Alternate solutions and useful results
- **Alternates: 25 of 31 questions** (Q1–Q5, Q7–Q10, Q12–Q16, Q18, Q19, Q21, Q23, Q25–Q31). Each verified against the answer. Examples: Q9 AM–GM instead of calculus; Q14 α = tan θ; Q15 complete the square in D; Q16 bounds from 2t ≤ 1+t² ≤ 2; Q13 G(x) = ½ ln(x²/(2x−1)) ≥ 0; Q19 scaling ansatz y = kx²; Q25 divide by e^{x+y} (Cauchy additive); Q30(D) f′ ≤ 2/x gives 2 ln 6 at once.
- **Questions with NO alternate (6), one line each:**
  - Q6 — only a reorganisation of the same integral ∫|x − x²| (signed integral plus correction); no different method.
  - Q11 — both parts are a single logarithmic antiderivative; the only variants (monotonicity of A(a) − 1/a) prove uniqueness but do not give a new route.
  - Q17 — α comes from equating two cosine-integral areas; every route is the same sin-difference computation.
  - Q20 — the e^x(h + h′) recognition is the only elementary route (by parts leads to the same cancellation).
  - Q22 — direct arc-length integral of a linear radicand; no different method.
  - Q24 — perfect square under the root is the only method.
- **Useful Result / Pattern: all 31 questions have 3–4 bullets.** Formulas checked on numerical cases (e.g. chord-area formula on Q1/Q4, semicubical-parabola arc length 13/6, ∫tanⁿ reduction at n = 3).
- Weaker alternates (flagged for review): Q5 (same formula applied to both areas), Q21 (power-law ansatz; uniqueness from the main method), Q23 (parametrisation instead of x(y)), Q31 (alternate covers only part (D); others referred back).

## make_ppt.py warnings
- `Q27: only 3 solution bullets` — resolved (a fourth sanity-check bullet added; the PDF's working is just three lines).
- `Q29, Q30, Q31: very long question - font reduced to 20 pt` — harmless (matching questions with two columns are long); left as is.
- No "could not convert" warnings: all 1214 equations converted to native PowerPoint equations.

## Skipped / assumed
- No slide rendering or thumbnails (no soffice); deck not visually inspected.
- Marks assumed as above. Hindi text and diagrams of the PDF were not reproduced (figure-based statements such as Q8, Q10, Q19 are described in words/LaTeX).
- Q22–24 and Q25–28 carry the passage text in the `paragraph` field.
