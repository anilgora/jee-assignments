# Definite Integration: revision kit report

- Items in the Quick Review: 39
- Batch XII: 183 graded questions, High threshold 17 -> High 3, Medium 20, Low 16
  - High items (numbers): [4, 12, 27]
- Batch XIII: 149 graded questions, High threshold 14 -> High 3, Medium 18, Low 18
  - High items (numbers): [4, 12, 27]

## Added items

## Rephrased items
- 3 (original 3): What is the relation of the limits with $dx$ in definite integration?
- 4 (original 4): What is the condition for the result $\int_a^b f'(x)\,dx=\big[f(x)\big]_a^b$?
- 5 (original 5): What is the condition for the result $\int_a^a f(x)\,dx=0$? What follows when $\int_a^b f(x)\,dx=0$?
- 8 (original 8): What is the value of $\int_0^{\pi/2}\sin^n x\,dx$ and $\int_0^{\pi/2}\cos^n x\,dx$ if $n=1,2,3,4$?
- 13 (original 13): If $f(y)$ is a non-negative continuous function such that $f(y)+f\left(y+\frac12\right)=7\ \forall\,y\ge0$, find $\int_0^5 f(y)\,dy$.
- 19 (original 19): What is the condition on $f(x)$ when we apply king on $\int_a^b x\,f(x)\,dx$?
- 33 (original 33): For a finite $n$, how to check the order among $\dfrac1n\sum_{r=0}^{n-1}f\left(\dfrac rn\right)$, $\int_0^1 f(x)\,dx$ and $\dfrac1n\sum_{r=1}^{n}f\left(\dfrac rn\right)$?

## Questions with no matching item
- J-A:18

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]

## Validation warnings
- none


---
## Run details (added by the routine, 2026-10-18)

