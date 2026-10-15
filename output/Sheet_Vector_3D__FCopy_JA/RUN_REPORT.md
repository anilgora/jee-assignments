# Run report - Sheet_Vector_3D__FCopy_JA (Exercise J-A, JEE Advanced previous-year Vector & 3D Geometry, 61 questions)

**Blueprint:** none used. **Concepts self-assigned (no blueprint) - please review.**
**Marks assumed (none printed):** 4 for single-correct, one-or-more-correct, integer and numerical types; 3 for paragraph-based and matching (Q25-26, Q42-43, matching Q11, 12, 15, 47, 53, 57, 61). Question types are interleaved in the sheet, so the deck has one section divider (Q1-61) stating this. Q42-43 (real exam: 2 marks) and Q48 (real: 3) use the defaults.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.32** (233 marks). Low versus JEE Advanced papers (about 2.6-3.2); the sheet mixes many easy older (2012-2019) questions.
- Adjusted levels: L0 = 2 (Q52, 53); L1 = 8; L2 = 25; L2.5 = 2 (Q30, Q41, multi-concept floor); L3 = 18; L4 = 6; L5 = 0.
- Q51-61 and Q41, 42, 43, 47, 48, 49, 50 are official questions already in the anchor bank, so the user's own ratings were used (e.g. Q43 = L4 although a fresh judgement would be ~2). Q44-46 (JEE 2022) rated by judgement (4, 4, 2). All others rated by judgement against anchors; no cross-chunk consistency pass beyond that.
- Workbook: Sheet_Vector_3D__FCopy_JA_difficulty.xlsx (no recalc.py; formula values cached only after opening in Excel).

## Solutions corrected / written
- Q11 - PDF plane (y+7) should be (y+2) (point (5,-2,-1)); answer unchanged.
- Q16 - wrong perpendicularity expression, "PQ" for PR, stray "1 = -1"; answer C right.
- Q19 - PDF says distance 3, question says 2; answer BD right.
- Q30 - (D): 4-2-2 = 0 so P3 is x-y+z=0 (PDF wrote 1); answer C, D unchanged.
- Q38 - projection vector u printed along PS instead of PQ; 2a/2b slip; case a>b conclusion; answer A, C unchanged.
- Q42 - printed Delta_x determinant wrong; corrected; answer 1 unchanged.
- Q54 - Q's z-coordinate is 3+l not 3+2l (l=-9, Q(-7,8,-6)); answer A, C.
- Q57 - PDF deduces alpha=0, should be gamma=0 (alpha=sqrt3); mapping unchanged.
- **Written:** Q49 - PDF stops at "now check the options"; planes derived and all four options checked.
- Kept as `pdf` with missing steps filled in (answers were right): Q1-10, 12-15, 17, 18, 20-29, 31-37, 39-41, 43-48, 50-53, 55, 56, 58-61 (per-question details in the speaker notes/solution bullets). Q40's PDF solution is cut off at the page break; the last steps were completed from p.35. Q21's stem lacked "=1" after |u x v| (print gap), restored as in JEE Adv 2016.

## Answer key problems
- None wrong. Extra valid answers outside the options: Q4 (plane x-y+z=3 also at the distance), Q10 (alpha=5 also a root); printed keys still correct. Q17: the PDF itself says the question "seems wrong"; the official answer 9 is reproduced with "component" read as the coefficient in the decomposition.

## Alternates and results
- Alternates for all 61 questions. Weaker ones (partly the same method, differently organised): Q46, Q50 (flagged by the worker), Q44-style reorganisations possible; replace if desired.
- **No question lacks an alternate.**
- Every question has useful_results.

## make_ppt.py output
- 2873 equations converted to native equations; 435 slides, 61 questions. No "could not convert" warnings.
- Notes only: "very long question - font reduced" for Q11, 12, 15, 22, 47, 49, 53, 54, 57, 61 (harmless).

## Skipped / assumed / guessed
- Concepts, chapters, ratings self-assigned; no rendering check (no PowerPoint/LibreOffice).
- Q1, Q7 have no options in the PDF and are typed Numerical; Q28, 29, 40 Numerical; Q51, 52 Integer (0-9). Q24 treated as planar. Q26 is pure trigonometry in a vector paragraph. Paragraph variables xi, psi, zeta in Q42-43 written as x, y, z. multi_concept set false for Q10 (L2); setting it true would raise it to 2.5.
- Work was split among six parallel sub-workers (one per ~10 questions); the lead merged their output.
