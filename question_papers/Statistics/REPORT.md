# Statistics: generation report

Blueprint: `qp_blueprints/Statistics.xlsx`. There is no `Statistics_config.xlsx`, so the check ran without `--config`.
This scheduled run made the paper on 19-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy, mpmath and python-docx were missing for `python3`. I installed them with `python3 -m pip install pandas openpyxl sympy mpmath python-docx`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- `build_paper.py --blueprint` passed with **no errors and no warnings** on the first build. No script was edited and no check was weakened.
- I rendered page 1 of each of the three PDFs, and page 2 of the questions PDF, and looked at them. The Hindi is shaped, the equations are typeset in 2D, and the frequency tables (LaTeX arrays) render in both languages. This paper has no paragraph question.

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the blueprint has only Single Correct and Numerical types and nothing above level 3.
- **Paper:** 29 questions (blueprint Sr No 270-298): 13 Single Correct (Q1-Q13), then 16 Numerical (Q14-Q29).
- **Reorder (`--reorder`):** the rows were not in type order, so they were renumbered (old Sr No -> new Q):
  270->1, 271->2, 274->3, 275->4, 276->5, 277->6, 278->7, 282->8, 285->9, 291->10, 292->11, 294->12, 298->13,
  272->14, 273->15, 279->16, 280->17, 281->18, 283->19, 284->20, 286->21, 287->22, 288->23, 289->24, 290->25, 293->26, 295->27, 296->28, 297->29.
- **Answer Plans:** the blueprint had none, so the script drew all 29. Every answer matches its plan; the build checks this.
  - SCQ: Q1 C, Q2 A, Q3 B, Q4 D, Q5 A, Q6 B, Q7 D, Q8 C, Q9 A, Q10 C, Q11 B, Q12 D, Q13 B.
  - Numerical: Q14 decimal between 0 and 1; Q15 positive 2-digit integer; Q16 negative integer; Q17 positive 3-digit integer; Q18 negative decimal; Q19 positive decimal; Q20 negative integer; Q21 positive decimal; Q22 decimal between 0 and 1; Q23 negative decimal; Q24 positive 2-digit integer; Q25 positive 3-digit integer; Q26 negative decimal; Q27 positive decimal; Q28 decimal between 0 and 1; Q29 negative integer.
- **Cells containing ";":** none.
- **Warnings.** I recorded these and did not fix them, because the blueprint is your decision. There were no errors, and the blueprint file was not edited.
  - Q11 (old row 292) and Q24 (old row 289) list 3 concepts in a Main paper. Kept as given; each question uses all 3.
  - Many concepts repeat across rows, which is natural for a single-chapter paper of 29 questions. The most repeated is "Standard deviation and variance of ungrouped data" (Q12, Q16, Q17, Q18, Q23, Q24, Q26, Q29). Others: "Arithmetic mean of ungrouped data" (Q1, Q2, Q14, Q25), "Median of ungrouped data" (Q3, Q13, Q19), "Mean deviation about the mean" (Q8, Q19, Q20), "Combined mean" and "Variance of a combination" (Q10, Q11, Q15), "Mode of ungrouped data" (Q5, Q6), "Mode of a continuous distribution" (Q6, Q7), "Median of a continuous distribution" (Q3, Q4), "Mean deviation about the median" (Q8, Q9), "Mean deviation of a continuous distribution" (Q21, Q22), "Change of origin and scale" (Q23, Q24), "Correcting after a wrong observation" (Q24, Q25), "Coefficient of variation" (Q11, Q26), "Mean and variance of an AP" (Q12, Q27), "Same mean, different variance" (Q28, Q29), "Mean of a continuous distribution" (Q1, Q15), "SD of a continuous distribution" (Q16, Q22). Each use has a different mechanism, and no data set or setup is reused.

## Answers
| Q | Type | Answer | Level (target) |
|---|---|---|---|
| 1 | SCQ | (C) | 3 (3) |
| 2 | SCQ | (A) | 2 (2) |
| 3 | SCQ | (B) | 3 (3) |
| 4 | SCQ | (D) | 2 (2) |
| 5 | SCQ | (A) | 2 (2) |
| 6 | SCQ | (B) | 3 (3) |
| 7 | SCQ | (D) | 2 (2) |
| 8 | SCQ | (C) | 2 (2) |
| 9 | SCQ | (A) | 2 (2) |
| 10 | SCQ | (C) | 2 (2) |
| 11 | SCQ | (B) | 3 (3) |
| 12 | SCQ | (D) | 2 (2) |
| 13 | SCQ | (B) | 2 (2) |
| 14 | Num | 0.6 | 2 (2) |
| 15 | Num | 20 | 2 (2) |
| 16 | Num | -25 | 2 (2) |
| 17 | Num | 144 | 3 (3) |
| 18 | Num | -1.75 | 3 (3) |
| 19 | Num | 8.75 | 2 (2) |
| 20 | Num | -2 | 3 (3) |
| 21 | Num | 10.5 | 2 (2) |
| 22 | Num | 0.85 | 3 (3) |
| 23 | Num | -3.25 | 2 (2) |
| 24 | Num | 36 | 3 (3) |
| 25 | Num | 573 | 2 (2) |
| 26 | Num | -7.5 | 3 (3) |
| 27 | Num | 8.76 | 3 (3) |
| 28 | Num | 0.8 | 2 (2) |
| 29 | Num | -8 | 3 (3) |

