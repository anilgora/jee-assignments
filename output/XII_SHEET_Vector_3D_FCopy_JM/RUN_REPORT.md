# Run report - XII_SHEET_Vector_3D_FCopy_JM (Exercise J-M, JEE Main previous-year Vector & 3D Geometry, 124 questions)

**Blueprint:** none used. **Concepts self-assigned (no blueprint) - please review.**
**Marks assumed (none printed):** 4 for every question (JEE Main default; Single Correct and Numerical alike). One section divider (Q1-124) states this. Type taken from whether options are printed.

## Difficulty
- Marks-weighted difficulty index (adjusted): **1.79** (496 marks). Well below JEE Advanced papers, as expected for a JEE Main sheet.
- Levels: L1 = 39, L2 = 72, L3 = 13, all others 0. No MCQs, so no multi-concept floor; no equivalence-relation questions.
- Rated by 9 parallel workers (ranges of 12-14 questions) with the calibrated rubric; no global consistency pass beyond that.

## Solutions corrected (34) - PDF working had a slip; answer unchanged unless stated
- Q4 only options A, B checked; C, D added. Q9 algebra typos (cos^2 = 1/2). Q16 c and b.c typos. Q17 wrong coplanarity expansion (b = 1). Q18 wrong image point (Q = (2,-2,4)). Q21 wrong last point. Q23 beta = -2 not 2. Q26 "collinear" should be "coplanar".
- Q38 parameter mislabelled, final substitution missing. Q40 premature sum, lambda step missing. Q41 foot sign. Q49 factor 2 missing. Q51 sign of +-sqrt2. Q54 v.c/|c| value. Q55 wording/count.
- Q59 sign in perpendicularity equation. Q67 invalid derivation (data inconsistent, see below). Q74 spurious term, plane wrong. Q78 (k-1)^2 not (k-2)^2. Q84 plane simplified wrongly.
- Q87 sign of q. **Q91 answer key wrong.** Q94 normals wrong. Q95 typo b-2a. Q97 factor 2 / expansion. Q98 missing factor 6.
- Q102 "=8" should be "=0". Q105 wrong first attempt removed. Q107 arithmetic slips. Q108 Q coordinates / "7Q". Q110 direction sign, point. Q113 second valid direction cosine added. Q119 working contradicted the key; written with the intended reading. Q123 beta = 15 not -15.
- **Written from scratch:** none. Others kept `pdf`, some with missing small steps filled in (Q12, Q31, Q35, Q36, Q65, Q71, Q75, Q101, Q109, Q114).

## Answer key / question problems
- **Q91: PDF key (D) is wrong; correct answer (C)** (S1 false, cos ACB = sqrt(2/3)); answer field says (C). Please review.
- Q67 flawed data (no such c exists; a.b = 2 contradicts a = -(b x c)); PDF itself notes "data error"; intended answer 0 kept.
- Q113: two options (A and B) are valid; key B kept. Q119: as printed no real a exists (cos of angle with plane); intended reading (angle with normal) gives key 3. Q18: options A and C are both printed (1,1,2); B kept. Q43: option A lies on both planes. Q51: sense of rotation unspecified, +-sqrt2, only sqrt2 is an option. Q72 option A is undefined (harmless).
- Stems repaired from garbled text/Hindi/page images: Q29 (|a| = 8), Q47 (point (0,0,6)), Q63, Q118 (angle PRQ = 60 deg), Q121.
- All other printed keys were independently verified (sympy/numpy) as right.

## Alternates and results
- Alternates for **89 of 124** questions. **No alternate (no genuinely different method; any other route is the same computation reworded):** Q1, 5, 14, 16, 22, 26, 31, 44, 45, 48, 49, 50, 55, 67, 68, 72, 76, 80, 82, 83, 86, 87, 89, 93, 100, 102, 104, 106, 108, 115, 116, 118, 119, 123, 124 (reasons per question in the workers' notes: single standard method - cross product / determinant / foot-of-perpendicular / skew-line formula / dot-product elimination). This is fewer than the "all questions" target by design: no padding.
- Every question (124/124) has useful_results.

## make_ppt.py output
- 3962 equations converted to native equations; 692 slides, 124 questions. No warnings, no "could not convert".
- build_report.py first failed on control characters in the ratings JSON (\v, \t from unescaped \vec / \times in 3 rating texts); repaired and rebuilt.

## Skipped / assumed / guessed
- Concepts, chapters, levels self-assigned; no rendering check (no PowerPoint/LibreOffice); no recalc of the xlsx.
- Figures were not reproduced; Hindi text used only to repair garbled English stems. Q83 is plane coordinate geometry inside a vector sheet.
- Work was split among 9 parallel workers; the lead merged their JSON and spot-checked only the structure and build.
