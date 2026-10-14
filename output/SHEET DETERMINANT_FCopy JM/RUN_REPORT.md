# Run report — SHEET DETERMINANT_FCopy JM

Paper: `papers/SHEET DETERMINANT_FCopy JM.pdf` (30 pages, "Exercise J-M": 35 JEE Main previous-year questions on determinants / linear systems, 2023-24; Q1–18 and Q21–33 single-correct, Q19, Q20, Q34, Q35 numerical). The text layer loses all Greek letters and symbols, so everything was read from page images. Hindi text left out (English deck).

Files: `…_Analysis.pptx` (220 slides), `…_content.json`, `…_ratings.json`, `…_difficulty.xlsx`.

## Blueprint and marks
- **No blueprint was used. Concepts self-assigned (no blueprint) - please review.**
- The paper prints no marks. Assumed (JEE Advanced defaults, as instructed; also stated on the section dividers): **4 marks** for every question (single-correct Q1–18, Q21–33 and numerical Q19, Q20, Q34, Q35). Not a JEE Main scheme (+4 / −1), so the index is a plain mean of levels.

## Difficulty (jee-advanced-difficulty-calibrated)
- Marks-weighted difficulty index (adjusted): **2.14** (140 marks).
- Questions per level: Level 1 — 2 (Q1, Q10); Level 2 — 26 (Q2–5, Q7–9, Q11–18, Q21, Q23–29, Q32, Q34, Q35); Level 3 — 7 (Q6, Q19, Q20, Q22, Q30, Q31, Q33); Levels 0, 4, 5 — none.
- No equivalence-relation adjustment and no multi-correct floor applied (no such questions). Low is expected: these are JEE Main questions, below the 2.6–3.2 range of full Advanced papers. Confidence Medium for Q3, Q6, Q19, Q20, Q22, Q30, Q31, Q33; High for the rest. `recalc.py` skipped (no `/mnt/skills`), so Excel formula cells have no cached values until opened in Excel.

## Solutions: corrected / written (14 corrected, 0 written; the other 21 are `pdf`)
- **Q1 — corrected:** PDF's third elimination "(iv)×2 − (iii)×5" should read "(iv)×2 − (v)×5". Values and answer right.
- **Q2 — corrected (gap):** PDF prints $D=a(15a^2+31a+37)$ then "D ≠ a" (typo for ≠ 0) without showing why the quadratic has no real root; discriminant (−1259) added.
- **Q3 — corrected (gap + misprint):** PDF evaluates only D and D_x; option-wise verdicts added. English option (D) ("no solution for all α≠−1 and β=2") is a mistranslation of the Hindi ("has a solution") and is false as printed too; key (A) stands.
- **Q5 — corrected (gap):** PDF finds only α = 4 and never β; β = 14 (consistency) added. The second equation is misprinted "2a + 2y + αz = 8" (should be 2x).
- **Q6 — corrected (gap):** PDF stops after the three case conditions; all four options decided, and the single point (−25/2, −11/4) found.
- **Q7 — corrected:** PDF says "when λ = −2, D ≠ 0"; D(−2) = 0 (shown just above), it is D₁ ≠ 0. Answer 6 right.
- **Q9 — corrected:** PDF claims "No solution" for α = 2, β = −1; the system has the unique solution (3/4, 3/4, −5/4) (D = 4 ≠ 0). Option (D) is still the false one.
- **Q11 — corrected (key problem):** PDF stops at D = 6 − 2α. All four options are true as printed (see below).
- **Q22 — corrected (gap):** options not decided in the PDF; why (B) fails (μ = 15 is also consistent when λ = ½) added.
- **Q23 — corrected:** PDF factorises λ+1−2λ² as "(λ+1)(2λ+1)" and writes RHS "13+μ"; correct is −(λ−1)(2λ+1)z = μ−13 ⇒ (λ−1)(2λ+1)z = 13−μ.
- **Q26 — corrected (typo):** D₃ is printed with a 3 in the first row, third column; it must be the constant column (5, 9, μ). Its expansion already uses 5.
- **Q30 — corrected (typo):** last line "= A₁₀ = 4α + 2α" should be 4α + 2β.
- **Q33 — corrected (mislabel):** column operations "C₂ → C₂ + C₁" (twice) should be C₂ → C₂ − C₁ and C₁ → C₁ − C₃ to give the printed matrix.
- **Q35 — corrected (typos):** printed D_z has third column (λ, 4, 1) instead of the constants (3, 4, −1); printed D has 4 instead of 5 in row 2. Expansions that follow use the right numbers.
- All other questions — `pdf`: every step re-derived with sympy; a few lines expanded (e.g. consistency checks at roots in Q19; x-coefficient check in Q14).

