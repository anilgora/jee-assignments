# Monotonicity: revision kit report

- Items in the Quick Review: 55
- Batch XII: 59 graded questions, High threshold 5 -> High 4, Medium 17, Low 34
  - High items (numbers): [13, 33, 36, 54]
- Batch XIII: 39 graded questions, High threshold 4 -> High 4, Medium 12, Low 39
  - High items (numbers): [13, 33, 36, 54]

## Added items
- 54: How to find the number of real roots of $f(x)=0$ (or the number of points where $y=f(x)$ cuts the $x$-axis) using monotonicity?  [source: J-II 42, 76; J-A 2.03, 2.13; J-M(XII) 7, 11, 14, 29, 33, 34, 51; J-M(XIII) 17, 19, 24, 29, 40; QB 153, 158, 159, 170, 171, 173]
- 55: How to solve an inequality of the type $f(A(x))>f(B(x))$ when $f$ is monotonic?  [source: J-II 31, 32; C-I 9; J-M(XII) 31]

## Rephrased items
- 23 (original 23): How to check whether $a^b$ is greater/less than $b^a$?
- 33 (original 33): What can you say about number of solutions of $f'(x)=0$ if $f(x)=0$ has $n$ solutions?
- 34 (original 34): What can you say about number of solutions of $f(x)=0$ if $f'(x)=0$ has $m$ solutions?

## Questions with no matching item
- J-II:85

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173]

## Validation warnings
- none

---
## Run details (added by the routine, 2026-10-18)

