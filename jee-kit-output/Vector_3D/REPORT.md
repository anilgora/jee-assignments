# Vector 3D: revision kit report

- Items in the Quick Review: 210
- Batch XII: 250 graded questions, High threshold 23 -> High 2, Medium 106, Low 102
  - High items (numbers): [74, 88]
- Batch XIII: 292 graded questions, High threshold 27 -> High 0, Medium 105, Low 105
  - High items (numbers): []

## Added items
- 208: How to find a line through a given point (or with a given direction) that intersects two given lines, and the distance of a point from a line measured parallel to another line?  [source: J-I:35, J-A:33, J-M(XII):85, J-M(XIII):30, J-M(XIII):87, J-M(XIII):142, J-M(XIII):153, J-M(XIII):156, J-M(XIII):189, J-M(XIII):191, QB:11, QB:42 ...]
- 209: How to use vectors for geometric proofs and maximum / minimum problems?  [source: J-I:8, J-II:8, J-A:1, DPP-5:11]
- 210: If $p\,\overrightarrow{OA}+q\,\overrightarrow{OB}+r\,\overrightarrow{OC}=\vec 0$ for a point $O$ inside $\triangle ABC$, how are the areas of the sub-triangles related?  [source: J-II:14, DPP-5:9]

## Rephrased items
- 56 (original 56): Explain Ceva's theorem (concurrent cevians of a triangle) and its vector proof by comparing coefficients.
- 181 (original 181): How to find the position vector of the centre of a parallelopiped?

## Questions with no matching item
- J-A:26
- J-A:42
- J-M(XII):83
- QB:60

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 62, 63, 64, 65, 66, 67, 68, 69]

## Validation warnings
- none

## Rebuild 2026-11-02 (complete master prompt list)
This kit replaces the 2026-10-17 Vector 3D kit. That first build used the saved index, which held only prompts 1-30 and therefore had 46 self-written items. Prompts 1-207 were now transcribed by hand from the page images of Quick_Review_English_Mathematics_v2.pdf, pages 57-63, in 40 headings. The corrected index is in jee-inputs/master_index.json and jee-inputs/master_index.review.md; only the Vector 3D entry was changed. Pages 64-65 of the master are the separate chapter Sets & Relations. All 767 questions were mapped again against the 207 prompts.

## Input files used (not modified)
- chapters/Vector_3D/Theory.pdf (theory sheet, 89 pages)
- chapters/Vector_3D/XII.pdf (XII sheet, 296 pages: J-I 54, J-II 70, J-M 124, J-A 57, C-I 24, C-II 47 questions)
- chapters/Vector_3D/XIII.pdf (XIII sheet, 348 pages; only its J-M (197 questions) was used)
- chapters/Vector_3D/DPP.pdf (DPP 1-10: 10+8+11+13+11+17+16+16+10+13 = 125 questions; 70 pages)
- chapters/Vector_3D/QB.pdf (JEE Main question bank, 69 questions; 58 pages)
- Master Quick Review: Quick_Review_English_Mathematics_v2.pdf, pages 57-63, uploaded in the session. It was not added to the repo because the file is 28 MB.

## Item numbering
- Final numbers 1-207 are master prompts 1-207, unchanged.
- 208-210 are added items, under the heading Miscellaneous:
  - 208: a line through a point, or with a given direction, that meets two given lines; also the distance of a point from a line measured along another line.
  - 209: vector methods for geometry proofs and max/min problems.
  - 210: area ratio p:q:r when pOA+qOB+rOC = 0.
- search_master.py found no prompt for any of the three in any chapter. Their source questions are listed under "Added items" above.

## Rephrased prompts
- 56 "Explain chivas theorem": read as Ceva's theorem. The theory sheet has no theorem by that name. Its section 1.9 Q4 is a Ceva problem (concurrent cevians, AF:FB = 2:1), solved by comparing coefficients of two independent vectors. The answer states Ceva's theorem with that vector proof. If you meant something else, only item 56 needs changing.
- 181 "How to find position vector of center of tetrahedron?": this prompt is listed under Parallelopiped, so it was read as the centre of a parallelopiped. Answer: the mid-point of any body diagonal.

## Graded counts and High items
- Batch XII:
  - Graded questions: J-M(XII) 124 + J-A 57 + QB 69 = 250. High threshold = max(2, round(0.091 x 250)) = 23.
  - High items: 74 (squaring a sum/difference of vectors, 28 questions) and 88 (cross product |a x b| = |a||b| sin theta, 26 questions).
