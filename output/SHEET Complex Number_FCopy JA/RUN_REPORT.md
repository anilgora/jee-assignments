# Run report — SHEET Complex Number_FCopy JA

Paper: `papers/SHEET Complex Number_FCopy JA.pdf` (30 pages, "Exercise J - A", the JEE Advanced exercise: 2012-2026 questions). Deck numbering Q1–Q31: Q1 SCQ, Q2–Q3 one-or-more correct, Q4–Q5 paragraph (one passage), Q6 SCQ, Q7–Q8 matching (Q8 has four sub-parts, kept as one matching question), Q9–Q10 integer, Q11–Q14 one-or-more correct, Q15 SCQ, Q16 numerical, Q17 MCQ, Q18 numerical, Q19 MCQ, Q20 SCQ, Q21–Q22 numerical, Q23 MCQ, Q24 numerical, Q25 matching, Q26 numerical, Q27–Q28 MCQ, Q29 numerical, Q30 MCQ, Q31 matching. The text layer garbles the maths, so everything was read from page images; Hindi text left out (English deck).

Files: `…_Analysis.pptx` (231 slides), `…_content.json`, `…_ratings.json`, `…_difficulty.xlsx`.

## Blueprint and marks
- **No blueprint was used** (`blueprints/` has no file for this paper). **Concepts self-assigned (no blueprint) - please review.**
- The paper prints no marks. Assumed (JEE Advanced defaults, also stated on the section dividers): **4 marks** for single-correct, one-or-more-correct, integer and numerical questions; **3 marks** for paragraph-based (Q4, Q5) and matching (Q7, Q8, Q25, Q31). Total 118 marks.

