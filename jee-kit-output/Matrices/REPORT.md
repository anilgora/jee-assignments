# Matrices: revision kit report

- Items in the Quick Review: 80
- Batch XII: 125 graded questions, High threshold 11 -> High 4, Medium 45, Low 31
  - High items (numbers): [32, 36, 53, 80]
- Batch XIII: 111 graded questions, High threshold 10 -> High 6, Medium 40, Low 34
  - High items (numbers): [22, 30, 32, 39, 53, 80]

## Added items
- 27: How do you handle trigonometric (rotation-type) matrices: product, powers, inverse?  [source: J-I: 12,13,27; J-II: 21; C-I: 14; J-M(XIII): 32; DPP-2: 6,9; DPP-5: 2,5,16; QB: 117,118,126,130]
- 32: How do you find $A^n$, an entry, the trace or the sum of all elements of $A^n$ (or of $A+A^2+\dots+A^n$)?  [source: J-A: 25; C-I: 1,2,18; C-II: 2,29; J-M(XII): 2,3,5,9,10,11,18,22,25,26,29,30,39,45; J-M(XIII): 6,12,16,20,26,44,53; DPP-5: 1; QB: 116,118,120,124,126,128,133,138,144,150,156]
- 72: How do you use a matrix defined by its action on column matrices ($AX_1=Y_1,\ AX_2=Y_2,\dots$)?  [source: J-I: 34; J-II: 22,34,35,36; J-M(XII): 17; J-M(XIII): 37,39,42,50; QB: 127]
- 73: How do you solve a matrix equation such as $AX=B$, $XA=B$ or $AXB=C$ for the unknown matrix $X$?  [source: J-II: 23; C-I: 21; C-II: 4,6,10]
- 80: How do you count (or find the extreme value of) matrices whose entries come from a given set and satisfy a condition?  [source: J-I: 38; J-A: 11,14,27,28,29; C-I: 19; C-II: 13,20,21,22,23,24,25,30; J-M(XII): 7,8,15,24,28,40,41,42,44; J-M(XIII): 4,15,25,27,50; QB: 121,131,136,149,151,160,163]

## Rephrased items

## Questions with no matching item
- J-A:19
- C-I:3
- C-II:17
- J-M(XII):13
- QB:114
- QB:115
- QB:119

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 161, 162, 163, 164]

## Validation warnings
- none

## Input files used (not modified)
- chapters/Matrices/Theory.pdf (theory sheet, 33 pages)
- chapters/Matrices/XII.pdf (XII sheet: J-1, J-2, J-M, J-A, C-I, C-II; 147 pages)
- chapters/Matrices/XIII.pdf (XIII sheet; only its J-M was used; 159 pages)
- chapters/Matrices/DPP.pdf (DPP 1-5, 46 pages)
- chapters/Matrices/QB.pdf (JEE Main question bank, Q114-164, 38 pages)
- Master prompt list: .claude/skills/jee-chapter-revision-kit/references/master_index.json (Matrices: 75 prompts in 18 headings, master pages 11-13). The master PDF (jee-inputs/quick_review_all_chapters.pdf) is not in the repo, so prompts were taken from the saved index text and not re-read from the scan: only obvious OCR typos were corrected (for example "ofa", "Whencan", "NIlpotent", a stray "|"); no prompt was reworded, so no item is tagged "rephrased".

## Item numbering
- The master list has the heading "Extra Reading Material" numbered 1-4 again; in this kit they are items 72-75 (o = 72-75). The heading "Important Definition(s)" occurs twice in the master (prompts 3-6 and 31-34) and is kept twice.
- Added items sit under the matching heading: rotation-type matrices (27, in Multiplication of Matrices), $A^n$ / sum of elements (32, in Characteristic Equation), matrix defined by columns (72) and matrix equations (73, in System of Equations), counting matrices (80, Miscellaneous). Final numbers in this report are the printed numbers; internally they are N1-N5.

## Question counts (from the sheets' last printed numbers)
J-I 38, J-II 39, J-M(XII) 45, J-M(XIII) 55, J-A 29, C-I 22, C-II 31, DPP-1 16, DPP-2 19, DPP-3 10, DPP-4 13, DPP-5 22, QB 51 (Q114-164). Total 390, all mapped (7 with no matching item, listed above).
- The sheet headings are "Exercise J-1" and "J-2" (not J-I / J-II); extraction was run with a patterns file for those two names.
- Graded counts: XII 45+29+51 = 125; XIII 55+29+51-24 = 111.

