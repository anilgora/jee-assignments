# Permutations & Combinations: revision kit report

- Items in the Quick Review: 106
- Batch XII: 85 graded questions, High threshold 8 -> High 2, Medium 51, Low 53
  - High items (numbers): [5, 26]
- Batch XIII: 92 graded questions, High threshold 8 -> High 3, Medium 52, Low 51
  - High items (numbers): [5, 26, 38]

## Added items
- 4: How to count "neither / none / at least one of several conditions" using inclusion-exclusion (Venn diagram)?  [source: J-I: 19,20; J-II: 31; J-M(XII): 21,23; J-M(XIII): 32; C-II: 2; DPP-6: 10; QB: 199]
- 8: How to find the numbers divisible by 2, 5, 6, 8, 9, 11 or 25?  [source: J-M(XII): 10,15,31; J-M(XIII): 11,16,25,37; DPP-1: 11,13; DPP-2: 17; DPP-4: 9]
- 9: How to count (and add) palindromic numbers or words?  [source: J-I: 29; J-M(XII): 11; DPP-1: 12; DPP-6: 9]
- 10: How to count numbers (or selections) whose digits are strictly increasing or decreasing?  [source: J-II: 13; J-M(XIII): 10; C-I: 12; DPP-3: 12; QB: 168]
- 26: How to count selections with conditions: particular persons always included, never included, together or not at all, or not together?  [source: J-I: 8; J-II: 2,3,4,6,7,11,12,42,43,44,48; J-M(XII): 2,5,20; J-M(XIII): 6,8,31,45,55; J-A: 8,9,12,18; C-I: 2; C-II: 7; DPP-3: 1,3,10,11; DPP-4: 11,13,14,17; QB: 167,170,190,194,198]
- 27: How to find the number of intersection points of lines, diagonals or chords?  [source: J-M(XIII): 48; C-I: 11; QB: 196]
- 28: How to arrange when some persons or objects are tied to particular places (seats, middle place, sides of a table)?  [source: J-I: 9; J-II: 14; DPP-4: 4,12,16; DPP-5: 14; DPP-6: 14]
- 68: How to count ordered pairs of numbers with a given LCM or GCD?  [source: C-I: 9; QB: 185]
- 89: How to count by remainder classes (parity or residues mod $m$) when a sum must be divisible by $m$?  [source: J-M(XII): 12; J-M(XIII): 7; QB: 184]
- 90: How to count arrangements in which adjacent objects must differ (colouring a line or a circle)?  [source: J-A: 13; DPP-2: 3,11,15]

## Rephrased items

## Questions with no matching item
- C-II:17

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199]

## Validation warnings
- none

## Input files used (not modified)
- chapters/Permutations_Combinations/Theory.pdf (theory sheet, 43 pages)
- chapters/Permutations_Combinations/XII.pdf (XII sheet: J-I 36, J-II 57, J-M 31, J-A 19, C-I 20, C-II 28 questions; 105 pages)
- chapters/Permutations_Combinations/XIII.pdf (XIII sheet; only its J-M (58 questions) was used; 119 pages)
- chapters/Permutations_Combinations/DPP.pdf (DPP 1-7: 22+17+17+17+15+20+1 = 109 questions; 42 pages)
- chapters/Permutations_Combinations/QB.pdf (JEE Main question bank, Q165-199, 35 questions; 17 pages)
- Master prompt list: .claude/skills/jee-chapter-revision-kit/references/master_index.json (Permutations & Combinations: 96 prompts in 26 headings, master pages 14-17). The master PDF jee-inputs/quick_review_all_chapters.pdf is not in the repo, so prompts were taken from the saved OCR index, not read from the scan.

## Question counts and grading
- Every sheet exercise was checked for contiguous numbering and no empty stems (J-I 1-36, J-II 1-57, J-A 1-19, C-I 1-20, C-II 1-28, J-M(XII) 1-31, J-M(XIII) 1-58, DPP-1..7, QB 165-199); each count matches the printed question numbers.
- Batch XII graded = J-M(XII) 31 + J-A 19 + QB 35 = 85; High threshold max(2, round(0.091 x 85)) = 8.
- Batch XIII graded = J-M(XIII) 58 + J-A 19 + QB 15 (20 of the 35 QB questions are the same as XIII J-M questions and are counted once, as J-M) = 92; High threshold 8.
- High items. XII: no. 5 (repetition in formation of numbers) and no. 26 (selections with conditions, added). XIII: the same two and no. 38 (arrange things when a few are alike). Medium/Low counts are in the first lines of this report. Low only means "not tested in these graded questions".
- Overlaps counted once (QB = XIII J-M): QB 174=J-M 49, 175=50, 176=51, 177=54, 178=39, 179=40, 180=42, 181=43, 182=23, 183=27, 190=55, 191=56, 192=57, 193=44, 194=45, 195=47, 196=48, 197=29, 198=31, 199=32. detect_overlaps.py suggested 19 of them; QB 178 (J-M(XIII) 39) was missed by the detector because its text is garbled and was added after comparing the pages. No QB question equals an XII J-M question.

