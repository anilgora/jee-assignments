# Run report — SHEET Complex Number_FCopy C2

Paper: `papers/SHEET Complex Number_FCopy C2.pdf` (29 pages, "Exercise C - II", 32 questions: Q1–22 subjective/numerical, Q23–25 and Q26–28 two paragraph sets, Q29–30 under a "Paragraph" header without a passage, Q31–32 match-the-column). The text layer drops minus signs and many symbols, so the maths was read from page images. Hindi text left out (English deck).

Files: `…_Analysis.pptx` (200 slides), `…_content.json`, `…_ratings.json`, `…_difficulty.xlsx`.

## Blueprint and marks
- **No blueprint was used** (`blueprints/` has no file for this paper). **Concepts self-assigned (no blueprint) - please review.**
- The paper prints no marks. Assumed (JEE Advanced defaults), also stated on the section dividers: **4 marks** for Q1–22 (subjective / numerical), **3 marks** for Q23–30 (paragraph-based single correct; Q29–30 follow the printed "Paragraph" header although they have no passage) and **3 marks** for Q31–32 (matching). Q25 has three correct options per the key but is kept as a paragraph question with 3 marks.
- Q1–22 are labelled "Numerical Type" where the answer is a single number and "Subjective Type" for prove / find-expression questions; both carry 4 marks.

## Difficulty (jee-advanced-difficulty-calibrated)
- Marks-weighted difficulty index (adjusted): **2.60** (118 marks).
- Questions per level: Level 1 — 1 (Q29); Level 2 — 12 (Q1, Q2, Q3, Q5, Q8, Q12, Q13, Q14, Q18, Q23, Q26, Q30); Level 3 — 18 (Q4, Q6, Q7, Q9, Q10, Q11, Q15, Q16, Q19, Q20, Q21, Q22, Q24, Q25, Q27, Q28, Q31, Q32); Level 4 — 1 (Q17); Levels 0 and 5 — none.
- No equivalence-relation adjustment and no multi-correct floor applied (no such questions).
- Confidence Low for Q15 (ambiguous wording); Medium for most; High for the easy ones. `recalc.py` was skipped (no `/mnt/skills`), so formula cells in the Excel file have no cached values until opened in Excel.

## Solutions: corrected / written (no question was `written`)
- **Q1 — corrected:** PDF never defines A, B, C and ignores the degenerate case t2+t3=0 (D undefined, z = z1). Added both.
- **Q11 — corrected:** PDF solves only (i)(a),(b); part **(ii) is missing**. Added (put x=i, take |·|², |1+i|^(2n)=2^n).
- **Q13 — corrected:** PDF stops at 2^n cos^n(θ/2) e^{iθ(n/2+1)}; the final step (equating real and imaginary parts to get (a) and (b)) was added.
- **Q15 — corrected:** PDF does not say where the angle tan⁻¹(1/3) is measured. Its working (line y=3x through the origin) only fits the angle at the origin O (which lies on the circle). With the central angle at C(3,4), Q = 3+√10/2 + i(4+3√10/2) and the key 3+7i would not follow. Key kept, assumption stated; rejection of root x=0 written out.
- **Q17 — corrected:** PDF dismisses the factor k = a/(1−a) with "not possible" and no reason; the distinctness argument (same elimination from b, c would force a=b=c) was added.
- **Q20 — corrected:** PDF takes b=1 from b(3a²−b²)=107 without excluding b=107 (3a²=11450 is not divisible by 3). Added; answer unchanged.
- **Q22 — corrected:** PDF lists the cases (a−b)²=0 and 1 without showing no other value is possible; added (a+b)² = 4−3(a−b)² ≥ 0. Answer unchanged.
- **Q23 — corrected (working wrong, key right):** PDF writes "x=0, (y−1)²=5, y=1±√5" and "only ⊥ point"; x=0 does not satisfy x+y=√2 with those y. Correct: intersect x+y=√2 with the circle, y = ((√2−1)±√(7+6√2))/2 ≈ 2.17 or −1.76, keep y≥1 → one point.
- **Q25 — corrected:** PDF only derives |z|−|w|+3 ∈ (−3,9), which supports (D) alone while its key is BCD. Exact range is (≈0.07, ≈5.30], inside the intervals of B, C, D but not A; computed (checked by sampling).
- **Q30 — corrected:** PDF's step is labelled "C3→C3+C1" and shows a matrix (first row 1, i−ω, ω²; rows 2 and 3 identical) that cannot come from the given determinant by that operation. Valid step: R1→R1+R3 makes row 1 equal row 2. Answer 0 correct.
- All other questions — `pdf`: checked step by step and reproduced (a few lines expanded for clarity: Q3 oddness of p, Q4 z=0, Q5 choice of root, Q8 Vieta, Q9 "same value for q").

