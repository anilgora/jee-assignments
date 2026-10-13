# Run report — SHEET CONIC SECTION_FCopy C2

Paper: `papers/SHEET CONIC SECTION_FCopy C2.pdf` (55 pages, "Exercise C-II", 65 questions: Q1–55 subjective / integer, Q56–61 comprehension (two paragraphs: 56–58, 59–61), Q62–65 match-the-column). The text layer loses the maths symbols, so every page was read as an image. Hindi translations were left out (English deck); the PDF's figures are described in words, not reproduced.

Files: `…_Analysis.pptx` (414 slides, 65 questions), `…_content.json`, `…_ratings.json`, `…_difficulty.xlsx`.

## Blueprint and marks
- **No blueprint was used** (`blueprints/` has no file for this paper). **Concepts self-assigned (no blueprint) - please review.**
- The paper prints no marks. Assumed (JEE Advanced defaults), stated on the section dividers: **4 marks** for Q1–55 (subjective / integer), **3 marks** for Q56–61 (paragraph single-correct) and **3 marks** for Q62–65 (matching).
- Q1–55 are labelled "Numerical Type" where the answer is a single number and "Subjective Type" otherwise (show / prove / find an equation); both carry 4 marks.

## Difficulty (jee-advanced-difficulty-calibrated)
- Marks-weighted difficulty index (adjusted = unadjusted, no adjustment applies): **2.72** (250 marks) — just above the 2.59 low end of the official Advanced range; a chapter sheet.
- Questions per level: Level 0 — 0; Level 1 — 1 (Q34); Level 2 — 24 (Q1, 2, 3, 6, 7, 11, 12, 22, 23, 25, 26, 29, 36, 37, 40, 41, 44, 46, 50, 52, 54, 60, 61, 65); Level 3 — 32 (Q4, 5, 8, 10, 13, 14, 15, 16, 17, 19, 20, 21, 24, 28, 30, 31, 33, 38, 39, 43, 45, 47, 48, 51, 53, 56, 57, 58, 59, 62, 63, 64); Level 4 — 8 (Q9, 18, 27, 32, 35, 42, 49, 55); Level 5 — 0.
- No equivalence-relation adjustment and no multi-correct floor (no such questions).
- Anchors for conics are few, so confidence is mostly Medium; High for the routine ones (e.g. Q1, Q34).
- Excel built with `build_report.py`; `recalc.py` skipped (no `/mnt/skills`), so formula cells have no cached values until opened in Excel.

## Solutions: corrected / written
**Corrected (11)** — all final answers were checked numerically and are right unless stated:
- **Q9 — corrected:** PDF labels the product of slopes "AB × BC" but writes the slopes of AB and of CS (altitude through the focus). Relabelled; added that the three parameters must be distinct.
- **Q16 — corrected:** PDF concludes t2 = −2k/a (and writes "f" for k); the correct value is t2 = +2k/a. The locus 2y² = ax − a² is unchanged.
- **Q17 — corrected:** part (c) says the family L′ "is L itself"; L′ is perpendicular to L but runs over the same pencil of lines through the focus. Reworded; answer x + 1 = 0 unchanged.
- **Q18 — corrected (answer of (c) wrong):** PDF writes 2x₁ = 4a + a t₃² (a t₁t₂ = 2a, not 4a) and gets y² − x + 4 = 0; the correct locus of the circumcentre is **y² = x − 2** (checked with t₁ = 1, t₂ = 2). Parts (a), (b) are right. The printed key lists only (a) and (b).
- **Q19 — corrected:** part (c) is given as 4(3 − 2√2) with no working; integral set-up and evaluation added (12 − 8√2).
- **Q21 — corrected:** the intermediate line "k² − 2α² − hα² − α³ = 0" has wrong signs; substituting m₃ = −k/α gives k² = α²h + α³ − 2α², which is the locus the PDF then states. α = 2 unchanged.
- **Q24 — corrected:** the proportion "h/(2cos t) = k/(4 sin t) = −6/−4" drops the factor 2 of "2ky"; correct is 2k/(4 sin t) = 3/2, giving h = 3cos t, k = 3 sin t, h² + k² = 9 (director circle).
- **Q32 — corrected:** (b) height written 20 + 20cos t for base ends (20cos t, ±16 sin t) should be 20 − 20cos t (same maximum 240√3); (c) area written ½·OP·PN, right angle is at N so ½·ON·NP (its next line already uses this).
- **Q45 — corrected:** the curve point (a sec t, −a tan t) is labelled M; it is N (M is the foot on the tangent). Answer 9 unchanged.
- **Q56 — corrected:** "k³ − 4k(2−h) + 8k = 0" has the last two signs reversed and the next line is not its expansion; redone from m₃ = −k/2 (k² = 4h).
- **Q63 — corrected:** in (D) "x = 1, y = 4 ⇒ C = −1" should be the point (1, 2). Answers unchanged.

**Written from scratch (12)** — the PDF's working (and often the statement) is grey boxes (images lost), or has no working:
- **Q33, Q35, Q37, Q38, Q39, Q41, Q42, Q48, Q49, Q51, Q53** — equations and most working lines are grey boxes; solutions written by me (details under "Assumed / reconstructed").
- **Q60 — written:** the PDF gives only the key (D) with no working.
- Questions marked `pdf` whose boxes hid single lines (Q34, Q36, Q40, Q43, Q44, Q46, Q47, Q50, Q52, Q55, Q57–59, Q61, Q62, Q64, Q65) were reproduced with the hidden lines restored by computation; no step contradicted the PDF.

