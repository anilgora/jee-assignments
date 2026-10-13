# Run report — SHEET CIRCLE LINE_FCopy JM

Paper: `papers/SHEET CIRCLE LINE_FCopy JM.pdf` (Exercise J-M, JEE Main 2023–2024 questions, 37 questions, all Circle).
Files: `_content.json`, `_Analysis.pptx` (225 slides), `_ratings.json`, `_difficulty.xlsx`.

## Blueprint
No blueprint was supplied. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none are printed in the paper): 4 for every single-correct question and 4 for every numerical (integer-answer) question, stated in the section dividers. 28 single-correct (SCQ) and 9 numerical questions.

## Difficulty (jee-advanced-difficulty-calibrated)
- Marks-weighted difficulty index: **1.97** (all questions 4 marks; no equivalence-relation or multi-correct adjustments apply).
- Level 1: 9 questions · Level 2: 20 · Level 3: 8 · Levels 0, 4, 5: none.
- Lowest-confidence ratings: Q4 (excircle ambiguity) and Q37.
- Index is far below official JEE Advanced (2.6–3.2) as expected for a JEE Main exercise.

## Solutions whose source is `corrected` (5)
- Q1: PDF's last line says θ3 = π/2; should be θ2 = π/2. Answer (D) unchanged.
- Q4: PDF assumes the incircle only. An excircle is also tangent to the three lines (excentre opposite B gives h+k = 5+5√2, i.e. option D). Kept official answer (A) and added a remark bullet.
- Q14: PDF's second centre/radius are wrong: it gives (28/3, −109/2) and r ≈ 49.78; correct is (28/3, −109/9), r = 80/9 ≈ 8.89 (still rejected since r < 8). Answer 7 unchanged.
- Q23: PDF writes (x−4)²+(y−2)²=20; correct is (x−8)²+(y−2)²=68. The centre (8,2) used afterwards is right; answer 18 unchanged.
- Q27: PDF solution prints the point as (−22/7, 4) instead of (−22/7, −4) (the line 7x−3y+10=0 it obtains is the right one), and its key says "B" for a numerical question; the answer is 2.
No question needed a `written` solution (every question had a PDF solution). Q16's PDF solution is cut off at the page footer; its last line was completed from the visible working (b²+b−a²=3), marked `pdf`.

## Answer-key concerns
- Q16: key printed as "C" but it is a numerical question; correct value **3**.
- Q27: key printed as "B"; correct value **2**.
- Q4: key (A) 5 is right for the incircle but (D) 5(1+√2) is also attained by an excircle (question is ambiguous).
- Q30: other side of the centre gives 3+√2 (not an option); (C) 3−√2 matches the key.
- Q28: the angle is taken as the principal value of sin⁻¹ (cosθ = +1/8, α = 6); the obtuse case (α² = 46) also gives (αβ)² = 1575, so the answer is unaffected.
- Q35: the PDF text prints "15/α"/"15/α−6" where 15/2 is meant (rendering quirk); used 15/2.

## Alternates and results
- Alternate solutions given for **34** questions (all except Q31, Q33, Q34). Each checked numerically/symbolically against the answer.
- No alternate (genuinely different method not available):
  - Q31: distance from external point to circle is d − r; only the 3-4-5 arithmetic remains.
  - Q33: any route (radical axis, equal tangent lengths, power of a point) is the same computation.
  - Q34: inradius and inscribed-square formulas are the only sensible route; other forms merely reword them.
- **Useful Result / Pattern given for all 37 questions.**

## make_ppt.py warnings
- Q31: "only 3 solution bullets" → fixed by splitting the solution into 5 steps. Rebuilt: no remaining warnings; 1125 equations converted natively, none left as LaTeX text.

## Skipped / assumed / guessed
- No rendering or thumbnails (no /mnt/skills; not required here), so layout was not visually inspected; the build ran without overflow warnings.
- Concepts and marks self-assigned as stated above. Excel recalculation step skipped (no recalc.py); formulas are live.
- Several alternates use classical results (Stewart's theorem, power of a point, pole–polar inversion, area-two-ways); each was spot-checked numerically in Python.