### Input files used
- Theory (combined; Monotonicity part = PDF pages 37-91 only): `chapters/Application_of_Derivative/Theory.pdf`
- XII sheet (combined): `chapters/Application_of_Derivative/XII.pdf` - reference for J-I, J-II, J-A, C-I, C-II and its own J-M
- XIII sheet (combined): `chapters/Application_of_Derivative/XIII.pdf` - only its J-M is used (skill rule)
- DPP (combined): `chapters/Application_of_Derivative/DPP.pdf` (DPP 3-4 are Monotonicity; one DPP-6 question is shared)
- Question Bank (this chapter's own, unchanged): `chapters/Monotonicity/QB.pdf` (21 questions, printed numbers 153-173 kept)
- Quick Review prompt list: skill `references/master_index.json` (Monotonicity, 53 prompts, 12 headings). `jee-inputs/master_index.json` and the master PDF are not in the repo; the PDF was not needed.
- No input file was moved, renamed or edited; no sheet had to be merged.

### Combined chapter (Application of Derivative = Tangent & Normal, Monotonicity, Maxima and Minima)
The extraction was run on the full combined sheets (J-I 74, J-II 127, C-I 34, C-II 52, J-M(XII) 59, J-M(XIII) 50, DPP-1..6 = 95). The Tangent & Normal classification saved in `jee-kit-output/Tangent_Normal/aod_question_classification.json` was reused unchanged; the 375 questions it had dropped were split here between Monotonicity and Maxima and Minima.
As in the Tangent & Normal run, J-A of this sheet is numbered by topic (1.xx Tangent & Normal, 2.01-2.13 Monotonicity, 3.01-3.16 Maxima and Minima) and was not found by `extract_questions.py`; the 15 J-A questions kept here were written into `question_index.json` by hand from the page text and images (printed numbers 2.01 ... kept).
The complete classification of all 527 sheet/DPP questions is saved in `aod_question_classification.json` in this folder for the Maxima and Minima run.

| Source | Total in sheet | Kept | Monotonicity only | Shared with sibling | Dropped (sibling only) |
|---|---|---|---|---|---|
| J-I | 74 | 26 | 25 | 1 | 48 |
| J-II | 127 | 63 | 50 | 13 | 64 |
| J-A | 30 | 15 | 13 | 2 | 15 |
| C-I | 34 | 17 | 12 | 5 | 17 |
| C-II | 52 | 14 | 14 | 0 | 38 |
| J-M(XII) | 59 | 23 | 20 | 3 | 36 |
| J-M(XIII) | 50 | 21 | 21 | 0 | 29 |
| DPP-1..6 | 95 | 28 | 27 | 1 | 67 |
| QB (own) | 21 | 21 | 21 | 0 | 0 |

Per batch: XII sheet (J-I, J-II, J-A, C-I, C-II, J-M(XII)) = 376 questions: kept 158 (134 Monotonicity only + 24 shared), dropped 218 (Tangent & Normal or Maxima and Minima only).
XIII batch (its J-M(XIII); the other exercises are taken from XII) = 50: kept 21 (none shared), dropped 29. DPP = 95: kept 28 (27 + 1 shared), dropped 67.

Shared questions (kept here and mapped only to Monotonicity items):
- with Maxima and Minima: J-I 50; J-II 43, 44, 45, 56 (greatest / least value in an interval - the sheet's own section and the master heading "Greatest and Least value" are in Monotonicity), 75, 76, 77, 78, 92, 96, 115, 119, 122; C-I 8, 14, 22, 30, 32; J-M(XII) 5, 49; DPP-6:12; J-A 3.01, 3.12.
- with Tangent & Normal: J-M(XII) 52 (already shared in the Tangent & Normal run).

Classification rules applied:
- The user's own QBs were used as the guide for the Monotonicity / Maxima split: the Monotonicity QB holds the "how many times does the curve cut the $x$-axis", one-one, critical-point and Rolle-type questions (e.g. J-M(XIII) 17, 19, 29, 39, 41 and the greatest term J-M(XIII) 18); the Maxima and Minima QB holds absolute max/min in an interval with modulus, three-distinct-roots parameter questions and geometry. The same split was used for the sheets: J-M(XII) 36, 38, 54, 57, J-M(XIII) 12, 33, 43, J-A 3.08 -> Maxima and Minima.
- Rolle's theorem and LMVT questions (J-I 41-48, J-II 46-55, 101-102, 125-126, DPP-4, C-I 10, 12, 26, C-II 19-26, J-M(XII) 12, 13, 35, 53, J-M(XIII) 26, 41) are Monotonicity (master headings).
- Asymptote / graph-plotting questions (J-II 89-94, 120, C-I 29, C-II 47-50) are Monotonicity (master headings "Plotting the graph", "Asymptote").
- Point of inflection / concavity, local extrema, geometry and cubic-analysis questions are Maxima and Minima; they are shared only when the solution genuinely needs the sign of $f'$ (intervals of monotonicity) or a monotonicity statement is an option.

Ambiguous classifications (closest chapter chosen):
- J-II 85 (paragraph on the cubic $8x^3+4ax^2+2bx+a$: sum of the base-2 logarithms of the roots) needs only Vieta's relations -> kept with its paragraph in Monotonicity, mapped `-`.
- C-II 47, 48 (domain and limits of $(1+\frac1x)^x$, paragraph on plotting) -> kept, mapped to item 45 (plotting with limits).
- J-A 2.04 (equal maxima of $f$, $g$ on $[0,1]$; intermediate value theorem) -> kept, mapped to item 22; IVT itself is in Continuity & Differentiability.
- J-II 122, C-I 14, C-I 34 (true/false statements on increasing functions, extreme values and integrals) -> kept; 122 and C-I 14 also shared with Maxima and Minima.
- J-II 43-45, 56 (greatest / least value) -> shared, see above. J-I 49 (greatest and least value on $[1,e^2]$, in the sheet's Maxima section) -> left to Maxima and Minima.
- C-I 8 ($f(x)=k$ with one positive and one negative root) and J-II 76 (number of real roots of a quartic) -> shared: graph from monotonicity, values at the extrema.

### Grading
- XII: graded = J-M(XII) 23 + J-A 15 + QB 21 = 59; High threshold max(2, round(5.37)) = 5.
- XIII: graded = J-M(XIII) 21 + J-A 15 + QB 21 - 18 overlaps = 39; High threshold max(2, round(3.55)) = 4.
- QB 156-173 = J-M(XIII) 37, 39, 40, 24, 25, 26, 27, 28, 16, 4, 5, 6, 41, 42, 29, 17, 18, 19 (detect_overlaps similarity 0.74-1.0; QB 160 = J-M(XIII) 25 at 0.74 confirmed by reading both) -> counted once for XIII. QB 157 / 168 vs J-M(XII) 29 / 35 (0.64) are different questions; no XII overlap.
- High items in both batches: 13 (intervals of monotonicity), 33 (roots of $f$ and $f'$, Rolle), 36 (choosing the Rolle function), 54 (added: number of real roots).
- J-A 2.01-2.13 and the shared 3.01, 3.12 are graded in both batches (the XIII sheet's J-A is the same, as noted in the Tangent & Normal run).

### Added items
- 54 (N1) Number of real roots / crossings of the $x$-axis by monotonicity: J-II 42, 76; J-A 2.03, 2.13; J-M(XII) 7, 11, 14, 29, 33, 34, 51; J-M(XIII) 17, 19, 24, 29, 40; QB 153, 158, 159, 170, 171, 173 (also C-I 8, 32, C-II 23, J-A 2.02). `search_master.py` "number of real roots" finds only Maxima and Minima prompt 27 ("number of real/imaginary roots of a cubic"), which covers cubics only; the general method (exponential polynomials, degree 4-8 polynomials, transcendental equations) is not in the master, so it was added.
- 55 (N2) Solving $f(A)>f(B)$ with monotonic $f$: J-II 31, 32; C-I 9; J-M(XII) 31. Searches for "f(a) > f(b)", "inequality" found nothing of this kind.
Both are under "Miscellaneous" (no matching master heading).

Coverage candidates not added (covered elsewhere in the master):
- Intermediate value theorem (J-A 2.02, 2.04, C-I 14) -> Continuity & Differentiability / Intermediate Value Theorem (IMVT).
- One-one / onto via monotonicity, monotonic nature of the inverse (J-I 28, 29, J-II 90, 105, J-M(XIII) 4, 5, 27) -> Function / One-One and Many-one Function, Inverse of a function; mapped to item 13.
- Nature of $f'$ from $f''$ (concavity) for $g=f(x)+f(1-x)$-type questions (J-II 114, J-M(XIII) 15, 23) -> Maxima and Minima / Significance on sign of second order derivative (prompts 21-22); mapped to items 13 and 11.
- Cauchy-type results $f'(c)=k\,g'(c)$ (J-I 45, J-II 49): "Cauchy" has no match, but they are solved by Rolle on $f-kg$, which item 36 now states; not added.
- Greatest term of a sequence (J-M(XIII) 18, QB 172) -> item 21 (greatest value by monotonicity); Binomial "Numerically Greatest Term" is a different idea.

### Rephrased / cleaned prompts
- 23: master OCR "How to check whether a' is greater/less than b*?" -> "$a^b$ ... $b^a$" (the theory sheet compares $a^b$ and $b^a$ through $\frac{\ln x}{x}$).
- 33, 34: master OCR "number of solutions of f(x) = 0 if f(x) = 0 has n solutions" lost the primes; restored from the theory sheet note (i)/(ii) of Rolle's theorem as $f'(x)=0$ / $f(x)=0$.
- OCR damage cleaned without changing the meaning in 5, 6, 12, 13, 16, 19, 20, 21, 24, 28, 29, 40, 48, 49, 51 ("ais", "ofa", "Howto", "| ", "asumptote"). The master PDF is not in the repo, so these could not be checked against the page image.

### Questions with no matching item (`-`)
- J-II 85 (Vieta only; see above).

### Source points to check
- Theory sheet Q.2 (vi) prints the decreasing interval of $\sin x$ on $\left[-\frac\pi2,\frac{3\pi}2\right]$ with garbled symbols; the Quick Review uses $\left[\frac\pi2,\frac{3\pi}2\right]$ (decreasing), which is correct.
- J-II 45 asks for the minimum of $(x-a)^3+(x-b)^3$ over all real $x$; as printed the function has no minimum on $\mathbb R$. The printed answer $\frac{(b-a)^3}{4}$ fits $|x-a|^3+|x-b|^3$ (minimum at $x=\frac{a+b}2$), so the modulus signs were most likely lost. Mapped to item 21 from its section; not used in any example.
- Theory sheet: "To define monotonicity function need not to be continuous" and the IIT/NCERT naming table were kept as printed.

### Other decisions
- The renderer was run from a copy of the skill scripts (session scratch folder) with the same change as in the Tangent & Normal run: `kit_grading.py` keeps non-integer question numbers (J-A 2.01 ...) as text and prints their ranges in steps of 0.01. Nothing in the skill folder was changed.
- All Quick Review examples were checked with sympy (intervals of $x^3-3x$, values $0,-2,2$ and range $[-2,18]$, roots of $3x^4+4x^3-12x^2+4$ ($4$) and of $x^7+5x^3+3x+1$ ($1$), $x^3-3x+1$ ($3$ roots), $3^4>4^3$, $e^\pi>\pi^e$, $c=2$, $c=e-1$, $c=2\pm\frac1{\sqrt3}$ with $a=11$, range $\left[\frac13,3\right]$ of $\frac{x^2-x+1}{x^2+x+1}$, division $\frac{x^3+x^2+x+3}{x^2-1}=x+1+\frac{2x+4}{x^2-1}$, $f'(x)$ of $x^{2/3}$, $b^2-3ac<0$ for $x^3+x^2+x$).
- Hindi follows the Tangent & Normal / Continuity runs for shared terms; new terms are in `hindi_glossary_additions.md`. "LMVT" is kept in Hindi Quick Review headings and prompts (as in the master), but written as "लग्रांज प्रमेय" in the Hindi notes lines. "Q/Q" is kept as notation.
- Mapping is judgement; paragraph questions (J-II 83-97, C-II 47-50, J-A 2.01-2.02, 2.06-2.08) were classified and mapped after reading their paragraphs. Figure questions (J-II 77, 78: graph of $f'$) were mapped from the stem.
- Word files validated with the docx validator (all passed); `verify_outputs.py` reports ALL GOOD.
