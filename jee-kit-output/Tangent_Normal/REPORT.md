# Tangent & Normal: revision kit report

- Items in the Quick Review: 32
- Batch XII: 23 graded questions, High threshold 2 -> High 8, Medium 4, Low 20
  - High items (numbers): [2, 8, 12, 14, 15, 16, 19, 31]
- Batch XIII: 9 graded questions, High threshold 2 -> High 3, Medium 4, Low 25
  - High items (numbers): [2, 14, 16]

## Added items
- 31: How to find the rate of change of a quantity, and solve related-rate problems (rate measure)?  [source: J-I 21, 23; J-II 22, 24-27; J-M(XII) 21, 23, 46; DPP-2 4, 6, 7, 9; QB 148]
- 32: For a point moving on a curve, how to compare the rates of change of its abscissa and ordinate?  [source: J-I 22; J-II 23]

## Rephrased items
- 9 (original 9): Write parametric coordinate for $\dfrac{x^n}{a^n}+\dfrac{y^n}{b^n}=1$.

## Questions with no matching item
- C-I:1

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [149, 150, 151, 152]

## Validation warnings
- none

---
## Run details (added by the routine, 2026-10-18)

### Input files used
- Theory (combined; Tangent & Normal part = pages 2-36 only): `chapters/Application_of_Derivative/Theory.pdf`
- XII sheet (combined): `chapters/Application_of_Derivative/XII.pdf` - reference for J-I, J-II, J-A, C-I, C-II and its own J-M
- XIII sheet (combined): `chapters/Application_of_Derivative/XIII.pdf` - only its J-M is used (skill rule)
- DPP (combined): `chapters/Application_of_Derivative/DPP.pdf` (DPP 1-2 are Tangent & Normal, 3-4 Monotonicity, 5-6 Maxima & Minima)
- Question Bank (this chapter's own, unchanged): `chapters/Tangent_Normal/QB.pdf` (6 questions, printed numbers 147-152 kept)
- Quick Review prompt list: skill `references/master_index.json` (Tangent & Normal, 30 prompts, 11 headings). `jee-inputs/master_index.json` and the master PDF are not in the repo; the PDF was not needed.
- No input file was moved, renamed or edited; no sheet had to be merged.

### Combined chapter (Application of Derivative = Tangent & Normal, Monotonicity, Maxima and Minima)
Extraction found J-I 74, J-II 127, C-I 34, C-II 52, J-M(XII) 59, J-M(XIII) 50, DPP-1..6 = 95. The counts on the contents pages do not match one chapter because the sheets are shared - expected.
The J-A exercise of this sheet is numbered by topic (1.01 = Tangent & Normal, 2.01-2.13 = Monotonicity, 3.01-3.16 = Maxima & Minima), so `extract_questions.py` did not find it; it was read by hand. Only J-A 1.01 is Tangent & Normal. (2.13 and 3.16 carry no number in the text layer; count of 30 is approximate.)
Every question was classified; `question_index.json` keeps only Tangent & Normal questions (152). Original numbers and exercise names are unchanged (J-A keeps its printed number 1.01).
The full classification is saved in `aod_question_classification.json` so the Monotonicity and Maxima and Minima runs can reuse it.

| Source | Total in sheet | Kept | T&N only | Shared with sibling | Dropped (sibling only) | Shared questions (Mo = Monotonicity, Mx = Maxima and Minima) |
|---|---|---|---|---|---|---|
| J-I | 74 | 23 | 23 | 0 | 51 | — |
| J-II | 127 | 38 | 34 | 4 | 89 | 58(Mx), 80(Mx), 81(Mx), 82(Mx) |
| J-A | 30 | 1 | 1 | 0 | 29 | — |
| C-I | 34 | 10 | 10 | 0 | 24 | — |
| C-II | 52 | 23 | 23 | 0 | 29 | — |
| J-M(XII) | 59 | 16 | 14 | 2 | 43 | 52(Mo), 55(Mx) |
| J-M(XIII) | 50 | 6 | 6 | 0 | 44 | — |
| DPP-1..6 | 95 | 29 | 28 | 1 | 66 | DPP-6:15(Mx) |
| QB (own) | 6 | 6 | 6 | 0 | 0 | — |

Per batch: XII sheet (J-I, J-II, J-A, C-I, C-II, J-M(XII)) = 376 questions: kept 111 (105 Tangent & Normal only + 6 shared), dropped 265.
XIII batch (its J-M(XIII); the other exercises are taken from XII) = 50: kept 6, dropped 44. DPP = 95: kept 29 (28 + 1 shared), dropped 66.

Classification rules applied:
- Rate-of-change (rate measure) questions are kept here: the combined theory sheet teaches "Rate Measure" in the Tangent & Normal part (section 6.2), and no chapter of the master Quick Review covers it.
- Minimum distance of a point / circle from a curve is kept here (master headings "Minimum Distance between two curves" exist only in this chapter), e.g. J-M(XII) 1, 43, J-M(XIII) 2, 35, 36, QB 147, 149, 151, 152.
- Questions where a tangent / normal must be set up and then optimised are shared with Maxima and Minima and mapped here only to tangent items (J-II 58, 80-82, J-M(XII) 55, DPP-6:15). J-M(XII) 52 (monotonicity plus a tangent through a given point) is shared with Monotonicity.
- Number-of-solutions questions that are really "curves touching" analysis ($e^x=kx$, $\ln x=kx$, $a^x=x$) are kept: J-I 17, 18, J-II 86-88, C-I 4, C-II 46.

Ambiguous classifications (closest chapter chosen):
- C-I:1 (slope of the line through two of the intersection points of two cubics) has no calculus at all; it sits among the tangent questions of C-I -> kept here, mapped `-`.
- J-M(XIII):13 (minimum length of the tangent segment of $9x^2+16y^2=144$ between the axes) -> dropped to Maxima and Minima: the tangent is the standard ellipse tangent (Ellipse chapter) and the difficulty is the minimisation.
- C-II:30 (greatest intercept between point of contact and foot of perpendicular, ellipse) and C-II:36 (greatest area of triangle APY, circle) -> dropped to Maxima and Minima for the same reason.
- J-M(XII):37, J-M(XIII):32, 48, 49 (areas of inscribed figures / triangle with a line through a point) -> dropped to Maxima and Minima (no tangent or normal needed).
- J-M(XIII):17, 19, 29 (how many times a curve crosses the $x$-axis) -> dropped to Monotonicity.
- J-I:72 ("horizontal tangent and point of inflection") -> dropped: only $f'=0$ is used.
- DPP-4:12 (LMVT, tangent parallel to a chord) -> dropped to Monotonicity (mean value theorem).
- J-M(XII):53 (line meets the graph twice, Rolle / LMVT) -> dropped to Monotonicity.

### Grading
- XII: graded = J-M(XII) 16 + J-A 1 + QB 6 = 23; High threshold max(2, round(2.09)) = 2.
- XIII: graded = J-M(XIII) 6 + J-A 1 + QB 6 - 4 overlaps = 9; High threshold 2.
- QB 149, 150, 151, 152 = J-M(XIII) 35, 1, 36, 2 (detect_overlaps similarity 0.9-0.93; 151 = 36 confirmed by reading both) -> counted once for XIII. No overlap with J-M(XII).
- With only 9 graded questions in XIII (and 23 in XII), the High / Medium / Low grades of this chapter rest on few questions; treat them as indicative.
- J-A 1.01 of the combined sheet is graded in both batches (the XIII sheet's J-A has the same 1.01).

### Added items
- 31 (N1) Rate measure / related rates: needed by J-I 21, 23; J-II 22, 24-27; J-M(XII) 21, 23, 46; DPP-2 4, 6, 7, 9; QB 148 (also C-I 6, C-II 7-12, 14, 42-44). `search_master.py` for "rate of change", "rate measure", "rate" found nothing in any chapter.
- 32 (N2) Comparing rates of abscissa and ordinate on a curve: J-I 22, J-II 23 (theory sheet Q.9 of 6.2).
Both are placed under a new "Miscellaneous" heading (skill rule: no matching master heading).

Coverage candidates not added (covered elsewhere in the master or by an existing item):
- Rolle / LMVT (J-M(XII) 12, 13, 53; DPP-4) -> Monotonicity / Rolle's Theorem, LMVT (dropped from this chapter).
- Tangent to a standard conic by the $T=0$ substitution (C-II 4, DPP-2:8) -> Parabola / Ellipse / Hyperbola tangent headings; the substitution rule is also in the notes (section 2).
- Angle between two lines from their slopes (C-II 5, DPP-2:11) -> Straight Line; mapped to item 19.
- Approximation errors in a triangle (C-II 13) -> item 28.

### Rephrased / cleaned prompts
- 9: the master text is OCR-garbled ("Write parametric coordinate for — + re 1, a"). Reconstructed from the theory sheet table (curve 4) as $\frac{x^n}{a^n}+\frac{y^n}{b^n}=1$; tagged `rephrased`. The master PDF is not in the repo, so this could not be checked against the page image.
- 8, 10, 12, 16, 24: OCR damage cleaned ("x\" oy\"", "| Howto", "ofa", "e*= kx, In(x) = kx and In(x)=kx’" -> $e^x=kx$, $\ln x=kx$, $\ln x=kx^2$) without changing the meaning.

### Questions with no matching item (`-`)
- C-I:1 (no calculus; see above).

### Source points to check
- Theory sheet 4.3 Q.6 and Q.7 answers say "If $0<k\le 1/e$ two solutions" (and $\le 1/(2e)$); at $k=1/e$ (resp. $1/(2e)$) there is exactly one solution (touching), as the same answer line also says. The Quick Review uses $0<k<1/e$ (resp. $<1/(2e)$) for two solutions.
- Theory sheet 1.1 Q.6: the piecewise function is garbled in the text layer; the printed answer ($T: x-y-2=0$, $N: x+y=0$, $f(1)=-1$, $f'(1)=1$) fits $f=x-2$ for $x\le1$ and $x^2-x-1$ for $x>1$, which the Quick Review uses (checked with sympy).
- Theory sheet 6.2 Q.9 ($x^3=12y$, abscissa faster than ordinate) answers $(-2,2)-\{0\}$; at $x=0$ the ordinate's rate is $0$, so $x=0$ also qualifies if $dx/dt\ne0$. The kit uses a different example (J-II 23) to avoid this.
- Theory sheet 3.2 Q.8 has no printed solution (answer 2 only); not used.

### Other decisions
- The skill's grading scripts read question numbers as integers; to keep the printed J-A number 1.01 the renderer was run from a copy of the skill scripts (in the session scratch folder) with one change in `kit_grading.py`: numbers that are not integers (1.01) are kept as text. Nothing in the skill folder was changed. A future skill version should accept such numbers.
- All Quick Review examples were checked with sympy before use (tangent/normal equations, ultimate-concept roots, common tangent $y=\pm\sqrt2x+\frac12$, distances $\sqrt5$, $\frac{3}{\sqrt2}$, $2\sqrt2$, angles, orthogonality condition for $a_1x^2+b_1y^2=1$, touching values $e$, $1/e$, $1/(2e)$, lengths $4\sqrt2,4,4\sqrt2,4$, $\sqrt{36.6}\approx6.05$, $\frac{dh}{dt}=\frac1{48\pi}$, points $(4,11)$, $(-4,-\frac{31}{3})$).
- Hindi follows the Circle / Parabola / Continuity runs for shared terms (स्पर्श रेखा, अभिलम्ब, प्रतिच्छेद कोण, लम्बकोणीय, ऊर्ध्वाधर स्पर्श रेखा, सन्निकटन); new terms are in `hindi_glossary_additions.md`. "LHD / RHD" are written as $f'(a^-)$, $f'(a^+)$ in Hindi.
- Mapping is judgement; paragraph questions (J-II 80-82, 86-88; C-II 42-46) were classified and mapped after reading their paragraphs. Figure-dependent stems were mapped from the stem and the printed solution.
- Word files validated with the docx validator (all passed); `verify_outputs.py` reports ALL GOOD.
