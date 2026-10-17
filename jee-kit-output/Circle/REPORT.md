# Circle: revision kit report

- Items in the Quick Review: 123
- Batch XII: 88 graded questions, High threshold 8 -> High 3, Medium 51, Low 69
  - High items (numbers): [6, 23, 32]
- Batch XIII: 64 graded questions, High threshold 6 -> High 2, Medium 48, Low 73
  - High items (numbers): [23, 32]

## Added items
- 12: How to find the image (reflection) of a circle in a given line?  [source: J-M(XII) 35; J-M(XIII) 2, 5, 18; DPP-1 2; QB 40, 57, 60, 68]

## Rephrased items

## Questions with no matching item
- C-II:6
- DPP-1:16

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69]

## Validation warnings
- none

## Input files used (not modified)
- chapters/Circle/Theory.pdf (theory sheet, 68 pages)
- chapters/Circle/XII.pdf (XII sheet: J-I 39, J-II 72, J-M 36, J-A 20, C-I 24, C-II 27 questions; 155 pages)
- chapters/Circle/XIII.pdf (XIII sheet; only its J-M (37 questions) was used; 155 pages)
- chapters/Circle/DPP.pdf (DPP 1-8: 21+19+22+14+20+19+18+20 = 153 questions; 77 pages)
- chapters/Circle/QB.pdf (JEE Main question bank, printed numbers Q38-69 = 32 questions; 24 pages)
- Master prompt list: .claude/skills/jee-chapter-revision-kit/references/master_index.json (Circle: 122 prompts in 27 headings, master pages 33-37). The master PDF is not in the repo and was not needed.

## Item numbering
- Final numbers 1-11 = master prompts 1-11; 12 = added item N1 (image of a circle in a line); 13-123 = master 12-122 (final = master + 1).

## Graded counts and High items
- Batch XII: J-M(XII) 36 + J-A 20 + QB 32 = 88 graded questions; High threshold max(2, round(0.091 x 88)) = 8.
  High items: 6 (centre and radius from the general equation), 23 (centre condition when the circle touches an axis, master 22), 32 (condition of tangency p = r, master 31).
- Batch XIII: J-M(XIII) 37 + J-A 20 + QB 7 new (38-43, 62) = 64 graded questions; High threshold 6.
  High items: 23 and 32.
- The mapping is spread over many items (circle questions usually combine 2-3 ideas), so only 2-3 items reach the High threshold; many items are Medium.

## Added item (why)
- N1 / final 12, image of a circle in a line: J-M(XII) 35; J-M(XIII) 2, 5, 18; DPP-1 2; QB 40, 57, 60, 68. search_master.py ("image of circle", "image of a circle", "mirror image", "reflection", "image") found only image of a point / line (Straight Line, Complex Number) and conic reflection properties, nothing for a circle. Example (DPP-1 2) checked with sympy: centre (-8,12) -> (-16,-2), circle x^2+y^2+32x+4y+235 = 0.

## Candidates not added because the master already covers them
- Circle touching two given lines (centre on an angle bisector): J-M(XII) 14, 15; J-M(XIII) 4, 14; J-II 19, 61; DPP-2 8; DPP-3 15, 16; QB 62. Angle bisectors are covered in Straight Line / Angle Bisector; questions mapped to item 32 (master 31, condition of tangency), with 23 (master 22) where axes are involved.
- Chord subtending a right angle at the origin (homogenisation): J-II 3, 23; DPP-3 20; DPP-5 5, 8, 11. Covered in Straight Line / Homogenisation; mapped to the circle-side items (T = S1, item 58; circle on a chord as diameter, item 15).
- Locus of mid-points of chords subtending a given angle at the centre: J-I 21; DPP-5 7, 10; J-M(XIII) 1; QB 56. Covered by item 1 (chord length vs angle at the centre).
- Locus of the centre of a circle touching a fixed circle and a fixed line (parabola): J-I 29; C-I 7; DPP-6 5; J-M(XII) 27. Covered by items 88 (touch externally, master 87) and 23 (master 22); the model answer of item 88 states the method.
- Max / min of px+qy or of a distance for a point on a circle: covered by items 26 (master 25) and 29 (master 28).

## Questions with no matching item / outside the chapter
- C-II 6 (locus of the centroid of a sliding isosceles right triangle): straight-line locus, no circle concept, mapped "-".
- DPP-1 16 (locus of x^3+y^3+3xy = 1: a line and an isolated point): factorisation, not a circle question, mapped "-".
- Questions whose other half belongs to another chapter were mapped to their circle step only: J-M(XII) 6 (tangent to a parabola), J-M(XII) 8 (counting relations), J-M(XII) 31 (equilateral triangle, orthocentre), J-M(XIII) 23 / QB 51 (least OA+OB, straight line), J-A 14 (orthocentre with two sides on given lines).

