# Trigonometric Ratio: revision kit report

- Items in the Quick Review: 90
- Batch XII: 29 graded questions, High threshold 3 -> High 8, Medium 21, Low 61
  - High items (numbers): [2, 21, 25, 27, 31, 33, 44, 47]
- Batch XIII: 23 graded questions, High threshold 2 -> High 9, Medium 16, Low 65
  - High items (numbers): [2, 21, 25, 26, 27, 33, 44, 47, 50]

## Added items
- 6: What follows from $\dfrac{\sin^4\theta}a+\dfrac{\cos^4\theta}b=\dfrac1{a+b}$?  [source: QB 2]

## Rephrased items

## Questions with no matching item

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XII: QB [5]
- Batch XIII: QB [5, 7, 8, 10]

## Validation warnings
- none

## Input files used (not modified)
- chapters/Trigonometric_Ratio/Theory.pdf (theory sheet, 43 pages)
- chapters/Trigonometric_Ratio/XII.pdf (XII sheet: J-I 29, J-II 42, J-M 14, J-A 6, C-I 19, C-II 34 questions; 100 pages)
- chapters/Trigonometric_Ratio/XIII.pdf (XIII sheet; only its J-M (11 questions) was used; 100 pages)
- chapters/Trigonometric_Ratio/DPP.pdf (DPP #0-#5: 25+34+35+40+24+14 = 172 questions; 71 pages)
- chapters/Trigonometric_Ratio/QB.pdf (JEE Main question bank, 10 questions; 8 pages)
- Master prompt list: .claude/skills/jee-chapter-revision-kit/references/master_index.json (Trigonometric Ratio: 89 prompts in 21 headings, master pages 48-51). The master PDF is not in the repo and was not needed.

## Item numbering
- Final numbers 1-5 = master prompts 1-5; 6 = added item N1; 7-90 = master 6-89 (final = master + 1).

## Graded counts and High items
- Batch XII: J-M(XII) 14 + J-A 6 + QB 9 (QB 5 counted once, see below) = 29 graded questions; High threshold max(2, round(0.091 x 29)) = 3.
  High items (final numbers): 2 (fundamental identities), 21 (complementary angles), 25 (one ratio given, find the others), 27 (compound-angle / C+D formulae), 31 (sin 2A), 33 (cos 2A), 44 (sin 3A), 47 (six important results).
- Batch XIII: J-M(XIII) 11 + J-A 6 + QB 6 new (1, 2, 3, 4, 6, 9) = 23 graded questions; High threshold 2.
  High items: 2, 21, 25, 26 (higher angle to acute angle), 27, 33, 44, 47, 51 (cos 36°).
- The graded sets are small (the J-M sections have only 14 and 11 questions and the QB only 10), so a single question changes an item's grade; treat Medium/Low with care.

## Added item (why)
- N1 / final 6, "sin^4/a + cos^4/b = 1/(a+b) => sin^2 = a/(a+b)": needed by QB 2 (10 sin^4 + 15 cos^4 = 6, find 8 sec^6 + 27 cosec^6). search_master.py ("sin4", "a+b", "sum of squares") found nothing in any chapter. Example checked with sympy: sin^2 = 3/5, 8 sec^6 + 27 cosec^6 = 250.

## Candidates not added because the master already covers them
- a cos t + b sin t = c written in tan(t/2) (roots tan(alpha/2), tan(beta/2)): J-II 41. Covered in Trigonometric Equation / Type 2 ("How to solve equation of the type a sin x + b cos x = c"); mapped to items 34 (cos 2A in tan) and 32 (sin 2A in tan).
- AM-GM to bound 2^sin x + 2^cos x: J-II 22. Covered in Sequence & Progression / Concept of AM-GM; mapped to 72 (a sin x + b cos x range, master 71).
- Removing a modulus by splitting the domain (range of |sin x| + cos x): J-II 30. Covered in Logarithm / Modulus Function; mapped to 72 and 75 (master 71, 74).
- Challenger-only ideas (not used for coverage): sum of squares = 0 (C-II 2, 19), substitution t = sin x + cos x (C-II 11, 24; also covered in Trigonometric Equation / Type 4).

## Questions with no matching item / outside the chapter
- No question was mapped "-". Questions whose other half belongs to another chapter were mapped to their trig-ratio step: J-I 13 and QB 3, J-M(XII) 3 (quadratic equations), J-I 26 (coins in a triangle, geometry; only tan 30° used), J-I 27 (comparing powers; weak fit, item 64 / master 63), J-I 28 (regular polygon in-/circumradius, Solution of Triangle), J-II 35, J-II 40, C-I 7, C-II 7, C-II 23, QB 1, J-M(XIII) 10 / QB 7 (trigonometric equations), J-A 4 (trigonometric inequation), J-M(XIII) 11 / QB 10 (G.P. sum), C-II 1, 30 (trivial H.P./G.P. step).

## Question Bank overlaps (counted once)
- QB 7 = J-M(XIII) 10, QB 8 = J-M(XIII) 7, QB 10 = J-M(XIII) 11 (detect_overlaps "LIKELY SAME", confirmed from page images): counted once in batch XIII.
- QB 5 = J-A 2 (same sum over k = 1..13 of 1/[sin(pi/4+(k-1)pi/6) sin(pi/4+k pi/6)], asked in the QB as a sqrt3 + b). detect_overlaps did not flag it because it only compares the QB with J-M. Decision: J-A is graded in both batches, so QB 5 is put in qb_overlap of BOTH batches to count it once.
- No QB question equals a J-M(XII) question.

## Uncertain decisions and notes
- Question extraction: the sheets print the exercise names as "Exercise J-1" / "Exercise J-2" instead of J-I / J-II, so extract_questions.py was run with a --patterns file (in the run's temporary folder) that accepts both. With it every exercise has consecutive numbers: J-I 1-29, J-II 1-42, J-M(XII) 1-14, J-A 1-6, C-I 1-19, C-II 1-34, J-M(XIII) 1-11, DPP #0-#5 (25/34/35/40/24/14), QB 1-10. The contents page gives no question counts, so counts were checked by consecutive numbering. The DPPs are numbered DPP #0 to #5 as printed (keys DPP-0 ... DPP-5).
- The text layer of all sheets loses Greek letters (theta, alpha, beta), so the stems in question_index.json are partly garbled; the mapping was done from the printed solutions and page images (all JM, JA and QB questions were checked on the page image).
- Master prompts: the OCR text of several prompts was garbled (3-6, 16-18, 27-28, 38, 57-60, 64, 66-68, 73, 76-79, 88). They were rewritten with the obvious mathematics (e.g. "sin* 6 + cos* 0" -> sin^4 theta + cos^4 theta; "( a 0) 2" -> (pi/2 - theta); "7-8" -> (pi - theta)) from the theory sheet's matching section; the meaning was not changed, so no item is tagged "rephrased". Prompt 5 OCR also contained the fraction of prompt 6 (OCR spill), removed.
- Mapping judgement: two-term fractions and plain expansions -> compound angle (master 26); fractions with several terms grouped by C+D -> master 29; tan50 - tan40 = 2 tan10 and tan70 = 2tan50 + tan20 type -> master 41; products like (1 + cos pi/8)...(1 + cos 7pi/8) -> master 25 (reduce to acute angles); squared-cosine sums with angles in A.P. -> master 82; J-II 29-31 carry a "Paragraph for 29 to 31" header but no paragraph is printed, so they were mapped as separate questions.
- Borderline main items (noted in the mapping files): J-M(XII) 5 (supplementary pairing vs sin 2A), J-M(XII) 11 (sin 36° as a root, mapped to cos 36° item), J-M(XIII) 1 (reduction vs cot + tan = 2 cosec 2A), J-M(XIII) 5 (figure; complementary angles vs compound angle), J-A 5 (compound angle vs several-term identity), C-II 2 (identity vs triangle), DPP-1 9-14 (finding A in [0°, 360°] from a standard value: kept in this chapter as quadrant signs + standard values, although it has a trigonometric-equation flavour).
- Model answers come from the theory sheet; worked examples were checked with sympy (e.g. sin20 sin40 sin80 = sqrt3/8, tan10 tan50 tan70 = 1/sqrt3, cos(pi/7)cos(2pi/7)cos(4pi/7) = -1/8, cos(2pi/7)+cos(4pi/7)+cos(6pi/7) = -1/2, sum 1/(cos r° cos(r+1)°) = 1/sin 1°, tan70 = tan20 + 2tan50, range of 3sin^2 + 5cos^2 + 2sqrt3 sin cos = [2, 6], 10 sin^4 + 15 cos^4 = 6 -> 250).
- Type 4 range (items 79, 80 / master 78, 79): the sheet's rule "check whether a sin x = b cosec x is possible, else [a^2 + b^2, inf)" is used as printed; its example 9 sin^2 x + 25 cosec^2 x gives [34, inf).

## Source errors found (none changes an answer key)
- J-I 26: the printed answer reads "B A"; the correct answer is B (6 + 4 sqrt3).
- C-I 19: the solution gives f4(pi/3) = 1/2; it is 1 - cos(20pi/3) = 3/2 (option B is false either way).
- J-M(XIII) 10 / QB 7: the solution lists garbled values of theta; the correct ones are pi/9, 5pi/9, 7pi/9, 11pi/9, 13pi/9, 17pi/9 (sum 6pi, as printed).
- J-M(XII) 14: the solution skips the sign rearrangement turning the sines into cos(pi/11)...cos(5pi/11).
- C-II 24: the solution writes "ln x - 1 = 2 sin theta" where the radius should be sqrt2; the answer e^4 is still right.
- DPP-4 23: the working is printed under "Ans." with an empty "Sol."; one line reads 2cos(A/2) where it should be 2sin(A/2).
- DPP-1 32, 33: solutions are blank in the source.

## New Hindi terms
- See hindi_glossary_additions.md.
