# Relations: generation report

Blueprint: `qp_blueprints/Relations.xlsx`. There is no `Relations_config.xlsx`, so the check ran without `--config`.
This scheduled run made the paper on 19-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy, mpmath and python-docx were missing for `python3`. I installed them with `python3 -m pip install pandas openpyxl sympy mpmath python-docx`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- `build_paper.py --blueprint` passed on the first build with **no errors and no warnings**. No script was edited and no check was weakened.
- I rendered page 1 of each of the three PDFs and looked at it. The Hindi is shaped and the equations are typeset in 2D. This paper has no paragraph question.

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the blueprint has only Single Correct and Numerical types and nothing above level 3.
- **Paper:** 9 questions: 1 Single Correct (Q1), then 8 Numerical (Q2-Q9).
- **Reorder (`--reorder`), old -> new:** 448->1, 442->2, 443->3, 444->4, 445->5, 446->6, 447->7, 449->8, 450->9.
- **Answer Plans:** the blueprint had none, so the script drew all 9. Every answer matches its plan; the build checks this.
  - Q1 Option C; Q2 positive 2-digit integer; Q3 negative decimal; Q4 negative integer; Q5 positive decimal; Q6 decimal between 0 and 1; Q7 positive 3-digit integer; Q8 negative integer; Q9 positive 2-digit integer.
- **Cells containing ";":** the check warned about spreadsheet rows 1, 2 and 7. With no config to split them, each cell was kept as **one** concept, as you instructed. The cell is "Cartesian product of sets; number of elements" (used in Q1 and Q2).
- **Warnings.** I recorded these and did not fix them, because the blueprint is your decision. There were no errors, and the blueprint file was not edited.
  - Q4 lists 3 concepts in a Main paper. I kept the row as given, and the question uses all 3 concepts.
  - Several concepts are repeated across rows, and each use has a different mechanism:
    - "Cartesian product of sets; number of elements" (Q1, Q2).
    - "Counting reflexive / symmetric / transitive / equivalence relations on a finite set" (Q4, Q5, Q6, Q9).
    - "Equivalence relations and equivalence classes" (Q4, Q7).
    - "Reflexive, symmetric, transitive and antisymmetric relations" (Q4, Q8).

## Answers
| Q | Type | Answer |
|---|---|---|
| 1 | SCQ | (C) 32 |
| 2 | Numerical | 34 |
| 3 | Numerical | -0.5 |
| 4 | Numerical | -21 |
| 5 | Numerical | 2.25 |
| 6 | Numerical | 0.6 |
| 7 | Numerical | 116 |
| 8 | Numerical | -15 |
| 9 | Numerical | 64 |

Every answer was recomputed in Python. Each count was checked by brute-force enumeration of the actual relations or subsets, and Q3 with sympy.

## Originality report
The web checks used web search. I searched each question's distinctive structure in words and symbols. Perfect novelty cannot be guaranteed. Please tell me if you recognise any question.

