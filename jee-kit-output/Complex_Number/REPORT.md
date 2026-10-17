# Complex Number: revision kit report

- Items in the Quick Review: 102
- Batch XII: 125 graded questions, High threshold 11 -> High 6, Medium 53, Low 43
  - High items (numbers): [9, 45, 46, 51, 76, 99]
- Batch XIII: 98 graded questions, High threshold 9 -> High 8, Medium 43, Low 51
  - High items (numbers): [6, 9, 45, 46, 47, 51, 76, 99]

## Added items
- 9: How to solve an equation in $z$ that also contains $\bar z$ or $|z|$ (e.g. $z^n=\bar z$, $z^2+|z|=0$)?  [source: J-I: 2,16; J-II: 5,12,48; J-M(XII): 4,24,32,46,47; J-M(XIII): 11,12,13,21,29,40; J-A: 14,18,22,25; DPP-1: 1,6; DPP-3: 15,16; QB: 319,323,332,337,344]
- 70: How to find an integral power $z^n$ (or $\alpha^n+\beta^n$ for complex roots) using DMT?  [source: J-I: 13,37; J-II: 13,17,31,42; J-M(XII): 2,11,18,42; J-M(XIII): 1,2,20,37; DPP-2: 12; DPP-5: 1; DPP-6: 9; QB: 320,343,354]

## Rephrased items

## Questions with no matching item
- J-M(XII):3

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 349, 350, 351, 352, 353, 354, 355, 356]

## Validation warnings
- none

## Input files used (not modified)
- chapters/Complex_Number/Theory.pdf (theory sheet, 44 pages)
- chapters/Complex_Number/XII.pdf (XII sheet: J-I 44, J-II 53, J-M 47, J-A 29, C-I 27, C-II 32 questions; 164 pages)
- chapters/Complex_Number/XIII.pdf (XIII sheet; only its J-M (50 questions) was used; 168 pages)
- chapters/Complex_Number/DPP.pdf (DPP 1-6: 18+20+23+15+14+15 = 105 questions; 62 pages)
- chapters/Complex_Number/QB.pdf (JEE Main question bank, Q308-356, 49 questions; 34 pages)
- Master prompt list: .claude/skills/jee-chapter-revision-kit/references/master_index.json (Complex Number: 100 prompts in 19 headings, master pages 21-24)

## Item numbering
- Final item numbers in the Quick Review: 1-8 = master prompts 1-8; 9 = added item (equations with $\bar z$, $|z|$); 10-69 = master prompts 9-68; 70 = added item (integral powers by DMT); 71-102 = master prompts 69-100.
- The master page prints the number 95 twice (prompts 95 and 96 in the saved index are both printed "95"), so the printed numbers of the last five prompts are one less than the index numbers. The index numbering (1-100) was kept.

## Graded counts and High items
- Batch XII: J-M(XII) 47 + J-A 29 + QB 49 = 125 graded questions; High threshold max(2, round(0.091 x 125)) = 11.
  High items: 9 (equations containing $\bar z$ / $|z|$, added), 45 ($|z_1-z_2|$ as distance, max/min), 46 (circle locus), 51 (locus by $z=x+iy$), 76 (powers of $\omega$), 99 (general equation of a line / half-planes).
- Batch XIII: J-M(XIII) 50 + J-A 29 + QB 19 new = 98 graded questions; High threshold round(0.091 x 98) = 9.
  High items: 6 (algebra), 9, 45, 46, 47 (distance-based loci: bisector, Apollonius, ellipse), 51, 76, 99.

## Candidates not added because another chapter of the master covers them
- Non-real roots of real polynomials occur in conjugate pairs (J-II 8, C-II 14, 21): covered in Quadratic Equation / Relation between roots and coefficient (prompt 4). Mapped to the conjugate item (11).
- Remainder theorem with complex divisors (J-II 18, DPP-1 4, DPP-5 14): covered in Quadratic Equation / Remainder Theorem. Mapped to algebra (6) or powers of $\omega$ (76).
- Greatest / least distance of a point from a circle (many max/min $|z-z_0|$ questions): covered in Circle / Position of a point wrt a circle (prompts 28-29). Mapped to item 45 ($|z_1-z_2|$) with the circle item as other; item 45's model answer states the rule.
- Area of a region given by inequalities (J-A 4, J-M(XIII) 41, 43, QB 317): covered in Area Under Curve / Area represented by inequalities. Mapped to the line / circle items.
- Determinants and matrices with $\omega$ or $i$ entries (J-A 3, 10, J-M(XII) 7, 13, 26, 45, J-II 33, QB 314, 348): matrix part covered in Matrices / Determinant; mapped to powers of $\omega$ / $i$.
- search_master.py was run for "conjugate pair", "remainder theorem", "de moivre", "integral power", "number of solutions", "regular polygon", "area of region", "greatest", "maximum value", "real root", "common root", "equation involving", "polynomial with complex"; only the two added items had no match anywhere.

