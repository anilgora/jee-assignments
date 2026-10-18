# Binomial_Theorem: generation report

Blueprint: `qp_blueprints/Binomial_Theorem.xlsx`. There is no `Binomial_Theorem_config.xlsx`, so the check ran without `--config`.
This scheduled run generated the paper on 18-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed. The Python packages pandas, openpyxl, sympy and mpmath were missing, so they were installed with `pip install pandas openpyxl sympy mpmath`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/` as instructed.

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the blueprint has only Single Correct and Numerical types and nothing above level 3. The paper name comes from the file name.
- **Paper:** 32 questions: 8 Single Correct (Q1-Q8), then 24 Numerical (Q9-Q32). This is the blueprint's own mix, kept as given.
- **Reorder (`--reorder`)**, old Sr No -> new Q:
  182->1, 187->2, 191->3, 196->4, 199->5, 208->6, 210->7, 213->8, 183->9, 184->10, 185->11, 186->12, 188->13, 189->14, 190->15, 192->16, 193->17, 194->18, 195->19, 197->20, 198->21, 200->22, 201->23, 202->24, 203->25, 204->26, 205->27, 206->28, 207->29, 209->30, 211->31, 212->32.
- **Answer Plans:** the blueprint had none, so the script drew all 32 at random:
  Q1 Option C, Q2 Option A, Q3 Option B, Q4 Option D, Q5 Option A, Q6 Option B, Q7 Option D, Q8 Option C, Q9 negative integer, Q10 positive 2-digit integer, Q11 negative decimal, Q12 decimal between 0 and 1, Q13 positive 3-digit integer, Q14 positive decimal, Q15 positive decimal, Q16 negative decimal, Q17 positive 2-digit integer, Q18 positive 3-digit integer, Q19 negative integer, Q20 decimal between 0 and 1, Q21 negative integer, Q22 negative decimal, Q23 positive 3-digit integer, Q24 decimal between 0 and 1, Q25 positive decimal, Q26 positive 2-digit integer, Q27 positive decimal, Q28 negative decimal, Q29 negative integer, Q30 positive 2-digit integer, Q31 decimal between 0 and 1, Q32 positive 3-digit integer. Every answer matches its plan (the build checks this), and no numerical answer repeats.
- **Warnings (recorded, not fixed; the blueprint is yours):**
  - The concept cells in file rows 1, 2, 3, 4, 6, 7 and 17 contain ";": "Binomial theorem for a positive integral index; general term" and "Number of terms; number of rational and irrational terms". No config was supplied, so each was kept as **one concept**.
  - Q10 (old 184) lists **4 concepts**, and Q11, Q15, Q17 and Q20 (old 185, 190, 193, 197) list **3**, although the Main pattern normally has at most two. Every listed concept was used.
  - Concepts repeat within the paper because this is a single-chapter paper. For example, "general term" appears in Q1, Q9, Q10 and Q11; "greatest binomial coefficient" in Q12, Q14 and Q15; "Euler's theorem" in Q7 and Q31. Each repeat uses a different mechanism and different expressions.
- No errors. The blueprint file was not edited.

## Originality report (per question)
Each mechanism was named before the question was written and checked against `known_skeletons.md`. Every question was also web-searched (standard mode).
"not found" = no similar problem turned up. "ingredient only" = only the standard ingredient or method turned up, not this construction. "found: redesigned" = a near-identical problem turned up and the question was replaced.

| Q | Type | Target | Rated | Mechanism | Web check |
|---|---|---|---|---|---|
| Q1 | SCQ | 3 | 3 | a four-term base that is secretly the cube (ax - 1/x)^3, so the fourth power is a 12th-power binomial in disguise; one coefficient fixes a, the constant term is then read off (way 4, hidden structure) | not found |
| Q2 | SCQ | 2 | 2 | rational/irrational term counting after the odd-r terms of (a+b)^n + (a-b)^n cancel, so the count is over even r only (way 5, the sum changes which terms exist) | ingredient only |
| Q3 | SCQ | 2 | 2 | the pair (m, n) is fixed by two coefficient conditions through the identity coefficient of x^2 = ((m-n)^2 - (m+n))/2, and the product then folds into (1-x^2)^4 (1+x)^4 (way 3, an object fixed by two conditions) | not found |
| Q4 | SCQ | 3 | 3 | the index n is recovered from an integration-type sum given only as a number, and then a differentiation-type sum is evaluated (way 5, one sum used to identify the expansion that the other needs) | not found |
| Q5 | SCQ | 3 | 3 | a family of alternating product sums T_k is summed over the shift k, so only the coefficients of x^0..x^10 of (1-x^2)^10 survive and a partial alternating sum appears (way 5) | not found |
| Q6 | SCQ | 2 | 2 | the product (e^x - 1) log(1+x) has its x^3 term cancel, so the limit needs the fourth-order coefficients of both series (way 4, a hidden cancellation) | not found |
| Q7 | SCQ | 2 | 2 | a power tower whose exponent is reduced modulo phi(77) = 60 by Euler's theorem and whose final power is split by Fermat's theorem modulo 7 and 11 (way 5, the two theorems at two different levels of the tower) | ingredient only |
| Q8 | SCQ | 2 | 2 | a double sum over i<j weighted by the gap j-i, which regroups by the gap into sums of products C_i C_(i+k) = C(12, 6+k) and then a weighted single sum (way 5) | not found |
| Q9 | Numerical | 3 | 3 | a sequence defined by a moving target power (the coefficient of x^n in the n-th power), which is non-zero only when 3 / n (way 2, a function defined by a construction) | not found |
| Q10 | Numerical | 3 | 3 | a product of a parametrised binomial with an odd-power expansion, where parity kills half of the cross terms; the constant term fixes a through a cubic with one real root, then another coefficient of the product is read (way 5, parity link between the two factors) | not found |
| Q11 | Numerical | 3 | 3 | the exponent p of the expansion is not given; it is fixed by requiring both a constant term and a term in x^24 (divisibility (p+1) / 6 and a size condition), and the answer is a coefficient for that p (way 3, an object fixed by two conditions) | not found |
| Q12 | Numerical | 2 | 2 | for an odd index the two middle terms share the greatest binomial coefficient, so their ratio collapses to the ratio of the two base terms (way 4, a hidden cancellation) | found: redesigned |
| Q13 | Numerical | 3 | 3 | the index is fixed by counting rational terms of a sum of two square roots, and the integral/fractional-part identity then gives (I+f)(1-f) = (a-b)^n with a - b = 3, not 1 (way 5) | ingredient only |
| Q14 | Numerical | 3 | 3 | the set of x for which the term with the greatest binomial coefficient is also a numerically greatest term, so the two notions of 'greatest' are reconciled (way 5) | ingredient only |
| Q15 | Numerical | 3 | 3 | three notions in one expansion (greatest binomial coefficient fixing n, numerically greatest term, middle term) compared through a ratio, with a negative base so that 'numerically' matters (way 5) | ingredient only |
| Q16 | Numerical | 2 | 2 | a difference of two fractional parts, each evaluated by a different binomial rewriting ((50-1)^1013 to one term, (10-1)^1013 to two terms), so the result is negative (way 5) | not found |
| Q17 | Numerical | 3 | 3 | the last two digits of 11^n + 9^n are found for all n at once from (10 +- 1)^n, giving 02 for even n and 20n mod 100 for odd n, and the divisible cases are then counted (way 2, a family analysed as a function of n) | not found |
| Q18 | Numerical | 2 | 2 | a power of 3 rewritten as a power of 9 = 10 - 1 so that a three-term binomial truncation gives the last three digits (way 4, hidden base change) | not found |
| Q19 | Numerical | 2 | 2 | a negative power of 1 - sqrt2 that is minus (1 + sqrt2)^7, so the integral-part argument must be done for a negative number (way 4, hidden reciprocal) | not found |
| Q20 | Numerical | 3 | 3 | a rational weight (r^2+3)/(r+1) that splits into a differentiation part, a plain part and an integration part, two of which vanish in the alternating sum (way 4, hidden cancellation) | not found |
| Q21 | Numerical | 3 | 3 | a binomial sum in the fractional part {x} collapses to ({x}-2)^9, whose obvious antiderivative is discontinuous at every integer, so the integral must be split and each unit piece is a C_r/(r+1)-type sum (way 5) | not found |
| Q22 | Numerical | 3 | 3 | alternating sums over every third binomial coefficient, filtered by the roots of z^3 = -1 (not of unity), and compared through a ratio (way 5) | not found |
| Q23 | Numerical | 2 | 2 | the numerator C(k,2) is exactly the Pascal difference of the two denominator factors, so the term splits as a difference of reciprocals of binomial coefficients (way 4, hidden telescoping) | not found |
| Q24 | Numerical | 3 | 3 | the weight n is split as (n+6) - 6, the absorption (n+6)/C(n+6,6) = 6/C(n+5,5) moves to a lower binomial, and both pieces are summed by factorial telescoping (way 5) | ingredient only |
| Q25 | Numerical | 2 | 2 | a trinomial whose terms form a geometric progression in x/2, so the coefficient can be found by the multinomial general term or by (1-y^3)^5 (1-y)^(-5) (way 5) | not found |
| Q26 | Numerical | 2 | 2 | the multinomial count of terms (36) differs from the number of terms after combining, and the gap at x^20 must be found from the general-term exponents (way 5) | ingredient only |
| Q27 | Numerical | 3 | 3 | a fourth-order coefficient of the product of a fractional-index binomial series and the exponential series, where the alternating binomial coefficients nearly cancel the exponential ones (a_1 = 0) (way 5) | not found |
| Q28 | Numerical | 3 | 3 | a fractional power with a free coefficient a is matched against a negative-index power so that the first-order terms cancel; the second-order coefficients then have opposite signs and add (way 5) | not found |
| Q29 | Numerical | 3 | 3 | two mirror-image variable powers whose second-order terms are equal and whose third-order terms are opposite, so the difference is of order x^3 (way 4, hidden symmetry) | not found |
| Q30 | Numerical | 2 | 2 | a power sum over a range longer than the modulus, so Fermat's theorem applies to all but the multiples of 41 (way 5) | ingredient only |
| Q31 | Numerical | 2 | 2 | a fractional part read as a remainder modulo a composite modulus, where Euler's theorem with phi(50) = 20 reduces the exponent (way 5) | ingredient only |
| Q32 | Numerical | 2 | 2 | a nested double sum C(6,j) C(j,i) over i < j, summed inner-first to 2^j - 1 and then by the binomial theorem twice (way 5) | ingredient only |

Standard ingredients worth flagging:
- Q2: counting irrational terms of a binomial with surds (a common JEE Main type). The new step is the cancellation in the conjugate sum.
- Q7, Q30, Q31: Fermat / Euler remainder computations are standard. The constructions (a tower modulo 77, a power sum running past the modulus, a fractional part modulo 50) are routine variants.
- Q13: the classic "(I+f)(1-f)" conjugate identity, here with two surds and a - b = 3.
- Q14, Q15: the ratio test for the numerically greatest term.
- Q24: sum 1/C(n+k,k) = k/(k-1) is a known identity. The question adds the weight n.
- Q26: number of terms after combining like terms.
- Q32: sum over i <= j of C(n,j) C(j,i) = 3^n is known. The question uses the strict inequality, which gives 3^n - 2^n.

**Q12 was redesigned after the web check.** The first design asked for a in (x + a/x)^10 when the middle term is 63/8. That is structurally the published JEE problem "(x sin x + 1/x)^10 with middle term 63/8". It was replaced by a ratio of the two middle terms of (2x + 6/(5x))^7.

Complete novelty cannot be guaranteed. If you recognise any question, say which one.

## Difficulty (calibrated 0-5 scale)
- Distribution: **Level 2: 15 questions** (Q2, Q3, Q6, Q7, Q8, Q12, Q16, Q18, Q19, Q23, Q25, Q26, Q30, Q31, Q32); **Level 3: 17 questions** (Q1, Q4, Q5, Q9, Q10, Q11, Q13, Q14, Q15, Q17, Q20, Q21, Q22, Q24, Q27, Q28, Q29).
- Every rated level equals its blueprint target, so no question is one level off.
- Marks-weighted index: **2.54** (SCQ 3 marks, Numerical 4 marks; no equivalence-relation or MCQ-floor adjustment applies). This is a JEE Main paper, so there is no official range to compare it with.
- Consistency pass (questions sorted by level, neighbours compared): the borderline pairs are Q1 (L3: hidden cube, then two general-term steps) against Q3 (L2: two coefficient equations, then one coefficient), and Q4 (L3) against Q20 (L3). Q4 is the lighter of the L3 questions. Q1, Q4, Q21, Q28 and Q29 were rated L3 with Medium confidence; each could be read as a strong L2. Q17 and Q22 could be read as weak L4.

## Problems found while verifying (all fixed before the build)
- Q12: replaced after the web check (see above).
- Q12 and Q15: the first versions gave 0.30 and 2.50, the same answers as Q24 and Q27. The constants were changed (6/(5x) instead of 3/(5x) in Q12; (1 - 3x)^8 instead of (2 - 5x)^8 in Q15) so the answer key has no repeats.
- Q13: the numerical check line in the full solution had a wrong value for (sqrt10 + sqrt7)^6. It was corrected to 38385.98.
- Q27: a stray factor in the shortened solution's first line was removed. The coefficients themselves were correct.
- Every answer was recomputed with sympy/mpmath independently of the hand solution: exact expansion for every coefficient question, brute-force search for uniqueness of the parameters (Q3 m, n up to 40; Q4 n; Q11 p up to 200; Q12 and Q15 n), sympy limits (Q6, Q28, Q29), mpmath nsum (Q24), modular powers (Q7, Q16-Q18, Q30, Q31) and high-precision floats for the integral-part questions (Q13, Q19).
- The web-search tool's summaries also recomputed several answers. Where they agreed with the code they were treated as a side check only; the code checks decide.

## Rows whose concepts were hard to combine naturally
- Q10 (four concepts in one Main numerical): combined as "the constant term of a product fixes a, then another coefficient of the product". "General term" and "coefficient of a specified power" overlap heavily with the other two concepts.
- Q11: "coefficient of a specified power" and "term independent of x" both act as existence conditions that fix p, and the answer is the x^24 coefficient. All three concepts are needed, but the general term carries most of the work.
- Q26 ("Multinomial: general term and coefficient extraction" with "Multinomial Theorem"): the two concepts are nearly the same. The multinomial-theorem count (36) is used as the contrast with the 21 distinct powers.
- Q21 ("handling discontinuous antiderivatives"): used as the trap that the natural antiderivative ({x}-2)^10/10 jumps at every integer. The integration-technique sum appears as the integral over one unit interval.

## Stem review
`review_stems.py` was run, and each stem was read as a student would read it (symbols and domains defined, conditions complete, one reading, a unique answer equal to the plan, options in one form). Changes: the Q12 redesign and the Q12/Q15 constants. This is a self-check; an independent reader may still find things.

## Notes
- Several numerical answers are exact decimals: Q11 -1.50, Q12 0.60, Q14 4.10, Q15 3.60, Q16 -0.80, Q20 0.25, Q22 -0.50, Q24 0.30, Q25 3.75, Q27 2.50, Q28 -1.25, Q31 0.34. None of them needs rounding.
- The Hindi is the assistant's own translation. Please check the specialised terms, for example संख्यात्मक रूप से महत्तम पद (numerically greatest term), भिन्नात्मक भाग (fractional part) and महत्तम द्विपद गुणांक (greatest binomial coefficient).
- `recalc.py` (the xlsx formula recalculation) is not available in this environment. The Excel summary uses live formulas that compute when the file is opened.
- Page 1 of each PDF was rendered and checked: the Hindi is shaped and the equations are 2D. There is no paragraph block in a Main paper.
- `_source/` holds `blueprint.json`, `meta.json` and `q01.json` ... `q32.json`. To fix a question, edit it and rerun `build_paper.py` with `--blueprint _source/blueprint.json`.