## Answer key
No key looked wrong. Every answer was checked by computation (numerical checks of the loci, areas and identities). Notes: the key of Q18 omits part (c) (and the PDF's working for (c) is wrong, above); Q9 / Q16 / Q19 / Q21 / Q24 have wrong working but right keys; Q44's answer, Q57 options (C), (D), Q59 options (B), (D) are grey boxes in the PDF.

## Alternate solutions and useful results
- **Alternates: 60 of 65 questions** (all except Q9, Q29, Q36, Q42, Q44). Each verified against the answer (numerically where a number is involved). Examples of genuinely different methods: Q3 extreme circles for the ellipse vertices; Q5 shear that preserves area; Q10 polar of (h,k) tangent to y² = 2x; Q15 point reflection in the contact point; Q16 Vieta on the cubic of the circle–parabola intersections; Q19 horizontal strips; Q27 rotated-tangent geometry (|M|² = 2p²); Q28 affine map to the unit circle; Q30 focal-triangle area b² tan(γ/2); Q32(b) auxiliary-circle equilateral triangle; Q34 vector reflection; Q35 two special perpendicular pairs; Q38 pole–polar; Q39 angle-bisector theorem on the focal radii; Q43 parabola parametrisation; Q45 polar form about the centre; Q47 midpoint ± 3(cos, sin); Q48 rotate to xy = c² and use t₁³t₂ = −1; Q49 internal-bisector length; Q51 asymptote coordinates (UV = 1); Q52 contact point is the midpoint of the intercept; Q55 focal sum MA + MB = 4.
- **Questions with NO alternate (5), one line each:**
  - Q9 — the altitude condition gives one cubic satisfied by each parameter; every other route (vectors, slopes, circumcircle) leads to the same three altitude equations.
  - Q29 — read off the ellipse and fit the parabola; no different method.
  - Q36 — the focal-sum definition is the only way to identify the locus; the "extreme circles" argument assumes the locus is an ellipse.
  - Q42 — eliminating the slope m from the two tangents is the only route; parametrising by angle gives identical algebra.
  - Q44 — ae = AE and a − A = 4 fix everything; no different method.
- **Useful Result / Pattern: all 65 questions have 3–4 bullets**, checked on numerical cases where they are formulas.
- Weaker alternates (flagged for review): Q2 (slope method leads to the same quadratic), Q8 (explicit parametrisation then verification), Q11 (AM-GM on the same quadratic), Q13 (composition of involutions is the same algebra), Q21 (checks α = 2 against the locus), Q25 (ratio sin²θ : cos²θ, same equations), Q50 (constant-area theorem), Q63 (standard-property recognition).

## make_ppt.py warnings
- `Q57: very long question - font reduced to 20 pt` and `Q58: … 22 pt` (long paragraph passage) — harmless, left as is.
- `could not convert $|{\rm slope}|=\sqrt3$` (Q54 alternate) — fixed by rewording ("its slope is ±√3"); rebuilt with no conversion warnings. All 2416 equations became native PowerPoint equations.

## Assumed / reconstructed / skipped
- **Reconstructed equations (grey boxes in the PDF):** Q33 standard ellipse x²/a² + y²/b² = 1 (a > r > b); **Q35** ellipse x²/4 + y² = 1 — recovered from the surviving line "x + 2y = 0" and the key 19 (it reproduces both); Q37 standard ellipse and angle π/4 — from the key "(4 − 2√2)r² = r²sec²(·)" (sec²(π/8) = 4 − 2√2); Q38, Q41, Q49, Q51, Q53 standard hyperbola/ellipse; **Q39** hyperbola x²/4 − y²/12 = 1 — from "e² = 1 + · = 4, b² = 12" and the key 45; **Q44** distance between foci 2√13 — from the data (a − A = 4, e/E = 3/7 do not fix c; 2√13 reproduces the standard answer x²/49 + y²/36 = 1, x²/9 − y²/4 = 1), the PDF's answer is hidden; Q46 e = √2 from the visible x² + y² = (x + y + 1)²; **Q50** hyperbola 4x² − 9y² = 180 — from P(9, 4) and the tangent x − y = 5; Q51 the locus form x²/a² − y²/b² = λ and the key 3 were derived (4λ = 3, checked on both asymptotes); **Q64** ellipse x²/25 + y²/9 = 1 and eccentric angle π/4 — from 16, 25, 9, 17.
- Options not recoverable: Q57 (C), (D); Q59 (D). Q59 (B) reconstructed as (2√2, 2√2), (−2√2, −2√2) (the key is B). They are marked "not legible in the PDF" on the slides.
- Q15 assumes the variable parabola opens opposite to the fixed one (the only way two equal parabolas with parallel axes touch). Q32(b) takes the apex of the isosceles triangle at the end of the major axis. Q53's product is stated in magnitude (|b² − a²m²|).
- No grading of figure-based statements (diagrams of the PDF not reproduced). Slides were rendered once with LibreOffice only as a sanity check (it shows the equations as LaTeX text; PowerPoint renders them natively), the deck was not inspected in PowerPoint.
