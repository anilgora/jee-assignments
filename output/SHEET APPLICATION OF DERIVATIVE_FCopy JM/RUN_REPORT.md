# Run report — SHEET APPLICATION OF DERIVATIVE_FCopy JM

Paper: `papers/SHEET APPLICATION OF DERIVATIVE_FCopy JM.pdf` (34 pages, 50 maths questions, JEE Main 2023–2024 previous-year problems on Application of Derivatives: 36 single-correct with four options, 14 numerical). The PDF text layer is garbled for maths, so every page was rendered to an image and read.

Files in this folder: `…_Analysis.pptx` (294 slides), `…_content.json`, `…_ratings.json`, `…_difficulty.xlsx`.

## Blueprint and marks
- **No blueprint was used** (`blueprints/` has no file for this paper). **Concepts self-assigned (no blueprint) - please review.**
- The paper prints no marking scheme. Marks assumed (JEE Advanced defaults, as instructed): **4 marks for every single-correct question and 4 marks for every numerical question**. Stated on the section divider.
- Question types: Q2, Q3, Q13, Q14, Q17, Q18, Q19, Q29, Q34, Q36, Q41, Q42, Q49, Q50 are numerical (no options); all others are single-correct. Q19 prints "Ans. B" although it has no options (see key issues).
- Hindi translations in the PDF were left out; the deck is English only.

## Difficulty (jee-advanced-difficulty-calibrated)
- Marks-weighted difficulty index (adjusted): **2.20** (all questions carry 4 marks, so this equals the mean level).
- Questions per level: Level 1 — 6 (Q1, Q9, Q20, Q25, Q32, Q38); Level 2 — 29 (Q3, Q4, Q5, Q7, Q8, Q10, Q11, Q12, Q13, Q14, Q15, Q18, Q23, Q24, Q27, Q28, Q30, Q31, Q33, Q37, Q39, Q40, Q43, Q45, Q46, Q47, Q48, Q49, Q50); Level 3 — 14 (Q2, Q6, Q16, Q17, Q19, Q21, Q22, Q26, Q29, Q34, Q35, Q36, Q42, Q44); Level 4 — 1 (Q41); Levels 0 and 5 — none.
- No equivalence-relation adjustment and no multi-correct floor (no such questions). As this is a JEE Main chapter sheet, 2.20 is below the official Advanced range (2.59–3.21), as expected.
- Confidence Medium for Q2, Q6, Q19, Q22, Q27, Q29, Q34, Q36, Q41, Q44; **Low for Q16 and Q35** (flawed/ambiguous questions).
- Excel built with `build_report.py`; `recalc.py` was skipped (no `/mnt/skills`), so formula cells have no cached values until the workbook is opened in Excel.

