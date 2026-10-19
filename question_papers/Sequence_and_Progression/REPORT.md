# Sequence and Progression: generation report

Blueprint: `qp_blueprints/Sequence_and_Progression.xlsx`. There is no `Sequence_and_Progression_config.xlsx`, so the check ran without `--config`.
This scheduled run made the paper on 19-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy, mpmath and python-docx were missing for `python3`. I installed them with `python3 -m pip install pandas openpyxl sympy mpmath python-docx`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- `build_paper.py --blueprint` passed with **no errors and no warnings**. No script was edited and no check was weakened.
- I rendered page 1 of each of the three PDFs and looked at it. The Hindi is shaped and the equations are typeset in 2D. This paper has no paragraph question.

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the blueprint has only Single Correct and Numerical types and nothing above level 3.
- **Paper:** 40 questions: 5 Single Correct (Q1-Q5), then 35 Numerical (Q6-Q40).
- **Reorder (`--reorder`), old -> new:** 46->1, 54->2, 65->3, 77->4, 79->5, 40->6, 41->7, 42->8, 43->9, 44->10, 45->11, 47->12, 48->13, 49->14, 50->15, 51->16, 52->17, 53->18, 55->19, 56->20, 57->21, 58->22, 59->23, 60->24, 61->25, 62->26, 63->27, 64->28, 66->29, 67->30, 68->31, 69->32, 70->33, 71->34, 72->35, 73->36, 74->37, 75->38, 76->39, 78->40.
- **Answer Plans:** the blueprint had none, so the script drew all 40. Every answer matches its plan; the build checks this.
  - SCQ: Q1 C, Q2 A, Q3 B, Q4 D, Q5 A.
  - Numerical: Q6 negative integer; Q7 positive 2-digit integer; Q8 negative decimal; Q9 decimal between 0 and 1; Q10 positive 3-digit integer; Q11 positive decimal; Q12 positive decimal; Q13 negative decimal; Q14 positive 2-digit integer; Q15 positive 3-digit integer; Q16 negative integer; Q17 decimal between 0 and 1; Q18 negative integer; Q19 negative decimal; Q20 positive 3-digit integer; Q21 decimal between 0 and 1; Q22 positive decimal; Q23 positive 2-digit integer; Q24 positive decimal; Q25 negative decimal; Q26 negative integer; Q27 positive 2-digit integer; Q28 decimal between 0 and 1; Q29 positive 3-digit integer; Q30 positive 2-digit integer; Q31 positive decimal; Q32 decimal between 0 and 1; Q33 negative integer; Q34 positive 3-digit integer; Q35 negative decimal; Q36 negative integer; Q37 positive 3-digit integer; Q38 decimal between 0 and 1; Q39 positive decimal; Q40 positive 2-digit integer.
- **Cells containing ";":** the check warned about spreadsheet rows 36 and 37. With no config to split them, each cell was kept as **one** concept, as you instructed. The cell is "Sequences defined by a recurrence relation; finding the nth term" (used in Q38 and Q39).
- **Warnings.** I recorded these and did not fix them, because the blueprint is your decision. There were no errors, and the blueprint file was not edited.
  - Rows with more than two concepts in a Main paper, kept as given, each question uses all of them: Q1 (3), Q10 (4), Q11 (3), Q17 (3), Q18 (3), Q22 (3), Q34 (3).
  - Q37 lists the same concept twice ("Telescoping series involving factorials" as Concept 1 and Concept 2). It is one concept, used once.
  - Many concepts repeat across rows (for example "Arithmetic Progression (AP) & Sum of AP" in Q1, Q6-Q11 and Q40; "Geometric Progression (GP) & Sum of GP" in Q1, Q4, Q10, Q13-Q18; the AM-GM concept in Q1, Q2, Q10, Q19-Q22). That is expected for a single-chapter blueprint. Each use has a different mechanism and no setup or function is reused.

