# Run report — SHEET BINOMIAL THEOREM_FCopy JM

Paper: `papers/SHEET BINOMIAL THEOREM_FCopy JM.pdf` (42 pages, 73 questions, all Binomial Theorem: Q1–10, 26–41, 49–52, 61–67 single correct; Q11–25, 42–48, 53–60, 68–73 numerical). Numbering is continuous 1..73 (the PDF's labels for Q57 and Q69 are not printed in its text layer but they are in the images).

Files in this folder: `…_Analysis.pptx` (384 slides), `…_content.json`, `…_ratings.json`, `…_difficulty.xlsx`.

## Blueprint and marks
- **Concepts self-assigned (no blueprint) - please review.** (`blueprints/SHEET BINOMIAL THEOREM_FCopy JM.xlsx` does not exist.)
- The paper prints no marking scheme. Marks assumed (JEE Advanced defaults): **4 marks for every single-correct question and 4 marks for every numerical/integer question** (all 73 questions are 4 marks). This is stated on every section divider (8 sections).

## Difficulty (jee-advanced-difficulty-calibrated)
- Marks-weighted difficulty index (adjusted): **1.90** (all marks equal, so it equals the mean level). This is a JEE Main chapter sheet, so it sits far below the official JEE Advanced range (2.59–3.21), as expected.
- Questions per level: Level 1 — 23 (Q1, 4, 6, 9, 11, 14, 17, 22, 25, 27, 32, 37, 39, 40, 42, 43, 47, 49, 52, 55, 61, 65, 73); Level 2 — 36; Level 3 — 12 (Q12, 19, 24, 28, 31, 46, 51, 57, 58, 66, 68, 72); Level 4 — 2 (Q60, Q70); Levels 0 and 5 — none.
- No equivalence-relation adjustment and no multi-correct floor applied (no such questions).
- Low-confidence rating: Q35 (no option fits; indexing from the end trips students). Several Medium-confidence ratings are in the workbook.
- Excel built with `build_report.py`; `recalc.py` was skipped (no `/mnt/skills`), so formula cells have no cached values until opened in Excel.

## Solutions: `corrected` (18) — one line each; none were `written`
- **Q2** — PDF line '15·10!/(30!)² = α·60!/(30!)²' has a typo (10! for 60!); answer 15 correct.
- **Q12** — PDF drops the sign: '(−1)^r 9Cr 2^(3r−9) = 21×4' must be −84; the 'only r = 3 works' step made explicit.
- **Q14** — PDF working gives 405 but its printed answer is 406 (answer key wrong, see below).
- **Q16** — PDF '−72023 = −7×7^2022' is a typo for −7^2023 and the jump from remainder 1 mod 5 to 7 mod 35 was unexplained; made explicit.
- **Q19** — PDF's last line (5e + e/2 − 1/e − e/2 + 1/2e) is garbled and the n = 0 term convention (1/(−1)! = 0) is missing; rewritten cleanly (answer 26 correct).
- **Q22** — PDF writes [2124 + 1]^19; should be 3124 + 1 (= 11·284 + 1). Answer 9 correct.
- **Q27** — PDF's final equation '11C5 (ab)^6 (1/2b)^5 = 32' is garbled; correct equation a⁶/(32b⁵) = a⁵/(729b⁶) gives 729ab = 32.
- **Q28** — PDF's own working shows 13·13^n − 11n − 13 ≡ n (mod 144), i.e. S2 is TRUE (n = 144m), yet the printed key is (D). Correct answer is (A) (answer key wrong).
- **Q32** — '(9x)^(13−r)' typo for (ax); rest correct.
- **Q38** — bracket '… − C9' should end at −C49; answer −99C49 correct.
- **Q43** — 7·3⁶/4 evaluated as 1275.85; it is 1275.75 (floor 1275 unchanged).
- **Q46** — n = 4 found 'by observation' without excluding n = 8, 12; α = −24, coefficient 4C3(−6)³ = −864 and λ = 36 were not written. Added.
- **Q48** — list 'n = 1, 7, 13, 20, …' has a typo (20 should be 19). Count 15 correct.
- **Q60** — Case I table row (4, 3, 8) should be (6, 3, 8); the numerical terms are right. Answer 678 correct.
- **Q62** — '12n − 40' should be '12n − 48'; resulting quadratic n² − 21n + 98 = 0 is the one the PDF states.
- **Q64** — PDF uses (n+1)/(r+1) = 55/34, n/r = 35/21 and '3n − 5r = 4'; correct are 55/35 and r/n = 21/35, so 3n − 5r = 0. Final n = 10, r = 6 correct.
- **Q65** — last line garbled ('= 5×7×3 z'); should read 210·a³/16 = 105.
- **Q72** — '140 < 2α/β < 248' typo for 281 (next line uses 281). n = 5 correct.
- All other questions: `pdf` — the working was checked step by step and reproduced (notation converted to LaTeX; a few compressed steps spelled out).

## Answer key problems
- **Q14**: key says 406; correct answer is **405** (the PDF's own working gives 405). Deck uses 405.
- **Q28**: key says (D) only S1 correct; correct answer is **(A)** both correct (checked numerically: 13^(n+1) − 11n − 13 ≡ n mod 144). Deck uses (A).
- **Q35**: key says '10 (Bonus)'. The PDF's own working gives |x| = 5/16, which is not among the options (8, 12, 10, 15). Deck answer: none of the options, |x| = 5/16 (Bonus).
- **Q51**: key says Bonus; I confirm the data are inconsistent (Pascal's rule forces C(2r+4, r+1) = 2, impossible). Deck answer: none/Bonus.
- Every other printed answer was verified by Python (exact arithmetic / sympy / numerical series) and is correct.

## Alternate solutions and useful results
- **Useful Result / Pattern slides: all 73 questions have them (2–5 bullets each).**
- **Alternates: 50 of 73 questions (Q1–Q73 except those listed below).** Each was checked against the answer. Examples of genuinely different methods: Q4 counting 4-subsets by their largest element; Q8 Lucas-type recurrence for pⁿ + qⁿ; Q10 and Q19 operator/Bell-number (Touchard) methods; Q37 integration of (1+x)ⁿ; Q60 palindromic symmetry (x³⁶ ↔ x⁸); Q66 G.P. sum; Q68 integrating an exponential generating function; Q70 integrating twice; Q62 Pascal's rule twice.
- Weaker alternates, flagged for review: **Q49** (special value n = 1, valid only because the question is single-correct), **Q11, Q14, Q30, Q40, Q42, Q43, Q65, Q69** ('clear the denominator' technique — a different calculation but close in spirit to the main one), **Q6, Q17, Q27, Q32** (factor out the denominator so only ab appears — genuinely shorter), Q18/Q29/Q36 (the (n+1)/k − 1 form of consecutive-coefficient ratios, a reparametrisation).
- **Questions with NO alternate (23) and why:**
  - Q12 — constant-term condition then coefficient; only one route.
  - Q24 — A.P. of binomial coefficients and a quadratic in 3^x; only the standard route.
  - Q25 — single exponent equation, r = 4 and C(22,4) = 7315.
  - Q26 — 'from the end' indexing, ratio collapses to 6^((n−8)/4); same computation any way.
  - Q33 — reduction mod 3 and mod 7 is already the minimal method.
  - Q35 — from-end ratio, a single route (and the question has no valid option).
  - Q39 — one congruence, 4² ≡ 1 (mod 15).
  - Q44 — multinomial casework is the only practical route (the factorisation (1+x)(1−2x+2x²) is heavier).
  - Q45, Q56 — counting r by divisibility; single method.
  - Q46 — conditions fix n = 4 by search; no other route.
  - Q48 — order of 3 mod 7 is the only route.
  - Q50 — absorption identity then bounding (r+1)/n; only route.
  - Q51 — data inconsistent (Bonus); nothing to solve.
  - Q52 — symmetry of C(18,6) = C(18,12) then a ratio; any other route repeats the same calculation.
  - Q53 — (1−x)(1+x+x²) = 1−x³ then residues mod 3; only route.
  - Q57 — absorption + Vandermonde is the only clean route.
  - Q61 — divisibility conditions on r leave r = 0, 15; single method.
  - Q63 — general term with surds; single method.
  - Q64 — absorption ratios for three coefficients; only route.
  - Q67 — two fractional-exponent general terms; only route.
  - Q71 — consecutive-term ratios; only route.
  - Q72 — moment identities and integration identity; other routes use the same identities.

## make_ppt.py warnings
- `Equations: 2303 converted to native PowerPoint equations.` No "could not convert" messages, no LaTeX left as text.
- `note: Q42 and Q55: only 3 solution bullets` — harmless: the PDF's complete working for these two is three lines long (Q42: one general-term step, Q55: (9−1)^(2t) = 9k+1). Left as is.
- No other warnings.

## Skipped / assumed / guessed
- Pages were read from rendered images (the text layer garbles all maths). No rendering of the finished deck was possible (no soffice in this environment), so the slide layout was not visually checked; the builder reported no overflow notes.
- Chapter for every question is 'Binomial Theorem' in the ratings workbook; concepts such as exponential series (Q10, Q19, Q68), logarithmic series (Q70) or number-theory remainders were kept as concept names inside the same chapter list (single entry or two entries where the topics are from different chapters).
- Difficulty levels were assigned relative to the calibrated anchors (JEE Advanced), so most questions of this JEE Main sheet land at Levels 1–2.
- For the questions with no printed marks, 4 marks each was assumed (stated on the section dividers).