## Answer key
Every answer was checked numerically (see below). No wrong key value found. Notes:
- **Q23 / Q25:** key right, PDF working wrong or too coarse (above).
- **Q31:** the printed key reads "(A) q (B) p or pqrs and t; (C) s (D) t"; the correct entry for (B) is (p) (f(x)=x, f(π/6)=π/6). Also (D) asks for a "maximum" of |Arg(1/(1−z))| which is only a supremum (π/2, never attained) — the key (t) is the intended answer.
- **Q32:** (A)–(s), (B)–(t), (C)–(r), (D)–(r) all verified.
- **Q16:** the PDF text layer shows "sin + i cos"; the page image shows "sin − i cos", for which the key 48(1−i) is right (with + the sum would be 48(1+i)).
- Q1, Q3, Q4, Q6, Q11–13, Q15 (partly), Q17 (find k) — proofs/derivations have no single numerical key to compare.

## Alternate solutions and useful results
- **Alternates: 28 of 32 questions** (all except Q13, Q20, Q21, Q30). Each verified against the answer. Examples: Q2 scaling rows to 2I−N with N of rank one (det = −4); Q7 identity (a²+b²)³=(a³−3ab²)²+(3a²b−b³)²; Q9 coefficient comparison gives p²+2p=4 without trig; Q10 similar triangles; Q17 linear system with determinant 1+k³; Q22 Eisenstein units; Q24 parallelogram law; Q25 bounding y∈[1,4] instead of solving.
- **Questions with NO alternate (4), one line each:**
  - Q13 — every route (induction, binomial with e^{iθ}, symmetrising) is the same expansion of e^{iθ}(1+e^{iθ})^n; no genuinely different method.
  - Q20 — only the factorisation b(3a²−b²)=107 works; the modulus identity N²+107²=(a²+b²)³ gives a check, not a derivation (given as a useful result).
  - Q21 — the quadratic-factor form (x²−sx+p)(x²−s̄x+p̄) is the same computation as the elementary symmetric functions (given as a useful result).
  - Q30 — the only simplification is the row dependency R1+R3=R2; no different method.
- **Useful Result / Pattern: all 32 questions have 3–4 bullets.** Formulas were checked numerically (e.g. roots-of-unity filter classes mod 3 and mod 4 for n=1..15, alternating trig sum for Q13, norm counts for Q22).
- Weaker alternates (flagged for review): Q6 (divisibility by t⁵−2 uses the same expansions), Q26–Q28 (option elimination by small n, not a new derivation), Q32 (alternate covers only parts (A) and (B)), Q5 (guess-and-verify integer cube root).

## make_ppt.py warnings
- `Q26, Q27, Q28, Q31, Q32: very long question - font reduced` — harmless (long paragraph / two-column matching text); left as is.
- No "could not convert" warnings: all 1319 equations converted to native PowerPoint equations. No "fewer than 4 bullets" or missing-field warnings.

## Skipped / assumed
- No slide rendering or thumbnails (no soffice); deck not visually inspected.
- Figures of the PDF (Q10, Q15, Q19, Q24 diagrams) were not reproduced; the statements are given in words/LaTeX.
- Marks assumed as above. Types for Q1–22 (Numerical vs Subjective) chosen by the form of the answer.
- Q10: assumed z1z2 is a side of the square (a diagonal on the real axis would put a vertex outside the triangle).
- Q15: angle taken at the origin (see correction above).
- Verification scripts used numpy/scipy (answers, identities, alternates, filter formulas); sympy was not needed.