### Input files used
- Theory (combined sheet "Indefinite & Definite Integration"; only the Definite part was used = PDF pages 83-178, sections 1.1-9): `chapters/Integration/Theory.pdf`
- XII sheet (combined): `chapters/Integration/XII.pdf`. Reference for J-I, J-II, J-A, C-I and C-II, and supplies J-M(XII).
- XIII sheet (combined): `chapters/Integration/XIII.pdf`. Only its J-M is used (skill rule).
- DPP (combined): `chapters/Integration/DPP.pdf`. Pages 57-124 ("Special DPP on Definite Integration" #1-5) were copied into a temporary PDF in the session scratch folder (pdfseparate / pdfunite) and indexed. Pages 1-56 (Indefinite DPPs) belong only to Indefinite Integration (all 124 questions were classified "Indefinite only" in the sibling run) and are not used here. The original was not changed.
- Question Bank (this chapter's own, unchanged): `chapters/Definite_Integration/QB.pdf`. It has 68 questions numbered **21-88** (the numbering continues the Indefinite QB 1-20); the printed numbers are kept.
- Quick Review prompt list: the skill's `references/master_index.json` (Definite Integration, 39 prompts in 13 headings, master pages 88-89). No `jee-inputs/master_index.json` and no master PDF in the repo; the PDF was not needed because the chapter is in the index.
- Classification of the shared sheets: `jee-kit-output/Indefinite_Integration/integration_question_classification.json` (made in the Indefinite Integration run from the page images), re-used and extended as below.
- No input file was moved, renamed or edited.

### Combined chapter (Integration = Indefinite Integration, Definite Integration)
`extract_questions.py` on the full combined sheets gave J-I 85, J-II 111, J-A 47, C-I 32, C-II 41, J-M(XII) 80, J-M(XIII) 100, Definite DPP #1-5 = 25+28+29+23+19, QB 68 (21-88). These match the earlier run and the PDFs (continuous numbering, no gaps). Questions classified "Indefinite only" were deleted from `question_index.json` before mapping and grading. The Definite DPPs are keyed **DPP-D1 ... DPP-D5** (as in the Indefinite kit) and appear in the practice maps as "DPP: D1(...)". Printed question numbers are kept everywhere.

| Source | Total | Kept | Definite only | Shared with Indefinite | Dropped (Indefinite only) |
|---|---|---|---|---|---|
| J-I | 85 | 59 | 55 | 4 | 26 |
| J-II | 111 | 64 | 41 | 23 | 47 |
| J-A | 47 | 46 | 34 | 12 | 1 |
| C-I | 32 | 26 | 21 | 5 | 6 |
| C-II | 41 | 24 | 14 | 10 | 17 |
| J-M(XII) | 80 | 69 | 55 | 14 | 11 |
| J-M(XIII) | 100 | 83 | 50 | 33 | 17 |
| Definite DPP #1-5 | 124 | 124 | 75 | 49 | 0 |
| Indefinite DPP #1-5 | 124 | 0 | 0 | 0 | 124 |
| QB (own) | 68 | 68 | 68 | 0 | 0 |

Per batch:
- **XII sheet** (J-I, J-II, J-A, C-I, C-II, J-M(XII)): 396 questions. Kept 288 (220 Definite only + 68 shared). Dropped 108 as Indefinite only.
- **XIII batch** (its J-M(XIII)): 100 questions. Kept 83 (50 Definite only + 33 shared). Dropped 17.
- **DPP:** 248 questions in the combined file. Kept 124 (the whole Definite series: 75 Definite only + 49 shared). Dropped the 124 Indefinite DPP questions.

Shared questions are mapped here only to Definite Integration items; their full list is in the Indefinite Integration REPORT.md (same split), plus J-I 84 and 85 (below).

**Decisions that differ from / complete the sibling run:**
- **J-I 84, 85** (reduction relations $5I_4-6I_6$ for $\int\sin^n x$, $I_4+I_6$ for $\int\tan^n x$; indefinite integrals) were "Indefinite only" there. They genuinely use this chapter's "Integration by Reduction" prompt, so they are kept here as shared (mapped to item 39).
- **J-II 87** (number of roots of $f$ from $f(x)f(-x)=9$, comprehension 85-87): no integration; kept here as the closest chapter (the comprehension is in the Definite part) and mapped to item 29. Uncertain.
- **J-II 96** (area of the triangle formed by $g(x)$ and the axes, comprehension 94-96): $f$, $g$ are found by determination-of-function methods; the area step is Area Under Curve. Kept and mapped to item 29. Uncertain.
- **J-A 18** (paragraph 18-19, JEE Adv 2015: signs of $f'$ from $F'<0$): no integral at all; kept because the paragraph is a Definite question, but mapped to `-` (no item). It is the only unmapped question; it is counted in the graded total (J-A) without raising any item.

### Grading
- **XII:** graded = J-M(XII) 69 + J-A 46 + QB 68 = 183. High threshold = max(2, round(16.65)) = 17.
- **XIII:** graded = J-M(XIII) 83 + J-A 46 + QB 68 - 48 overlaps = 149. High threshold = max(2, round(13.56)) = 14.
- **High items** (same three in both batches): 4 (Newton-Leibnitz / evaluating by an antiderivative; XII 46, XIII 46), 12 (P3 for non-uniform functions: modulus, $[x]$, $\{x\}$, piecewise; XII 35, XIII 22), 27 (Leibnitz rule; XII 32, XIII 23). Next in line: 29 determination of function (XII 13), 14 odd/even (12), 2 substitution (12/13), 16 king (9/12), 30 limit of sum (11/7).
- Item 4 is the item for every question whose difficulty is the evaluation itself (definite integration through indefinite methods: substitution, parts, partial fractions). The indefinite techniques are covered in the Indefinite Integration Quick Review, so they were not added here (cross-chapter rule).
- J-A is the same sheet exercise for both batches, so it is graded in both, as in the earlier combined runs.
- **QB overlaps (XIII), 48 questions counted once:** QB 37-65 and 70-88 are J-M(XIII) questions. `detect_overlaps.py` flagged 41 of them; 7 more were confirmed by reading the stems, options and answers: QB 37 = J-M(XIII) 83, QB 41 = 88, QB 60 = 67, QB 73 = 98, QB 82 = 75, QB 85 = 44, QB 88 = 49. Checked and **not** the same: QB 35 vs J-M(XIII) 19, QB 66 / 69 vs 45, QB 26 vs 32, QB 30 vs 28. No overlap with J-M(XII) (all candidates were different questions: QB 23, 25, 28, 34). QB 21-36 and 66-69 are unique to the QB.

### Added items
- None. The only coverage candidate was "if $\int_a^b f=0$ then $f$ has a root in $(a,b)$" (J-I 27; J-A 26, 35). `search_master.py` finds Rolle's theorem (Monotonicity) and IVT (Continuity & Differentiability), so no item was added; the fact is stated in the model answer of item 5 (theory sheet "Important Points" 2), and these questions are mapped to item 5.
- Other candidates not added: integrating a power series term by term (J-M(XIII) 14; DPP-D2:17) - covered in Binomial Theorem / "Summation of Series Type 4"; mapped to item 4. Improper / divergent integrals (DPP-D2:21, 25) - only in the DPP, not in the master; mapped to item 4. Beta-function relations $I(m,n)$ (QB 32, 41; J-M(XIII) 88) - mapped to item 39 (reduction); no master match for "beta".

### Rephrased / reconstructed prompts
The OCR of the master pages for this chapter is damaged in every math-heavy prompt, and without the master PDF the page images could not be checked. **Please check these against the printed master:**
- **3** "relation of limits with dx": answered as "limits are values of the variable in the differential" (theory sheet "Important Points" 5, $\int x\,d(\ln x)$). Tagged rephrased.
- **4** read as $\int_a^b f'(x)dx=[f(x)]_a^b$ (theory "Important Points" 3). Tagged rephrased.
- **5** read as $\int_a^a f\,dx=0$ (theory point 4); the root-existence fact (point 2) was added to the same prompt. Tagged rephrased.
- **6** read as bringing $\lim_{n\to\infty}$ inside $\int_p^q$ (theory point 6).
- **7** read as $\int_a^b f+\int_c^d g=bd-ac$ (theory, inverse functions).
- **8** read as $\int_0^{\pi/2}\sin^n x$, $\int_0^{\pi/2}\cos^n x$ for $n=1..4$ (theory "Important results" 1-4); the upper limit $\frac\pi2$ is an inference. Tagged rephrased.
- **13** the OCR "f(y)+... [y+3)=7 ... fro) dy" was read as $f(y)+f(y+\frac12)=7\ \forall y\ge0$, find $\int_0^5 f(y)dy$; this is exactly DPP-D3 Q29 (answer $\frac{35}2$). Tagged rephrased.
- **19** read as the condition $f(a+b-x)=f(x)$ for $\int_a^b xf(x)dx$. Tagged rephrased.
- **24** read as $\int_0^{\pi/2}\ln(\sin x)dx$.
- **33** the OCR of the three limits was garbled; written as the order of the left sum, the integral and the right sum (theory 5.2). Tagged rephrased.
- Headings kept as printed, including "Walli's Theorem".

### Source points to check (found while mapping)
- **DPP-D2:12:** printed answer $(1-e)/(1+e)$ ignores the jump of $1/(1+e^{1/x})$ at $0$; the value is $2/(1+e)$ (already noted in the Indefinite report).
- **DPP-D3:19:** the upper limit is printed as $\pi$ but should be $a$.
- **DPP-D4:6:** sign slip in the last solution line (printed answer D is right).
- **DPP-D4:17:** $\int dx/\sqrt{1+x^2}$ worked as $\tan^{-1}$ in the solution (answer B still right).
- **DPP-D1:20:** the solution states $x=\sin^2\theta$ but uses $x=\sin\theta$; printed answer correct.
- **J-II 78(a):** "$2e^{(n-4)/2}$" is a typo for $2e^{(\pi-4)/2}$.
- **J-II 64:** the solution substitutes $\sec x=t$ across the break at $\frac\pi2$; the final answer is still right.
- **J-M(XII) 76:** the "Ans." line reads "Official Answer NTA (24)".
- **J-A 24:** printed as "Bonus". **J-A 35:** English option (C) prints the limit as $1$; the Hindi option and the solution use $-1$.
- **C-II 29:** the solution says $\lambda=\pi/4$ midway, then gives $\pi/2$ (the printed, correct answer).
- **DPP-D5:14:** the Hindi stem is missing in the PDF.

### Checks on the kit's own content
- Every Quick Review example (39 items) was checked with sympy / mpmath: e.g. $\int_0^2[x^2]dx=5-\sqrt2-\sqrt3$, $\int_0^{16\pi/3}|\sin x|dx=\frac{21}2$, $\int_0^{\pi/2}\sin^4x\cos^6x\,dx=\frac{3\pi}{512}$, $\frac{d}{dx}\int_x^{x^2}\ln t\,dt=(4x-1)\ln x$, the limit $\frac23$, $k=\frac23$, $\frac\pi4$, $\ln3$, $\frac4e$, $\frac{35}2$.
- All Word files passed the docx validator (`defusedxml` was installed for it). `verify_outputs.py` reports ALL GOOD. Sample pages of the Quick Review, Hindi short notes and the mind map were rasterised and checked by eye.

### Other decisions
- The renderer was run from a copy of the skill scripts in the session scratch folder. One line of `kit_grading.py` was changed (as in the Indefinite run) so that DPP labels such as "D1" sort correctly. Nothing in the skill folder was changed.
- Mapping is judgement. Each question was mapped from its stem, its exercise sub-heading (J-I / J-II are printed by property) and the method notes recorded from the solutions in the sibling run; a few were read in full from the sheet text (J-A 18, J-M(XII) 65, QB 36). A question that combines methods is mapped to the property or step that carries the difficulty, with at most one "other" item. Match-the-column and paragraph questions are mapped once, to the dominant idea.
- In the Hindi files "limit" ($\lim$) is written सीमा-मान, to keep it apart from सीमा (limits of integration). `\text{}` never contains Hindi.
