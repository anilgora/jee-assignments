# Sets: generation report

Blueprint: `qp_blueprints/Sets.xlsx`. There is no `Sets_config.xlsx`, so the check ran without `--config`.
This scheduled run made the paper on 19-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy, mpmath and python-docx were missing for `python3`. I installed them with `python3 -m pip install pandas openpyxl sympy mpmath python-docx`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- `build_paper.py --blueprint` passed with **no errors and no warnings** on the first build. No script was edited and no check was weakened.
- I rendered page 1 of each of the three PDFs (and page 2 of the questions PDF) and looked at them. The Hindi is shaped and the equations are typeset in 2D. This paper has no paragraph question.

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the blueprint has only Single Correct and Numerical types and nothing above level 3.
- **Paper:** 7 questions (blueprint Sr No 435-441): 1 Single Correct (Q1), then 6 Numerical (Q2-Q7).
- **Reorder (`--reorder`):** the rows were already in the required order. Nothing was renumbered: blueprint rows 435-441 are Q1-Q7.
- **Answer Plans:** the blueprint had none, so the script drew all 7. Every answer matches its plan; the build checks this.
  - Q1 Option C; Q2 positive 2-digit integer; Q3 negative decimal; Q4 negative integer; Q5 positive decimal; Q6 decimal between 0 and 1; Q7 positive 3-digit integer.
- **Cells containing ";":** the check warned about spreadsheet rows 1 and 2. With no config to split them, the cell was kept as **one** concept, as you instructed. The cell is "Representation of sets; empty, finite, infinite, equal and equivalent sets" (used in Q1 and Q2).
- **Warnings.** I recorded these and did not fix them, because the blueprint is your decision. There were no errors, and the blueprint file was not edited.
  - Q2 (row 436) lists 3 concepts in a Main paper. Kept as given; the question uses all 3.
  - Concepts repeated across rows: "Representation of sets..." (Q1, Q2), "Subsets, power set..." (Q2, Q3), "Union, intersection, complement, difference and symmetric difference" (Q2, Q4). Each use has a different mechanism, and no setup is reused.

## Answers
| Q | Type | Answer | Level (target) |
|---|---|---|---|
| 1 | SCQ | (C) | 2 (2) |
| 2 | Num | 19 | 3 (3) |
| 3 | Num | -4.5 | 2 (2) |
| 4 | Num | -3 | 3 (3) |
| 5 | Num | 12.5 | 2 (2) |
| 6 | Num | 0.35 | 3 (3) |
| 7 | Num | 792 | 3 (3) |

I recomputed every answer in Python, separately from the written solutions: sympy for the sets in Q1 plus a fine numeric scan for T and W, brute force over every candidate subset in Q2 and Q7 (all 1024 subsets for Q7), enumeration of the triples in Q3, an element-by-element check that X is unique in Q4, sympy for Q5 and Q6, and a one-million-trial simulation for Q6 (0.3506).

## Level distribution and index
- Level 2: 3 questions (Q1, Q3, Q5). Level 3: 4 questions (Q2, Q4, Q6, Q7).
- Marks-weighted index (SCQ 3 marks, Numerical 4 marks): **2.59**. No question is about equivalence relations, so no +0.5 adjustment applies, and there is no MCQ floor.
- **No question is one level off its target.** Each rated level equals the blueprint level.
- Consistency pass: I sorted the questions by level and compared neighbours. Q5 (Venn survey) is the hardest Level 2. Q2 (counting with the symmetric difference) is the easiest Level 3. Q7 (2-adic casework) is the hardest Level 3; it is close to Level 4 but stays at 3.

## Originality report
The web checks used web search. I searched each question's distinctive structure in words and symbols. No search found the same construction. Perfect novelty cannot be guaranteed. Please tell me if you recognise any question.

| Q | Mechanism | Web check | Standard ingredient |
|---|---|---|---|
| 1 | One finite set {-1,0,1} defined three ways (x³ = x, \|x\| = x², integer solutions of \|x-1\|+\|x+1\| = 2), against the real solution set (an interval) and the strict-inequality set (empty); the verdicts turn on the triangle-inequality equality case. | not found | "which sets are equal / empty" lists |
| 2 | Subsets X of A∪B that are equivalent to A but not equal to it, with A Δ X ⊆ B ("agrees with A outside B"); gives C(6,3) − 1. | not found | counting fixed-size subsets |
| 3 | The elements of S are the solutions of x+y+z = 5; compare the power sets of T (xyz ≠ 0) and S∖T; log₄ of 2^(6−15). | ingredient only | **yes**: beggar's-method counts and 2ⁿ subsets |
| 4 | The set equation (A Δ X)' = B ∪ C' solved by De Morgan, then cancelling with A Δ A = ∅; signed sum of X. | ingredient only | solving A Δ X = B appears as an abstract exercise |
| 5 | Survey where the all-three count is unknown and fixed by "none = all three"; percentage of exactly-two readers among readers. | ingredient only | **yes**: GMAT-style "none equals all three" problems exist, with different data and question |
| 6 | Independent events with P(A) known: "at least one" (through its complement) and "exactly one" give b+c−bc and b+c−2bc; exactly two from the partition none/one/two/three. | not found | close in spirit to the JEE problem with given "exactly one / exactly two / none" probabilities |
| 7 | Product of a subset divisible by 12 = 2²·3, turned into intersection conditions (meets {3,6,9}; meets {4,8} or has two of {2,6,10}); counted by complements of 2ⁿ type. | not found | "subsets with even product" type |

## Problems found while verifying
- Q7: one web-search summary gave 776 for a similar count, because it counted E∩F as 8 instead of 24. Brute force over all 1024 subsets confirms **792**.
- Q6: one web-search summary called the data inconsistent, because it treated the problem as having two events. With three events the data are consistent: P(B) and P(C) are 0.4 and 0.5 (in either order), and both orders give 0.35.
- Stem review (a self-check; an independent reader may still find things): in Q2 and Q4 the definition of Δ first used the letters X, Y, which clashed with the unknown set X. I rewrote it with M, N. Q4 states the universal set and the complement, and I checked that X exists and is unique.

## Rows whose concepts were hard to combine naturally
- **Q3 (row 437, negative decimal plan):** a count of subsets is a positive integer. To meet the planned negative-decimal style I asked for log₄(m/n), which is a derived quantity. The base-4 logarithm is the least natural part of the paper.
- **Q4 (row 438, negative integer plan):** set sizes cannot be negative, so the question asks for the sum of the elements of X, using a universal set that contains negative integers.
- **Q5:** "percent" is written as a word because the build does not allow the % sign outside maths.

## Notes
- The Hindi is my own translation. Please review the specialised terms (तुल्य समुच्चय, घात समुच्चय, सार्वत्रिक समुच्चय, परस्पर स्वतंत्र घटनाएँ).
- `_source/` holds `blueprint.json`, `meta.json` and `q01.json`-`q07.json`. To fix a question, edit its JSON and rerun `build_paper.py`.
