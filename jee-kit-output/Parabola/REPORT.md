# Parabola: revision kit report

- Items in the Quick Review: 99
- Batch XII: 84 graded questions, High threshold 8 -> High 7, Medium 36, Low 56
  - High items (numbers): [21, 32, 43, 47, 50, 74, 76]
- Batch XIII: 71 graded questions, High threshold 6 -> High 6, Medium 32, Low 61
  - High items (numbers): [21, 32, 43, 47, 65, 76]

## Added items

## Rephrased items
- 71 (original 71): How to find locus of a point P if a condition on the slopes of the normals drawn from P to the parabola is given?

## Questions with no matching item
- J-II:67
- J-A:17
- J-M(XIII):5
- J-M(XIII):37
- DPP-2:6
- DPP-2:7
- DPP-3:14
- QB:74
- QB:91

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [80, 84, 85, 86, 87, 88, 89, 90, 91]

## Validation warnings
- none

---
## Run details (added by the routine, 2026-10-17)

### Input files used
- Theory (combined, Parabola part = pages 1-52 only): `chapters/Conic_Section/Theory.pdf`
- XII sheet (combined): `chapters/Conic_Section/XII.pdf` - reference for J-I, J-II, J-A, C-I, C-II and its own J-M
- XIII sheet (combined): `chapters/Conic_Section/XIII.pdf` - only its J-M is used (skill rule)
- DPP (combined): `chapters/Conic_Section/DPP.pdf` (DPP 1-4 are the "Special DPP on Parabola"; 5-7 Ellipse; 8-10 Hyperbola)
- Question Bank (this chapter's own, unchanged): `chapters/Parabola/QB.pdf` (22 questions, printed numbers 70-91 kept as printed)
- Quick Review prompt list: skill `references/master_index.json` (Parabola, 99 prompts, 18 headings). `jee-inputs/master_index.json` and the master PDF are not in the repo; the PDF was not needed.
- No input file was moved, renamed or edited; no sheet had to be merged.

### Combined chapter (Conic Section = Parabola, Ellipse, Hyperbola)
Extraction found J-I 46, J-II 100, J-A 44, C-I 20, C-II 65, J-M(XII) 67, J-M(XIII) 64 and DPP-1..10 (163). The counts on the sheets' contents pages do not match a single chapter because the sheets are shared - expected.
Every question was classified; `question_index.json` keeps only Parabola questions (294 of 591). Original numbers and exercise names are unchanged.
The full classification is saved in `conic_question_classification.json` so the Ellipse and Hyperbola runs can reuse it.

| Source | Total in sheet | Kept | Parabola only | Shared with sibling | Dropped (sibling only) | Shared questions (E = Ellipse, H = Hyperbola) |
|---|---|---|---|---|---|---|
| J-I | 46 | 19 | 19 | 0 | 27 | — |
| J-II | 100 | 50 | 44 | 6 | 50 | 49(E), 61(E), 93(E), 94(E,H), 95(E,H), 97(E) |
| J-A | 44 | 30 | 24 | 6 | 14 | 14(E), 19(E), 20(E), 26(E), 31(E), 41(E) |
| C-I | 20 | 14 | 13 | 1 | 6 | 7(H) |
| C-II | 65 | 27 | 21 | 6 | 38 | 29(E), 31(E), 55(E), 58(H), 63(E,H), 65(E,H) |
| J-M(XII) | 67 | 32 | 24 | 8 | 35 | 10(H), 21(H), 32(E), 38(E), 39(E), 60(H), 62(H), 63(H) |
| J-M(XIII) | 64 | 28 | 24 | 4 | 36 | 9(E), 12(H), 32(H), 41(E) |
| DPP-1..4 | 63 | 63 | 63 | 0 | 0 | — |
| DPP-5..10 | 100 | 10 | 1 | 9 | 90 | DPP-5:5(E), DPP-6:3,11,12(E), DPP-7:8,9(E), DPP-9:17(H), DPP-10:7(H); DPP-6:13 is Parabola only |
| QB (own) | 22 | 22 | 22 | 0 | 0 | — |

Per batch: XII sheet (J-I, J-II, J-A, C-I, C-II, J-M(XII)) = 342 questions: kept 172 (145 Parabola only + 27 shared), dropped 170.
XIII batch (its J-M(XIII); the other exercises are taken from XII) = 64: kept 28 (24 + 4 shared), dropped 36. DPP = 163: kept 73 (64 + 9 shared), dropped 90.

Classification rules applied:
- General-conic questions (definition of a conic, nature of a conic from its equation or from focus/e/directrix, "which conic is this locus") are kept in Parabola, because in the master Quick Review the headings "Conic Section: Definition" and "General Equation of Conic" exist only in the Parabola chapter. If the conic turns out to be an ellipse or hyperbola only (e.g. J-I:29, J-I:45, DPP-5:12, DPP-8:10, DPP-8:14), the question was dropped.
- A question using a parabola and an ellipse/hyperbola is shared and mapped here only to parabola items.
- Paragraph/matrix questions were classified by reading their paragraph in the PDF (J-II 59-72, J-A 4-5, 9-10, 19-20, 23-25, 28-29, 34-35, C-II 56-61, DPP-4:11-13, DPP-6:11-13, DPP-7:8-9).

Ambiguous classifications (closest chapter chosen):
- J-II:67 - circle-only part of a paragraph whose other questions (68, 69) are parabola loci -> kept in Parabola, mapped `-`.
- J-A:24 - 2017 matrix question; the suitable conic turns out to be the circle $x^2+y^2=a^2$ -> kept in Parabola (tangent at a point, item 47). J-A:23 (ellipse) dropped, J-A:25 (parabola) kept.
- J-A:28, J-A:29 - 2019 matrix sets mainly on circles, with a common tangent to $x^2=8y$ -> kept in Parabola (common tangent).
- J-A:17 and J-M(XIII):37 (= QB:91) - circle-tangent questions where the parabola only gives the point $P$ -> kept, mapped `-`.
- J-II:100 (circles / branches of a hyperbola matrix) -> dropped to Hyperbola. C-I:20 (differential equation whose solutions are ellipses/hyperbolas, empty stem in the extracted text) -> dropped.
- J-M(XIII):22 - the extracted text is a sets question ("In a group of 100 persons..."), apparently mis-extracted or misplaced in the sheet -> dropped (not Parabola). Check this page.
- J-M(XIII):5 (two parabolas meeting on $y=1$; really a quadratic-equation / G.P. question) -> kept, mapped `-`.
- J-II:94, J-II:95, C-II:63, C-II:65 (matrix questions covering several conics) -> shared with Ellipse and Hyperbola.

### Grading
- XII: graded = J-M(XII) 32 + J-A 30 + QB 22 = 84; High threshold 8. XIII: J-M(XIII) 28 + J-A 30 + QB 22 - 9 overlaps = 71; High threshold 6.
- QB 80, 84-91 are the same questions as J-M(XIII) 35, 52-57, 36, 37 (detect_overlaps similarity 0.87-1.0) -> counted once for XIII. No overlap with J-M(XII).
- J-A of the combined sheet is graded in both batches (skill rule: J-A comes from the XII reference sheet).

### Added items
None. Coverage candidates found in the questions and not added, because another chapter of the master already covers them:
- Circle touching a curve at a given point (J-II:25, J-M(XII):23, 52, QB:81, DPP-6:13) -> covered in Circle / Family of Circle Type 4 (prompt 73); mapped here to item 47.
- Angle between two curves / orthogonal curves (DPP-1:4, C-I:14, C-II:31) -> Tangent & Normal / Orthogonal curves; mapped to item 47.
- Mirror image of a parabola in a line (J-A:11, J-M(XII):31) -> Straight Line / Concept of Image; mapped to items 21/22.
- Minimum distance between two curves (J-I:32) -> Tangent & Normal / Minimum Distance between two curves; mapped to 66.
- Area of a triangle from its vertices (J-M(XII):1, C-II:5, J-II:64) -> Straight Line / Area of Triangle; the parabola form $a^2|(t_1-t_2)(t_2-t_3)(t_3-t_1)|$ is written into item 98.
- Chords of a circle bisected by the parabola (J-M(XIII):56, QB:88) -> Circle / chord with given mid-point; mapped to 25.

### Rephrased / cleaned prompts
- 71: the master text of prompt 71 is a copy of prompt 46 (tangents); under the heading "Normal to Parabola from a point" it was rephrased to the same question for normals.
- Prompts with OCR damage were cleaned without changing their meaning (e.g. "y’ = 4ax" -> $y^2=4ax$, "t, and t," -> $t_1$ and $t_2$). Prompt 96 now names the axis ("intersect the axis at T and G"), which the master leaves implicit. The master PDF is not in the repo, so math prompts could not be re-read from the page image.

### Questions with no matching item (`-`)
J-II:67 (circle only), J-A:17 and J-M(XIII):37 = QB:91 (circle tangents), J-M(XIII):5 (quadratic/G.P.), DPP-2:6 (tangent length to a circle), DPP-2:7 (count of common chords), DPP-3:14 (number of intersections of $y=Ax^2$ with a hyperbola), QB:74 (circle through the axis-intercepts).

### Source points to check
- Theory sheet p.5-6 table "Other standard parabolas" prints the directrix of $x^2=4ay$ as $y=a$; it should be $y=-a$. The Quick Review uses $y=-a$.
- Theory sheet p.8 example (tangent at vertex $3x-4y=5$, focus $(1,2)$): in the extracted text the right side reads $8\left(\frac{3x-4y-5}{5}\right)$; with the focus on the negative side the correct form is $8\cdot\frac{4y-3x+5}{5}$ (checked with sympy against $PS=PM$, directrix $3x-4y-15=0$). The Quick Review uses the checked form.
- J-II:45: extracted text says tangents from $(1,2)$ to $y^2=4x$, but $(1,2)$ lies on the parabola; the printed answers ($x-y=1$, area $8\sqrt2$) fit $(-1,2)$, so a minus sign is probably lost in the text (not checked on the page image).
- Theory highlight 7 note says the tangents at the ends of a focal chord meet "on the foot of the directrix"; that is true only for the latus rectum - in general they meet on the directrix. The Quick Review states the general result.

### Other decisions
- All Quick Review examples (56 checks) were verified with sympy before use.
- Hindi uses the Circle-run terms for shared words (e.g. निदेशक वृत्त); new terms are in `hindi_glossary_additions.md`.
- Mapping is judgement; figure questions (e.g. J-I:4, J-II:53) were mapped from the stem and solution text.
