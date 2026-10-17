# Straight Line: revision kit report

- Items in the Quick Review: 186
- Batch XII: 69 graded questions, High threshold 6 -> High 5, Medium 45, Low 136
  - High items (numbers): [33, 42, 53, 115, 118]
- Batch XIII: 68 graded questions, High threshold 6 -> High 4, Medium 47, Low 135
  - High items (numbers): [53, 114, 115, 118]

## Added items
- 56: How do you find the area of the triangle formed by three given lines?  [source: J-II 13, 28; DPP-4 14; DPP-9 8]
- 97: A line through a fixed point (a, b), a, b > 0, cuts the positive axes at A and B. How do you find the least area of triangle OAB and the least value of OA + OB?  [source: C-II 17; J-M(XIII) 35; DPP-7 10; DPP-4 3; DPP-5 9]

## Rephrased items

## Questions with no matching item
- C-I:21

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 36, 37]

## Validation warnings
- none

## Input files used (not modified)
- chapters/Straight_Line/Theory.pdf (theory sheet, 88 pages)
- chapters/Straight_Line/XII.pdf (XII sheet: J-I 39, J-II 56, J-M 28, J-A 4, C-I 30, C-II 26 questions; 137 pages)
- chapters/Straight_Line/XIII.pdf (XIII sheet; only its J-M (44 questions) was used; 150 pages)
- chapters/Straight_Line/DPP.pdf (DPP 1-9: 24+18+18+21+19+18+14+12+12 = 156 questions; 104 pages)
- chapters/Straight_Line/QB.pdf (JEE Main question bank, Q1-37; 33 pages)
- Master prompt list: .claude/skills/jee-chapter-revision-kit/references/master_index.json (Straight Line: 184 prompts in 30 headings, master pages 27-32)

## Item numbering
- Final numbers 1-55 = master prompts 1-55; 56 = added item N2 (area of triangle formed by three lines); 57-96 = master 56-95; 97 = added item N1 (least area / least sum of intercepts for a line through a fixed point); 98-186 = master 96-184.

## Graded counts and High items
- Batch XII: J-M(XII) 28 + J-A 4 + QB 37 = 69 graded questions; High threshold max(2, round(0.091 x 69)) = 6.
  High items: 33 (internal division), 42 (circumcentre from vertices), 53 (area of triangle), 115 (orthocentre by altitudes, master 113), 118 (distance of a point from a line, master 116).
- Batch XIII: J-M(XIII) 44 + J-A 4 + QB 20 new = 68 graded questions; High threshold 6.
  High items: 53, 114 (image of a point in a line, master 112), 115, 118.
- J-A has only 4 questions in this sheet (2013, 2014 and two 2025 questions on the same locus); the grading therefore rests mostly on JM and QB.

## Added items (why)
- N2 / final 56, area of the triangle formed by three lines: J-II 13, 28; DPP-4 14; DPP-9 8. search_master.py ("area of triangle formed by", "three lines", "triangle formed by lines", "area of triangle") found only the vertex formula and Parabola / Solution of Triangle prompts. Formula from the theory sheet (cofactor form) and checked with sympy on J-II 13 (area 3/2).
- N1 / final 97, least area and least OA+OB for a line through a fixed point: C-II 17, J-M(XIII) 35, DPP-7 10, DPP-4 3, DPP-5 9 (C-II 17 is Challenger and only supports it). search_master.py ("minimum area", "sum of intercepts", "least value", "minimum value", "intercepts") found no matching prompt in any chapter.

## Candidates not added because the master already covers them
- Distance of a point from a line measured along / parallel to a given line (J-I 12, J-M(XIII) 22, 27): covered by item 99 (parametric form, master 97/99).
- Locus of the intersection of perpendicular lines through two fixed points (J-II 22, DPP-5 5): covered by master 66 (angle APB = 90 degrees).
- Counting lattice points inside a triangle (J-M(XIII) 8): mapped to master 123 (point inside a triangle).
- Rotation of a line about a point (J-M(XIII) 24, QB 10, DPP-5 2): covered by master 110 (line at a given angle).
- Sum / product of distances on a line through the origin (OP, OR, OQ in A.P./H.P.; DPP-6 4, 13, 14, C-II 7): covered by master 97 (parametric form) with master 38 (harmonic) where relevant.

