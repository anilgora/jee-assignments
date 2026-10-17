# Inverse Trigonometric Function: revision kit report

- Items in the Quick Review: 44
- Batch XII: 58 graded questions, High threshold 5 -> High 6, Medium 15, Low 23
  - High items (numbers): [3, 17, 31, 32, 42, 44]
- Batch XIII: 47 graded questions, High threshold 4 -> High 8, Medium 10, Low 26
  - High items (numbers): [3, 17, 31, 32, 38, 39, 42, 44]

## Added items
- 35: How to find the range or extreme values of expressions like $(\sin^{-1}x)^2$ + $(\cos^{-1}x)^2$ or $(\tan^{-1}x)^3$ + $(\cot^{-1}x)^3$?  [source: J-M(XII):10, QB:74, J-I:18 (also theory sheet 3.6 Q.6, Q.7)]

## Rephrased items

## Questions with no matching item

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [77, 78, 79, 80, 81, 82, 83, 84, 85, 88, 89]

## Validation warnings
- none

## Item numbering
- Final numbers 1-34 = master prompts 1-34. Final 35 = added item N1 (placed under "Property 4 of ITF" after master 34). Final 36-44 = master prompts 35-43 (final number = master number + 1).
- High items in master numbers: XII -> 3 (domain and range of the 6 ITFs), 17 (convert one inverse to another / evaluation), 31 (trigonometric substitution), 32 (sin⁻¹x + cos⁻¹x = π/2), 41 (ITF equations), 43 (series). XIII -> 3, 17, 31, 32, 37 (cot⁻¹ to tan⁻¹), 38 (adding two angles), 41, 43.

## Graded counts and High threshold
- Batch XII: J-M(XII) 25 + J-A 14 + QB 19 = 58 graded; High threshold max(2, round(0.091 x 58)) = 5.
- Batch XIII: J-M(XIII) 25 + J-A 14 + QB 8 new = 47 graded (QB 77-85, 88, 89 are J-M(XIII) questions, counted once); High threshold max(2, round(4.28)) = 4.
- The graded sets are small, so High needs only 4-5 questions. Low (0 graded questions) is mostly the graph / definition prompts (1-2, 4-7, 9-10, 21-29), which no JM / JA / QB question tests directly.

## Question Bank overlap (checked by eye)
- XIII: QB -> J-M(XIII): 77->22, 78->17, 79->19, 80->20, 81->1, 82->2, 83->3, 84->4, 85->5, 88->25, 89->14 (79 and 89 were only "possible" in detect_overlaps.py; same stems and same answers when read).
- XII: none. Suggested pairs QB 71/74 -> J-M(XII) 22 and QB 88 -> J-M(XII) 14 are different questions; rejected XIII suggestions QB 71/74 -> 16.

## Cross-chapter rule (coverage check)
- Added N1 (range / extreme values of (sin⁻¹x)² + (cos⁻¹x)², (tan⁻¹x)³ + (cot⁻¹x)³, (sec⁻¹x)² + (cosec⁻¹x)²): search_master.py found nothing for it; needed by J-M(XII) 10, QB 74, and it is the method of theory sheet 3.6 Q.6-Q.7.
- Not added because the master already covers them: computing the domain of a composite expression (Function / Algebra of a function, prompt 11 "How to compute domain of a function"); range of a function and identical functions (Function); period / GIF / signum parts of mixed questions (Function). Domain/range questions were mapped to item 3 (domain and range of the 6 ITFs), which carries the ITF-specific condition.
- Folded into existing items instead of new items (uncertain): three-angle tan⁻¹ sum (put into the answer of 38); sin⁻¹x + sin⁻¹y and cos⁻¹x − cos⁻¹y formulas (answers of 38, 39; the theory sheet gives only the tan⁻¹ forms - these standard results were added with their conditions); the reduction tan⁻¹ x + cot⁻¹ x = π/2 inside equations like (tan⁻¹x)² + (cot⁻¹x)² = 5π²/8 (J-I 18) was mapped to 33 with 41.

## Questions with no matching item
- None mapped "-". Questions that are mainly from other chapters but contain one ITF step were mapped to that step: J-II 1 (graph of an even periodic function; only arc cos f(2) is ITF) -> 3; J-II 41 (match column: period / range, only "range of sin⁻¹√(log ...)" is ITF) -> 3; J-II 43 (factorial sums with [ ] inside sin⁻¹ / tan⁻¹) -> 17; C-I 12 (graph of an even function) -> 3; J-A 8 (trigonometric sums with cos⁻¹) -> 17. These are uncertain.

