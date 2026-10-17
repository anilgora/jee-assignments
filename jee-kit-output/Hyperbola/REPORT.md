# Hyperbola: revision kit report

- Items in the Quick Review: 84
- Batch XII: 44 graded questions, High threshold 4 -> High 6, Medium 18, Low 60
  - High items (numbers): [6, 8, 10, 18, 39, 49]
- Batch XIII: 37 graded questions, High threshold 3 -> High 6, Medium 19, Low 59
  - High items (numbers): [6, 8, 10, 18, 48, 49]

## Added items
- 80: The tangent at $P$ meets the asymptotes at $Q$ and $R$. What can you say about $P$ and the triangle $CQR$?  [source: DPP-10:6, J-II:77, C-II:50, C-II:51]
- 82: What are the tangent and normal at $P(t)$ on $xy=c^2$, and where does the normal meet the curve again?  [source: J-I:44, J-I:45, J-I:46, DPP-10:7, DPP-10:8, DPP-10:10, DPP-10:11, C-I:7]
- 83: What is the chord of $xy=c^2$ joining $t_1,t_2$, and the chord with a given mid-point?  [source: J-I:43, DPP-10:9, DPP-10:12, J-M(XIII):12, C-II:47]
- 84: A circle meets $xy=c^2$ in four points $t_1,t_2,t_3,t_4$. What relations hold?  [source: J-II:76]

## Rephrased items
- 17 (original 17): What does 'everything' mean for a hyperbola?

## Questions with no matching item

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [117, 118, 119, 120, 121, 126, 127, 128]

## Validation warnings
- none

---
## Run details (added by the routine, 2026-10-17)

