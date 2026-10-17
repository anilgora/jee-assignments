# Logarithm: revision kit report

- Items in the Quick Review: 46
- Batch All: 104 graded questions, High threshold 9 -> High 8, Medium 20, Low 18
  - High items (numbers): [9, 10, 11, 13, 14, 23, 24, 25]

## Added items
- 45: How do you compare two logarithmic numbers (decide $>$, $<$ or $=$)?  [source: DPP-4 Q15, Q21]
- 46: How do you simplify a nested radical $\sqrt{a\pm2\sqrt b}$?  [source: DPP-1 Q4]

## Rephrased items

## Questions with no matching item

## Question Bank questions counted once (overlap with a batch JM set)

## Validation warnings
- none

## Run notes (Logarithm: theory sheet + DPP only)

**Input files used (not modified):** `chapters/Logarithm/Theory.pdf` (22 pages, text PDF), `chapters/Logarithm/DPP.pdf` (59 pages, scanned images). No XII sheet, XIII sheet or Question Bank exists for this chapter. Prompt list: skill's `references/master_index.json` (Logarithm, 44 prompts, master pages 4-5); no master PDF was present, so the prompts could not be re-read from the page images.

**Grades are based on DPP questions only.** One Quick Review per language (batch "All"): 104 graded questions (DPP-1: 20, DPP-2: 30, DPP-3: 25, DPP-4: 29). High threshold = 9 (about 9.1 percent). High = 8 items (9, 10, 11, 13, 14, 23, 24, 25), Medium = 20, Low = 18. Low only means not tested in these DPP questions. Low items: 1, 6, 17, 18, 19, 22, 26, 28, 29, 30, 32, 33, 36, 39, 40, 41, 43, 44. In particular the DPPs contain almost no modulus-inequality, exponential-inequality, irrational-inequality, antilog or characteristic/mantissa questions, so those items show Low although they are in the theory sheet.

**Question extraction.** `extract_questions.py` found nothing (scanned PDF, as expected). `question_index.json` was written by hand from the page images. Stems are plain-text paraphrases of the printed stems (maths simplified), so the "Question" column in the xlsx is approximate; question numbers, DPP numbers and printed answers are as printed. Counts checked against the PDF: DPP-1 = 20, DPP-2 = 30, DPP-3 = 25, DPP-4 = 29. The overlap check was skipped (no QB).

**Added items (cross-chapter rule checked with `search_master.py`):**
- 45 (N1) comparing two logarithmic numbers: DPP-4 Q15, Q21. Master search for "compare/greater" found nothing equivalent in any chapter.
- 46 (N2) nested radical sqrt(a +- 2 sqrt b): DPP-1 Q4. No match in any chapter.

**Candidates not added (covered elsewhere or by an existing item):**
- Log inequality true for all real x (DPP-4 Q17): mapped to item 27; the quadratic "always positive" part is covered in Quadratic Equation (Relation between roots and coefficients / sign of quadratic).
- Sum / product of roots after substitution (DPP-4 Q5, Q13, Q16): covered in Quadratic Equation (items 3, 7); mapped to the log items only.
- Nested modulus ||x-1|-1| <= 1 (DPP-4 Q9): mapped to item 38 (applied twice); no master item for nested modulus.
- Telescoping product/sum of logs (DPP-1 Q6, Q11): mapped to item 13 (chain form).

**Rephrased items:** none by meaning. Typos from the master OCR were corrected in the prompt wording only (for example "Howclub", "logartihmic", "ofa"). Items 25 and 26 are garbled in the master text; they were read as "(variable)^(variable)" and its special case a^b = a^c (a = 1 or b = c), which matches the theory sheet (section 4.3). Please compare with the master page image.

**Uncertain mapping decisions (judgement calls):**
- DPP-1 Q17 (four statements), Q20 and DPP-4 Q28, Q29 (match-the-column, several parts) are mapped to the item that carries most parts plus the others as "also used".
- DPP-4 Q18-20 (paragraph) share one setup; each is mapped separately.
- DPP-4 Q23 (proof) is mapped to item 10 (power of the number); DPP-1 Q9 to item 4 (log to exponential form).
- DPP-4 Q28 part B (x^4 + 4 prime) is not a log idea; the question is still mapped by its log parts.
- Questions mapped to "-" : none.

**Source errors found in the printed solutions (answers recomputed):**
- DPP-2 Q2: printed answer 3 is right; the printed solution ends with "x = 3^1 = 1" (typo).
- DPP-2 Q3: printed answer 8 is right; the printed solution writes "2^x = 9+7" and "x = 4" (wrong); correct is 2x-7 = 9, x = 8.
- DPP-2 Q14: printed answer {2+10^-7, 3, 102} is right; the printed solution lists x = 2 (log(x-2) = 0 gives x = 3).
- DPP-2 Q7 and Q11 end with "Final solution x in { }" although the answers 1/3 and 16/5^(1/3) are correct.
- DPP-4 Q21(iv): the printed answer line repeats "(ii)"; the intended part is (iv) (>).
- DPP-1 Q2 and DPP-3 Q15 solutions are correct; DPP-3 Q9 solution is correct (x = 7).
- All printed final answers of DPP-2, DPP-3 and selected DPP-1/DPP-4 questions were re-checked numerically (38 checks, no failure); every example in the Quick Review was verified with sympy / numeric checks (nested radical, base-change chain, 49^log_7 5 = 25, modulus and irrational inequality solution sets, log inequality with variable base, characteristic/mantissa values, digit counts).

**Theory sheet issues (not changed in the kit):** the theory sheet's irrational-inequality section 8 has garbled symbols in the extracted text (types 4 and 5); the kit uses the standard results and its own verified examples. Section 5 example 3 answer (-3,-2) U (-1,0) U (1,3) was verified.

**New Hindi terms:** see `hindi_glossary_additions.md`.
