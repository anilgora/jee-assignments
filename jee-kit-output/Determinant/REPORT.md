# Determinant: revision kit report

- Items in the Quick Review: 45
- Batch XII: 58 graded questions, High threshold 5 -> High 5, Medium 9, Low 31
  - High items (numbers): [15, 38, 40, 42, 45]
- Batch XIII: 66 graded questions, High threshold 6 -> High 5, Medium 10, Low 30
  - High items (numbers): [15, 38, 40, 42, 45]

## Added items
- 43: How do you solve an equation of the form (determinant in $x$) $=0$?  [source: J-II: 7,8,9; J-M(XII): 4; J-M(XIII): 14,21; J-A: 3,4; QB: 96; DPP-1: 1,17; DPP-2: 10; DPP-3: 2,3,7; C-I: 9,18,22; C-II: 17]
- 44: How do you find the degree, a coefficient, or the constant term of a determinant that is a polynomial in $x$?  [source: J-I: 6; J-II: 25; QB: 101; DPP-2: 18; DPP-3: 1,11; C-I: 6,9,19]
- 45: How do you handle a determinant whose elements are trigonometric (or other) functions: simplify, find its range/maximum/minimum or the number of roots?  [source: J-II: 5,7,32; J-M(XII): 4,6,8,11,22; J-M(XIII): 8,12,27; J-A: 2; QB: 89,95,103,106; DPP-2: 19; DPP-4: 4,11; C-I: 3,5,8,12,13,15,17,18,19,22; C-II: 10,16,23,24]

## Rephrased items

## Questions with no matching item

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [112]

## Validation warnings
- none

## Input files used (not modified)
- chapters/Determinant/Theory.pdf (theory sheet, 22 pages)
- chapters/Determinant/XII.pdf (XII sheet: J-1, J-2, J-M, J-A, C-I, C-II; 107 pages)
- chapters/Determinant/XIII.pdf (XIII sheet; only its J-M was used; 116 pages)
- chapters/Determinant/DPP.pdf (DPP 1-4, 47 pages)
- chapters/Determinant/QB.pdf (JEE Main question bank, Q89-113, 22 pages)
- Master prompt list: .claude/skills/jee-chapter-revision-kit/references/master_index.json (Determinant: 42 prompts, 12 headings, master pages 9-10). Prompts were taken from the saved index text (not re-read from the scan images); none needed rewording, so no item is tagged "rephrased".

## Question counts (from the sheets' last printed numbers)
J-I 22, J-II 33, J-M(XII) 26, J-M(XIII) 35, J-A 7, C-I 22, C-II 24, DPP-1 17, DPP-2 19, DPP-3 12, DPP-4 12, QB 25 (Q89-113). Total 254, all mapped (none unmapped).
- The sheet headings are "Exercise J-1" and "J-2" (not J-I / J-II); extraction was run with a patterns file for those two names. J-II 7, 8, 20 and C-II 5 had empty or garbled stems in the extracted text; they were read from the text of the solution/page image and mapped by their content.

## Overlap
QB 112 = J-M(XIII) 2 (same stem, checked by eye) -> counted once in batch XIII. Other "possible" pairs flagged by the script (QB 89/XII 23, QB 92/XII 22, QB 105/XII 13, QB 107/XII 14, QB 89/XIII 12, QB 94/XIII 27, QB 105/XIII 24) were compared by eye: different questions, not overlaps. Graded counts: XII 26+7+25 = 58, XIII 35+7+25-1 = 66.

## Coverage check (Challenger excluded)
Three items were added (43-45 = N1-N3): solving a determinant equation, polynomial determinant (degree/coefficient/constant term), and trigonometric/function determinants (range, extrema, roots). Searched the master index first (search_master.py with "determinant", "polynomial", "coefficient of x", "degree of", "factor theorem", "range", "complex", "conjugate", "omega"): the hits are in other chapters (Quadratic Equation, Function, Complex Number...) but none covers a determinant-specific method, so the items were added here. Not added (no new item): determinants with complex entries or Hermitian type (only C-II 14, a Challenger question, mapped to the properties item); differentiation of a determinant (master heading under Method of Differentiation); determinants with angles of a triangle (mapped to the trigonometric item).

## Source errors found / uncertain source items
- Theory sheet, minors/cofactors example (Q.2): the printed answers 33, 9, 15, 12 cannot be reproduced from the matrix as printed; own example used instead.
- Theory sheet, multiplication Q.3 and J-II 15: the sheet prints $+2(a_1-a_2)\dots(b_3-b_1)$; computing the determinant of $(a_i+b_j)^2$ with sympy gives $-2(a_1-a_2)(a_2-a_3)(a_3-a_1)(b_1-b_2)(b_2-b_3)(b_3-b_1)$. The kit uses the sympy sign. (Prove-type questions are unaffected.)
- J-M(XII) 18: first equation of the system is missing in the extracted text; mapped as an inconsistency question (38) from the visible part.
- Printed answers were not re-verified for every one of the 254 questions; only the examples inside the Quick Review were verified with sympy.

## Uncertain mapping decisions (judgement; text of the stem is garbled or the idea is mixed)
- Standard-determinant vs operation questions: DPP-2 1, 2, 4, 11, 12, 13; DPP-3 4, 5, 12; DPP-4 3, 7, 9, 10; J-I 3, 4, 10, 11; J-II 10; C-I 10, 16; J-M(XIII) 31 (mapped to the nearest of standard determinants / row operations / multiplication).
- DPP-2 10 and DPP-1 17 (equation in $x$) mapped to the added item "solve determinant = 0".
- J-A 2 (trigonometric system) mapped to homogeneous system + trigonometric item.
- QB 113: the logarithmic AP part is outside the chapter (needs the Logarithm / Sequence chapters); mapped to the 3x3 expansion item plus the AP-row item.
- QB 90: logs of GP terms; mapped to the AP-in-row item.
- C-II 17-19, 20-24 (paragraph questions): mapped by the paragraph's content.
- Questions needing a point-to-plane distance (J-M(XII) 24, J-M(XIII) 18) are mapped to the system items only; the distance step belongs to the 3-D geometry chapter.

## New Hindi terms
See hindi_glossary_additions.md.
