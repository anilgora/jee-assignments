# Function: revision kit report

- Items in the Quick Review: 139
- Batch XII: 77 graded questions, High threshold 7 -> High 3, Medium 37, Low 99
  - High items (numbers): [74, 80, 103]
- Batch XIII: 76 graded questions, High threshold 7 -> High 3, Medium 36, Low 100
  - High items (numbers): [11, 80, 103]

## Added items
- 99: How to solve the standard functional equations $f(x+y)=f(x)+f(y)$, $f(x+y)=f(x)f(y)$ and $f(xy)=f(x)+f(y)$?  [source: J-I:22, J-I:24, J-A:9, J-A:14, J-M(XII):8, J-M(XII):11, J-M(XII):20, J-M(XIII):2, J-M(XIII):15, J-M(XIII):46, QB:63]
- 100: How to find a polynomial (or its value) when its values at several points are given?  [source: J-II:19, J-M(XII):10, C-I:21, C-II:2]
- 101: How to evaluate sums like $\sum f\left(\frac kn\right)$ when $f(x)+f(1-x)$ is constant?  [source: J-II:21, J-A:6, J-M(XII):17, J-M(XIII):3, QB:44, QB:47]
- 102: Which polynomials satisfy $f(x)\cdot f\left(\frac1x\right)=f(x)+f\left(\frac1x\right)$?  [source: QB:48]

## Rephrased items

## Questions with no matching item
- J-II:20
- J-A:7
- J-A:8
- J-A:10
- C-II:6
- J-M(XIII):27
- DPP-1:12
- QB:36
- QB:70

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]

## Validation warnings
- none

## Item numbering
- Final numbers 1-98 = master prompts 1-98. Final 99-102 = added items N1-N4 (placed under "Functional Equation" after master 98). Final 103-139 = master prompts 99-135 (final number = master number + 4).
- High items in master numbers: XII -> 74 (one-one / many-one), 80 (onto / into), 99 (composite from rule); XIII -> 11 (computing domain), 80, 99.

## Graded counts and High threshold
- Batch XII: J-M(XII) 28 + J-A 14 + QB 35 = 77 graded; High threshold max(2, round(0.091 x 77)) = 7.
- Batch XIII: J-M(XIII) 47 + J-A 14 + QB 15 new = 76 graded (QB 50-59 and 61-70 are J-M(XIII) questions, counted once); High threshold 7.
- Low = 0 graded questions; many Low items are definition / graph prompts (1-54, 60-73) that no graded question tests directly.

## Question Bank overlap (checked by eye)
- XIII: QB -> J-M(XIII): 50->36, 51->37, 52->28, 53->30, 54->32, 55->33, 56->18, 57->20, 58->1, 59->6, 61->44, 62->45, 63->46, 64->47, 65->35, 66->23, 67->24, 68->25, 69->26, 70->27 (69, 70 and 59 were only "possible" in detect_overlaps.py; same stems and answers).
- XII: none. Suggested pairs QB 42/66/68 -> J-M(XII) 6 are different questions (same template). Rejected XIII suggestions: QB 38-12, 39-34, 42-25.

## Questions with no matching item / outside the chapter (mapped "-")
- J-II 20 and C-II 6 (remainder theorem: covered in Quadratic Equation / Remainder Theorem).
- J-A 7 (determinant + quadratic polynomial from max/min of g; Determinant chapter), J-A 8 (x^2 sin(pi/x^2): zeros / increasing statements need calculus), J-A 10 (counting relations: Sets & Relations, see below).
- J-M(XIII) 27 = QB 70 (sum of k x^k and its derivative: Sequence & Progression), DPP-1 12 (trigonometric series ratio: Trigonometric Ratio).
- QB 36 (reflexive / symmetric / transitive relation on functions: Sets & Relations, see below).

## Cross-chapter rule (coverage check)
- search_master.py found nothing for f(x+y), Cauchy, f(1-x), f(1/x): items N1-N4 were added (sources listed under "Added items").
- Not added because the master already covers them: remainder theorem (Quadratic Equation / Remainder Theorem); relations, reflexive / symmetric / transitive / equivalence (the saved master index files these Sets & Relations prompts under Vector 3D, prompts 31-52 "Types of a relation"); range of a quadratic (Quadratic Equation / Range of a Quadratic Polynomial); a sin x + b cos x bounds (Trigonometric Ratio); counting with nPr / nCr (Permutations & Combinations).
- One-off candidates not added (mapped to the nearest item): Hermite-type sum of [1/2 + k/1000] (DPP-1 1 -> 36 GIF properties); recursion f(n+1) = 2f(n)+1 and sum k f(k) recursion (J-I 21, J-M(XIII) 8 -> 96 type 1); f(n)+f(n+1)/n = 1 counting (J-M(XIII) 6 = QB 59 -> 96, other 93); non-decreasing / increasing maps (C-II 13 -> 93, Challenger only).
- Sets & Relations: the Function sheets contain only two relation questions (QB 36, J-A 10), so no relation items were added here. The master's relation prompts (Vector 3D 31-52 in the saved index) are still not in any kit; they would need their own Sets & Relations kit.