| Q | Mechanism | Web check | Standard ingredient |
|---|---|---|---|
| 1 | The common part n(A∩B) is solved from n((A×B)∪(B×A)) = 70 − k², then used in a new product. | ingredient only: the identity (A×B)∩(B×A) = (A∩B)×(A∩B) is a textbook (NCERT-type) exercise | yes, that identity |
| 2 | Count the subsets of A×A that are products X×Y and avoid (1,2). The empty product comes from many pairs (X,Y), so it is counted once. | not found | 2^n subsets |
| 3 | The relation (x²+ax+b)y = 4x−3. The domain comes from the roots of the coefficient, and the vertical-line test fails only on the line x = 3/4, where the equation becomes 0 = 0. | not found | none beyond definitions |
| 4 | Symmetric + transitive relations on a 4-set are equivalence relations on their support (52 of them). The antisymmetric ones are the subsets of the diagonal (16), so 16 − 37. | ingredient only: JEE Main 2024 "symmetric, not reflexive" counts are different | partition counts (Bell numbers) |
| 5 | m(R) is the minimum number of pairs to add to reach an equivalence relation. It is averaged over all 64 symmetric relations, using the split (closure size − n(R)). | ingredient only: the single-relation "minimum pairs to add" exercise is standard | closure by linked classes |
| 6 | p/q: three classes of size ≥ 2 vs two classes of size ≥ 2 on a 6-set. The two-class count is 2^5 − 1 minus the singleton cases. | ingredient only: Stirling numbers S(n,2) = 2^(n−1) − 1 are standard; the class-size restriction is the new part | **yes**: without the restriction this would be a table look-up, which is why I added it |
| 7 | R = "largest odd divisor", composed with R⁻¹. The composite is the "same odd part" equivalence relation, and n(S) is the sum of squares of the chain sizes. | not found | chains m, 2m, 4m (known from divisibility selection problems) |
| 8 | The family (x−y)² ≤ k on Z passes through the empty relation, the identity relation and non-transitive relations. The answer is the sum of the k that give a transitive relation (vacuous transitivity is the trap). | not found | \|a−b\| ≤ 1 "not transitive" example |
| 9 | R ∪ R⁻¹ = A×A and R ∩ R⁻¹ = I_A decode to reflexive and antisymmetric with exactly one orientation per pair, giving 2^6. | ingredient only: the 2^(n choose 2) tournament count | yes, the count itself is a known formula; the decoding is the task |

## Difficulty (calibrated 0-5 scale)
- Levels: L2: Q1, Q7, Q8, Q9; L3: Q2, Q3, Q4, Q5, Q6. Every question is at its target level, so none is one level off.
- The equivalence-relation adjustment (+0.5) applies to Q4, Q5, Q6 and Q7. There is no MCQ, so the MCQ floor does not apply.
- Marks-weighted index (SCQ 3, Numerical 4; 35 marks): **2.57 before** the equivalence adjustment and **2.80 after** it. This is a chapter paper in the Main pattern, so there is no expected range.
- Confidence: Q1 High, all others Medium.
- Consistency pass: Q7 (L2, equivalence) is the hardest L2 and Q6 (L3) is the easiest L3. The difference is the restricted case analysis in Q6 against the direct class listing in Q7, so I kept both.

## Rows whose concepts were hard to combine naturally
- **Q6** ("counting equivalence relations" + "2^n and 2^n − 1 combinations"): the first design was a plain ratio of Stirling numbers. The web check showed it is a table look-up, so I added the "each class has at least two elements" condition. The 2^5 − 1 count then needs a correction step.
- **Q4** (three concepts in a Main row): all three are used naturally. The answer is negative because it is asked as a difference, p − q.

## Problems found while verifying
- **Q5:** the first choice, a 4-element set, gave the integer 5, which does not fit the "positive decimal" plan. I used the 3-element set (mean 2.25).
- **Stem review (self-check; an independent reader may still find things):**
  - Q2: "and (1,2) ∉ S" could be read as a condition on X and Y, so I moved it before the product condition.
  - Q1: I tidied the distractor note in the full solution.
  - No other changes.

## Hindi
The Hindi is my own translation, using the standard terms from `hindi_terms.md` (स्वतुल्य, सममित, संक्रामक, प्रतिसममित, तुल्यता संबंध, प्रतिलोम संबंध, तत्समक संबंध). Please review the specialised terms.

## Files
- `Relations_Shortened_Solutions.docx`, `Relations_Full_Solutions.docx`
- `Relations_Questions_EN_HI.pdf`, `Relations_Questions_and_Shortened_Solutions.pdf`, `Relations_Questions_and_Full_Solutions.pdf`
- `Relations_difficulty.xlsx` (internal)
- `_source/`: `blueprint.json`, `meta.json`, `q01.json`-`q09.json`. To fix a question, edit its file and rebuild with `build_paper.py`.
