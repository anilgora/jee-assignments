# Binomial Theorem: revision kit report

- Items in the Quick Review: 69
- Batch XII: 106 graded questions, High threshold 10 -> High 2, Medium 36, Low 31
  - High items (numbers): [13, 23]
- Batch XIII: 105 graded questions, High threshold 10 -> High 3, Medium 31, Low 35
  - High items (numbers): [13, 15, 23]

## Added items
- 15: How to handle the ratio of consecutive terms or coefficients (three consecutive coefficients in a given ratio or in AP)?  [source: J-I: 1,7; J-II: 1; J-M(XIII): 3,18,29,36,50,51,62,64,71; J-A: 1; C-I: 15; C-II: 5; QB: 256,260,267,275]
- 16: How to solve equations involving binomial coefficients (${}^nC_x={}^nC_y$, Pascal's rule, equal coefficients of two terms)?  [source: J-I: 5,16; J-II: 1,28; J-M(XIII): 50,64; C-I: 8,10; DPP-3: 9,11; QB: 267]
- 17: How to find the maximum / least value of a term (or coefficient) that contains a parameter such as $\sin\theta$ or $x$?  [source: J-M(XII): 5,42; QB: 269,272]
- 32: How to handle $(x+a)^n\pm(x-a)^n$ (even / odd terms only, degree of the polynomial)?  [source: J-I: 4,34; DPP-1: 13; QB: 257,268]
- 37: How to count the distinct terms in a sum of several expansions?  [source: DPP-1: 17]
- 67: How to use the binomial theorem for approximations and bounds (small $x$, large powers)?  [source: J-M(XII): 3,4,10]

## Rephrased items
- 48 (original 43): When the general term contains $r$ (type 1), how to remove $r$?
- 49 (original 44): When the general term contains $r^2$ (type 1), how to remove $r^2$?

## Questions with no matching item
- J-I:13
- J-A:3
- DPP-3:7
- QB:258

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307]

## Validation warnings
- none

## Input files used (not modified)
- chapters/Binomial_Theorem/Theory.pdf (theory sheet, 32 pages)
- chapters/Binomial_Theorem/XII.pdf (XII sheet: J-I 36, J-II 41, J-M 47, J-A 7, C-I 16, C-II 20 questions; 116 pages)
- chapters/Binomial_Theorem/XIII.pdf (XIII sheet; only its J-M (73 questions) was used; 132 pages)
- chapters/Binomial_Theorem/DPP.pdf (DPP 1-4: 17+12+16+17 = 62 questions; 29 pages)
- chapters/Binomial_Theorem/QB.pdf (JEE Main question bank, Q256-307, 52 questions; 29 pages)
- Master prompt list: .claude/skills/jee-chapter-revision-kit/references/master_index.json (Binomial Theorem: 63 prompts in 16 headings, master pages 18-20)

## Uncertain decisions and notes
- The master PDF (jee-inputs/quick_review_all_chapters.pdf) is not in the repo, so the 63 prompts come from the saved OCR index and could not be checked against the page image. OCR noise (e.g. "Howto", stray quote marks, "r?" for r^2) was cleaned by hand. Prompts 43 and 44 (r and r^2 in the general term) are reconstructed from context and tagged rephrased; prompts 4, 8, 9, 10, 56-59 and 62-63 had lost math and were reconstructed from the heading and the theory sheet.
- Model answers come from the theory sheet; every example was checked with sympy / direct computation (remainders, sums, coefficients, NGT ranges).
- QB overlap: QB 274-287 and 295-307 (27 questions) equal J-M(XIII) questions (2, 3, 5, 7-10, 26, 27, 31, 33, 35, 38, 41, 12, 14-16, 19-24, 46-48) and are counted once in batch XIII. QB 283 and 287 were below the script's "LIKELY SAME" level but identical by eye. No QB question equals a J-M(XII) question (script's "possible" matches for XII were checked by eye and rejected; QB 259/265 vs J-M(XIII) 42/65 and QB 292 vs 47 also rejected).
- Graded questions: batch XII = J-M(XII) 47 + J-A 7 + QB 52 = 106; batch XIII = J-M(XIII) 73 + J-A 7 + QB 25 new = 105; High threshold 10 in both.
- XII sheet J-II 27-32 form a paragraph set on lattice paths (P(a,b) = (a+b)C_a); they were mapped by the identity they use (sum of binomial coefficients, nCx = nCy, hockey stick, Vandermonde, Pascal).
- Questions with no matching item: J-I 13 (sum of products of linear factors), J-A 3 (coefficient of x^9 in the product of (1+x^k): counting partitions), DPP-3 7 (product of odd numbers as factorials), QB 258 (subsets with an even product).
- Questions where the stem was garbled or truncated in the PDF text and the mapping is a best guess: J-II 21 (mapped to Gauss-technique / properties of nCr), J-I 30, J-M(XII) 26, J-M(XIII) 58, 60, 69 (stem not extracted; mapped as coefficient of a power of x), QB 288, 290, DPP-3 12, 14, DPP-4 6, 12.
- Challenger C-II 14-20 are comprehension / match questions; mapped from the visible parts only.
- Added items (6) are those listed above; none of them is covered in another chapter of the master (checked with search_master.py: "three consecutive", "nCr = nCs", "even terms", "distinct terms", "degree of polynomial", "Fermat", "cyclicity" returned nothing relevant). Concepts judged already covered by existing items: Fermat / cyclicity remainders (items on base conversion), roots-of-unity filter (C-II 13 only, Challenger, not added).
- Source errors: none found that change an answer. DPP-1 17 (number of different terms in the sum of three expansions, printed answer 4017) was not re-derived; item 37's example uses a small sum I verified myself.
- Items never used by any question (original prompt numbers, both batches): 1, 2, 3, 4, 5, 8, 10, 22, 35, 38, 45, 46, 48, 51, 52, 55, 60, 61 (Low = not tested in these questions).
