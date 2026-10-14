# Run report — SHEET DETERMINANT_FCopy C2

Paper: `papers/SHEET DETERMINANT_FCopy C2.pdf` (19 pages, "Exercise C - II", 24 questions: Q1–16 subjective / numerical, Q17–19 paragraph set 1, Q20–22 paragraph set 2, Q23–24 paragraph set 3). The text layer loses many symbols, so the maths was read from page images. Hindi text left out (English deck).

Files: `…_Analysis.pptx` (150 slides), `…_content.json`, `…_ratings.json`, `…_difficulty.xlsx`.

## Blueprint and marks
- **No blueprint was used. Concepts self-assigned (no blueprint) - please review.**
- The paper prints no marks. Assumed (JEE Advanced defaults), also stated on the section dividers: **4 marks** for Q1–16 (subjective / numerical; Q1, Q3, Q6 labelled "Numerical Type", the rest "Subjective Type"), **3 marks** for Q17–24 (paragraph based single correct).

## Difficulty (jee-advanced-difficulty-calibrated)
- Marks-weighted difficulty index (adjusted): **2.45** (88 marks).
- Questions per level: Level 1 — 2 (Q22, Q23); Level 2 — 11 (Q1, Q2, Q4, Q7, Q13, Q14, Q15, Q18, Q20, Q21, Q24); Level 3 — 10 (Q3, Q5, Q6, Q8, Q9, Q10, Q11, Q12, Q17, Q19); Level 4 — 1 (Q16); Levels 0 and 5 — none.
- No equivalence-relation adjustment and no multi-correct floor applied (no such questions). Confidence Medium for Q3, Q6, Q8–Q12, Q16, Q17, Q19; High for the rest. `recalc.py` was skipped (no `/mnt/skills`), so formula cells in the Excel file have no cached values until it is opened in Excel.

## Solutions: corrected / written (11 corrected, 3 written; Q2, Q9, Q10, Q12, Q14, Q15, Q20–Q24 are `pdf`)
- **Q1 — corrected:** the PDF names only $C_1\to C_1-C_2$ but the determinant it prints needs also $C_2\to C_2-C_3$; both are now named.
- **Q3 — corrected:** (i) sign slip "x cos p + y sin p = cos q" (should be −); (ii) cancelling cos q − sin q − 1 needs cos q − sin q ≠ 1, which "sin q ≠ cos q" does not guarantee (q = 0: equations 1 and 3 coincide, x²+y²+z² not fixed). Key 2 stands under the extra assumption.
- **Q4 — written:** the solution printed under Q4 is Q5's (system with k); a fresh solution was written. Printed answers are right.
- **Q5 — corrected (gap):** PDF asserts infinite solutions at k = 2 without checking consistency; check added. All values and key right.
- **Q6 — corrected (gap):** PDF only treats numerator d−2b = +1; added numerators ≥ 2 and −1 (with ad−bc<0). Answer 19 confirmed by brute force over all 120 choices.
- **Q7 — corrected:** PDF says "subtract" where the arithmetic is addition; no check of the third equation at λ = −5; key prints "λ = 5" for λ = −5. Fixed.
- **Q8 — corrected:** sign errors: D = −(a−b)(b−c)(c−a) (PDF: +); D1 and D3 also wrong in sign; with PDF's D, y comes out −(ab+bc+ca), contradicting its own key. Corrected values give the key.
- **Q11 — corrected:** PDF drops the ± when taking the square root of Δ² (only Δ² is determined; the claimed identity holds up to sign); typo cz3 in the second determinant.
- **Q13 — corrected (gap):** consistency at λ = 5 was asserted from D = D1 = D2 = D3 = 0; third-equation check added.
- **Q16 — written:** PDF only quotes the identity and the row expansion, ending "= 0" with no proof; the cancellation of the six products was written out and checked numerically.
- **Q17 — written:** PDF only says "put x = y/r, z = yr ⇒ y = 1"; factorisation of Δ and the algebra to y⁴ = 1 written.
- **Q18 — corrected:** PDF assumes the roots are in G.P. (x = y/r, z = yr), not given; replaced by AM–GM (sum 21, product 343). Answer unchanged.
- **Q19 — corrected:** PDF takes x = y = z = 1 ("d = 0"), which is not valid (x = y = z = t gives Δ = 0 for every t, and 2xy²z+x²z² = 3t⁴). Correct argument for distinct x, y, z: xyz(xy+yz+zx) = x+y+z and A.P. ⇒ xz(2y²+xz) = 3.
- All other questions — `pdf`: checked step by step (sympy / numerics) and reproduced; a few lines expanded for clarity (Q9 scaling step, Q10 final expansion, Q12, Q20–Q22 individual determinants).

## Answer key
Every answer was checked symbolically or numerically. No wrong final key value; notes:
- **Q7:** the key prints "If λ = 5" where λ = −5 is meant (the printed solution is for −5).
- **Q3 / Q19:** key values 2 and 3 hold only under an extra condition (cos q − sin q ≠ 1; x, y, z distinct, as in Q17) that the question as printed does not state.
- **Q11:** the stated identity holds only up to sign.
- Q1, Q2, Q9, Q10, Q12, Q14–Q16 are proofs / derivations with no numerical key.

## Alternate solutions and useful results
- **Alternates: 21 of 24 questions** (all except Q17, Q18, Q19). Each verified (sympy / numerically). Examples: Q1 sum of the three equations (x = a s/(1+a)); Q2 cyclic identity on p=y−z etc.; Q8 Vieta (a,b,c are the roots of t³+xt²+yt+z); Q9 rank-one update of scalar matrix; Q10 Vandermonde via R2 − (p+q+r)R3; Q12 row operation + Cauchy–Binet; Q15 orthogonal rows MMᵀ = (1+a²+b²)²I; Q20–22 elimination E1 − 2E3 = (a−2)y; Q24 equal row sums.
- **Questions with NO alternate (3), one line each:**
  - Q17 — the only route is to factor Δ as V·[xyz(xy+yz+zx) − (x+y+z)] and substitute the G.P.; checking y = 1 against the options is not a derivation.
  - Q18 — AM–GM equality is the unique route (the PDF's G.P. substitution is invalid); no second method.
  - Q19 — same factorisation as Q17 with an A.P.; parametrising x = y−d, z = y+d only repeats the same algebra with heavier expansion.
- **Useful Result / Pattern: all 24 questions have 4 bullets.** Formulas checked numerically (e.g. Q1 condition ab+bc+ca+2abc = 1, Q10 half-angle identities, Q15 det at a=1,b=0, Q17 Schur-type determinants, Q19 numeric example y = 1.3).
- Weaker alternates (flagged for review): Q11 (eigenvalue view of (d−f)I+fJ replaces only the last stage of the main method), Q16 (permutation-sign regrouping of the same cancellation), Q23 (domain argument is trivial; the closed form is given as a check).

## make_ppt.py warnings
- None. "838 equations converted to native PowerPoint equations"; no "could not convert", no "fewer than 4 bullets", no missing-field warnings.

## Skipped / assumed
- No slide rendering or thumbnails (no soffice); deck not visually inspected.
- Marks assumed as above; Q1, Q3, Q6 typed "Numerical", other Q1–16 "Subjective" (build_report type "Numerical" for all of Q1–16, "Para SCQ" for Q17–24).
- Q17–19 follow the paragraph header; Q19 assumes x, y, z distinct (stated in Q17 only).
- Q16 assumes all tangents are defined; Q9 assumes abc ≠ 0 in the scaling step (the result holds as a polynomial identity regardless).
- Verification used sympy / plain Python (answers, determinant factorisations, alternates).