## Answers
| Q | Type | Answer | Q | Type | Answer |
|---|---|---|---|---|---|
| 1 | SCQ | (C) 45/2 | 21 | Num | 0.41 |
| 2 | SCQ | (A) 7+4√3 | 22 | Num | 2.75 |
| 3 | SCQ | (B) 745 | 23 | Num | 12 |
| 4 | SCQ | (D) 6 | 24 | Num | 4.8 |
| 5 | SCQ | (A) 1/2 | 25 | Num | -2.5 |
| 6 | Num | -1444 | 26 | Num | -2 |
| 7 | Num | 35 | 27 | Num | 48 |
| 8 | Num | -3.5 | 28 | Num | 0.75 |
| 9 | Num | 0.25 | 29 | Num | 650 |
| 10 | Num | 120 | 30 | Num | 15 |
| 11 | Num | 152.5 | 31 | Num | 3.75 |
| 12 | Num | 37.2 | 32 | Num | 0.2 |
| 13 | Num | -0.5 | 33 | Num | -40 |
| 14 | Num | 36 | 34 | Num | 868 |
| 15 | Num | 840 | 35 | Num | -2.1 |
| 16 | Num | -10 | 36 | Num | -2 |
| 17 | Num | 0.51 | 37 | Num | 840 |
| 18 | Num | -84 | 38 | Num | 0.4 |
| 19 | Num | -2.5 | 39 | Num | 1.5 |
| 20 | Num | 243 | 40 | Num | 18 |

Every answer was recomputed in Python, independently of the written solution: exact fractions or sympy for closed forms, brute force for Q6, Q11, Q12 and Q34, numerical scans for the extrema (Q10, Q20, Q21, Q22), a 200 000-game simulation for Q16, and high-precision partial sums for the infinite series.
Q21 is the only answer that is not exact: the minimum is √2 − 1 = 0.4142..., so 0.41 is unambiguous to two decimals.

## Originality report
The web checks used web search. I searched each question's distinctive structure in words and symbols. Perfect novelty cannot be guaranteed. Please tell me if you recognise any question.

