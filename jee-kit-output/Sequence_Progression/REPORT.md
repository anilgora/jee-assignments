# Sequence & Progression: revision kit report

- Items in the Quick Review: 67
- Batch XII: 134 graded questions, High threshold 12 -> High 4, Medium 43, Low 20
  - High items (numbers): [5, 20, 25, 48]
- Batch XIII: 133 graded questions, High threshold 12 -> High 4, Medium 46, Low 17
  - High items (numbers): [5, 18, 25, 48]

## Added items
- 12: The ratio of the sums of $n$ terms of two APs is given. How do you find the ratio of their $k^{th}$ terms?  [source: DPP-1 Q8, J-I Q6, JM(XII) Q12]
- 13: How do you use the sum of terms that are equidistant from the two ends of an AP?  [source: DPP-1 Q3, JM(XIII) Q21, J-II Q1]
- 14: How do you count or add the numbers lying in a range that are divisible by $a$ or $b$ (or leave a given remainder)?  [source: DPP-2 Q1, DPP-1 Q7, JM(XIII) Q2, JM(XII) Q14]
- 22: How do you convert a recurring decimal into a fraction?  [source: DPP-2 Q6]
- 27: How do you find the condition when three terms of a GP (or AP) are the sides of a triangle?  [source: JM(XIII) Q61, Q59]
- 51: How do you find the sum of the products of numbers taken two at a time?  [source: J-I Q38, J-II Q22]
- 65: How do you handle terms written in groups (the $n^{th}$ group, rows of numbers)?  [source: J-II Q20, JM(XII) Q44, JM(XIII) Q75, Q76]
- 66: How do you solve real-life and geometrical problems that lead to an AP or a GP?  [source: DPP-3 Q15, JM(XIII) Q67, Q68, J-I Q8]
- 67: How do you use "a sum of squares equals zero" to get relations among $a,b,c$?  [source: DPP-3 Q17, QB Q53, J-I Q11, JM(XIII) Q59]

## Rephrased items
- 20 (original 17): Memorize the formulae for $S_n$ of a GP and its derivation.

## Questions with no matching item
- C-I:15
- C-II:4
- C-II:13
- DPP-1:15
- QB:71

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]

## Validation warnings
- none

## Run notes (Sequence & Progression)

**Input files used (not modified):** `chapters/Sequence_Progression/Theory.pdf` (50 pp), `XII.pdf` (150 pp), `XIII.pdf` (170 pp), `DPP.pdf` (48 pp, 4 DPPs), `QB.pdf` (43 pp, questions numbered 22-88). Prompt list: skill's `references/master_index.json` (Sequence & Progression, 58 prompts, master pages 6-8). No master PDF was present, so the prompts were not re-read from the page images; the OCR typos were corrected only in wording (for example "Howto", "ofa", "n®").

**Question extraction (counts checked against the PDFs):** J-I 39, J-II 36, J-A 15, C-I 25, C-II 35, JM(XII) 52, JM(XIII) 77, DPP-1 16, DPP-2 26, DPP-3 19, DPP-4 17, QB 67. The sheets' contents pages list page numbers only, not question counts, so the counts were checked against the last printed question number of each exercise. Stems in the index are text-extracted and sometimes garbled; ambiguous ones were read from the page images (J-I 30, J-II 15/17/23-25, C-II 2/3/22/24-33/35, JM(XIII) 31/42/50/59, QB 37/38).

**Overlap QB / JM(XIII):** 26 QB questions equal a JM(XIII) question (QB 57-68, 75-88). They are counted once in the XIII batch and mapped identically. No QB question equals a JM(XII) question. detect_overlaps also listed QB 42 vs JM(XIII) 23 (similarity 0.61): checked by eye, they are different questions, so not treated as overlap.

**Grades.** XII: 134 graded questions (JM(XII) 52 + J-A 15 + QB 67), High threshold 12 -> High items 5, 20, 25, 48 (final numbers). XIII: 133 graded questions (JM(XIII) 77 + J-A 15 + QB 67 - 26 overlap), threshold 12 -> High items 5, 18, 25, 48. J-I, J-II, C-I, C-II and the DPPs are mapped (they appear in the practice map) but not graded. Low only means "not tested in these questions".

