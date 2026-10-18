# Maxima and Minima: revision kit report

- Items in the Quick Review: 34
- Batch XII: 63 graded questions, High threshold 6 -> High 5, Medium 13, Low 16
  - High items (numbers): [4, 7, 8, 13, 27]
- Batch XIII: 45 graded questions, High threshold 4 -> High 5, Medium 8, Low 21
  - High items (numbers): [4, 7, 8, 13, 27]

## Added items
- 23: How to prove an inequality (or find a maximum) using concavity (chord and curve)?  [source: J-II 75; J-A 3.05 (theory sheet 3.2 Q.5-7)]
- 34: How to find a polynomial when its points of extrema (and some values or a limit) are given?  [source: J-I 61; J-II 57, 60, 62; J-A 3.03; C-I 31; C-II 31; J-M(XII) 20, 55 (theory sheet 2.2 Q.3)]

## Rephrased items

## Questions with no matching item
- J-I:69

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 194, 195, 196]

## Validation warnings
- none

---
## Run details (added by the routine, 2026-10-18)

### Input files used
- Theory (combined; Maxima and Minima part = PDF pages 91-118 only, from "MAXIMA & MINIMA 1.1"): `chapters/Application_of_Derivative/Theory.pdf`
- XII sheet (combined): `chapters/Application_of_Derivative/XII.pdf` - reference for J-I, J-II, J-A, C-I, C-II and its own J-M
- XIII sheet (combined): `chapters/Application_of_Derivative/XIII.pdf` - only its J-M is used (skill rule)
- DPP (combined): `chapters/Application_of_Derivative/DPP.pdf` (DPP-5 and DPP-6 are Maxima and Minima)
- Question Bank (this chapter's own, unchanged): `chapters/Maxima_and_Minima/QB.pdf` (23 questions, printed numbers 174-196 kept)
- Quick Review prompt list: skill `references/master_index.json` (Maxima and Minima, 32 prompts, master pages 84-85). `jee-inputs/master_index.json` and the master PDF are not in the repo; the PDF was not needed.
- No input file was moved, renamed or edited; no sheet had to be merged.

### Combined chapter (Application of Derivative = Tangent & Normal, Monotonicity, Maxima and Minima)
`extract_questions.py` was run on the full combined sheets (J-I 74, J-II 127, C-I 34, C-II 52, J-M(XII) 59, J-M(XIII) 50, DPP-1..6 = 95, QB 23). The classification of every sheet / DPP question saved by the Monotonicity run (`aod_question_classification.json`, copied into this folder) was reused unchanged: every question labelled "Maxima and Minima" or "... + Maxima and Minima (shared)" was kept, all others were deleted from `question_index.json` before mapping and grading.
J-A of this sheet is numbered by topic (1.xx Tangent & Normal, 2.xx Monotonicity, 3.01-3.16 Maxima and Minima) and is not found by `extract_questions.py`; the 16 J-A questions 3.01-3.16 were written into `question_index.json` by hand from the page text (XII pages 187-199); 3.01 and 3.12 were copied from the Monotonicity index. Printed numbers kept.

| Source | Total in sheet | Kept | Maxima and Minima only | Shared with sibling | Dropped (sibling only) |
|---|---|---|---|---|---|
| J-I | 74 | 26 | 25 | 1 | 48 |
| J-II | 127 | 43 | 26 | 17 | 84 |
| J-A | 30 | 16 | 14 | 2 | 14 |
| C-I | 34 | 12 | 7 | 5 | 22 |
| C-II | 52 | 15 | 15 | 0 | 37 |
| J-M(XII) | 59 | 24 | 21 | 3 | 35 |
| J-M(XIII) | 50 | 23 | 23 | 0 | 27 |
| DPP-1..6 | 95 | 40 | 38 | 2 | 55 |
| QB (own) | 23 | 23 | 23 | 0 | 0 |

Per batch: XII sheet (J-I, J-II, J-A, C-I, C-II, J-M(XII)) = 376 questions: kept 136 (108 Maxima and Minima only + 28 shared), dropped 240 (Tangent & Normal or Monotonicity only).
XIII batch (its J-M(XIII); the other exercises are taken from XII) = 50: kept 23 (none shared), dropped 27. DPP = 95: kept 40 (38 + 2 shared), dropped 55.

Shared questions (kept here and mapped only to Maxima and Minima items):
- with Monotonicity: J-I 50; J-II 43, 44, 45, 56, 75, 76, 77, 78, 92, 96, 115, 119, 122; C-I 8, 14, 22, 30, 32; J-M(XII) 5, 49; DPP-6:12; J-A 3.01, 3.12.
- with Tangent & Normal: J-II 58, 80, 81, 82 (tangent of greatest / least slope); J-M(XII) 55 (cubic touching the $x$-axis, local maximum value); DPP-6:15 (least area of the triangle cut off by a tangent).

Ambiguous classifications / mappings:
- J-I 69 (rate at which the radius of a leaking balloon decreases) is a rate-of-change question (Tangent & Normal / rate measure), not maxima-minima. It was labelled Maxima and Minima in the saved classification (it sits in the sheet's "Geometry based questions" section) and Tangent & Normal had already dropped it, so it was kept here so that it appears in some kit, and mapped `-`.
- Greatest / least value questions (J-I 49, 51, 55, 57; J-II 43-45, 56, 63, 115; J-M(XII) 4, 36, 38, 54, 57, 59; J-M(XIII) 11, 12, 22, 30, 33, 43; QB 176, 179, 184, 187, 188, 191, 192 ...): the method ("greatest and least value in an interval") is a master heading of Monotonicity, so no item was added; they are mapped to items 7 / 8 (greatest / least value), whose model answers now state the method (critical points + end points).
- Range of $a\sin x+b\cos x$, AM-GM type minima (DPP-5:8, 5:11, DPP-6:1, 6:8, 6:9, J-I 55): covered by Trigonometric Ratio "Range of trigonometric functions" and Sequence & Progression "AM-GM"; mapped to items 7 / 8.
- Points where $f'$ does not exist (modulus, piecewise; J-I 52, 58, 63, J-A 3.02, 3.04, J-M(XII) 42, 56, QB 174, 178, DPP-5:17, 19 ...) are mapped to item 13 (first derivative approach) with item 4 (continuity not needed) as the other item; this is why item 4 is graded High.
- Functions given as $\int_0^x\phi(t)\,dt$ (J-I 59, J-II 121, J-A 3.01, 3.14, J-M(XIII) 34, QB 177, 196, DPP-5:15, 5:20): Leibniz rule is in Method of Differentiation / Definite Integration; mapped to item 13.
- J-A 3.05 (paragraph, $F=e^{-x}f$ concave up with $F(0)=F(1)=0\Rightarrow F<0$) mapped to the added concavity item; J-A 3.06 to item 13.
- J-II 123 ($\lim f=\lim[f]$) mapped to item 2 (minima at $x=a$: $f(x)$ approaches an integer from above).

### Grading
- XII: graded = J-M(XII) 24 + J-A 16 + QB 23 = 63; High threshold max(2, round(5.73)) = 6.
- XIII: graded = J-M(XIII) 23 + J-A 16 + QB 23 - 17 overlaps = 45; High threshold max(2, round(4.10)) = 4.
- QB 179-192, 194-196 = J-M(XIII) 43, 44, 45, 46, 47, 30, 31, 32, 33, 22, 8, 9, 11, 12, 49, 50, 34 (detect_overlaps similarity 0.7-0.94; 185 = 31 and 191 = 11 at 0.70 confirmed by reading both). QB 176 vs J-M(XIII) 43 (0.61) and QB 192 vs J-M(XII) 57 (0.71) are different questions; no XII overlap.
- High items in both batches (renderer numbers): 4 (continuity not needed), 7 (greatest value), 8 (least value), 13 (first derivative approach), 27 (geometrical problems).
- J-A 3.01-3.16 are graded in both batches (the XIII sheet's J-A is the same, as noted in the Tangent & Normal run).

### Added items
- 23 (N2), under "Significance on sign of second order derivative": proving inequalities / finding maxima by concavity (chord above / below the curve). Source: J-II 75 (JEE 2004), J-A 3.05; theory sheet 3.2 Q.5-7. `search_master.py` "concave inequality", "Jensen", "convex", "chord" found nothing of this kind.
- 34 (N1), under "Miscellaneous": finding a polynomial from its extremum points, values and a limit. Source: J-I 61; J-II 57, 60, 62; J-A 3.03; C-I 31; C-II 31; J-M(XII) 20, 55; theory sheet 2.2 Q.3. Searches "polynomial extrema", "polynomial degree extremum" found nothing.

Coverage candidates not added (covered elsewhere in the master):
- Greatest / least value in an interval -> Monotonicity / Greatest and Least value (prompts 21, 22, 24).
- Leibniz rule for $\int^x$ -> Method of Differentiation / Differentiation of Integration (31), Definite Integration (28).
- Range of $a\sin x+b\cos x$ -> Trigonometric Ratio / Range of Trigonometric Functions type 3 (71); AM-GM -> Sequence & Progression / Concept of AM-GM.
- Minimum distance of a point / line from a conic (J-I 65 uses reflection) -> Parabola / Ellipse "Tangent & Normal" (65, 66, 49, 50); mapped to item 27 (geometry).
- Number of real roots of non-cubic equations (J-A 3.08 quintic, J-II 76 quartic) -> Monotonicity added item "number of real roots"; mapped here to item 28 (roots of a cubic) / concavity items.

### Rephrased / cleaned prompts
- No prompt was rephrased. OCR damage was cleaned without changing the meaning in 4, 10, 12, 13, 14, 15, 16, 26, 29, 30, 31, 32 ("ata", "ofa", "Whatis", "Howto", "| ", f'"(a) -> $f''(a)$); the master heading "n" derivative test" was written as "$n$th derivative test".
- The master lists the heading "Maxima and Minima at a point" twice (prompts 1-3 and 4); merged into one heading.
- Prompt 27 (number of real / imaginary roots of a cubic) sits under "Geometrical Problems" in the master; it was kept in master order but placed as the first item of "Analysis of Cubic Equation", where the theory sheet treats it. The master PDF is not in the repo, so wording could not be checked against the page image.

### Questions with no matching item (`-`)
- J-I 69 (rate of change; see above).

### Source points to check
- Theory sheet 2.2 Q.1 (iv) $y=4x^3-12x$: the answer line says maxima at $x=-1$, minima at $x=1$ (correct), but the worked solution below says "Maxima at $x=1$, minima at $x=-1$" (wrong). The Quick Review uses the correct version (checked with sympy).
- Theory sheet 1.1: definition of minima is printed "at $x=b$" but uses $f(a)$; written with $a$ in the kit.
- DPP-6 Q.9 (least value of $2^{(x^2-3)^3+27}$): the printed answer is (A) $2^{27}$, but its own solution (and sympy) gives $2^0=1$, option (C).
- J-A 3.10: printed answer AD is correct, but the solution text says "Hence $f$ has local maximum at $x=2$"; from $f''(2)=f(2)>0$ it is a local minimum.
- J-A 3.05 / 3.06 (paragraph): the printed solutions are swapped / end with the other question's option; the printed answers (3.05 D, 3.06 C) are correct.
- J-II 98: the printed answer AB includes $2$ (value at the end point $x=2$), which is the greatest value, not a local maximum value in the strict sense; not used in any example.

### Other decisions
- The renderer was run from a copy of the skill scripts (session scratch folder) with the same change as in the Tangent & Normal and Monotonicity runs: `kit_grading.py` keeps non-integer question numbers (J-A 3.01 ...) as text and prints their ranges in steps of 0.01. Nothing in the skill folder was changed.
- All Quick Review examples were checked with sympy ($x^3-3x$ on $[-2,3]$: $-2, 2, -2, 18$; sign scheme of $(x-1)(x-2)^2(x-3)(x-4)$; $f''(\pm1)=\pm24$ for $4x^3-12x$; $f'(0)=f''(0)=0$, $f'''(0)=30$ for $x^5-5x^4+5x^3-1$; inflection $x=1$ of $x^3-3x^2$; $-2<a<2$ for $x^3-3x+a$; factorisations of $f'$ for $x^3-6x^2+9x$, $x^3+3x^2$, $x^3+6x^2+9x$; $k=3$, $C=1$ giving $x^3-3x+1$; $3\sin\frac\pi3=\frac{3\sqrt3}2$; rectangle in a semicircle maximum $r^2$ at $x=r\sqrt2$).
- The sheet's naming is "concave" for $f''>0$ and "convex" for $f''<0$; the kit uses "concave up / concave down" and mentions the sheet's naming once.
- Cubic conditions (items 29-32, master prompts 28-31) are stated for leading coefficient $a>0$ with the note "swap if $a<0$", matching the theory sheet's worked example (which assumes $a>0$).
- Hindi follows the Tangent & Normal / Monotonicity runs for shared terms; new terms are in `hindi_glossary_additions.md`. "AM-GM" is kept in Latin in one flowchart line.
- Mapping is judgement; figure questions (J-II 77, 78: graph of $f'$; DPP-6:10: graph of $f''$; DPP-6:17) were mapped from the stem; DPP-5:15 and DPP-6:9 (garbled text) were read from the page images.
- Word files validated with the docx validator (all passed); `verify_outputs.py` reports ALL GOOD.