I recomputed every answer in Python (exact fractions and sympy), separately from the written solutions, and checked uniqueness where a parameter is involved:
- Q1: the grouped table built from the squares, and the other boundary convention (giving -1/6) as a check.
- Q3, Q9, Q19: grid search over real x for the median condition. Q3 and Q19 have one solution each; Q9 has exactly two (1 and 16).
- Q6: every k from 1 to 14 tried; only k = 6 works.
- Q5: the divisor counts of 1-40 with sympy.
- Q14: solved for r, and checked numerically.
- Q16 and Q26: both roots of the quadratic found, and the side condition checked.
- Q17: the variance minimised with sympy.
- Q18: the quadratic V(λ) found symbolically.
- Q20: a fine grid search for the maximum of D(t).
- Q29: brute force over all 10 pairs and all integer x.

## Level distribution and index
- Level 2: 17 questions (Q2, Q4, Q5, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q15, Q16, Q19, Q21, Q23, Q25, Q28). Level 3: 12 questions (Q1, Q3, Q6, Q11, Q17, Q18, Q20, Q22, Q24, Q26, Q27, Q29).
- Marks-weighted index (SCQ 3 marks, Numerical 4 marks): **2.43**. No question is about equivalence relations, and there is no MCQ, so neither adjustment applies.
- **No question is one level off its target.** Each rated level equals the blueprint level.
- Consistency pass: I sorted the questions by level and compared neighbours. Q1 (grouping error of the mean) and Q6 (two modes) are the easiest Level 3s and are close to 2. I kept them at 3 because each links two ideas and has a trap. Q22 (complete the table, then MD and SD) is the most mechanical Level 3. Q13 (quartiles of a list) is the easiest Level 2. Q16 and Q12 are the hardest Level 2s. The anchor bank has only three Statistics questions (2023-P1-Q15 at L0, 2025-P1-Q14 at L2, 2026-P2-Q12 at L2), so most Level 3 ratings are Medium confidence.

## Originality report
The web checks used web search. I searched each question's distinctive structure in words and symbols. Perfect novelty cannot be guaranteed. Please tell me if you recognise any question.

