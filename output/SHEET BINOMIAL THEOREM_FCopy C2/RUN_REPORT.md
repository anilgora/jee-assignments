# Run report — SHEET BINOMIAL THEOREM_FCopy C2

Paper: `papers/SHEET BINOMIAL THEOREM_FCopy C2.pdf` (19 pages, "Exercise C-II", 20 questions: Q1–13 subjective/integer, Q14–19 comprehension (two paragraphs), Q20 match-the-column). The text layer lost the maths symbols, so every page was read as an image. Hindi translations were left out (English deck).

Files: `…_Analysis.pptx` (126 slides), `…_content.json`, `…_ratings.json`, `…_difficulty.xlsx`.

## Blueprint and marks
- **No blueprint was used. Concepts self-assigned (no blueprint) - please review.**
- The paper prints no marks. Assumed (JEE Advanced defaults), stated on the section dividers: **4 marks** for Q1–13 (subjective / integer / numerical, incl. the three "prove/show" questions Q5, Q7, Q9), **3 marks** for Q14–19 (paragraph single-correct) and **3 marks** for Q20 (matching).

## Difficulty (jee-advanced-difficulty-calibrated)
- Marks-weighted difficulty index (adjusted): **2.45** (179 / 73) — below the official Advanced range 2.59–3.21, as expected for a chapter sheet.
- Questions per level: Level 1 — 2 (Q7, Q17); Level 2 — 8 (Q1, Q2, Q4, Q5, Q8, Q11, Q15, Q19); Level 3 — 9 (Q3, Q6, Q9, Q12, Q13, Q14, Q16, Q18, Q20); Level 4 — 1 (Q10); Levels 0 and 5 — none.
- No equivalence-relation adjustment and no multi-correct floor (no such questions).
- Confidence Medium for most, High for Q1, Q7, Q11, Q15, Q17, Q19. Proof questions (Q5, Q7, Q9) were rated as Numerical-type (no proof type in the anchor vocabulary).
- Excel built with `build_report.py`; `recalc.py` skipped (no `/mnt/skills`), so formula cells have no cached values until opened in Excel.

## Solutions: corrected / written (none were `written`)
- **Q5 — corrected (omission):** part (d) ends "1/(n+1){1}" without saying why the bracket is 1; added (alternating sum of C(n+1,j) is 0). (a)'s factorial form replaced by the equivalent ratio C(n,r)/C(n,r−1) = (n−r+1)/r.
- **Q7 — corrected (omission):** the PDF stops at 2S = 2^{2n} − C(2n,n) and has no answer line; added ΣC_i² = C(2n,n) and the expansion into the required form. Note the printed statement "2n!/(2(n!)²)" is only true if read as (2n)!/(2(n!)²).
- **Q8 — corrected (omission):** added the check over divisors k of 200 showing 16+50 = 66 is the minimum. Answer unchanged.
- **Q9 — corrected (garbled working):** part (b)'s printed lines are garbled (exponent n(n+1)/2 − 1 shown as (n²+n−2)/2, factor not explained); restated as P(1/x) = P(x)/x^N. Part (c) both equations shown. Only part (a) is given on the answer line.
- **Q10 — corrected (working wrong, key right):** PDF writes 5^89{5+25+125}; (x{x})² is 5^178, not 5^89·25. Correct: y+y²+y³ with y = 5^89, reduced mod 31 using 5³ ≡ 1. Remainder 0 unchanged (checked numerically).
- **Q11 — corrected (working wrong, key right):** PDF solves t³ = 3^12 as t = 3^9 (|x−2| = 9, x = 11, −7). Correct t = 3^4, |x−2| = 4, x = 6, −2. Sum 4 is the same either way.
- **Q13 — corrected (garbled working):** the root-of-unity filter step was a garbled list; restated step by step. Answer 2 unchanged (checked n = 1…6).
- **Q15 — corrected (notation):** PDF's index i in the greatest-term formula is the r of T_{r+1} (gets i = 4) and then says "5th term"; restated with r = 4, term number 5. Answer (B) unchanged.
- **Q16 — corrected (working wrong, key right):** PDF says "greatest coefficient will be the middle term"; the coefficients of (1+2x)^8 are C(8,r)·2^r, whose maximum is a tie at r = 5, 6 (terms 6 and 7), sum 13 — key (D) is right, the stated reasoning is not.
- **Q20 — corrected (working wrong, key right):** (C) is first marked "→ Q" and uses the false identity x(1+x+x²)^n = (x^n+x^{n+1}+x^{n+2})^n, ending with n(n+1) (not an option). Correct value is f(−1) + (−1)f′(−1) = n+1, i.e. (P), matching the key. (D) has no working in the PDF; f(−2) = 3^n added.
- All other questions (Q1, Q2, Q3, Q4, Q6, Q12, Q14, Q17, Q18, Q19) — `pdf`: checked step by step and reproduced.

## Answer key
Every answer was checked by computation (sympy / big-integer arithmetic): Q1 816, Q2 1024, Q3 2187, Q4 722, Q6 502, Q8 66, Q10 0, Q11 4, Q12 5, Q13 2, Q14 9, Q15 5, Q16 13, Q17–19 as printed, Q20 as printed. **No wrong answer key found.** Wrong *working* with a correct key: Q10, Q11, Q16, Q20(C). Q6's key assumes the representation 202·C(200,100)+2^200 with m, n, p even is the intended one (uniqueness not proved).

## Alternate solutions and useful results
- **Alternates: 19 of 20 questions** (all except Q11). Each verified numerically or symbolically against the answer. Examples: Q1 hockey-stick on Σ(1−t)^j; Q2 Pascal recurrence b_{n+1}−b_n = (1+a)^n; Q4 trace recurrence P+Q = 724 and f²/(1−f) = P+Q−2; Q5 integration of (1+x)^n; Q7 Laurent-polynomial symmetry; Q9 factor (1+x) so a_k = q_k+q_{k−1}; Q13 Pascal-vector recurrence with factor −1 per three steps; Q14 exact squaring R = 577+408√2; Q20 palindromic pairing.
- **Question with NO alternate:** Q11 — after log simplification the equation 3^{3u−9} = 3^3 is a single step; the only variant (monotonicity of 3^{3u−9}) is not a genuinely different method.
- Some alternates are close cousins of the main route (Q3 factorisation view, Q8 pair counting, Q15 listing of binomial coefficients, Q16 explicit table, Q19 norm multiplicativity); they are different viewpoints but short.
- **useful_results** given for all 20 questions.

## make_ppt.py output
Only informational lines: "Equations: 821 converted to native PowerPoint equations." and "Saved … (126 slides, 20 questions)". No warnings (no "could not convert", no missing source/answer/key idea, no short solutions).

## Skipped / assumed
- Deck not rendered to images (no LibreOffice/skills); layout not visually inspected.
- Hindi text omitted; marks and "subjective → Numerical" rating type assumed as above.
