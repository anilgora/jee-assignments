# Indefinite Integration: revision kit report

- Items in the Quick Review: 48
- Batch XII: 58 graded questions, High threshold 5 -> High 4, Medium 28, Low 16
  - High items (numbers): [1, 7, 15, 17]
- Batch XIII: 71 graded questions, High threshold 6 -> High 5, Medium 27, Low 16
  - High items (numbers): [1, 7, 15, 17, 31]

## Added items
- 7: What is the general method of substitution, and which forms does it give directly?  [source: J-I 4, 5; J-II 4-10; DPP; J-M (both); QB (theory sheet section 2)]
- 48: How to integrate $\dfrac{1}{(x-a)^m(x-b)^n}$ when $m+n=2$ (powers may be fractions)?  [source: J-M(XII) 18; J-M(XIII) 82; J-A 27; QB 3]

## Rephrased items
- 5 (original 5): Integrate $\dfrac1{1+\sin x}$ (and $\dfrac1{1+\cos x}$).
- 22 (original 21): How to integrate $\sqrt{\text{Quadratic}}$?
- 45 (original 44): How to integrate $\int\dfrac{dx}{(ax+b)\sqrt{px+q}}$ and $\int\dfrac{dx}{(ax^2+bx+c)\sqrt{px+q}}$?
- 46 (original 45): How to integrate $\int\dfrac{dx}{(ax+b)\sqrt{px^2+qx+r}}$?
- 47 (original 46): How to integrate $\int\dfrac{dx}{(ax^2+b)\sqrt{px^2+q}}$?

## Questions with no matching item

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [6, 7, 8, 9, 10, 11, 12, 13, 14, 18, 19, 20]

## Validation warnings
- none


---
## Run details (added by the routine, 2026-10-18)