## Item numbering
- The master list numbers "Extra Reading Material" 1-16 again after the main 1-80 (the last prompt, "x1 + 2x2 + ... + kxk = n", sits under a heading whose OCR is unreadable). They are items o = 81-96 here; the heading of the last one is reconstructed as "Ordered and weighted solutions (0 < x1 <= x2 <= ... <= xk)" from the OCR fragment, so check it against the scan.
- Added items sit under the matching master headings, so the final item numbers shift (the first report list above gives final numbers; ids N1..N10 are the added items).
- Master prompts with garbled maths ("m^n or n^m", "nCr", "D_n", P(n,k), Stirling) were rebuilt from the surrounding words and the theory sheet; no prompt was reworded, so no item is tagged "rephrased". Prompt 53 ("proper divisors") was given the usual meaning (divisors other than 1 and N) because the sheet does not define it.

## Added items (coverage check, Challenger not used) and candidates not added
Added (not covered in any chapter of the master Quick Review; checked with search_master.py): N2 inclusion-exclusion for counting; N9 divisibility tests (2, 5, 6, 8, 9, 11, 25); N7 palindromes; N3 strictly increasing / decreasing digits; N1 selections with conditions (committee type); N4 intersection points of lines / diagonals / chords; N8 arrangements with persons tied to places; N5 ordered pairs with a given LCM / GCD; N6 remainder-class counting; N10 adjacent-different colouring of a line or circle. Their source questions are listed above.
Candidates considered and not added (mapped to the nearest existing item):
- subsets / pairs of disjoint subsets (3^n) -> item 7 (m^n); fixed relative order of some objects -> item 34; multiplicative partitions (product of digits = N) -> item 76; arrangements with exactly r repeats of a digit -> items 4 / 31; inclusion-exclusion for probability of unions is in Probability / Venn Diagram, but that is a probability formula, so the counting version was still added as N2.

## Questions with no matching item
- C-II:17 (symmetric 0/1 determinant, count of matrices with a given determinant value; it belongs to Determinants).

## Source errors found and uncertain decisions
- J-M(XIII) 14 (ASSASSINATION, vowels together): the sheet prints 504000; the theory sheet's own formula 8!/(4!2!) x 6!/(3!2!) = 840 x 60 = 50400 is correct (confirmed by brute force). Mapped normally.
- J-M(XIII) 35 (digits a, b, c in A.P., 9-digit numbers): NTA key 1260 counts the block method without removing double counting; brute force with digits 1,2,3 gives 944 (distinct-digit A.P. triples) or 1208 (constant triples counted too). Left as printed; mapped to item 31 (alike objects) with item 2 as "other".
- J-M(XII) 7 prints "i + j + k <= 15"; the intended condition is i + j + k != 15 (answer 443 = 455 - 12). J-M(XII) 24 is "sum of first three digits divisible by the last digit" (the stem text lost the word "sum"; answer 1086 checked). J-M(XII) 15, 16 etc. print the NTA answer key only.
- J-II 23 is a proof (no printed answer); J-II 53-57 and J-A 2, 3 (paragraph on the numbers a_n, b_n, c_n) were read from the page image / paragraph text; C-I 3, C-II 22-24 and QB 165 (figures) were read from page images.
- All numerical examples in the model answers were recomputed with Python (brute force / sympy).
- Mapping is judgement; the weakest places are figure questions, garbled stems (C-II 16, J-II 35(d), J-II 46-47 "S's and P's separated") and questions that need two items (kept to one main and at most two "other").
- Several items have no main-concept question at all (for example the "What is circular permutation" and "Bell number" items); they stay in the Quick Review because they are in the master list.
- Item 84 (partition recurrence) uses Euler's pentagonal-number recurrence; items 82-96 come from standard theory because the theory sheet does not cover the "Extra Reading Material" (partitions, Bell, Stirling, totient, Fibonacci were verified by computation).

## New Hindi terms
See hindi_glossary_additions.md.