- Batch XIII:
  - Graded questions: J-M(XIII) 197 + J-A 57 + QB 38 = 292. QB 32-54 and 62-69 are J-M(XIII) questions and are counted once. High threshold = 27.
  - No item reaches 27, so no item is High. The most tested items are 82 (foot of perpendicular on a line, 24), 142 (distance of a point from a plane, 24), 117 (SD between skew lines, 23), 74 (19), 72 (18) and 62 (17).
- Why so few High items: the fixed rule sets High at 9.1% of the graded questions, and 207 detailed prompts share the questions out. In the first build, coarse items such as "dot product" reached High.

## Cross-chapter rule (coverage check)
- These methods have no prompt and were not added, because they are covered elsewhere or are one-off:
  - Three planes / homogeneous system (J-II 42, 70; DPP-7 4): covered in Determinant / System of Equations. Mapped to 152 with 194.
  - Euler-line relation 3G = H + 2O (QB 21): mapped to 47 with 44.
  - Length of the projection of a segment on a plane (J-I 51): one-off. Mapped to 81 with 79.
  - Edge of a tetrahedron on two given planes (J-A 45): one-off. Mapped to 152.
  - Tetrahedron volume from opposite edges (DPP-10 10): one-off. Mapped to 170.
  - De Gua's theorem (QB 9): one-off. Mapped to 97.
  - Rotation of a vector (J-M(XIII) 4; DPP-1 3, DPP-4 6): mapped to 199.
  - v = omega x r (DPP-8 8): a mechanics application.
- Lagrange's identity has no prompt of its own. Questions that use it are mapped to 88 with 68.

## Questions with no matching item / outside the chapter
- These four are mapped "-":
  - J-A 26: pure trigonometry.
  - J-A 42: consistency of a linear system.
  - J-M(XII) 83: a 2D straight-line question.
  - QB 60: a system of linear equations.
- These match-the-column questions are mapped to their vector rows only: J-A 15, C-II 43, 45, 46, 47.
- J-II 56: only the vector part is mapped; the rest needs the normal to a curve, which is outside the chapter.

## Uncertain decisions and notes
- Question extraction: the sheets print "Exercise J-1 / J-2", so extract_questions.py was run with --patterns. All exercises have consecutive numbering.
- QB overlap with J-M(XIII), checked by eye:
  - The pairs are 32-159, 33-161, 34-163, 35-166, 36-168, 37-172, 38-173, 39-175, 40-176, 41-181, 42-189, 43-120, 44-121, 45-122, 46-123, 47-126, 48-128, 49-131, 50-132, 51-136, 52-144, 53-145, 54-151, 62-177, 63-179, 64-180, 65-138, 66-139, 67-156, 68-157, 69-158.
  - For QB 65, detect_overlaps suggested J-M(XIII) 18; the real match is 138.
  - No QB question equals a J-M(XII) question.
- Model answers come from the theory sheet. Every example was checked with sympy.
- 147, acute or obtuse bisector plane: the sheet gives no rule, so the standard rule was used. Make d1, d2 > 0; if n1.n2 > 0, the bisector containing the origin is the obtuse one.
- 148, "angle bisector containing a fixed point": read as the bisector of the angle in which the point lies.
- Theory sheet section 14 Q.1, line of greatest slope: the direction ratios read from the text layer, (3, 1, -4), do not lie in the given plane. (n_H x n_G) x n_G gives 3, -1, 1, which item 207 uses.
- Source errors found while mapping:
  - The printed solutions of J-I 8, C-I 11 and C-I 12 belong to other questions; the printed answers are still right.
  - The solutions of J-I 46 and J-I 54 are copies of the previous question's solution.
  - J-I 35: the solution prints Q(a,a,0) instead of (a,a,a).
  - J-II 44: the printed answer 212 is k^2, not k.
  - J-II 63: the stem assumes four independent vectors in 3D, which is impossible.
  - J-A 17: the sheet's own solution says the question looks wrong.
  - J-M(XII) 67: the sheet marks it "Data error".
  - J-M(XIII) 16: the printed answer is "Drop" (bonus).
  - DPP-1 4: the solution is copied from Q3; the answer is still right.
  - DPP-5 9: the solution gives [t] = 6, but the printed answer [t] = 3 is correct.
- The short notes, formula sheet, mind map and flowcharts are the same as in the 2026-10-17 build. They already cover every topic of the full prompt list.
- Hindi: "unit vector" is now मात्रक सदिश everywhere, as in the glossary additions. Terms added this time: सहसीमान्त कोर, पार्श्व कोर, पिण्ड विकर्ण, सेवा प्रमेय.