## Questions with no matching item / outside the chapter
- J-M(XII) 3: matrix with row sums 1 (no complex numbers) - mapped "-".
- Mixed-chapter questions mapped only to their complex-number part: J-A 8 (match: vectors, differentiability, $\omega$ - mapped to powers of $\omega$), J-A 27 (sets $a+b\sqrt2$; only statement D uses $\cos+i\sin$ - mapped to CiS), C-II 31 (match: vectors, integral, $\arg\frac1{1-z}$ - mapped to $1\pm z$ with $|z|=1$).

## Uncertain decisions and notes
- The master PDF (jee-inputs/quick_review_all_chapters.pdf) is not in the repo, so the 100 prompts come from the saved OCR index and could not be checked against the page image. OCR noise ("Howto", "@" for $\omega$, "n"" for $n^{th}$, "e"2")" for $e^{i\theta}$, "zz =| z|’" for $z\bar z=|z|^2$) was cleaned by hand; prompt 65 ("multiply by $e^{i\theta}$"), 83 ("product of all three $n^{th}$ roots" read as "all $n^{th}$ roots") and 94/95 ($x^{3m}, x^{3m+1}, x^{3m+2}$ and $x^{pm},\dots$) were reconstructed from the heading and the theory sheet. No prompt was rephrased in meaning.
- Question extraction: the sheets print "Exercise J-1 / J-2" instead of "J-I / J-II", so a patterns file was passed to extract_questions.py. In J-I, question 26 is printed without its full stop, and J-A question 22 has no number in the PDF text (it is drawn as an image); the script stopped at J-I 25 and J-A 21. A small wrapper around the skill's script (same output format) accepted a number without a full stop when it is the next in sequence and split the unnumbered J-A 22 from J-A 21 at its stem. All counts were then checked against the highest question number in each exercise (J-I 44, J-II 53, J-M 47/50, J-A 29, C-I 27, C-II 32, DPP 18/20/23/15/14/15, QB 308-356).
- QB overlap: QB 323-344 and 349-356 (30 questions) equal J-M(XIII) questions 40-48, 26, 29-33, 12, 15-21, 49, 50, 34-39 and are counted once in batch XIII. QB 344 was below the script's "LIKELY SAME" level but is identical to J-M(XIII) 21 by eye. QB 346 (script: "possible" with J-M(XIII) 34) is a different question. No QB question equals a J-M(XII) question (the script's "possible" matches 308, 328, 330, 334, 336 vs J-M(XII) 22/43 were rejected by eye).
- J-M(XIII) 10 is marked "Drop" in the sheet; it was still mapped (unit modulus / circle) and counted as graded.
- J-M(XIII) 20 / QB 343: the PDF text shows "x^2 - 2x + 2 = 0" but the printed answer (-128) fits $x^2-\sqrt2x+2=0$ (root sign lost in the text). The N2 model answer uses the $\sqrt2$ version, verified with sympy.
- Paragraph questions (J-II 36-38, 39-41, J-A 4-5, C-II 23-25, 26-28) were mapped from the paragraph text.
- Model answers come from the theory sheet; every example was checked with sympy or direct computation (powers of $i$, square roots, quadratic roots, polar forms, DMT powers and roots, $\omega$ identities, roots-of-unity products, series sums, circle radius, concyclic test).
- Garbled stems mapped as best guess (stems lost their fractions in the PDF text): J-I 7, 22, 24, 26, 31; J-II 13, 31, 42; J-M(XII) 12, 19, 40; J-M(XIII) 7, 11, 22, 27; DPP-1 10; DPP-4 10; QB 309, 315.
- Items never used by any question (final numbers): 4, 5, 17, 20, 21, 28, 29, 33, 34, 36, 43, 58, 59, 60, 61 (master prompts on representation and on angle conventions) and 100 (image of a point). Low = not tested in these questions.
- Source errors found: none that change an answer, apart from the lost $\sqrt2$ in J-M(XIII) 20 / QB 343 noted above (a text-extraction issue, the printed sheet is presumably correct).

## New Hindi terms
- See hindi_glossary_additions.md.