| Q | Mechanism | Web check | Standard ingredient |
|---|---|---|---|
| 1 | An AP and a GP share terms 1 and 3, so a₂ and b₂ are the AM and GM of 1 and r²; min of a₂ + 8/b₂ by a 1:2 AM-GM split; answer a₁₀ + b₄. | not found | three-term AM-GM |
| 2 | GM fixed, so G² = AH makes A·4H constant; AM-GM gives A = 4, H = 1; ratio of the recovered numbers. | not found | G² = AH |
| 3 | Seats per row; increases in AP; the second-order sequence is fixed by rows 3 and 6 (not consecutive terms). | ingredient only | **yes**: method of differences is a textbook routine |
| 4 | GP terms as coefficients of a line tangent to 12(x²+y²) = 1 give 12r⁴ = 1 + r²; sum of squares is sign-independent. | not found | GP with coefficient lines (known for parabolas) |
| 5 | Weighted Cauchy-Schwarz equality vector (1/2, 2, 9/2), then the angle with i + j + k. | not found | Cauchy-Schwarz equality case |
| 6 | Decreasing and increasing finite APs; overlap window [-50, 20] cut from opposite ends; complement sum. | ingredient only | **yes**: common terms form an AP with difference lcm |
| 7 | AP recovered from neighbour products 10, 40, 88 (their differences are 2d·a, second difference 2d²). | not found | none beyond AP |
| 8 | AP fixed by the variance of nine terms and a₁a₉ = m² − 16d². | not found | variance of an AP |
| 9 | AP weighted by 1/(n−1)!: two exponential moments give a + d and (a + d)² + d². | not found | Σn/n! = e, Σn²/n! = 2e |
| 10 | Inserted AMs, GMs, HMs: G₂³ = 1000 gives ab; A₁H₃ = ab makes A₁ + 36H₃ a fixed-product AM-GM. | ingredient only | **yes**: A_k H_(n+1−k) = ab |
| 11 | Two APs decoded from symmetric-term conditions; mean of their common terms. | not found | common terms |
| 12 | "Common terms have difference 36" means lcm(p, q) = 36; weighted mean over the 25 pairs. | ingredient only | **yes**: count of pairs with given lcm |
| 13 | Series of GP partial sums with an unknown ratio a; closed form 4/(2 − a) is inverted. | ingredient only | sums of partial sums of a GP |
| 14 | GP recovered from Σb_n and Σn·b_n; then Σn²·b_n by a second AGP differencing. | ingredient only | **yes**: Σn²xⁿ formula |
| 15 | Σ\|1 + z^k\|⁸ over 12th roots of unity: \|w\|² = w·w̄ and a GP filter leave only 12·C(8,4). | ingredient only | **yes**: roots-of-unity filter |
| 16 | Alternating die game with an immediate-loss face and different winning faces; round analysis, then GP. | ingredient only | **yes**: classic "A and B throw alternately" |
| 17 | Σn(2ⁿ − 1)/6ⁿ split into two AGPs with ratios 1/3 and 1/6. | ingredient only | Σnxⁿ |
| 18 | GP with ratio 1 − ω; De Moivre gives (1 − ω)⁶ = −27; ω³ = 1 clears the denominator. | not found | ω identities |
| 19 | Planes tx + y + (4/t)z = −9/2: Cauchy-Schwarz minimum inside, AM-GM over t outside; equality point. | not found | distance of a plane from the origin |
| 20 | α + β = π/2 with unequal weights 24 and 2; t = tan²α gives 123 + 50t + 72/t; the symmetric guess π/4 gives 245, not 243. | not found | (1 + 1/sinⁿ)(1 + 1/cosⁿ) type |
| 21 | Tangent to the unit circle cuts a right triangle; c = ab, AM-GM gives c ≥ 2, and the inradius is increasing in c. | not found | least triangle area for a tangent |
| 22 | Max HM of x, y, z under x + 4y + 9z = 18 (Cauchy-Schwarz or pairwise AM-GM); A·H at x = 2y = 3z. | not found | AM-HM |
| 23 | HP h_n = 60/n from two terms; the number of integer terms is the divisor count of 60. | not found | n-th term of an HP |
| 24 | HP terms from sum and product via b = 2ac/(a + c): a cubic with two roots to reject; extend the HP; HM of a and d. | not found | three numbers in HP |
| 25 | HM of the pairwise products of a cubic's roots is 3αβγ/(α + β + γ). | ingredient only | Vieta |
| 26 | Infinite product of GP terms with halving exponents; log₂ turns it into the AGP Σ(k − 4)/2^k. | ingredient only | **yes**: 2^(1/2)·4^(1/4)·8^(1/8)… = 4 |
| 27 | (n² + 1)/n splits into an AGP part and a log-series part; α + log_e β is unique since e^k is irrational. | not found | Σnxⁿ, Σxⁿ/n |
| 28 | Pronic numerators over 3^(n+1); one shift-and-subtract gives an AGP. | ingredient only | **yes**: Σn(n+1)xⁿ |
| 29 | Second differences 2 + 2ⁿ; first differences are an AP part plus a GP part. | not found | method of differences |
| 30 | Differences in GP; the closed form is used for a threshold (3¹³ vs 3¹⁴). | not found | method of differences |
| 31 | T_n = Σk(k + 1) telescoped, then (n + 3) split as (n + 2) + 1 into two telescoping pieces. | not found | Σ1/(n(n+1)(n+2)) |
| 32 | x_n = 2n/(2n + 1) from a telescoping sum feeds an inverse-tangent telescoping; tan S = 1/5. | not found | tan⁻¹ difference formula |
| 33 | Alternating 4/(n(n+1)(n+2)): partial fractions give three shifted copies of log 2. | not found | log 2 = 1 − 1/2 + 1/3 − … |
| 34 | N recovered from A_N = 5/21; then Σk(k+1)(k+2) and the quartic telescoping Σk/(k⁴ + k² + 1) at N. | ingredient only | **yes**: each of the three sums is a textbook sum; the link through N is the new part |
| 35 | Σtan kθ·tan(k+1)θ with θ = tan⁻¹(1/3) beside Σk(k + 1); 5θ passes π/2. | not found | tan A tan B identity |
| 36 | Ratio of two surd telescopings is exactly 1/√(n + 1); log₁₀ of it. | ingredient only | **yes**: both sums are known (JEE Main 2012 type) |
| 37 | (k² + k − 1)/(k + 2)! = k/(k + 1)! − (k + 1)/(k + 2)!. | ingredient only | factorial telescoping |
| 38 | u_(n+1) = 4u_n + 3ⁿ becomes a GP after the shift u_n + 3ⁿ; weighted sum against 1/8ⁿ. | not found | linear recurrence |
| 39 | Two-state ball passing; p_(n+1) = 1/5 + (3/5)p_n; Σ(p_n − q_n) = Σ(3/5)ⁿ. | not found | two-state Markov chain (random walk on a triangle type) |
| 40 | Line meets a cubic at abscissae in AP; sum 3a = 6 fixes the middle (inflection) abscissa; the sum of squares fixes d and the line. | not found | roots of a cubic in AP |