| Q | Mechanism | Web check | Standard ingredient |
|---|---|---|---|
| 1 | Grouping error: the class-mark mean minus the true mean of the squares 1..225, with 225 on a class boundary. | not found | grouped mean as an estimate |
| 2 | Two running means of an AP fix a and d; the mean of the block a11..a30 is asked. | not found | **yes**: the mean of the first n AP terms is a + (n-1)d/2 |
| 3 | An ungrouped set with a parameter is fixed by its median (casework), then merged into a grouped table, whose median is asked. | not found | grouped median formula |
| 4 | The distribution is given by the rule "number not less than 10k = 50 - 2k²", converted into class frequencies and then the median. | not found | more-than ogive |
| 5 | The mode of the divisor counts d(1)..d(40) is 4 (14 times), not 2 (12 primes). | not found | divisor counting |
| 6 | The ungrouped unique mode must equal the grouped interpolated mode, which fixes the unknown frequency k = 6. | not found | grouped mode formula |
| 7 | Frequencies k²(7-k) with a near tie (48 against 50) next to the modal class. | not found | grouped mode formula |
| 8 | 1..9 plus the outlier 40: the gap between the mean deviation about the mean and about the median. | not found | MD about the median is the least |
| 9 | The unknown observation moves the median; piecewise MD with a flat middle piece and two solutions. | not found | none beyond the definition |
| 10 | The combined variance is inverted for the difference of means (two roots); an order condition picks one. | ingredient only | **yes**: the combined-variance formula run backwards is a common exercise type |
| 11 | Two groups with equal CV of 20% are pooled; the between-group term raises the CV to 50/√3. | not found | combined variance |
| 12 | An AP data set plus its own mean: the variance scales by n/(n+1), giving a quadratic in n. | not found | **yes**: AP variance d²(n²-1)/12 |
| 13 | Squares of -7..7: quartiles read from a doubled list, Q/M = 1 (convention stated). | not found | quartile positions |
| 14 | Six-term GP: S6 = (1+r)(1+r²+r⁴), so the mean ratio to the alternate terms is (1+r)/2. | **found: redesigned** (see below) | GP sum |
| 15 | A missing class frequency fixed through the combined mean with an ungrouped second section. | not found | missing-frequency problems |
| 16 | An ungrouped set with one free value tied to a grouped variance by a factor of 5; the root is picked by k < 10. | not found | missing observation from the variance |
| 17 | The variance of t, 2t, 576/t, 1152/t becomes (11s²-23040)/16 with s = t + 576/t; then AM-GM. | not found | AM-GM on t + a/t |
| 18 | The variance of x² + λx is a quadratic in λ with its vertex at -Cov(x², x)/Var(x). | ingredient only | quadratic vertex |
| 19 | Median of 8 values fixes x by position casework; then the MD about the mean. | not found | none beyond the definitions |
| 20 | Data t, -t, f(t), f(-t) with f odd: the mean is always 0 and the MD is a cubic on [-3,0]; derivative tests. | not found | derivative tests |
| 21 | Missing frequency from the mean, then the MD about the mean. | not found | **yes**: textbook grouped-MD layout |
| 22 | The ratio MD/SD of one grouped table, completed from the mean. | not found | grouped MD and SD |
| 23 | The transformation y = ax + b recovered from the target mean and variance, with a < 0. | ingredient only | **yes**: origin and scale rules |
| 24 | A misread observation corrected on the coded scale, where u = -5 and u = 5 have equal squares. | not found | correction of the sums |
| 25 | A digit-reversed observation: the change in the mean gives 99(c - 3) = 198. | not found | **yes**: misread-observation correction (the reversal is new) |
| 26 | The CV condition gives a quadratic in x with one integer root (27); then a shift tuned to a new CV. | not found | CV is unchanged in sigma under a shift |
| 27 | AP values with GP frequencies 1, 3, 9, 27: the weighted mean is an AGP sum; with the AP mean it fixes a and d. | not found | AGP sum by S - rS |
| 28 | Equal means fix the unknown frequency (zero coded sum); the variances are then compared. | not found | **yes**: comparing consistency of equal-mean series |
| 29 | An unknown pair is replaced keeping the mean and doubling the SD: (y-x)² = (p-q)² + 720, a perfect-square test. | not found | recovering observations from the mean and variance |

## Problems found while verifying
- **Q14 redesigned after the web check.** The first design (five GP terms with a given mean and a given mean of reciprocals, using Σx / Σ(1/x) = (middle term)²) matched a published problem type (Canvas Classes, and a careers360 question on the ratio of the sum of five GP terms to the sum of their reciprocals). I replaced it with the six-term version, which compares the mean with the mean of the alternate terms. The search for the new version found nothing.
- Q6: the first frequency choice (6 twice, 12 three times, 25 four times) let the modal class become a tie for k = 1. I changed the frequencies to 6 once, 12 four times and 25 four times. The modal class is then the same for every k, and k = 6 is unique.
- Q1: the answer depends on the class-boundary convention. With 225 in [200,225) the answer would be -1/6, which is option B. The stem states half-open classes.
- Q13: textbooks differ on quartile positions for ungrouped data, so the stem states the 4th and the 12th observations.
- Q23: the answer is exact only with the population variance (divide by n), which is the JEE convention.
- Q25: the change in the mean alone gives only a - c = 2, so the stem gives two digits of the recorded value.
- The stem review is a self-check; an independent reader may still find things. I also added order and side conditions where a quadratic had two roots: Q10 (Q's mean is greater), Q16 (k < 10), Q26 (x is an integer) and Q29 (x < y, integers).

## Rows whose concepts were hard to combine naturally
- **Q20 (mean deviation about the mean + derivative tests):** a mean deviation is piecewise linear in the data, so a smooth function needed a family of data sets. The odd-function construction (t, -t, f(t), f(-t)) works, but it is somewhat artificial.
- **Q27 (mean/variance of an AP + AGP):** an AGP appears naturally only as a weighted mean (AP values with GP frequencies). With 4 terms the AGP sum is short, and a student can add it directly.
- **Q11 and Q24 (three concepts each):** all three are used in one chain in each question, with no concept dropped.

The Hindi is my own translation. Please review the specialised terms (विचरण गुणांक, चतुर्थक विचलन, माध्य विचलन).