## Solutions: corrected / written (none were `written`)
- **Q3 — corrected:** PDF writes the slope condition with an unjustified absolute value, `-4 = |(-1-3b)/(1+b)|`; fixed to `-4 = -(1+3b)/(1+b)` and added the step `4(1+b)=1+3b`. Result unchanged (b=-3, a=7).
- **Q6 — corrected:** PDF says `h(x)∈(h(-1),h(2))=(-8,8)` but `h(-1)=-10`, so the interval is `(-10,8)`. Option (B) remains the answer, now justified correctly (e.g. h(-0.9)≈-9.43).
- **Q10 — corrected:** PDF's displayed `S = l1²/8 + l2²/4π` drops the factor 3 (3A₂ = 3l₂²/4π). The next line uses the right coefficient, so the ratio 6:1 is unchanged.
- **Q11 — corrected:** PDF labels its conclusions "option (4)/(1)", which do not match (A)–(D), and never rules out (B). Relabelled and added the argument f(0)=g(0), f'>g' ⇒ f>g.
- **Q12 — corrected:** PDF prints `f(2) = -4 = 4` (stray "= 4") and omits that f is decreasing on both pieces (the reason the extrema are at the endpoints).
- **Q16 — corrected:** the question's data are inconsistent (see key issues). PDF's "g' is increasing" is a typo for "g is increasing" and its bounds contradict each other. Rewritten so that (B) is justified as a vacuous truth.
- **Q19 — corrected:** PDF stops after the intermediate value theorem (≥2 roots) without showing there are no more, and prints "Ans. B" for a numerical question. Added Descartes' rule (signs +,−,−,−,+: at most 2 positive roots in t=e^{2x}) ⇒ exactly 2.
- **Q21 — corrected (answer key wrong):** PDF's working ends at e³+e⁶+e¹¹, which is option **(D)**, but the PDF's key says (A) e⁵+e⁶+e¹¹. The key is wrong; answer given as (D). Also read the radical as √(3e), the only reading consistent with a local maximum.
- **Q22 — corrected:** PDF gives only f''(5π/6)<0 and no endpoint comparison; added the factorisation f'=(1−cos x)(1−2cos 2x) (critical points 0, π/6, 5π/6) and compared with f(0)=0, f(π)=π. Answer unchanged.
- **Q24 — corrected:** PDF writes "Let x=π/12" (it is the angle; the root is x=cos(π/12)) and says f'>0 on the closed interval; actually f'(1/2)=0, f'>0 on (1/2,1]. Conclusion unchanged.
- **Q30 — corrected:** PDF states the maximum without a check and does not note that the cubic P(d) has no global maximum (P→+∞ as d→−∞); added the second-derivative test (local max at d=8/5) and the caveat. Key (B) retained.
- **Q35 — corrected:** PDF silently assumes the circle touches the parabola at its vertex (0,6); stated the assumption. See key issues.
- **Q37 — corrected:** PDF's line for f' is garbled/incorrect in print (`cos x − 4x²/π − 3`); correct is f'=cos x+3−(2/π)(2x+1). Rebuilt the bound 3−2/π−4x/π>0.
- **Q41 — corrected:** PDF counts "f³f'' has ≥6 roots, so its derivative has ≥5 roots", but that derivative is f²(3f'f''+ff‴): roots of f² are not roots of the asked expression, and roots of f and f'' may coincide. Added the Rolle argument that handles both. Answer 5 unchanged.
- All other questions — `pdf`: the working was checked step by step and reproduced (small additions only: e.g. Q20 second-derivative sign, Q45 numerical check of the other options).

## Answer key
Every printed answer was checked by direct computation (sympy / numerical scans). Problems:
- **Q21: key wrong.** Printed (A); correct (D) e³+e⁶+e¹¹ (explained above).
- **Q19: key garbled.** Printed "B" for a numerical question; the number of intersection points is 2.
- **Q16: question flawed.** With g(x)=x ln x f(x)−x non-decreasing we need g(2)≤g(4), but g(2)=ln2−2≈−1.31 > g(4)=2ln2−4≈−2.61: no such function exists. Both statements hold vacuously, so (B) is consistent with the key.
- **Q30: question loose.** "Greatest" product: a₁a₄a₅=(2−5d)(2−2d)(2−d) has no global maximum; d=8/5 is the local maximum (the key).
- **Q35: ambiguous.** The key (D) corresponds to the circle x²+(y−4)²=4 (touching the parabola at its vertex). A smaller circle (centre (0,3√3−2), radius ≈1.6) is tangent to both lines and to the parabola from inside and matches none of the options.
- Q9 has a hidden caveat (x=1 must be a turning point of f; fails for a=−2) but the key 6 holds; noted in the Useful Result slide.

## Alternate solutions and useful results
- **Alternates: 40 of the 50 questions** (Q1–Q7, Q10–Q15, Q17–Q29, Q31–Q33, Q36, Q37, Q39, Q40, Q42–Q46, Q48, Q49). Each was checked against the answer. Examples: Q1 sign changes of the quartic; Q2 minimise a quadratic in x; Q3 logarithmic derivative; Q10, Q13 Cauchy–Schwarz/Titu; Q19 palindromic substitution u=t+1/t; Q20, Q32, Q49 AM–GM; Q23 test function f=x²; Q24 x=cosθ with cos3θ; Q26 symmetry + one Rolle; Q31, Q39 substitution t=x^{1/3}, (x−2)^{1/3}; Q36 trigonometric parametrisation; Q44 general circumscribed-rectangle formula; Q45 ln x/x; Q48 AM–GM on 3/p+5/q=1.
- **Questions with NO alternate (10), one line each:**
  - Q8 — the only natural method is the sign of the roots of f' (f'(0)<0 ⇔ product of roots<0); the Vieta variant is the same idea restated.
  - Q9 — the common root comes from subtracting the two derivatives; no different route exists.
  - Q16 — data inconsistent; only the monotonicity/vacuity argument exists.
  - Q30 — a cubic with a fixed term; AM–GM does not apply (factors have no constant sum, the maximum is only local).
  - Q34 — the wavy-curve/parity rule is the only method; any other is the same sign scheme.
  - Q35 — the problem is ambiguous; no honest second derivation.
  - Q38 — f'=x^x(1+ln x) is the standard and the only short method; convexity of x ln x is the same derivative.
  - Q41 — Rolle on f³f'' is the idea; no different elementary route.
  - Q47 — roots of f' (a, 2a) give α=a, α²=2a at once; scaling x=au only restates it.
  - Q50 — straight-line chain (critical point, inequality, interval); no different method.
- Weaker alternates (flagged for review): **Q6** (same data, definite integrals instead of constants), **Q12** (vertex of each parabolic piece instead of f'), **Q22** (factorised f' read by signs; still derivative based), **Q27** (clears negative powers; mostly algebraic), **Q42** (amplitude/mean argument is a rephrasing of the PDF's range argument), **Q23** (test function; valid because the answer is unique).
- **Useful Result / Pattern: all 50 questions have 4 bullets each.** Formulas were checked on numerical cases (e.g. Q2 formula r²=b²(1−h²/(a²−b²))=12.8; Q13 min tangent length a+b=7; Q48 ladder length 11.194 vs numerical 11.194).

## make_ppt.py warnings
- The build printed no warnings: "Equations: 1827 converted to native PowerPoint equations. Saved … (294 slides, 50 questions)". No "could not convert" notes, so no equation was left as LaTeX text.

## Skipped, assumed or guessed
- Skipped (not available in this environment): `recalc.py`, thumbnails/soffice rendering, and visual inspection of the rendered slides.
- Q21: the PDF's radical is typeset ambiguously (√3e); read as √(3e) (the only reading with a local maximum, and what the PDF's own working uses).
- Q16, Q30, Q35: question flaws noted above; the printed key was kept where it is the intended answer (Q16 B, Q30 B, Q35 D).
- Q19 is treated as numerical (answer 2).
- Levels are my calibrated judgement against the anchors (Application-of-Derivatives anchors are few; Medium/Low confidence listed above).
- The sheet's Hindi text and the PDF's small graphs (Q12, Q17, Q29, Q33) were not reproduced.
