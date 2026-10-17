# Trigonometric Equation: revision kit report

- Items in the Quick Review: 29
- Batch XII: 37 graded questions, High threshold 3 -> High 9, Medium 3, Low 17
  - High items (numbers): [9, 13, 15, 16, 17, 20, 21, 23, 24]
- Batch XIII: 25 graded questions, High threshold 2 -> High 9, Medium 2, Low 18
  - High items (numbers): [13, 15, 16, 17, 19, 20, 21, 23, 24]

## Added items

## Rephrased items

## Questions with no matching item
- J-II:29
- C-I:6
- DPP-8:23

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [15, 16, 17, 18, 19, 20, 21, 22, 23]

## Validation warnings
- none

## Input files used (not modified)
- chapters/Trigonometric_Equation/Theory.pdf (theory sheet, 30 pages)
- chapters/Trigonometric_Equation/XII.pdf (XII sheet: J-I 22, J-II 32, J-M 19, J-A 5, C-I 20, C-II 23 questions; 91 pages)
- chapters/Trigonometric_Equation/XIII.pdf (XIII sheet; only its J-M (16 questions) was used; 91 pages)
- chapters/Trigonometric_Equation/DPP.pdf (DPP #6, #7, #8: 29 + 32 + 39 = 100 questions; 42 pages)
- chapters/Trigonometric_Equation/QB.pdf (JEE Main question bank, questions 11-23 = 13 questions; 9 pages)
- Master prompt list: .claude/skills/jee-chapter-revision-kit/references/master_index.json (Trigonometric Equation: 29 prompts in 11 headings, master pages 52-53). The master PDF was not needed.

## Item numbering
- Final numbers 1-29 = master prompts 1-29 (no item added, none rephrased).

## Graded counts and High items
- Batch XII: J-M(XII) 19 + J-A 5 + QB 13 = 37 graded questions; High threshold max(2, round(0.091 x 37)) = 3.
  High: 9 (sin/cos/tan = same ratio), 13 (solutions in an interval), 15 (Type 1 factorisation), 16 (a sin x + b cos x = c), 17 (non-standard values), 20 (Type 3 transformations), 21 (substitution), 23, 24 (Type 5 boundedness).
- Batch XIII: J-M(XIII) 16 + J-A 5 + QB 4 new (11-14) = 25 graded questions; High threshold 2.
  High: 13, 15, 16, 17, 19 (sin x = sin alpha with alpha variable), 20, 21, 23, 24.
- Item 13 collects almost every "number / sum of solutions in [a, b]" question as a secondary item, so it is High in both batches. The graded sets are small; one question can change a Medium/Low grade.

## Question Bank overlaps (counted once)
- QB 15 = J-M(XIII) 14, QB 16 = 7, QB 17 = 8, QB 18 = 9, QB 19 = 10, QB 20 = 12, QB 21 = 15, QB 22 = 16, QB 23 = 13. detect_overlaps marked all "LIKELY SAME" except QB 22 ("possible", similarity 0.74); the stems are identical, so QB 22 was also put in the overlap.
- No QB question equals a J-M(XII) or J-A question (the "possible" XII matches are different equations).
- The QB file is numbered 11-23 as printed (it is the Trigonometric Equation part of a Trigonometry question bank); the numbers were kept.

## Coverage check: candidates not added (covered in another chapter)
- "f(x) = k has a solution / exactly n solutions" (parameter range for solvability, graphical counting): covered in Function / Miscellaneous (prompts 134, 135). Questions J-I 18, 19, C-I 2, J-M(XIII) 1, 13, QB 23 were mapped to 15 (+24); J-M(XII) 11 (2 theta - cos^2 theta + sqrt2 = 0, one real solution) to 24 (+13).
- Range of a sin x + b cos x and of quadratic trig expressions: covered in Trigonometric Ratio / Range of Trigonometric Functions (71-79).
- Domain of the equation (tan, sec, log base): covered in Function / Domain (11). Instead of a new item the rule was put into the model answer of item 25 (and 13); such questions use 25 as "also used".
- Modulus cases (|cos x| = sin x, |tan x| = tan|x|): covered in Logarithm / Modulus Function; mapped to 9 / 27-28.
- Root location of a quadratic in sin x: covered in Quadratic Equation / Location of Roots.
- No new item was needed: every other method in the non-Challenger questions is one of the 29 prompts.

## Questions with no matching item / outside the chapter
- J-II 29 (expansion of sin 5 theta in powers of sin theta; Trigonometric Ratio identity), C-I 6 (a1 + a2 cos 2x + a3 sin^2 x = 0 for all x; identity), DPP-8 23 (x^3 - 2x + 1 = 0 satisfied by 2 sin 45 deg, 2 sin 18 deg, 2 sin 234 deg; Trigonometric Ratio values) mapped "-".

## Uncertain decisions and notes
- Extraction worked with the default patterns: J-I 1-22, J-II 1-32, J-M(XII) 1-19, J-A 1-5, C-I 1-20, C-II 1-23, J-M(XIII) 1-16, DPP-6 1-29, DPP-7 1-32, DPP-8 1-39, QB 11-23, all consecutive. The contents page has no question counts, so counts were checked by numbering. The DPPs are numbered #6, #7, #8 as printed (keys DPP-6, DPP-7, DPP-8).
- The text layer loses Greek letters and fractions; empty or garbled stems (J-II 2, 11, 12, 18, 21, 23-28; C-II 3, 7, 9, 12-17, 19-21) were read from the page images. All JM, JA and QB stems were readable in the text layer; QB 12 was checked on the page image.
- The J-II section header "SYSTEM OF TRIGONOMETRIC EQUATION" carries over to Q23-32 in the extracted text, but those are comprehension / multiple-correct / matrix-match questions on mixed types; they were mapped by their content.
- Type 3 split: item 19 = "same ratio of two variable angles" (sin 3x = sin x, sin 2 theta = cos 3 theta, tan(pi cos) = cot(pi sin)); item 20 = "sums/products transformed by C +- D to factorise". Borderline: J-II 5 (19 main, 20 other), J-I 10 and J-M(XII) 5 (product formula giving cos 3x: 20), J-II 28 (16 main; then sin = sin with variable angle).
- J-I 1, DPP-6 18, 19 ("most general value satisfying both equations") were mapped to the system item 29 (+9); the theory sheet treats them as general-solution examples.
- J-M(XII) 18 (reduces to tan 3 theta = 5) mapped to 17 (non-standard value) + 13.
- Exponential/log equations (32^{tan^2}, 9^{1-tan^2}, 8^{2 sin^2}, log_{cos x} cot x, e^{sin x}) were mapped to 21 (substitution).
- J-A 5 (List-I/II: number of elements of four equations in intervals) mapped to 13 (+16, 9).
- Item 17 uses its own example (3 sin x + 4 cos x = 5) so that it differs from item 16; every worked example was checked with sympy (e.g. sin theta + sin 5 theta = sin 3 theta in [0, pi] gives 0, pi/6, pi/3, 2pi/3, 5pi/6, pi; sqrt3 sin x + cos x < 1 iff x in (2n pi - 4pi/3, 2n pi); 2 sin(3x + pi/4) = sqrt(1 + 8 sin 2x cos^2 2x) at pi/12 and 17pi/12).
- Master prompt OCR was garbled only in symbols (@ for alpha, sin' for sin^2); the prompts were written with the obvious mathematics, meaning unchanged, so none is tagged "rephrased".
- Items 1-3, 5, 6, 8, 10-12, 14, 18, 22, 25-28 are Low or Medium because the graded sets (JM, JA, QB) rarely ask for them directly; they still carry DPP and sheet questions in their practice maps. Item 22 (t = sin x +- cos x) has no question in any set (the theory sheet has one example).

## Source errors found
- None found in the questions checked on the page images (J-II 1, 2, 11, 12, 18, 21-28; C-II 2-21; QB 11-12). The JM answers are the official NTA keys.

## New Hindi terms
- See hindi_glossary_additions.md.