The Hindi is my own translation. Please review the specialised terms.

## Difficulty (calibrated 0-5 scale)
- **Levels:** L2 (16): Q2, Q3, Q7, Q8, Q13, Q19, Q23, Q24, Q25, Q26, Q28, Q30, Q32, Q35, Q36, Q37. L3 (24): Q1, Q4, Q5, Q6, Q9, Q10, Q11, Q12, Q14, Q15, Q16, Q17, Q18, Q20, Q21, Q22, Q27, Q29, Q31, Q33, Q34, Q38, Q39, Q40.
- **Weighted index:** 2.60. All marks are equal, so it is the mean level. There is no equivalence-relation adjustment and no MCQ, so the adjusted index is also 2.60.
- **Off target:** none. Every question is rated at its target level.
- **Borderline (Medium confidence):** Q38 (L3) could be read as L2 if the shift u_n + 3ⁿ is familiar to the student. Q4, Q19 and Q24 are near the boundary of their levels.
- **Consistency pass:** I sorted the questions by level and compared neighbours. I compared the hardest L2 questions (Q19, Q24, Q32) with the easiest L3 questions (Q22, Q38, Q40). Each of those L2 questions only chains standard steps that the stem makes visible, so I kept the levels.

## Rows where the concepts were hard to combine naturally
- **Q35** (product-of-linear-factors telescoping + tan/cot telescoping): the two concepts share a structure (sums of products of consecutive terms) but not one situation. The question puts the two parallel sums E_n and F_n side by side and asks for their ratio. This is the least natural combination in the paper.
- **Q36** (miscellaneous telescoping + surds) and **Q34** (three telescoping types): these are linked through a ratio or a shared index, not one object.
- **Q10** (four concepts in a Main row): all four are used, through the inserted AMs, GMs and HMs and an AM-GM step.
- **Q22** (AM-GM + AM/GM/HM relation + Cauchy-Schwarz): Cauchy-Schwarz and the pairwise AM-GM give the same bound, so the solution shows both routes.

## Problems found while verifying (all fixed before the build)
- **Q4:** the first design (a triangle with sides in GP and a 120° angle) led to the cubic r³ − r² − 1 = 0, which has no closed form. I replaced it with the tangent-line design.
- **Q10:** the stem opened a sentence with the imperative "insert". I rewrote it in the passive.
- **Q21:** the answer cannot be exact: √2 − 1 rounds to 0.41. I kept the design and checked that the rounding is unambiguous.

## Files
- `Sequence_and_Progression_Shortened_Solutions.docx`, `Sequence_and_Progression_Full_Solutions.docx`
- `Sequence_and_Progression_Questions_EN_HI.pdf`, `Sequence_and_Progression_Questions_and_Shortened_Solutions.pdf`, `Sequence_and_Progression_Questions_and_Full_Solutions.pdf`
- `Sequence_and_Progression_difficulty.xlsx` (internal)
- `_source/`: `blueprint.json`, `meta.json` and `q01.json`-`q40.json`. To fix a question, edit its JSON and run `build_paper.py` again.