## Uncertain decisions and notes
- Question extraction: extract_questions.py found only 2 questions in J-II and 2 in C-I, because some question numbers in XII.pdf are printed without a dot ("3      The line ..."). A patched copy of the script (in the run's temporary folder, not in the skill) also accepts "<next number> + two spaces + capital letter"; with it every exercise has consecutive numbers: J-I 1-39, J-II 1-72, J-M(XII) 1-36, J-A 1-20, C-I 1-24, C-II 1-27, J-M(XIII) 1-37, DPP 21/19/22/14/20/19/18/20, QB 38-69. The sheet's contents page has no question counts, so counts were checked against consecutive numbering and the "Ans." lines (J-II 3, 28, 37 and C-II 1, 5, 7, 18-20 are "prove that" questions without an answer line; DPP-3 17, DPP-5 19 too).
- The Question Bank is numbered 38-69 as printed (it is an extract of a larger booklet); the original numbers are kept.
- QB overlap: QB 44-61 and 63-69 are J-M(XIII) 29, 30, 31, 32, 33, 34, 35, 23, 25, 12, 13, 14, 1, 2, 3, 4, 5, 6, 26, 27, 28, 16, 17, 18, 19 (detect_overlaps.py "LIKELY SAME"; QB 50 "possible" was checked by eye: same question as J-M(XIII) 35, its stem is cut in the text layer). They are counted once in batch XIII. QB 38-43 and 62 have no JM partner. No QB question equals a J-M(XII) question.
- Comprehension questions were mapped using the paragraph text: J-II 48-50 (line with p1 + 3p2 = k touches a fixed circle), 51-53 (incircle of an equilateral triangle, JEE 2008), 54-56 (three circles S1, S2, S3); J-A 1-2 (JEE 2012), 9-10 (JEE 2018 chords through P0); C-II 21-23 and 24-26; DPP-4 9-11, DPP-6 12-14, DPP-7 15-17, DPP-8 10-13 and 14-16. Match-the-column questions (J-II 71, 72; C-II 27; J-A 20) were mapped to the concept of their first rows with the others as "other".
- Figure questions (J-II 5, C-I 17, DPP-2 8, C-II 24-26, DPP-7 8) were mapped from their wording; J-II 5 went to item 24 (chord diagram, master 23) as the nearest fit.
- Mapping judgement: "one diameter of S1 is a chord of S2" -> item 101 (bisecting the circumference, master 100); circles with two given tangents and a given normal -> 32 with 42 (normal through the centre); tangents at the ends of a chord -> 65 (external point from the chord of contact, master 64); circumcircle of OPQ where OP, OQ are tangents -> 50 (master 49); counting common tangents -> the matching position item 87-91 (master 86-90).
- Prompt 68 (lambda infinite) and prompts with Greek letters were printed with $\alpha$, $\beta$, $\lambda$ in math; the OCR wording "S| and S,", "ofa", "Howto" was cleaned by hand. No prompt was rephrased in meaning, so no item is tagged "rephrased".
- Model answers come from the theory sheet; worked examples were checked with sympy (circle through three points, centre/radius of 3x^2+3y^2-5x-6y+4 = 0, image circle, tangents from (3,-3), T = S1 chord 9x-2y-5 = 0, pole (-25,50), family examples lambda = 4/3 -> 7x^2+7y^2-10x-10y-12 = 0 and x^2+y^2+x-6y+3 = 0, radical centre (1,2), TCT length 20, common tangents of x^2+y^2 = 1 and (x-1)^2+(y-3)^2 = 4, orthogonality checks, angle pi/4 between circles).
- Source error found: theory sheet, Diametrical form, Q2 (circle circumscribing the quadrilateral 2x+3y = 2, 3x-2y = 4, x+2y = 3, 2x-y = 3): the printed answer 8x^2+8y^2-25x-3y+18 = 0 takes the sides in the listed order, but the printed solution uses a different pairing and ends with x^2+y^2+3x-5y-6 = 0 (both are cyclic quadrilaterals). The Quick Review example (item 76, master 75) uses the listed order and the printed answer, verified with sympy.
- Hindi: Latin letters are kept only inside math and for JM, JA, DPP, QB; in the Quick Review the prompts' own abbreviations DCT / TCT are kept (with the Hindi names प्रत्यक्ष / अनुप्रस्थ उभयनिष्ठ स्पर्श रेखा); in the short notes they are written in Hindi.

## New Hindi terms
- See hindi_glossary_additions.md.