**Added items (cross-chapter rule checked with `search_master.py`, nothing equivalent found in any chapter):** ratio of S_n of two APs (final no. 12); sum of equidistant terms of an AP (13; the sheet has it only as a highlight, not as a prompt); count/sum of numbers divisible by a or b (14); recurring decimal as GP (22); triangle sides in GP (27); sum of products two at a time (51); groups/rows of numbers (65); real-life and geometric AP/GP problems (66); sum of squares = 0 trick (67). Searched keywords: groups, triangle sides, products two at a time, recurring decimal, greatest integer, weighted AM-GM, divisible by, remainder, inclusion, bounce, sum of squares, ratio of sum of n terms, equidistant.

**Candidates not added:**
- Greatest integer of a sum (JM(XII) Q30, C-II Q4): no matching master item in any chapter, but the question is just "sum the series, then take the floor"; mapped to the summation item (44).
- Pairing f(n)+f(100-n)=1 (C-II Q4): Challenger (not used for coverage); mapped "-".
- Minimising a product/term of an AP via a quadratic in d (DPP-1 Q11, JM(XIII) Q7): covered by the quadratic-minimum idea in Quadratic Equation; mapped to the AP items.
- Counting problems with gcd/number theory (JM(XIII) Q16, Q5, QB Q59, JM(XII) Q29, QB Q71): not AP ideas except the AP of multiples; mapped to item 14 where an AP of multiples is used, QB Q71 to "-".

**Rephrased items:** only original item 17 ("Memorize formulae for S_n of AP and its derivation" under the heading Sum of n terms of GP): the master text says AP but the heading is GP; rewritten as GP. Items 25/26 of the master OCR were readable. Other OCR typos were corrected without changing meaning.

**Uncertain mapping decisions (judgement calls):**
- Match-the-column and multi-part questions (J-II Q34-36, C-II Q35) are mapped to the item that carries most parts, others as "also used".
- J-II Q21 (four parts) -> splitting for type 3 (main) with method of difference and continued products as others.
- Logarithm-based AP/GP/HP conditions (J-I Q3, JM(XII) Q1/Q6, JM(XIII) Q1/Q47, DPP-4 Q13) are mapped to "a,b,c in AP/GP" (items 6/21) with "convert GP to AP" or "operation on all terms" as the other item; the log work itself belongs to the Logarithm kit.
- Ratio/second-difference questions J-A Q13 (area of l_i * w_i) -> type 2 identification (46).
- Telescoping questions with factor products (JM(XIII) Q31, Q65, Q77, JM(XII) Q33/Q45, C-I Q16, DPP-4 Q3/Q16) are mapped to the nearest of items 49/51/54/58; the choice between these four is a judgement.
- JM(XIII) Q59 is mapped to the sum-of-squares item with GP condition and triangle sides as others.
- Not classifiable and mapped "-": C-I Q15 (n-th term after deleting perfect squares), C-II Q4 (pairing trick), C-II Q13 (stem empty in the PDF), DPP-1 Q15 (bell game, LCM), QB Q71 (3^n+7^n multiple of 10).
- Paragraph question groups (J-II Q23-25, C-II Q24-25, Q29-30, Q31-33) are mapped one by one using the paragraph setup.

**Source/extraction issues found (answers recomputed only where used in an example):** DPP-3 Q3 has no printed answer captured by the extraction (the question is mapped normally; its answer was not re-derived). JM(XIII) Q61 shows answer "A" in the index (extraction glitch; correct value 1, as in the Quick Review example). Printed answers were not otherwise re-verified question by question; every example in the Quick Review and notes was checked with sympy / exact arithmetic (sum of alternating squares to 2003 = 2007006, inclusion-exclusion sum 3050, S_30 = 310, p = 7/47, type 2/3/4 sums, 11/96, 2/9, 337500 and others).

**Not possible in this run:** Word equations cannot be previewed in LibreOffice; the verifier reports 0 raw LaTeX and equations present in every docx. Hindi was written by the author with the glossary; new terms are in `hindi_glossary_additions.md`.