## Uncertain decisions and notes
- extract_questions.py did not find J-I / J-II because the sheets print "Exercise J-1" / "Exercise J-2"; it was run with --patterns accepting 1/2 (no change to the skill). Counts: J-I 22, J-II 44, J-A 14, C-I 13, C-II 19, J-M(XII) 25, J-M(XIII) 25, DPP-6 17, DPP-7 13, DPP-8 14, QB 19 (numbered 71-89 in the bank) = 225. The contents pages give no question counts; numbering in each region was checked to be continuous.
- The DPP file contains "Special DPP on ITF" numbers 6, 7, 8 (not 1-3); keys DPP-6, DPP-7, DPP-8 keep the printed numbers.
- The text layer left the stems of J-II 19, J-II 21, C-II 1 and C-II 12 empty; they were read from the PDF text further down / the page: J-II 19 (sin⁻¹x + sin⁻¹y = 2π/3, cos⁻¹x − cos⁻¹y = π/3), J-II 21 (three equations), C-II 1 (cos⁻¹6x + cos⁻¹3√3x² = π/2), C-II 12 (three ITF inequalities).
- Read from the page image: J-I 6, J-II 24-25 (paragraph on sin⁻¹(2x/(1+x²)), cos⁻¹((1−x²)/(1+x²)), tan⁻¹(2x/(1−x²))), J-II 41, J-II 43, J-A 14, C-I 11, C-II 14-16 (paragraph S_n, C_n, T_n = sums of sin(sin⁻¹ x^k) etc., mapped to property 1), J-M(XII) 12, 13, 20, J-M(XIII) 25, QB 71, QB 86.
- Multi-part J-II questions (2, 4, 7, 9, 12, 14, 21) are mapped once by their main concept.
- XIII has its own exercises, but per the skill only its J-M was used; all other exercises come from the XII (reference) sheet.
- Mapping is judgement, especially evaluation questions (17 vs 38/39) and equations (41 vs the property used). Domain questions with several ITFs and logs are all mapped to 3.

## Source errors / oddities found
- J-M(XII) 11 is marked "Bonus" in the sheet.
- The extracted answer keys of J-M(XIII) 9, 12, 13, 14, 15 are garbled in the text layer ("()", "(20)", "D", "B" for numerical questions); the sheet's own answers were not used for anything in the kit.
- Theory sheet 3.4-3.6: the text layer shows strict signs in the domain conditions ("|x| > 1" for sec⁻¹ / cosec⁻¹, "−1 < x < 1" for sin⁻¹(−x)); this may be a lost "≥" glyph and was not checked on the page image. The kit uses the correct closed conditions |x| ≥ 1 and −1 ≤ x ≤ 1.

## Examples verified with sympy
- cos(tan⁻¹2) = 1/√5; sin(2tan⁻¹2) = 4/5; cos(2tan⁻¹3) = −4/5; sin⁻¹(sin 6) = 6 − 2π; sin⁻¹(sin 9) = 3π − 9; cos⁻¹(cos 5) = 2π − 5; tan⁻¹(tan 12) = 12 − 4π; cot⁻¹(cot(−6)) = 2π − 6 (each value checked to lie in the principal range); tan⁻¹½ + tan⁻¹⅕ + tan⁻¹⅛ = π/4; tan⁻¹3 − tan⁻¹½ = π/4; cos(½cos⁻¹⅛) = 3/4; 6x² + 5x − 1 = 0 roots 1/6, −1 and tan⁻¹(1/3)+tan⁻¹(1/2) = π/4; cot(tan⁻¹51 − tan⁻¹1) = 26/25; (tan⁻¹(−1))² + (cot⁻¹(−1))² = 5π²/8 with cot⁻¹ in (0, π); a² + (π/2 − a)² = 2(a − π/4)² + π²/8 and the (tan⁻¹)³ + (cot⁻¹)³ range [π³/32, 7π³/8); telescoping forms of Σtan⁻¹(2r/(r⁴+r²+2)) and Σtan⁻¹(1/(x²+(2r−1)x+r²−r+1)).
- Note: sympy's acot uses a different branch for negative arguments; the JEE convention cot⁻¹ ∈ (0, π) was used throughout.

## Hindi
- New terms are listed in hindi_glossary_additions.md.

## Input files used (not modified)
- chapters/Inverse_Trigonometric_Function/Theory.pdf (theory sheet, 37 pages)
- chapters/Inverse_Trigonometric_Function/XII.pdf (XII sheet, 126 pages: J-I 22, J-II 44, J-M 25, J-A 14, C-I 13, C-II 19)
- chapters/Inverse_Trigonometric_Function/XIII.pdf (XIII sheet, 127 pages; only its J-M (25 questions) was used)
- chapters/Inverse_Trigonometric_Function/DPP.pdf (Special DPP on ITF 6-8: 17 + 13 + 14 = 44 questions; 27 pages)
- chapters/Inverse_Trigonometric_Function/QB.pdf (JEE Main question bank, questions 71-89 = 19 questions; 13 pages)
- Master prompt list: .claude/skills/jee-chapter-revision-kit/references/master_index.json (Inverse Trigonometric Function, master pages 71-72, 43 prompts in 12 headings). The master PDF is not in the repo; prompt wording was taken from the saved index with OCR slips corrected only ("ofa", "Howto", "inetrval", and the garbled superscript ⁻¹ in prompts 19-37).