### Input files used
- Theory (combined sheet "Indefinite & Definite Integration"; Indefinite part = PDF pages 1-82 only, sections 1.1-8.6): `chapters/Integration/Theory.pdf`
- XII sheet (combined): `chapters/Integration/XII.pdf`. It is the reference for J-I, J-II, J-A, C-I and C-II, and it supplies its own J-M.
- XIII sheet (combined): `chapters/Integration/XIII.pdf`. Only its J-M is used (skill rule).
- DPP (combined): `chapters/Integration/DPP.pdf`. Pages 1-56 are "Special DPP on Indefinite Integration" #1-5 and pages 57-124 are "Special DPP on Definite Integration" #1-5. Both series restart at DPP #1, so the file was split into two temporary copies in the session scratch folder (pdfseparate / pdfunite). The original was not changed.
- Question Bank (this chapter's own, unchanged): `chapters/Indefinite_Integration/QB.pdf` (20 questions).
- Quick Review prompt list: the skill's `references/master_index.json` (Indefinite Integration, 46 prompts, master pages 86-87). The repo has no `jee-inputs/master_index.json` and no master PDF. The PDF was not needed because the chapter is in the index.
- No input file was moved, renamed or edited.

### Combined chapter (Integration = Indefinite Integration, Definite Integration)
`extract_questions.py` was run on the full combined sheets: J-I 85, J-II 111, J-A 47, C-I 32, C-II 41, J-M(XII) 80, J-M(XIII) 100, Indefinite DPP #1-5 = 27+24+31+23+19, Definite DPP #1-5 = 25+28+29+23+19, QB 20. All counts were checked against the PDFs: numbering is continuous with no gaps, and every DPP count matches its pages.

This is the first run of the Integration group, so every question was classified here. Each question was read from the page image, using its worked solution to judge the method. The full classification is saved as `integration_question_classification.json` for the Definite Integration run. Questions labelled "Definite Integration only" were deleted from `question_index.json` before mapping and grading.

The rule from the run prompt was applied. A definite-integral question is shared only when finding the antiderivative is a real part of the difficulty (substitution, parts, partial fractions, trigonometric substitution, classic $e^x(f+f')$ ...). Properties, limit of a sum, the Leibniz rule, functional equations, inequalities and estimates are Definite only.

**Question keys.** The Indefinite DPPs keep the keys DPP-1 ... DPP-5. The kept questions of the Definite DPP series are keyed **DPP-D1 ... DPP-D5** (Definite DPP #1 ... #5) and appear in the practice maps as "DPP: D1(...)". Printed question numbers are kept everywhere.

| Source | Total | Kept | Indefinite only | Shared with Definite | Dropped (Definite only / neither) |
|---|---|---|---|---|---|
| J-I | 85 | 30 | 28 | 2 | 55 |
| J-II | 111 | 70 | 47 | 23 | 39 + 2 |
| J-A | 47 | 13 | 1 | 12 | 34 |
| C-I | 32 | 11 | 6 | 5 | 21 |
| C-II | 41 | 27 | 17 | 10 | 14 |
| J-M(XII) | 80 | 25 | 11 | 14 | 55 |
| J-M(XIII) | 100 | 50 | 17 | 33 | 50 |
| Indefinite DPP #1-5 | 124 | 124 | 124 | 0 | 0 |
| Definite DPP #1-5 | 124 | 49 | 0 | 49 | 75 |
| QB (own) | 20 | 20 | 20 | 0 | 0 |

Per batch:
- **XII sheet** (J-I, J-II, J-A, C-I, C-II, J-M(XII)): 396 questions. Kept 176 (110 Indefinite only + 66 shared). Dropped 220 (218 Definite only + 2 belonging to neither).
- **XIII batch** (its J-M(XIII); the other exercises come from XII): 100 questions. Kept 50 (17 Indefinite only + 33 shared). Dropped 50.
- **DPP:** 248 questions. Kept 173 (124 Indefinite only + 49 shared). Dropped 75.

Shared questions (kept here and mapped only to Indefinite Integration items):
- J-I: 34, 35
- J-II: 40, 41, 42, 43, 44, 46, 47, 50, 51, 52, 56, 57, 58, 59, 61, 67, 68, 77, 78, 82, 83, 84, 100
- J-A: 2, 5, 6, 8, 13, 16, 21, 25, 27, 31, 32, 41
- C-I: 7, 8, 9, 15, 23
- C-II: 14, 15, 16, 17, 18, 20, 22, 23, 33, 40
- J-M(XII): 3, 7, 13, 17, 28, 37, 38, 46, 54, 56, 69, 70, 79, 80
- J-M(XIII): 3, 6, 10, 13, 15, 18, 36, 40, 41, 42, 43, 46, 49, 53, 55, 58, 62, 63, 66, 68, 74, 75, 76, 86, 89, 90, 91, 93, 94, 96, 97, 98, 100
- DPP-D1: 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25
- DPP-D2: 1, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 17, 18, 19, 21, 22
- DPP-D3: 4, 18, 20, 28
- DPP-D4: 21
- DPP-D5: 1, 6, 10, 14

**Ambiguous classifications** (decided as noted):
- **J-M(XII) 1:** partial-fraction coefficient algebra with no integration. Kept and mapped to item 37 (non-repeated linear factors).
- **J-M(XII) 60:** a differential equation (variables separable) whose integration step is $e^x=t$. Kept as the closest chapter and mapped to the general substitution item (7). The Differential Equation run may want it too.
- **J-II 85:** find $f(x)f(-x)$ from $\int f'/f$, inside a definite-integral comprehension. Kept as Indefinite.
- **J-II 87 and J-II 96:** J-II 87 is about the roots of $f$ and continuity; J-II 96 is the area of a triangle. Both were labelled "neither" and dropped here, and are left for the Definite Integration run to decide.
- **Borderline Definite vs shared.** These were decided by judgement and could reasonably go either way:
  - Marked Definite: J-I 27, 32; J-II 48, 49, 62, 64, 65, 102, 105; C-I 6, 10, 13, 28; J-M(XII) 76; Definite DPP-1:1, 2:2, 3:15, 3:19, 5:5.
  - Marked shared: J-I 34; J-II 43, 44, 46, 51, 61, 82-84; J-A 2, 5, 21; C-I 23; C-II 15, 33, 40; J-M(XII) 7, 38, 46, 69, 80; J-M(XIII) 18, 42, 43, 46, 55, 58, 62, 63, 75, 90, 97, 98, 100; Definite DPP-1:4, 1:25, 2:14, 2:15, 2:17, 2:19, 4:21, 5:6.
- **Definite only, though partly another chapter:**
  - J-M(XIII) 19, 34: integral equations that turn into differential equations.
  - J-A 44: Leibniz rule, then a linear differential equation.
  - J-M(XII) 51: area interpretation.

### Grading
- **XII:** graded = J-M(XII) 25 + J-A 13 + QB 20 = 58. High threshold = max(2, round(5.28)) = 5.
- **XIII:** graded = J-M(XIII) 50 + J-A 13 + QB 20 - 12 overlaps = 71. High threshold = max(2, round(6.46)) = 6.
- **QB overlaps (XIII):** QB 6-14, 18, 19 and 20 are J-M(XIII) 78, 79, 80, 50, 51, 52, 25, 28, 29, 81, 30 and 31. detect_overlaps gave similarities of 0.74-0.93; QB 19 = J-M(XIII) 30 was confirmed by reading both. Two lower matches are different questions: QB 16 vs J-M(XII) 19 (0.64) and QB 4 vs J-M(XIII) 80 (0.60). There is no XII overlap.
- **High items (renderer numbers):**
  - XII: 1 (definitions / constant of integration), 7 (general substitution, added), 15 (parts formula), 17 (tricks of parts: 1 as second function, cyclic, reduction relations).
  - XIII: the same four plus 31 ($1/(a\sin^2x+b\cos^2x+\dots)$, $\tan x=t$).
- J-A is the same sheet exercise for both batches, so it is graded in both, as in the earlier combined runs.

### Added items
- **7 (N1), under "Integration by Substitution":** the general substitution $\int f(\phi(x))\phi'(x)dx$, with $\int f'/f$ and $\int f^nf'$.
  - Why: the master has this heading and four special prompts (tan/cot/sec/cosec, $1/(a\sin x+b\cos x)$, inverse-trig and log substitutions), but no prompt for the general method, which is the main idea of a large share of the questions.
  - Source: J-I 4, 5; J-II 4-10; many DPP, J-M and QB questions; theory sheet section 2.
  - `search_master.py` finds the heading only in this chapter.
- **48 (N2), under "Integration of Irrational Algebraic Functions":** $\int\dfrac{dx}{(x-a)^m(x-b)^n}$ with $m+n=2$; put $\dfrac{x-a}{x-b}=t$.
  - Source: J-M(XII) 18; J-M(XIII) 82; J-A 27; QB 3.
  - `search_master.py` searches for "(x-a)^m", "power of (x-a)" and "x-a/x-b" found nothing.

Coverage candidates not added:
- **Reduction formulas $I_n$** (J-I 84, 85; J-II 82-84; J-M(XII) 69; J-M(XIII) 46, 90, 98): covered under Definite Integration / "Integration by Reduction". Mapped here to item 17 (tricks of parts).
- **Term-by-term integration of an infinite series** (Definite DPP-2:17): a one-off and not a standard Indefinite Integration method, so it was mapped to item 2. Searches for "series term by term" and "infinite series integral" found nothing.
- **Determining $C$ from a given value / finding $f$ from $f'$:** very common in J-M and QB. Folded into item 1, whose answer now says how $C$ is fixed.

### Rephrased / reconstructed prompts
The OCR text of this chapter's master pages is badly damaged, and without the master PDF in the repo the page images could not be checked. Prompts were reconstructed from the OCR fragments and the matching sections of the theory sheet. **Please check these against the printed master:**
- **5:** the OCR "Integrate T+sin(x) ° (Gy)" was read as $\dfrac1{1+\sin x}$ (and $\dfrac1{1+\cos x}$), matching theory sheet 1.2.4. Tagged rephrased.
- **4:** "sin" x, cos" x" was read as $\sin^nx$, $\cos^nx$ for small $n$ (theory 1.2.3 Q.3-8).
- **12, 13, 17, 18:** reconstructed as the standard results of theory 3.1, 3.2, 4.2 and 4.3.
- **21:** ",/Quadratic" was read as $\sqrt{\text{Quadratic}}$. Tagged rephrased.
- **22:** read as linear/quadratic, linear/$\sqrt{\text{quad}}$ and linear$\cdot\sqrt{\text{quad}}$ (theory 4.4 profile 6).
- **26:** read as $\int e^{g(x)}(f(x)g'(x)+f'(x))dx$.
- **41:** read as $(ax^2+bx+c)/(x^4+px^2+q)$ with $q>0$ (theory 8.2).
- **44-46** (printed 43-45, because the master prints the number 43 twice): reconstructed from theory 8.3 P-2/P-3, P-4 and P-5. Tagged rephrased.
- **16** ("the trick of integration by parts"): answered with three tricks: take 1 as the second function, cyclic integrals, and forcing / reduction.
- **40** ("taking out power of $x$ as common"): answered with $\sqrt{x^2}=|x|$ and the sign of $x$.
- The master headings "Miscellaneous" and "Miscellaneous type" were kept as two separate headings, as printed.

### Questions with no matching item
- None. Every kept question has a main item.

### Source points to check (printed answer or solution errors found while mapping)
**Printed answers that are wrong or misprinted:**
- **QB 8 = J-M(XIII) 80:** options C and D are both "7" and the printed answer is D (7), but the solution gives $\alpha+\gamma/\beta=1+3=4$.
- **Indefinite DPP-3:27:** the printed answer $\tfrac12\log(\cos^2x+2\sin^2x)$ belongs to a different integrand. The question and its solution give $-\tfrac14\cos2x+C$.
- **Indefinite DPP-3:19:** the printed answer is missing the factor 2 that the solution has.
- **Indefinite DPP-5:15:** the printed answer has $e^{\cos x}$; it should be $\ln(xe^{\sin x})$.
- **Indefinite DPP-5:17:** the printed answer has $+\tan^{-1}(\dots)$; the (correct) solution gives $-\tan^{-1}(\dots)$.
- **Definite DPP-2:12:** the printed answer $(1-e)/(1+e)$ is wrong. $1/(1+e^{1/x})$ jumps at 0, and the value is $2/(1+e)$.
- **J-II 78(a):** "$2e^{(n-4)/2}$" is a typo for $2e^{(\pi-4)/2}$.
- **Indefinite DPP-2:23:** the "Ans." line is blank; the answer appears only in the solution.
- **J-A 24 and J-M(XIII) 27:** printed as "Bonus".

**Misprints in stems or options:**
- **Indefinite DPP-5:12:** the stem prints the denominator $x^3+1$; the answer and solution use $x^3+x$.
- **Definite DPP-3:19:** the upper limit is printed as $\pi$ but should be $a$.
- **J-A 35:** the English option (C) prints the limit as 1, while the Hindi option and the solution use $-1$.

**Slips in worked solutions (printed answers still correct):**
- **Indefinite DPP-5:11:** the partial-fraction constants are wrong; sympy gives $A=-30/343$, $C=30/343$.
- **Indefinite DPP-5:16 and DPP-4:8:** sign / factor slips in the last line.
- **Definite DPP-1:20:** the solution states a different substitution from the one it actually uses.
- **Definite DPP-4:6:** a sign slip in the last line.
- **Definite DPP-4:17:** $\int dx/\sqrt{1+x^2}$ is worked out as $\tan^{-1}$.
- **J-II 25:** the last solution line has $4\cos^{2/3}x$ instead of $4\cot^{2/3}x$.
- **J-II 107(B):** $\int dt/\sqrt{t^2-2}$ is worked out as the log form of $\int dt/(t^2-2)$.
- **C-II 29:** the solution says $\lambda=\pi/4$ midway, then gives $\pi/2$, which is the printed (correct) answer.

**Checks on the kit's own content:** the theory sheet was used only for method statements, and no formula was copied from garbled text. Every Quick Review example was checked with sympy by differentiating the answer: 47 integrals, including those of the added items.

### Other decisions
- The renderer was run from a copy of the skill scripts in the session scratch folder. One line of `kit_grading.py` was changed so that DPP labels such as "D1" (the Definite DPP series) sort correctly. Nothing in the skill folder was changed.
- `\text{}` never contains Hindi. Inside math the Hindi files write $Q$ for "quadratic" and $\text{Dr}$ for "denominator"; each is explained in the surrounding sentence. "ILATE" is kept in Latin, inside math.
- Mapping is judgement. A question that combines methods is mapped to the method that carries the difficulty, with at most two "other" items. Multi-part (matrix-match / paragraph) questions are mapped once, to the dominant method.
- All Word files passed the docx validator (`defusedxml` had to be installed for it). `verify_outputs.py` reports ALL GOOD.