## Overlap
24 QB questions (134-153, 161-164) are the same as J-M(XIII) questions (script similarity 0.76-0.95; the stems were compared by eye and are the same JEE Main 2023 questions: QB 134=XIII 1, 135=2, 136=4, 137=5, 138=6, 139=7, 140=8, 141=9, 142=10, 143=11, 144=12, 145=17, 146=18, 147=23, 148=24, 149=25, 150=26, 151=27, 152=28, 153=30, 161=13, 162=14, 163=15, 164=31). They are counted once in batch XIII and carry the same mapping as the J-M(XIII) question. Four pairs flagged "possible" for batch XII (QB 131/J-M(XII) 28, 144/9, 150/9, 160/24) were compared by eye: different questions, not overlaps.

## Coverage check (Challenger excluded)
Five items were added (N1-N5): counting / extreme value of matrices with restricted entries; rotation-type (trigonometric) matrices; $A^n$ and the sum of all elements of $A^n$; matrix defined by its action on column matrices; matrix equations $AX=B$, $XA=B$. Searched the master index first (search_master.py with "number of matrices", "count", "rotation", "matrix power", "A^n", "column vector", "matrix equation", "sum of all elements", "eigen"): nothing in any chapter covers them (the hits were only existing Matrices prompts 25, 26, 27-30, 61, 66, 67 or unrelated chapters).
Not added (covered in another chapter): consistency / unique / infinite solutions of $AX=B$, homogeneous systems, Cramer's rule (covered in Determinant / System of Equations and System of Homogeneous Linear Equations); the questions were mapped to items 68, 69, 70, 71 of this chapter. Evaluating a determinant itself (Determinant chapter).

## Questions with no matching item
J-A 19 (determinant with binomial sums, Binomial Theorem / Determinant), C-I 3 (determinant row-operation question), C-II 17 (number-theory use of a determinant), J-M(XII) 13 (determinant with greatest-integer entries), QB 114, 115, 119 (minimum of a determinant of entries in $b$, $\theta$, A.P. - Determinant chapter).

## Source errors found / uncertain source items
- Printed answers were not re-verified for every one of the 390 questions; only the examples inside the Quick Review were verified with sympy / brute force (for example: the number of invertible $2\times2$ matrices with entries in {0,1,2} is 50 of 81, with entries in {0,1} it is 6 of 16).
- Many stems with 2D matrices come out garbled from the PDF text (matrix entries lost); those questions were mapped from the stem words, the exercise header and the printed solution, and a few pages were read as images (J-II 28-36, C-II 17-31).

## Uncertain mapping decisions (judgement; the matrix in the stem is not readable or the idea is mixed)
- J-I 10 (stem lost; mapped to multiplication), J-II 15 (A given by a_{12}, a_{23}, a_{31} and a relation with A^T; mapped to symmetric/skew items 44, 41), J-II 1 (counts of entries of triangular/diagonal matrices; item 7).
- J-M(XII) 10, 11, 25, 29, 45 and J-M(XIII) 12, 16, 31 (the matrix is lost in the extracted text): mapped by the printed solution / answer type to the powers item (N3) or the nearest standard item.
- C-II 17-19: a determinant / circle paragraph; only the matrix product that writes the circle's equation is mapped (item 19), C-II 17 is left unmapped.
- Questions that use a determinant result inside a matrix argument (J-M(XIII) 2, 9; J-I 24) are mapped to the invertibility / determinant-of-product items; the determinant evaluation itself belongs to the Determinant chapter.
- QB 158 (norm relation $A=XB$): mapped to the trace-of-$AA^T$ item and orthogonality.
- J-A 29 (match the following with golden-ratio entries): counting item N1, plus symmetric matrices 41/42.
- Parts of paragraph questions in C-II 20-31 are mapped by the paragraph's content (symmetric 0/1 matrices, the set $T_p$, the system (E)); C-II 29-31 are match-the-following questions mapped to the main item of the matrix part only.

## Hindi
New terms are in hindi_glossary_additions.md. "singular / non-singular" are written अव्युत्क्रमणीय / व्युत्क्रमणीय; "rank" is kept as रैंक. Prompt numbers and formulas are the same in English and Hindi.