## Answer key
- **Q11: key (D) looks wrong.** As printed, all four statements are true (α = 3, β = 14 gives infinitely many solutions; α = 3, β = 24 none; α = −3 unique for every β). The deck shows "Key: (D) — but all four statements are true as printed". The Hindi version of (A) ("का अद्वितीय हल नहीं …") seems to say "no unique solution", which would make (A) the answer; the English text does not.
- **Q3:** key (A) is right; English option (D) is also false as printed (translation slip, see above).
- Every other answer was verified by sympy (determinant / rank checks) and matches the key: Q1 C, Q2 B, Q4 D, Q5 D, Q6 D, Q7 B, Q8 C, Q9 D, Q10 D, Q12 B, Q13 B, Q14 A, Q15 D, Q16 C, Q17 A, Q18 D, Q19 24, Q20 6, Q21 D, Q22 B, Q23 B, Q24 D, Q25 C, Q26 D, Q27 D, Q28 A, Q29 B, Q30 A, Q31 B (as printed with γ in the last numerator), Q32 C, Q33 C, Q34 55, Q35 38.
- Q29 option (D) is printed "m² + n² − m n = 68" (likely "−m−n" or similar); transcribed as printed, it is false either way.

## Alternate solutions and useful results
- **Alternates: 33 of 35 questions** (all except Q2 and Q34). Each checked numerically (the multipliers / values used reproduce the answer). Main ideas: row-combination ($R_3=pR_1+qR_2$, Q1, Q4–6, Q17, Q24–26, Q28, Q29, Q32, Q33, Q35), elimination to $c\,z=d$ (Q3, Q10, Q11, Q13, Q16, Q22), rank-one update / matrix determinant lemma (Q8, Q14, Q31), Vieta/Descartes shortcut (Q19), summing after expanding (Q20), Cramer + 4×4 consistency determinant (Q15, Q18), column operation (Q30), adding equations (Q7, Q9), eliminating x first (Q27), R₁−R₂ simplification (Q21). Weaker alternates (flagged for review): Q21 and Q27 use the same criterion as the main method with a shorter reduction; Q15 (Cramer vs. the PDF's elimination) is a different route to the same pair of conditions.
- **Questions with NO alternate (2):**
  - Q2 — the only task is to show a cubic determinant never vanishes; positivity of the quadratic factor is the same step as the main solution (no different method).
  - Q34 — the only route is expanding the 3×3 determinant (scalar triple product / Sarrus is the same expansion).
- **Useful Result / Pattern: all 35 questions have 4 bullets.** Formulas checked on a numerical case (e.g. Q1, Q4, Q6, Q9, Q14, Q16, Q17, Q20, Q30, Q31, Q34 checks are written in the bullets).

## make_ppt.py warnings
- `note: Q4: very long question - font reduced to 22 pt.` — harmless (the system and the second system are in one stem); accepted.
- `could not convert $(\lambda-1)(2\lambda+1)=…$` appeared once because of a stray leading space inside the dollars (Q23 results); fixed by removing the space, rebuilt: no remaining warnings. 1220 equations converted to native PowerPoint equations.

## Skipped / assumed
- No slide rendering or thumbnails (no soffice); deck not visually inspected.
- Marks assumed 4 for all questions (see above). Types: Q19, Q20, Q34, Q35 as "Numerical", the rest "Single Correct".
- Chapter set to "Determinant" for all questions in the Excel report. Q8 (range of sine), Q12/Q27 (trig equations), Q14/Q5/Q21 (quadratic roots), Q18 (point–plane distance), Q20 (sums) carry a second concept from another chapter, listed separately in the deck.
- Q11's answer is shown as "Key (D)" with the discrepancy stated in the solution, not changed to another option (the English text has no false statement).
- Verification used sympy / plain Python.
