# Run report: JEE_Main_Question_Bank_01_Algebra_14

Paper: `papers/JEE_Main_Question_Bank_01_Algebra_14.pdf` (printed Q261-Q280, renumbered 1-20), all Binomial Theorem (Q20 also exponential series). All single-correct.
Files: `_content.json`, `_Analysis.pptx` (114 slides), `_ratings.json`, `_difficulty.xlsx`.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): **4 per question**, single-correct = JEE Advanced default. Stated on the section divider.

## Difficulty
Marks-weighted difficulty index: **2.15** (equal marks; no equivalence-relation or multi-concept adjustments).
Level 1: 1 (Q19). Level 2: 15 (Q1-9, 11, 13, 14, 15, 17, 20). Level 3: 4 (Q10, 12, 16, 18). Levels 0, 4, 5: none.
JEE Main-style bank rated on the Advanced scale, so the index is below the official range. All ratings Medium confidence (loose anchors).

## Solutions: corrected / written
No question was `written`. Corrected (answers unchanged in every case):
- **Q6 (printed 266):** PDF factorises the G.P. sum and states k = 63 without showing why no larger k works; maximality argument (order of 49 mod 49^k+1 must divide 126, so k | 63) added.
- **Q7 (267):** PDF writes "k = 2 => r = ±5"; r = 6k^2 - 19 = 5 only (r = -5 impossible). The count of 4 pairs is right (brute force).
- **Q8 (268):** PDF labels -96 as the coefficient of x^2 (alpha); it is the coefficient of x^4 (alpha), 36 is that of x^2 (beta).
- **Q15 (275):** PDF sums from r = 0, but the given sum starts at r = 1 (a_{-1} undefined); the r = 0 term is 0, so the value stands.
- **Q18 (278):** PDF concludes [x] is even from "x - x' is an even integer" without showing 0 < x' < 1 (needed for [x] = x - x'); same for y. Bounding bullets (8sqrt3 in (13,14), 7sqrt2 in (9,10)) added.
Reproduced from the PDF (`pdf`): all others. Small fill-ins: Q3 states that the x^16 coefficient in (1-x^3)^9 is 0 (PDF jumps to 9C6); Q16 rewrites the messy last lines; Q19's last printed term 1/(51!·1!) is numerically 1/(51!·0!) (PDF uses 0!), noted in the solution.

## Answer key
All printed keys match my own computation (exact arithmetic / brute force for every question). No wrong key.

## Alternates and results
Alternates for 16 of 20 questions (Q1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 17, 18, 19, 20). Techniques: option elimination with one equation (Q1), congruence filter n = 3 mod 5 (Q2), Binomial(20,1/2) moment E[X^2] (Q4), substitution v = x^4 (Q5), halving the G.P. (Q6), bounding (r+1)/6 and squares (Q7), Chebyshev T6 via x = cos t (Q8), absorption identity and odd-subset count (Q10), sum of squares (Q11), weighted AM-GM (Q12), Vandermonde (Q14), pairing r with 11-r (Q15), hockey stick (Q17), power-sum recurrence parity (Q18), generating function sinh x e^x (Q19), operator method x d/dx (Q20).
Weaker alternates (close in spirit to the main solution): Q5 (reparametrisation only), Q10 (same two facts via different identities), Q11.
All 20 questions have useful_results.

## Questions with NO alternate
- **Q3:** the only route is the pairing (1-x)(1+x+x^2) = 1-x^3 followed by matching exponents; the alternatives (expanding the trinomial) are far heavier, not elegant.
- **Q9:** any approach reduces to the term 16C8 2^8 / sin^8(2θ) and its extremes on each interval; no different method.
- **Q13:** all routes are evaluations of f at 1 and -1 (even/odd split); no genuinely different method.
- **Q16:** every route computes K, the middle term and the ratio 100/101 in the same way (Kummer's theorem gives only l, not n).

## make_ppt.py warnings
None (738 equations converted; no "could not convert" messages). Notes about missing alternates appeared only before the alternates were attached correctly to the JSON; the final build printed none.

## Skipped / assumed
No rendering/thumbnail check (no soffice). Concepts, marks and levels assumed as above. Hindi/English duplicate text ignored. Page images were read for Q5, 8, 9, 12, 13, 15, 19, 20 where the text layer was garbled.
