# Ellipse: revision kit report

- Items in the Quick Review: 68
- Batch XII: 60 graded questions, High threshold 5 -> High 8, Medium 19, Low 41
  - High items (numbers): [6, 8, 10, 15, 20, 36, 41, 45]
- Batch XIII: 53 graded questions, High threshold 5 -> High 6, Medium 18, Low 44
  - High items (numbers): [6, 8, 20, 36, 41, 45]

## Added items
- 18: How to find the locus when a point has coordinates of the form $(p\cos\theta,\ q\sin\theta)$ - e.g. a point dividing a rod sliding on the axes, or dividing the ordinate of a circle in a fixed ratio?  [source: J-II:3, J-II:28, J-II:96, J-M(XIII):42, QB:107]

## Rephrased items
- 19 (original 18): What does 'everything' mean for an ellipse?

## Questions with no matching item

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [103, 104, 105, 106, 107, 110]

## Validation warnings
- none

---
## Run details (added by the routine, 2026-10-17)

### Input files used
- Theory (combined Conic Section sheet, Ellipse part = PDF pages 53-82 only): `chapters/Conic_Section/Theory.pdf`
- XII sheet (combined): `chapters/Conic_Section/XII.pdf` - reference for J-I, J-II, J-A, C-I, C-II and its own J-M
- XIII sheet (combined): `chapters/Conic_Section/XIII.pdf` - only its J-M is used (skill rule)
- DPP (combined): `chapters/Conic_Section/DPP.pdf` (DPP 5-7 are the Ellipse DPPs; DPP 1-4 Parabola, 8-10 Hyperbola; a few ellipse questions sit in DPP 8-10)
- Question Bank (this chapter's own, unchanged): `chapters/Ellipse/QB.pdf` (19 questions, printed numbers 92-110 kept as printed)
- Quick Review prompt list: skill `references/master_index.json` (Ellipse, 67 prompts, 11 headings, master pages 42-44). `jee-inputs/master_index.json` and the master PDF are not in the repo; the PDF was not needed.
- No input file was moved, renamed or edited; no sheet had to be merged.

### Item numbering
The Quick Review numbers items consecutively. The one added item is number 18 (end of "Auxiliary Circle and Eccentric Angle"), so master prompts 18-67 appear as items 19-68 (master number + 1). The "High items" above use the final numbers: XII High = master prompts 6, 8, 10, 15, 19, 35, 40, 44; XIII High = master 6, 8, 19, 35, 40, 44.
Everywhere else in this "Run details" section, item numbers are master prompt numbers (the ids used in `question_map.json`; the added item is `N1`), except "item 31" and "Item 18" which are final numbers as printed in the Quick Review.

### Combined chapter (Conic Section = Parabola, Ellipse, Hyperbola)
Extraction found J-I 46, J-II 100, J-A 44, C-I 20, C-II 65, J-M(XII) 67, J-M(XIII) 64 and DPP-1..10 (163) - the same counts as the Parabola run. The counts on the sheets' contents pages do not match one chapter because the sheets are shared - expected.
The Parabola run's classification (`jee-kit-output/Parabola/conic_question_classification.json`) was reused for the Parabola part; every question it had marked "dropped (Ellipse/Hyperbola)" was read again and split between Ellipse and Hyperbola. `question_index.json` keeps only Ellipse questions (203 sheet/DPP questions + 19 QB). Original numbers and exercise names are unchanged.
The full, extended classification is saved in `conic_question_classification.json` in this folder for the Hyperbola run.

| Source | Total in sheet | Kept | Ellipse only | Shared with sibling | Dropped (sibling only) | Shared questions (P = Parabola, H = Hyperbola) |
|---|---|---|---|---|---|---|
| J-I | 46 | 17 | 14 | 3 | 29 | 12(H), 14(H), 15(H) |
| J-II | 100 | 33 | 21 | 12 | 67 | 49(P), 57(H), 61(P), 75(H), 81(H), 82(H), 91(H), 93(P), 94(P,H), 95(P,H), 97(P), 98(H) |
| J-A | 44 | 14 | 8 | 6 | 30 | 14(P), 19(P), 20(P), 26(P), 31(P), 41(P) |
| C-I | 20 | 4 | 3 | 1 | 16 | 20(H) |
| C-II | 65 | 26 | 20 | 6 | 39 | 29(P), 31(P), 44(H), 55(P), 63(P,H), 65(P,H) |
| J-M(XII) | 67 | 27 | 20 | 7 | 40 | 32(P), 38(P), 39(P), 44(H), 59(H), 65(H), 67(H) |
| J-M(XIII) | 64 | 26 | 17 | 9 | 38 | 9(P), 30(H), 41(P), 44(H), 46(H), 47(H), 48(H), 50(H), 62(H) |
| DPP-1..4 | 63 | 0 | 0 | 0 | 63 | — |
| DPP-5..7 | 48 | 45 | 41 | 4 | 3 | DPP-5:5(P), DPP-6:3(P), DPP-7:8(P), DPP-7:9(P); dropped DPP-6:11, 12, 13 (Parabola) |
| DPP-8..10 | 52 | 11 | 1 | 10 | 41 | DPP-8:1, 4, 5, 7, 15(H), DPP-9:3, 11, 18(H), DPP-9:17(P); DPP-9:16 and DPP-10:2 are Ellipse only |
| QB (own) | 19 | 19 | 19 | 0 | 0 | — |

Per batch: XII sheet (J-I, J-II, J-A, C-I, C-II, J-M(XII)) = 342 questions: kept 121 (86 Ellipse only + 35 shared), dropped 221.
XIII batch (its J-M(XIII); the other exercises are taken from XII) = 64: kept 26 (17 + 9 shared), dropped 38. DPP = 163: kept 56 (43 + 13 shared), dropped 107.

Classification rules applied:
- A question is kept if its main topic is the ellipse or if it genuinely needs an ellipse result (foci, $e$, LR, tangent, chord...). Questions where an ellipse and a hyperbola (or parabola) are both worked with are shared and mapped here only to ellipse items.
- Questions on the general conic (nature of a conic, definition) stay in Parabola (as in the Parabola run) unless the curve is only an ellipse (e.g. J-I:7, DPP-5:12 are kept here).
- Paragraph / matrix questions were classified by reading their paragraph or rows in the PDF text: J-II 59-61 (ellipse $\frac{x^2}9+\frac{y^2}4=1$) kept, J-II 62-63 (circle and hyperbola) dropped; J-II 94, 96, 97, 98; C-II 59-61 (conic is the rectangular hyperbola $xy=8$) dropped; C-II 63-65; DPP-7:8-13; DPP-9:13-15 (hyperbola) dropped, DPP-9:16-18 kept.

Ambiguous classifications (closest chapter chosen):
- J-I:15, J-II:75, J-II:95 (which curves does a product equation represent), C-I:20 (solution of a differential equation is "an ellipse or a hyperbola"), DPP-9:11 (which conic has most normals from a point), J-II:98 (matrix with ellipse and hyperbola rows) - kept and shared with Hyperbola.
- J-M(XIII):22 - the Parabola run thought this sets question ("In a group of 100 persons...") was mis-extracted. It is genuine: the sets answer gives the numbers used in the eccentricity of an ellipse. Kept in Ellipse (item 6).
- DPP-9:16-18 - the extracted text lost the sign of "conic C: $\frac{x^2}{16}\ \frac{y^2}{12}=1$"; Q18 speaks of its minor axis, and the answers fit the ellipse $\frac{x^2}{16}+\frac{y^2}{12}=1$. Kept in Ellipse; this corrects the Parabola run, which labelled DPP-9:17 "Parabola + Hyperbola" (it is Parabola + Ellipse).
- DPP-6:11-12 - the Parabola run marked them shared with Ellipse, but the paragraph curve is the parabola $y^2-8x-4y+28=0$; dropped here (Parabola only).
- C-II:43 (circle meets the hyperbola $x^2-y^2+6x+16y-46=0$), J-II:90 (director circle of a hyperbola) and J-II:100 - dropped to Hyperbola.
- J-M(XII):39, J-II:93, C-II:29 - the ellipse only supplies a point or the LR ends for a parabola question; kept as shared (the ellipse step is real) and mapped to the ellipse item used.

### Grading
- XII: graded = J-M(XII) 27 + J-A 14 + QB 19 = 60; High threshold max(2, round(0.091 x 60)) = 5.
- XIII: graded = J-M(XIII) 26 + J-A 14 + QB 19 - 6 overlaps = 53; High threshold 5.
- QB 103-107 and 110 are the same questions as J-M(XIII) 58, 59, 40, 41, 42, 43 (detect_overlaps similarity 0.79-0.98) -> counted once for XIII. No overlap with J-M(XII).
- J-A of the combined sheet is graded in both batches (skill rule: J-A comes from the XII reference sheet).

### Added item
- Item 18 (tag `added`): locus of a point of the form $(p\cos\theta, q\sin\theta)$ - rod sliding on the axes, point dividing the ordinate of a circle in a fixed ratio. Needed by J-II:3, J-II:28, J-II:96(B), J-M(XIII):42 = QB:107; the theory sheet treats it (section 1.4 Q.1 and Ex.10). `search_master.py` for "rod", "sliding", "ends on axes" found nothing in any chapter.

Coverage candidates not added, because another chapter of the master already covers them:
- Area of an ellipse $\pi ab$ (C-II:30, DPP-5:11, J-A:30, QB:109, J-M(XIII):59 = QB:104) -> Area Under Curve / "Area bounded by a curve" and "curve given in parametric form" (prompts 1, 25); mapped to items 6, 7, 15, 62.
- Locus of the foot of the perpendicular from the centre on a tangent (J-I:28) -> Straight Line / Equation of a line (prompt 93); mapped to 35 (the result is also written in item 66's answer).
- Common tangent of an ellipse and a circle / parabola / ellipse (J-I:34, J-II:43, J-II:46, J-M(XII):35, 66, 67, DPP-6:3, DPP-7:8, J-A:41, QB:96) -> Tangent & Normal / Ultimate Concept (prompt 13) and Circle / Common Tangents; mapped to 35.
- Curves cutting orthogonally (J-II:81, C-II:31, J-M(XIII):30) -> Tangent & Normal / Orthogonal curves; mapped to the ellipse item used (6, 40, 8).
- Confocal ellipse and hyperbola (J-I:14, J-II:57, C-II:44, DPP-8:5, J-M(XII):59, J-M(XIII):46) -> Hyperbola / Highlights (prompt 71); mapped to item 19 (foci).
- Number of normals from a point (DPP-9:11) and the focal-chord relation $\tan\frac\alpha2\tan\frac\beta2=\frac{e-1}{e+1}$ (J-I:41, J-II:12) are written into the answers of items 47 and 34 instead of new items.

### Rephrased / cleaned prompts
- Master prompt 18 is a statement ("Everything means ..."), turned into the question "What does 'everything' mean for an ellipse?" (tag `rephrased`).
- OCR damage was cleaned without changing meaning: "C, and C, ... C, is contained in C," -> $C_1$, $C_2$ with $C_2$ inside $C_1$ (prompt 27, the order follows the theory sheet's version); "P( ~ ) and Q( 8)" -> $P(\alpha)$, $Q(\beta)$ (prompts 34, 48); "b in terms ofa", "Whatis", leading "|" etc. The master PDF is not in the repo, so math prompts could not be re-read from the page image.

### Questions with no matching item (`-`)
None - every kept question maps to an ellipse item.

### Source points to check
- Theory sheet PDF p.57 (sheet p.5), 1.6 Ex.1: $\frac{(x-y+1)^2}{32}+\frac{(x+y-3)^2}{50}=1$ is reduced to denominators 16 and 25, but the solution then takes $b^2=9$ and gives $e=\frac45$, $\ell_{LR}=\frac{18}5$. With $b^2=16$ the correct values are $e=\frac35$, $\ell_{LR}=\frac{32}5$ (checked on the page image). The Quick Review (final item 31 = master 30) uses the corrected values.
- Theory sheet 4.1 Ex.1 (tangent to $4x^2+3y^2=12$ perpendicular to $y=2x+7$): printed "Ans. $y=2x\pm4$"; the worked solution and a sympy check give $y=-\frac x2\pm\frac{\sqrt{19}}2$. Not used in the kit.
- Item 10: the product of focal distances is least ($b^2$) at the vertices and greatest ($a^2$) at the ends of the minor axis - checked, as QB:92 needs both.

### Other decisions
- All Quick Review examples (about 30 numeric checks plus the symbolic results for items 44, 47, 48, 63, 66 and the foot-of-perpendicular loci) were verified with sympy before use.
- Hindi reuses the Parabola/Circle run terms (नाभि, नियता, उत्केन्द्रता, नाभिलम्ब, निदेशक वृत्त, स्पर्श जीवा, ध्रुव/ध्रुवी); new terms are in `hindi_glossary_additions.md`.
- Mapping is judgement; matrix-match questions were mapped to the item of their ellipse rows (e.g. J-II:94 (C), (E); J-II:97 (C), (D)); figure questions (J-II:10) from the stem.
- All eight Word files pass the docx schema validator; `verify_outputs.py` reports ALL GOOD (no raw `$` left, every equation native).