## Questions with no matching item / outside the chapter
- C-I 21 (areas 4, 9, 49 of triangles cut off by lines through an interior point parallel to the sides): pure similar-triangle geometry, mapped "-".
- Questions whose second half belongs to another chapter were mapped to their straight-line step only: J-M(XIII) 1 (tangent to a parabola), J-M(XII) 12 and J-M(XIII) 29 (linear system), QB 3 (equal roots), QB 6 (binomial mean), QB 35 (image of a parabola).

## Uncertain decisions and notes
- The master PDF (jee-inputs/quick_review_all_chapters.pdf) is not in the repo; the 184 prompts come from the saved OCR index. OCR noise ("Ifall", "ofa", "Howto", "| What", "Ptolmey", "Conjuagte", "homegenise", "@" for alpha, "4" for lambda, "7 APB" for angle APB, "[PA - PB|") was cleaned by hand. No prompt was rephrased in meaning, so no item is tagged "rephrased".
- Prompt 179 ("centre of conic in different cases") is answered for pair of lines, central conics and parabola, since the theory sheet only says "pair of lines POI"; prompt 152 ("all 4 methods") lists four methods (vertices + ratio, sign method, separation of B and C, interior point) because the sheet's own list of four could not be read cleanly from the text layer.
- Question counts were checked against the "Ans." lines of every exercise: J-I 39/39, J-II 56/56, J-M(XII) 28 (29 "Ans." lines: one repeated answer line), C-I 30 (29 "Ans." lines), C-II 26/26, J-M(XIII) 44/44, DPP 24, 18, 18, 21 (20), 19, 18 (17), 14, 12 (11), 12, QB 37/37. Where one "Ans." line fewer was found, a paragraph or match-the-column answer is printed jointly; no question was lost (numbers are consecutive).
- QB overlap: QB 19-33, 36, 37 are J-M(XIII) 32, 33, 34, 39, 40, 41, 18, 19, 20, 21, 24, 25, 26, 27, 28, 42, 43 (detect_overlaps.py "LIKELY SAME", checked by eye) and are counted once in batch XIII. QB 8 (orthocentre of lines y = x+1, y = 4x-8, y = mx+c) is only similar to J-M(XIII) 10 (circumcentre) and was kept. QB 34 and 35 have no JM partner. No QB question equals a J-M(XII) question.
- Comprehension questions (J-II 32-34 medians paragraph, 35-36 bisectors paragraph; C-II 18-20 square, 21-23 isosceles triangle; DPP-5 11-16, DPP-6 9-11, DPP-7 8-10, DPP-8 7-11) were mapped using the paragraph text; match-the-column questions (J-II 53-56, C-II 24-26, DPP-1 23-24, DPP-4 21, DPP-5 18-19, DPP-7 14, DPP-9 12) to the concept of their first rows with the others as "other".
- Figure questions (C-II 1 zig-zag insect, DPP-1 7 zig-zag particle, DPP-5 8 graph of y-x against y+x) were mapped from their wording.
- Mapping judgement: "equal areas PAB = PBC = PCA" -> centroid (39); third-vertex / reverse-orthocentre questions -> altitudes (113); light-ray questions -> image of a point (112) or the shortest-path items (154-156) when a minimum is asked; "isosceles triangle with two given sides" and "line equally inclined to two lines" -> bisector formula (145).
- Model answers come from the theory sheet; every worked example was checked with sympy (64 checks: e.g. cos A = 63/65, incentre (1,1) and excentre (-3,3), orthocentre (5/3, 7/3), Euler line O = (6,2), pentagon area 36.5, three-line area 3/2, least OA+OB = 18, image (3/13, 2/13), bisectors 11x-3y+9 = 0 and 21x+27y-121 = 0, internal bisector 11x+2y+78 = 0, P(-11,-17), p = -5, reflected ray 29x-2y = 31, diagonal 21x-11y-15 = 0, c = 3 for the pair of lines).
- Source errors found: the theory sheet (2.4, orthocentre) prints the tan-weighted formula under the heading "Co-ordinates of circumcenter"; it is the orthocentre formula and is used as such (item 43). An early draft of item 170's example (three lines, two perpendicular) was corrected to the verified condition $a^2+ac+bd+d^2=0$ for $ax^3+bx^2y+cxy^2+dy^3=0$.
- Hindi: Latin letters are kept only inside math and for JM, JA, DPP, QB, H.P., A.P., G.P.; Quick Review prompts that name points (A, B, P, OAB) keep the Latin point names.

## New Hindi terms
- See hindi_glossary_additions.md.