### Input files used
- Theory (combined Conic Section sheet, Hyperbola part = PDF pages 83-117 only): `chapters/Conic_Section/Theory.pdf`
- XII sheet (combined): `chapters/Conic_Section/XII.pdf` - reference for J-I, J-II, J-A, C-I, C-II and its own J-M
- XIII sheet (combined): `chapters/Conic_Section/XIII.pdf` - only its J-M is used (skill rule)
- DPP (combined): `chapters/Conic_Section/DPP.pdf` (DPP 8-10 are the Hyperbola DPPs; DPP 1-7 contain no hyperbola question)
- Question Bank (this chapter's own, unchanged): `chapters/Hyperbola/QB.pdf` (18 questions, printed numbers 111-128 kept as printed)
- Quick Review prompt list: skill `references/master_index.json` (Hyperbola, 80 prompts, 16 headings, master pages 45-47). `jee-inputs/master_index.json` and the master PDF are not in the repo; the PDF was not needed.
- No input file was moved, renamed or edited; no sheet had to be merged.

### Item numbering
Items 1-79 = master prompts 1-79. Added item N4 is placed at the end of "Asymptote" as item 80, so master prompt 80 ("Derive everything for $xy=c^2$") is item 81, and the added items N1-N3 follow it as items 82-84 under "Rectangular Hyperbola $xy=c^2$". The High-item numbers above are final numbers; all of them are 1-79, so they equal the master numbers.
In `question_map.json` the ids are master numbers plus `N1`-`N4`.

### Combined chapter (Conic Section = Parabola, Ellipse, Hyperbola)
Extraction found J-I 46, J-II 100, J-A 44, C-I 20, C-II 65, J-M(XII) 67, J-M(XIII) 64 and DPP-1..10 (163) - the same counts as the Parabola and Ellipse runs. The counts on the sheets' contents pages do not match one chapter because the sheets are shared - expected.
The classification saved by the Ellipse run (`conic_question_classification.json`, copied into this folder unchanged) covers every question; every value containing "Hyperbola" was kept. The kept stems were re-read (and paragraphs / matrix questions checked in the PDF text) and no classification needed to change. `question_index.json` keeps only Hyperbola questions (162 sheet/DPP questions + 18 QB). Original numbers and exercise names are unchanged.

| Source | Total in sheet | Kept | Hyperbola only | Shared with sibling | Dropped (sibling only) | Shared questions (P = Parabola, E = Ellipse) |
|---|---|---|---|---|---|---|
| J-I | 46 | 13 | 10 | 3 | 33 | 12(E), 14(E), 15(E) |
| J-II | 100 | 31 | 23 | 8 | 69 | 57(E), 75(E), 81(E), 82(E), 91(E), 94(P,E), 95(P,E), 98(E) |
| J-A | 44 | 6 | 6 | 0 | 38 | — |
| C-I | 20 | 4 | 2 | 2 | 16 | 7(P), 20(E) |
| C-II | 65 | 21 | 17 | 4 | 44 | 44(E), 58(P), 63(P,E), 65(P,E) |
| J-M(XII) | 67 | 20 | 11 | 9 | 47 | 10(P), 21(P), 44(E), 59(E), 60(P), 62(P), 63(P), 65(E), 67(E) |
| J-M(XIII) | 64 | 21 | 12 | 9 | 43 | 12(P), 30(E), 32(P), 44(E), 46(E), 47(E), 48(E), 50(E), 62(E) |
| DPP-1..7 | 111 | 0 | 0 | 0 | 111 | — |
| DPP-8..10 | 52 | 49 | 40 | 9 | 3 | DPP-8:1, 4, 5, 7, 15(E), DPP-9:3, 11, 18(E), DPP-10:7(P); dropped DPP-9:16, 17, DPP-10:2 (Ellipse) |
| QB (own) | 18 | 18 | 18 | 0 | 0 | — |

Per batch: XII sheet (J-I, J-II, J-A, C-I, C-II, J-M(XII)) = 342 questions: kept 95 (69 Hyperbola only + 26 shared), dropped 247.
XIII batch (its J-M(XIII); the other exercises are taken from XII) = 64: kept 21 (12 + 9 shared), dropped 43. DPP = 163: kept 49 (40 + 9 shared), dropped 114.

Ambiguous classifications (kept from the Ellipse run, closest chapter chosen):
- J-I:15, J-II:75, J-II:95 (which curves does a product equation represent), C-I:20 (solution of a differential equation is "an ellipse or a hyperbola"), DPP-9:11 (which conic has most normals from a point), J-II:98 (matrix with ellipse and hyperbola rows) - shared with Ellipse; mapped here to the hyperbola item used.
- J-II:57 - the conic from the differential equation is the rectangular hyperbola $x^2-y^2=1$; kept (shared with Ellipse for part (b)).
- J-II:100 (matrix on circles; only row (D) "two branches of a hyperbola" is hyperbola) - kept here only, mapped to item 79.
- C-II:59-61 - paragraph conic is $xy=8$ (the stem text is lost in extraction; checked in the Ellipse run); kept and mapped to item 81 ($xy=c^2$).
- J-II:63 and QB:116 (circle $x^2+y^2-8x=0$ meets $\frac{x^2}9-\frac{y^2}4=1$ at $A,B$) - the hyperbola part is only solving the two curves; mapped to item 3.
- J-II:48 (tangents from a point of the hyperbola to a circle) - the hyperbola only supplies $(3\sec\theta,2\tan\theta)$; mapped to item 14.

### Grading
- XII: graded = J-M(XII) 20 + J-A 6 + QB 18 = 44; High threshold max(2, round(0.091 x 44)) = 4.
- XIII: graded = J-M(XIII) 21 + J-A 6 + QB 18 - 8 overlaps = 37; High threshold max(2, round(3.37)) = 3.
- QB 117, 118, 119, 120, 121, 126, 127, 128 are the same questions as J-M(XIII) 60, 62, 44, 45, 46, 63, 64, 49 (detect_overlaps similarity 0.87-1.0) -> counted once for XIII. No overlap with J-M(XII).
- J-A of the combined sheet is graded in both batches (skill rule). Only 6 J-A questions are hyperbola questions, so the grades lean on J-M and QB.

### Added items (coverage check)
`search_master.py` was run for each candidate ("xy = c", "rectangular hyperbola", "normal meets the curve again", "asymptotes in", "area of triangle formed by tangent", "circle meets", "orthocentre"); nothing in any chapter covers them except the bare heading "Rectangular Hyperbola xy = c²" with its single prompt 80.
- Item 80 (N4): tangent meets the asymptotes at $Q,R$: $P$ is the mid-point, area $CQR=ab$. Needed by DPP-10:6, J-II:77 (and Challenger C-II:50, 51). Theory sheet section 7, points 13-14.
- Item 82 (N1): tangent / normal at $t$ on $xy=c^2$, normal meets again at $t^3t_1=-1$, tangency condition $k^2+4mc^2=0$. Needed by J-I:44, 45, 46, DPP-10:7, 8, 10, 11.
- Item 83 (N2): chord of $xy=c^2$ joining $t_1,t_2$ and with a given mid-point. Needed by J-I:43, DPP-10:9, 12, J-M(XIII):12.
- Item 84 (N3): circle meeting $xy=c^2$ in four points ($t_1t_2t_3t_4=1$, $\sum x_i=-2g$, $\sum y_i=-2f$). Needed by J-II:76; theory sheet section 8 Q.2.

Coverage candidates not added, because another chapter of the master already covers them:
- Locus of the foot of the perpendicular from the centre on a tangent / normal (J-II:36, J-M(XII):46, C-II:45, DPP-10:11) -> Straight Line / Equation of a line (prompt 93); the hyperbola results are written into items 45 and 82, questions mapped to 39/45/46/50.
- Common tangent of a hyperbola with a circle / parabola (J-II:62, J-M(XII):10, J-M(XII):67, DPP-9:12, DPP-10:7, C-I:7) -> Circle / Common Tangents and Tangent & Normal; mapped to item 39 (or 82 for $xy=c^2$).
- Product of focal distances (J-II:56, J-M(XIII):61, 63, QB:112, 115) - not a separate master prompt; written into the answer of item 10 instead of a new item.
- Number of normals from a point (DPP-9:11) - written into item 51.

### Prompt / heading clean-up
- The saved master index puts prompt 1 under the heading "Ellipse: Introduction" (index error at the page break); it is placed under "Hyperbola: Introduction" here.
- Heading "Auxuliary Circle and Eccentric Angle" spelled "Auxiliary"; heading "Rectangular Hyperbola xy = c”" written as $xy=c^2$.
- Prompt 17 is a statement ("Everything means ..."), turned into the question "What does 'everything' mean for a hyperbola?" (tag `rephrased`).
- OCR damage cleaned without changing meaning: "S,S, and T" -> $S$, $S_1$, $T$; "P(@ ) and Q( 2)" -> $P(\alpha)$, $Q(\beta)$; "b in terms ofa", "Whatis", leading "|" and "." etc. The master PDF is not in the repo, so math prompts could not be re-read from the page image.

### Questions with no matching item (`-`)
None - every kept question maps to a hyperbola item.

### Source points to check
- Theory sheet p.2 (PDF p.84), 1.1: "ax²+2hxy+by²+2gx+2fy+c = 0 will represent an ellipse if Δ≠0; h² > ab and e > 1" - should read "a hyperbola". Item 1 states the hyperbola condition.
- Theory sheet section 7, Questions on Asymptotes Q.1: the constant for the pair of asymptotes of $3x^2-5xy-2y^2-5x+11y-8=0$ is $\lambda=-\frac{38}{49}$ (asymptotes $(3x+y-\frac{38}7)(x-2y+\frac17)=0$); the printed value appears without the minus sign in the extracted text. Item 75 uses $-\frac{38}{49}$ (checked with sympy).
- Theory sheet 1.2 point 12 says "Any chord of the ellipse passing through center ..." in the hyperbola section (copy-paste slip; not used).

### Other decisions
- All Quick Review examples (eccentricities, foci, LR lengths, the $PS=e\,PM$ expansion, tangents from a point, point of contact, normal at $(6,3)$, normal-condition identity, intersection of tangents at $\alpha,\beta$, least distance from a line, asymptote constant, area $CQR$, $t^3t_1=-1$, the four-point circle relations) were verified with sympy before use.
- Grading counts a question for its main item and every "other" item, as the skill says.
- Hindi reuses the Parabola/Ellipse run terms; new terms are in `hindi_glossary_additions.md`.
- Mapping is judgement; matrix-match questions were mapped to the item of their hyperbola row (J-II:94 row (A) -> 39; J-II:98 -> 73; C-II:65 -> 27).
- All eight Word files pass the docx schema validator; `verify_outputs.py` reports ALL GOOD (no raw `$` left, every equation native). The docx validator needed the Python module `defusedxml`, which was installed with pip for this run.
