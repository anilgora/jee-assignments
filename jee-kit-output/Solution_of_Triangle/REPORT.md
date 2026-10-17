# Solution of Triangle: revision kit report

- Items in the Quick Review: 84
- Batch XII: 23 graded questions, High threshold 2 -> High 12, Medium 10, Low 62
  - High items (numbers): [3, 6, 10, 12, 13, 16, 19, 21, 31, 32, 40, 51]
- Batch XIII: 17 graded questions, High threshold 2 -> High 8, Medium 13, Low 63
  - High items (numbers): [10, 12, 13, 19, 21, 31, 32, 40]

## Added items

## Rephrased items
- 61 (original 61): What is the value of $\sum r_1$?

## Questions with no matching item
- C-II:12

## Question Bank questions counted once (overlap with a batch JM set)

## Validation warnings
- none

## Input files used (not modified)
- chapters/Solution_of_Triangle/Theory.pdf (theory sheet, 31 pages)
- chapters/Solution_of_Triangle/XII.pdf (XII sheet: J-I 39, J-II 37, J-M 10, J-A 13 (numbered 1-11, 14, 15), C-I 22, C-II 31 questions; 107 pages)
- chapters/Solution_of_Triangle/XIII.pdf (XIII sheet; only its J-M (4 questions, JEE Main 2023-2024) was used; 103 pages)
- chapters/Solution_of_Triangle/DPP.pdf (DPP #1, #2, #3: 24 + 15 + 18 = 57 questions; 23 pages)
- No Question Bank file exists for this chapter (optional); the QB part was skipped.
- Master prompt list: .claude/skills/jee-chapter-revision-kit/references/master_index.json (Solution of Triangle: 84 prompts in 18 headings, master pages 54-56). The master PDF was not needed.

## Item numbering
- Final numbers 1-84 = master prompts 1-84 (no item added). Item 61 is tagged "rephrased" (see below).

## Graded counts and High items
- No QB, so graded = the batch's J-M + J-A (`graded_sources` = J-M, J-A).
- Batch XII: J-M(XII) 10 + J-A 13 = 23 graded questions; High threshold max(2, round(0.091 x 23)) = 2.
  High: 3 (sine law), 6 (sine law in two sub-triangles), 10 (three sides known), 12 (two sides + included angle), 13 (nature of triangle), 16 (projection in questions), 19 (area), 21 (half-angle formulae), 31 (R = a / 2 sin A), 32 (R = abc / 4 Delta), 40 (inradius), 51 (tangent lengths s - a).
- Batch XIII: J-M(XIII) 4 + J-A 13 = 17 graded questions; High threshold 2.
  High: 10, 12, 13, 19, 21, 31, 32, 40.
- The graded sets are small (the XIII sheet has only 4 JM questions), so one question can change a Medium/Low grade. Many items (definitions, positions of centres, excentral triangle, regular polygon) are Low only because JM/JA rarely ask them directly; their practice maps still list J-I, J-II, DPP and Challenger questions.

## Coverage check: candidates not added
- Conditional identities in a triangle (e.g. cos A + cos B + cos C = 1 + r/R, used in DPP-2 3 and DPP-3 11): covered in Trigonometric Ratio / Trigonometric Identities for a triangle.
- Max / min of trigonometric expressions of the angles (J-I 25, J-M(XIII) 2 "cos 2A + cos 2B + cos 2C least"): covered in Trigonometric Ratio / Inequalities in a triangle (prompts 86, 87). Questions mapped to the triangle item they then use (21, 83).
- Common root of two quadratics (J-II 25): covered in Quadratic Equation / Condition of common root(s); mapped to 40 (+13).
- Distance between special points (OI^2 = R^2 - 2Rr, OH^2): no master prompt anywhere, but no non-Challenger question needs it (DPP-2 3 "OI parallel to BC" is solved with the distances R cos A = r, item 34), so no item was added.
- Area ratio of a triangle cut off by points dividing the sides (J-M(XIII) 1): solved with Delta = (1/2) ab sin C, mapped to 19; no new item.
- No new item was needed: every method in the non-Challenger questions is one of the 84 prompts.

## Questions with no matching item / outside the chapter
- C-II 12 (circle rolling inside a crescent; arc length - pure circle geometry, Challenger) mapped "-".

## Uncertain decisions and notes
- Question index: extract_questions.py found every exercise with the default patterns, but it requires consecutive numbers and therefore dropped J-A 14 and 15 (the sheet prints J-A 1-11 and then 14, 15 - a paragraph on JEE (Adv.) 2023; numbers 12, 13 do not exist in either sheet). These two questions were appended to question_index.json by hand with their printed numbers and answers (1008 and 0.25); both answers were re-checked numerically (sympy).
- All other counts were checked against the sheets by numbering (the contents pages have no question counts): J-I 1-39, J-II 1-37, J-M(XII) 1-10, J-M(XIII) 1-4, J-A 1-11, 14, 15, C-I 1-22, C-II 1-31, DPP-1 1-24, DPP-2 1-15, DPP-3 1-18. DPPs are numbered #1, #2, #3 as printed.
- Master prompt 61 reads "What is the value of Snr ?" in the OCR; it was read as $\sum r_1$ (sum of exradii, the heading is "Excircle and exradii") and answered with $\sum r_1 = 4R + r$, $\sum r_1r_2 = s^2$, $rr_1r_2r_3=\Delta^2$. Tagged "rephrased".
- The master list repeats two prompts under "Incircle and Inradius": 50 = 44 (position of incentre) and 52 = 45 (finding the incentre geometrically). Both copies were kept (one item per prompt) with the same short answer and a pointer to the first; all questions were mapped to 44 / 45, so 50 and 52 are Low with empty practice maps.
- OCR noise in prompts ("Howto", "ofa", "| ", "ain terms of sin A", "polygoin") was cleaned; the meaning was not changed.
- The text layer loses fractions and Greek letters; J-I/J-II identity and figure questions (J-I 6, 10, 16, 35; J-II 21, 23, 24, 33-37; C-I 2, 9, 19; C-II 18, 23-31) were mapped from the readable part of the stem plus the printed solution text. Mapping is judgement: the borderline ones are
  - identity proofs (J-II 3-8, DPP-1 1-16): mapped to the rule the printed solution starts with (sine rule 5, projection 16, cosine rule 8, half-angle 21);
  - J-I 35 (P, Q trisect the hypotenuse, AP = 3, AQ = 4): cosine rule in sub-triangles, mapped 8 (+6);
  - J-I 8 (log identity in a right triangle) mapped to 13 (right-angle condition a^2 + b^2 = c^2), the only triangle fact it uses;
  - J-M(XIII) 3 (cos A + 2 cos B + cos C = 2 -> a + c = 2b) mapped to 5 (+10);
  - J-A 7 (median/altitude intersection with p = sqrt3, q = 1, R = 1) mapped to 31 (+68, 40, 19); J-A 14 (sides in A.P., A - C = pi/2, R = 1) to 31 (+19).
  - DPP-2 2 (two larger sides 10, 9, angles in A.P.): the third side comes from the quadratic of the ambiguous case (x^2 - 10x + 19 = 0, both roots valid), so it was mapped to 24 (+25).
- Every worked example in the model answers was checked with sympy (e.g. 13-14-15 triangle: Delta = 84, r = 4, R = 65/8, r1 = 21/2, tan(A/2) = 1/2; ambiguous case B = 30 deg, c = 8, b = 6 gives a = 4sqrt3 +- 2sqrt5; tangent-rule example B - C = 30 deg; cyclic quadrilateral 2, 5, 3, 2 has area 4sqrt3).

## Source errors found
- Theory sheet, pedal triangle: "FD = b' = R sin 2B = a cos B" - the last term should be b cos B (R sin 2B = 2R sin B cos B = b cos B). The Quick Review and notes use b cos B.
- No wrong printed answer was found in the graded (JM, JA) questions; J-A 14/15 answers were recomputed and agree.

## New Hindi terms
- See hindi_glossary_additions.md.