## Difficulty (jee-advanced-difficulty-calibrated)
- Marks-weighted difficulty index (adjusted): **2.79** (118 marks), inside the official JEE Advanced range of 2.59–3.21.
- Questions per level (adjusted): Level 1 — 2 (Q1, Q28); Level 2 — 8 (Q2, Q7, Q9, Q11, Q12, Q16, Q21, Q22); Level 2.5 — 1 (Q3); Level 3 — 16 (Q4, Q5, Q6, Q8, Q10, Q13, Q14, Q15, Q17, Q18, Q19, Q20, Q24, Q25, Q27, Q31); Level 4 — 2 (Q23, Q29); Level 5 — 2 (Q26, Q30); Levels 0 — none.
- **Official questions reused your own ratings** (they are in the anchor bank): Q19 (2021-P1-Q16, L3), Q20 (2021-P1-Q4, L3), Q24 (2023-P1-Q11, L3), Q25 (2023-P1-Q17, L3), Q26 (2023-P2-Q11, L5), Q27 (2024-P1-Q5, L3), Q28 (2025-P1-Q7, L1), Q29 (2025-P2-Q13, L4), Q30 (2026-P2-Q9, L5), Q31 (2026-P1-Q13, L3). Because the paper here has no printed marks I used 3 marks for the matching items (the original papers' marks differ); the levels are unchanged. The other 21 questions I rated myself with nearest anchors.
- Multi-correct floor 2.5 applied to Q3 (level 2 raised to 2.5; matrices + cube roots of unity). For Q13, Q14, Q27, Q30 the floor is already met. No equivalence-relation adjustment (none involved).
- Low confidence: Q23 (no close anchor). Medium: most self-rated questions.
- `recalc.py` skipped (no `/mnt/skills`), so the Excel formula cells have no cached values until opened in Excel.

## Solutions: corrected / written
`written` (2): 
- **Q5 — written:** the PDF has no solution (blank "Sol."), only a stray distance expression at the end of Q4. Wrote the full solution (distance from (1,−3) to the line √3x+y=0, foot of perpendicular inside S).
- **Q15 — written:** blank "Sol." in the PDF. Wrote the full solution (nearest point of the exterior of the circle to 1, then the argument of −i = −π/2).

`corrected` (14):
- **Q1:** PDF says only a ≠ 3/4; the exact condition is a < 3/4 (a > 3/4 also gives real roots). Answer unchanged.
- **Q3:** PDF proves only "3 | n ⇒ P² = 0"; the converse (sum ≠ 0 when 3 ∤ n) added.
- **Q4:** PDF has S1 centred at (0,1) (it is the origin), numerator (x−1)+i(y−√3) with denominator 2 (should be i(y+√3), denominator 4) and mentions the point (1,−3) in the area part. Fixed; the line √3x+y=0 and area 20π/3 unchanged.
- **Q10:** PDF "r ≠ odd" (must be "r odd") and a jump to r = s = 1 without case check (r = 3, s = 2, 3). Added.
- **Q11:** PDF never examines option (B). Verdict added (centre 1/(2a), not −1/(2a)).
- **Q13:** PDF (C) has a typo (Arg(z1/z) = Arg z1 + Arg z2 + 2nπ instead of Arg(z1/z2) = Arg z1 − Arg z2 + 2nπ) and (D) is just "If is circle" (text lost). Rewritten.
- **Q14:** PDF's argument is only sketched and the last case is an unfinished chain of equalities; case analysis rewritten (determinant |s|²−|t|²; counter-example s = t = 1, r = i for (B)).
- **Q16:** PDF puts (1,2,3) and says "minimum = 3" without showing nothing smaller exists; the bound (largest gap ≥ 2) added.
- **Q17:** PDF does not say why (A) and (D) fail; verdicts added (|z+½| can equal √7/2 > ½; S is infinite).
- **Q20:** PDF claims the maximum for Q occurs at equal angles; |sin| is not concave on (0, 2π), so Jensen's inequality does not apply. Replaced by the rigorous bound |sin θ| ≤ θ (gives ≤ 4π). Answer unchanged.
- **Q23:** PDF proves only the necessary condition r⁴ + 1/r⁴ ∈ ℤ; added the check that (A) is actually attained (43 + 2 = 45 = 6² + 3²).
- **Q26:** PDF writes the vertices as 2e^{irπ/8}; for a regular octagon it is 2e^{irπ/4}. Fixed; the rest and the answer 512 are the PDF's.
- **Q27:** see answer-key note below (option (A) is printed with "=" instead of "⊂").
- **Q31:** PDF (R) takes γ−1 = −ω² (it is ω) and gets the right sum −1 only by luck; (S) stops at p³+r³ = −4 without finishing the fraction. Both corrected; key C unchanged.
- All other questions (Q2, Q6, Q7, Q8, Q9, Q12, Q18, Q19, Q21, Q22, Q24, Q25, Q28, Q29, Q30) — `pdf`: checked line by line and reproduced (a few steps expanded for clarity).

## Answer key
- **Q27: the key looks inconsistent with the printed question.** Option (A) is printed as "ℤ ∪ T₁ ∪ T₂ = S"; the PDF's own solution proves only "⊂ S", and the key is ACD. With "=" (A) is false (√2 ∈ S is not in ℤ ∪ T₁ ∪ T₂: every element of T₁ ∪ T₂ has p² − 2q² = ±1 but √2 has −2), so the correct answer for the question as printed is **(C, D)**. I kept (C, D) in the deck and wrote the condition under which the key (A, C, D) holds ("⊂") in the answer box and the correction note. Please decide which reading you want.
- All other answers were checked (numerically in Python where possible: Q6, Q10, Q15–Q18, Q20–Q26, Q29–Q31, plus the alternates) and the key is correct: Q1 D, Q2 CD, Q3 BCD, Q4 B, Q5 C, Q6 C, Q7 C, Q8 as printed, Q9 4, Q10 1, Q11 ACD, Q12 BD, Q13 ABD, Q14 ACD, Q15 B, Q16 3, Q17 BC, Q18 8, Q19 BD, Q20 C, Q21 0.50, Q22 4, Q23 A, Q24 281, Q25 B, Q26 512, Q28 AD, Q29 −2, Q30 BD, Q31 C.
- Q6: the PDF text layer drops the bar; the page image shows 1/ᾱ (conjugate). With 1/α (no bar) the stated answer would not follow, so ᾱ was used.
- Q7: options (B) and (D) are identical in the paper as printed (kept as printed); the key (C) is unaffected.
- Q5: min over S is an infimum (attained only on the boundary line, which S excludes); reported as the minimum as the key does.

## Alternate solutions and useful results
- **Alternates: 30 of 31 questions** (all except Q9). Each verified against the answer (numerically or symbolically). Examples: Q1 real/imaginary parts give x = −½ and a = ¾ − y²; Q3 rank-one P = uuᵀ; Q6 identity |1 − āb|² − |a − b|² = (1 − |a|²)(1 − |b|²); Q10 Cayley–Hamilton (P² = −det P·I for trace 0); Q12 a − 1/(z+1); Q14 determinant of the real-linear map z ↦ sz + t z̄; Q20 chord ≤ arc; Q22 polar form; Q26 product of sines identity; Q28 Apollonius formula; Q29 period 6; Q30 Möbius viewpoint; Q31 1/(α+1) = −α, 1/(p+1) = p.
- **Question with NO alternate (1):** **Q9** — every term |α_{k+1} − α_k| is the same chord, so the only possible method is the one given (equal chords, ratio of counts 12/3); an arc-length or geometric restatement would be a reworded copy. Useful results given.
- Weaker alternates (flag for review): Q2 (exponent arithmetic mod 12 is close to the main method), Q5 (quadratic minimisation vs perpendicular distance), Q21 (polar form vs conjugate method), Q13 (alternate covers (B) and (D) only), Q8 (covers (A) and (D) only), Q7 (covers (R), (S) only; (P), (Q) are one-liners).
- **Useful Result / Pattern: all 31 questions** have 3–4 bullets; formulas were checked on at least one numerical case (e.g. Σ over roots of unity, Eisenstein norm values, Apollonius centre, Q20 sums).

## make_ppt.py warnings
- `Q7, Q8, Q25, Q31: very long question - font reduced to 20 pt` — harmless (long matching text); left as is.
- No "could not convert" warnings: all 1434 equations converted to native PowerPoint equations. No "fewer than 4 bullets" or missing-field warnings.

## Skipped / assumed
- No slide rendering or thumbnails (no soffice); deck not visually inspected.
- Figures printed in the PDF (Q2, Q4, Q13 diagrams) were not reproduced; statements are in words/LaTeX.
- Marks assumed as above. Q8 (four sub-parts) kept as one matching question with one level. Q4/Q5 share the paragraph text.
- Chapter for Q31 is Quadratic Equation (self-assigned) in the ratings file; deck concepts are self-assigned and need your review.
- Verification scripts used numpy only (scipy not installed).
