# Run report - B1 Assignment Vector 3D

Paper: `papers/B1 Assignment Vector 3D.pdf` (80 maths questions, 38 pages, Matrix JEE Academy solutions).
Files: `B1 Assignment Vector 3D_Analysis.pptx` (487 slides), `_content.json`, `_ratings.json`, `_difficulty.xlsx`, this report.

## Blueprint and marks
- No blueprint was available: **Concepts self-assigned (no blueprint) - please review.**
- The PDF prints no marks. Marks assumed, as the run instructions say: single-correct 4, one-or-more-correct 4, integer/numerical 4, subjective 4, paragraph 3, matching 3 (total 308 marks). This is stated in every section divider.
- Structure used: Q1-17 single correct, Q18-35 one or more correct, Q36-44 paragraph (three passages), Q45-72 numerical/integer, Q73-76 subjective (prove / find), Q77 numerical, Q78-80 matching.
- Integer-type label (0 to 9) used where the answer is a digit 0-9 (Q57-Q72); numerical label for the rest (Q45-56, Q77).

## Difficulty
- **Marks-weighted difficulty index (adjusted): 2.53** (308 marks).
- Levels (before adjustment): Level 0: 0, Level 1: 5, Level 2: 34, Level 3: 36, Level 4: 5, Level 5: 0.
- Adjusted levels: 1 (5 questions), 2 (29), 2.5 (5), 3 (36), 4 (5). The 2.5 floor lifted five one-or-more-correct questions rated 2: Q22, Q29, Q32, Q33, Q34.
- No equivalence-relation adjustment applies (no such question).
- Level 4: Q18, Q20, Q35, Q39, Q41. Low-confidence ratings: Q20, Q23, Q35, Q40, Q53, Q72.
- `_difficulty.xlsx` was built with `build_report.py`; the xlsx recalc step was skipped (no /mnt/skills), so formulas have no cached values until opened in Excel.

## Solutions whose source is corrected (one line each)
- Q4: PDF line "= 2 - 2(lm+mn+nl) - 2(l+m+n)" has a sign error (should be +2(lm+mn+nl)); later lines and answer (A) are fine.
- Q5: PDF calls alpha "lambda"; corrected to alpha = 5 and lambda in {0, -3}; the root -3 gives alpha*lambda = -15 (not an option), so (D) 0 stands.
- Q14: PDF gave y = a/(2p); correct is y = a/(2q). Ratio q/p unchanged.
- Q16: third row of the determinant printed as (0, 2, 3), should be (1, 2, 3); correct value is sqrt3 - 1/2 = 2cos(pi/6) - sin(pi/6), option (C).
- Q20: PDF used 24[abc] = 18; the volume is 24[abc]^2 = 18. See key problems below.
- Q21: PDF used a CROSS product for the coefficients ab cos(...) (they are dot products): p = (a.b)c, q = -(a.c)b. Answer (B, C) unchanged.
- Q24: PDF took AO = i + j + sqrt3 k (the position vector of the centre) instead of O - A = j + sqrt3 k; the correct foot of the altitude is (1,2,2sqrt3), option (A) only. See key problems.
- Q26: PDF's first dot equation misprints 3x + y/2 + z/2 (should be 3x + 3y/2 + 3z/2, harmless); the PDF's own x = sqrt3/sqrt2 makes (B) true, and (D) was never examined (179 lattice points, not 125). Answer is (A, B, C).
- Q30: area determinant printed with rows (1,1,1),(2,-1,-1); correct rows are AB = (0,-1,-1), AC = (2,-1,-1). h = 2 and the answer are unchanged.
- Q43: PDF compared the angle of the plane's normal (54.7 degrees) with 60 degrees; the criterion needs the angle of the plane with the axis (35.3 degrees). Checked also by substitution (x^2 + 3xy + y^2 = 0, two real lines). Answer (A) unchanged.
- Q47: PDF line "3 lambda + 1 - lambda + 2 + 2 - (4 lambda - 3) = 4" is mis-transcribed; correct equation gives lambda = 1. Answer 10 unchanged.
- Q59: PDF's area expression (1/2) sqrt26 (1/5) sqrt(26/100) is wrong (AP = 1/5); area = sqrt26/10 = sqrt(13/50). Answer 2 unchanged.
- Q64: stray "/2" in "1/2 a^2 sin60 = 4sqrt3/2"; a^2 = 16 is right. Answer 8 unchanged.
- Q67: PDF's "|a| perp |b|" is meaningless; also see key problems (|a| = |b| cannot hold on [1,3]).
- Q76: PDF answer +-(1/2)(i - j) is not a unit vector; correct is +-(1/sqrt2)(i - j).