## Prompt wording (OCR clean-up, not rephrasing)
- Master prompts were taken from the saved index; only OCR slips were corrected, meaning unchanged: "Howto/ofa" spacing, 26 "x approaches to 0 / -co" read as x -> infinity / -infinity (the theory sheet's limit discussion is for x -> +-infinity), 52 "y = x°" read as y = x^3 (uncertain; the OCR degree sign is most likely a lost superscript 3), 66 "f(-{x|)" read as f(-|x|), 49 "How to find define" read as "How to define". The master PDF is not in the repo, so these could not be checked against the page image.

## Uncertain decisions and notes
- extract_questions.py did not find J-I / J-II because the sheets print "Exercise J-1" / "Exercise J-2"; it was run with --patterns accepting 1/2 (no change to the skill). Counts cross-checked against numbered lines of every region: J-I 31, J-II 41, J-A 14, C-I 21, C-II 24, J-M(XII) 28, J-M(XIII) 47, DPP 12+16+12+12+14 = 66, QB 35 (numbered 36-70 in the bank). The contents pages give no question counts.
- XIII's own J-A region has 16 numbered lines vs 14 in XII; per the skill, J-A was taken from the XII sheet (reference) only.
- J-II 8 has sub-parts (a)-(f) and J-II 1-7, 9-15 are multi-part; each is mapped once, by its main concept (others list the rest).
- Paragraph / match-the-column questions (J-II 23-28, J-II 39-41, C-II 15-24, DPP-4 8-10, DPP-1 12, DPP-2 12, DPP-4 12, DPP-5 12): mapped by their first in-chapter statement; DPP-2 13-16 are graph-sketching tasks (mapped to the GIF / signum / fractional-part items).
- J-I 18, J-A 8, J-M(XIII) 5, DPP-1 12 were read from the page image (garbled text layer).
- Graded weight is thin (76-77 graded questions), so High needs only 7 questions; the grades reflect only these JM / JA / QB questions.
- Mapping is judgement, especially "range" questions (55-59 vs domain/standard-function items) and composite piecewise questions (104 vs 99).

## Source errors found
- J-M(XIII) 23 prints two answers, "Ans. 384" and "Ans. Matrix 180"; the solution and QB 66 give 180, which is correct (240 onto functions minus 60 with f(a) = 1).
- J-M(XIII) 22 is marked "(Bonus)" in the sheet.
- Theory sheet 7.1: the derivative test for one-one is stated as "dy/dx >= 0 or <= 0 (always)"; the Quick Review adds "equality only at isolated points" (correct condition).
- Theory sheet periodic properties print "sin nx, cos nx ... period 2pi or pi according as n odd/even"; this is the rule for sin^n x, cos^n x and is written that way in item 125.

## Examples verified with sympy
- domain of sqrt((x-3)/(x+2)); 4^x - 3*2^x + 2 = 0; log2 x + log2(x-2) = 3; range of (2x+5)/(3x-4) and of (x^2-x+1)/(x^2+x+1) = [1/3, 3]; sin 4 < 0 for range on [0,4]; (2x+1)/(x+4) = 2 - 7/(x+4); inverse of (x+5)/(3x-4); f = (x-1)/(x+1) has f^2 = -1/x, f^4 = x; onto count 240 (5 -> 4); 5P4 = 120, 625-120 = 505; P(4) = 34; 4^x/(4^x+2) pair sum 1 and sum 39/2; 1+x^n identity; (x+1)^2 - 1 = x -> 0, -1; (2x+3)/(x-2) self-inverse; f' = 3(x-2)^2; 4^4 - 4! = 232; f(136) = 12; 7-xPx-3 values 1, 3, 2.

## Hindi
- New terms are listed in hindi_glossary_additions.md. "LCM / HCF" are written ल.स.प. / म.स.प. in Hindi files.

## Input files used (not modified)
- chapters/Function/Theory.pdf (theory sheet, 50 pages)
- chapters/Function/XII.pdf (XII sheet, 128 pages: J-I 31, J-II 41, J-M 28, J-A 14, C-I 21, C-II 24 questions)
- chapters/Function/XIII.pdf (XIII sheet, 142 pages; only its J-M (47 questions) was used)
- chapters/Function/DPP.pdf (DPP 1-5: 12+16+12+12+14 = 66 questions; 48 pages)
- chapters/Function/QB.pdf (JEE Main question bank, questions 36-70 = 35 questions; 23 pages)
- Master prompt list: .claude/skills/jee-chapter-revision-kit/references/master_index.json (Function, master pages 66-70, 135 prompts in 20 headings). The master PDF is not in the repo.