## Solutions whose source is written (PDF had none or unusable working)
- Q22: PDF only showed collinear => (A) and (C); I checked all four options.
- Q23: PDF working is inconsistent (see key problems); wrote the analysis that shows the data are inconsistent.
- Q27: PDF only derived coplanarity; I checked each option.
- Q34: PDF has no solution ("Sol. -").
- Q35: PDF has no solution.
- Q39, Q40: PDF has no solution (Q41's partial working was completed and kept as pdf).
- Q53: the PDF's working belongs to Q54 (and its key 0.85 is Q54's); figure missing; wrote the solution (assumes B is the mid-point of EF).
- Q61: PDF working stops after one sentence.
- Q63: PDF working stops before the final value.
- Q71: PDF gives only "eliminating lambda, mu we get w + 2u = 6"; wrote all steps.
- Q72: PDF solution is a broken image.
- Q73: PDF solution is a broken image (answer "-" for a proof question).
- Q80: PDF's working is a copy of Q79's; wrote the four items.
- Added checks (kept as pdf): Q28 (options A and D), Q31, Q7 (justification of S >= -3/2), Q25 (option A).

## Answer key / question problems (please look at these)
- **Q20**: with the printed vectors the volume 24[abc]^2 = 18 gives sin3t(1+sin t) - sin2t = +-1, whose only root in (0, pi/2) is t = 1.076 rad; none of pi/9, 2pi/9, pi/3, 4pi/9 satisfies it. The key (A, B, D) cannot be derived (it corresponds to sin3t = +-sqrt3/2). Shown as "no option"; probably the vector a is misprinted.
- **Q23**: r = x a + y b + z(a + b) lies in the plane of a, b, so r.(a x b) = 2 is impossible (same if the third vector is a x b). Key (A, C, D) is not derivable; reported as given.
- **Q24**: correct answer is (A) only; the key (B, C) is wrong.
- **Q26**: key (A, C) omits (B), which is true; correct (A, B, C).
- **Q35**: (B) and (D) verified, (C) is false; (A) is undefined as printed (no plane containing L is parallel to the plane because d.n = 4); key (A, B, D) kept with a caveat.
- **Q39**: option (B) is printed with denominator |a x b| but should be |a x b|^2 (numerically checked); (B) is the intended answer.
- **Q29**: the question is printed with cos^2 x but the solution and all options need cos 2x; I transcribed it as cos 2x.
- **Q45-Q54 decimals**: Q52 key 3.12 is 3.125 truncated; Q54 key 0.85 is 6/7 = 0.857 truncated.
- **Q53**: key 0.85 belongs to Q54; computed answer is 2 (checked numerically under the mid-point assumption).
- **Q56**: second angle pair printed {b, a}; read as {b, c}.
- **Q67**: the printed condition |a| = |b| holds only at x of about 0.083, not on [1,3]; answer 3 follows only if it is assumed to hold throughout.
- **Q72**: computed lambda = 2 (exact with the reciprocal basis, and numerically); the key says 1.
- **Q73**: the relation is 2/lambda3 = 1/lambda1 + 1/lambda2, so lambda1, lambda3, lambda2 are in H.P. (lambda3 is the middle term).
- **Q80 (c)**: as printed both lines pass through (-1,0,0), so AB = 0 (not an option); key gives 3. Option (D) is fixed by items (a), (b), (d).
- Q2, Q53 rely on figures: Q2's figure was read from the PDF image; Q53's figure is missing.

## Alternates, results
- Alternate solutions given for 76 of 80 questions; all are different techniques (similar triangles, special values, coordinates, reciprocal basis, Gram formula, partitions, Cauchy-Schwarz geometry, etc.) checked against the answer. Some are lighter-weight (testing options/special cases) where no deeper second method exists.
- **No alternate** for: Q14 (the only natural route is the square-completion |px - qy|^2 >= 0; every other route is a rewording), Q20 (data inconsistent with the key; only direct determinant evaluation), Q23 (data inconsistent), Q35 (direct computation of projections/images is the only route).
- **Useful Result / Pattern given for every question (1-80).**

## make_ppt.py output
- 2630 equations converted to native PowerPoint equations; **no "could not convert" warnings**.
- Notes only: font reduced for very long questions - Q19 (22 pt), Q28 (20 pt), Q42 (20 pt), Q43 (22 pt), Q44 (22 pt), Q78, Q79, Q80 (20 pt). Harmless; accepted.
- The deck was not rendered (no soffice/thumbnails in this environment), so slide layout was not visually inspected.

## Assumed / guessed / skipped
- Concepts and levels are my own (no blueprint). Anchors cited in the ratings workbook are approximate nearest matches from anchors.md; rating of Q72 and Q39/Q41 could reasonably be one level either way.
- Marks as above; "Subjective Type" label added for Q73-76 (not in the standard label list); rated as Numerical in the workbook.
- No AIR marks slide (not supplied). The comparison slide uses the built-in JEE Advanced indices.
- Nothing else skipped; speaker notes of the first solution slide carry the correction notes for the corrected questions.
