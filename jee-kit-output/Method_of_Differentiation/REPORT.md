# Method of Differentiation: revision kit report

- Items in the Quick Review: 35
- Batch XII: 38 graded questions, High threshold 3 -> High 12, Medium 9, Low 14
  - High items (numbers): [3, 4, 5, 6, 7, 11, 15, 18, 20, 23, 29, 30]
- Batch XIII: 33 graded questions, High threshold 3 -> High 9, Medium 8, Low 18
  - High items (numbers): [3, 4, 6, 7, 11, 18, 20, 28, 29]

## Added items
- 17: How to differentiate an infinite expression such as $y=x^{x^{x^{\cdots}}}$ or $y=\sqrt{x+\sqrt{x+\cdots}}$?  [source: J-I:18, J-I:19, J-I:20, J-I:24]
- 22: How to find $\frac{d^2x}{dy^2}$ in terms of the derivatives of $y$ w.r.t. $x$?  [source: J-I:46, J-M(XII):13, C-II:6]
- 27: How to differentiate a function containing modulus (or defined piecewise) at a point?  [source: J-I:28, J-I:30, J-I:33]
- 28: How to find $f(x)$ when its definition contains its own derivative values, e.g. $f(x)=x^3+x^2f'(1)+xf''(2)+f'''(3)$?  [source: J-II:29, J-II:42, J-M(XIII):1, J-M(XIII):6, J-M(XIII):15, QB:145]

## Rephrased items
- 2 (original 2): What does a dot at the top of a function represent?
- 3 (original 3): Write the derivatives of all 19 standard functions.
- 12 (original 12): What is another method to differentiate $(f(x))^{g(x)}$?
- 15 (original 15): How to find the derivative of a function which is given in implicit form?
- 16 (original 16): What is the value of $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$ in case of a homogeneous equation in $x$ and $y$?
- 19 (original 18): What are the different ways to represent $\frac{dy}{dx}$, $\frac{d^2y}{dx^2}$, $\frac{d^3y}{dx^3}$, ...?
- 20 (original 19): What do you mean by $\frac{d^2y}{dx^2}$?
- 23 (original 21): How to plot the graph of ITFs like $\sin^{-1}\frac{2x}{1+x^2}$ by defining them piecewise and then finding limits, intervals of monotonicity and nature of concavity?
- 25 (original 23): How to find the coefficient of $x$, $x^2$ in any expansion?
- 26 (original 24): What is the condition for $f(x)$ to be divisible by $(x-a)^2$?
- 30 (original 26): What is L'Hospital rule?
- 31 (original 27): What are the things to keep in mind while applying L'Hospital rule?
- 32 (original 28): How many times can we apply L'Hospital rule?
- 33 (original 29): How to find the limit in case of $0^0$, $\infty^0$ forms?

## Questions with no matching item
- C-I:14
- C-II:9
- C-II:15
- C-II:24
- J-II:21
- J-II:47
- QB:131

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146]

## Validation warnings
- none

## Item numbering
- Final numbers 1-16 are master prompts 1-16. Added item 17 follows (infinite expressions, under "Derivative of implicit functions").
- Master prompts 17-20 are final 18-21. Added item 22 follows (d²x/dy², under "Higher order derivatives").
- Master 21 -> 23 and master 22-24 -> 24-26. Added items 27 (modulus / piecewise derivative) and 28 (f defined through its own derivative values) follow under "Miscellaneous".
- Master 25-31 are final 29-35. All 14 master headings are kept, in the master's order.

## Graded counts and High threshold
- **Batch XII:** J-M(XII) 16 + J-A 6 + QB 16 = 38 graded questions. High threshold = max(2, round(0.091 x 38)) = 3.
- **Batch XIII:** J-M(XIII) 25 + J-A 6 + QB 2 new = 33 graded questions. 14 QB questions are J-M(XIII) questions and are counted once. High threshold = max(2, round(3.0)) = 3.
- **Low items:** XII 2, 8, 12, 14, 16, 17, 19, 25-27, 31, 33-35; XIII 2, 8, 13, 14, 16, 17, 19, 21-27, 31, 33-35. No JM, JA or QB question tests these directly. Low means only "not tested in these questions".
- **Small graded sets:** the JM/JA/QB sets are small (38 and 33 questions), so a threshold of 3 makes many items High. That is the fixed rule; it is not a judgement.

## Question Bank overlap (checked by eye on the page images)
- **XIII**, QB -> J-M(XIII): 133->18, 134->19, 135->22, 136->23, 137->24, 138->10, 139->11, 140->12, 141->13, 142->14, 143->8, 144->25, 145->15, 146->16.
  - The script missed QB 135 = J-M(XIII) 22; it was found by eye.
  - QB 145 = JM 15 (not JM 1, which uses the same f but asks something else).
  - The twin questions have identical mappings.
- **XII:** no QB question equals a J-M(XII) question. This was checked by eye and agrees with the script.
- QB 131 and QB 132 match no J-M question in either batch.

## Added items (coverage check) and the cross-chapter rule
Every candidate was checked with search_master.py, using synonyms.
- **17 Infinite expressions** (x^x^x..., √(x+√(x+...)), continued fractions): no match in any chapter. Needed by J-I 18, 19, 20, 24.
- **22 d²x/dy² = −y₂/y₁³:** no match ("d2x/dy2", "second derivative inverse"). Needed by J-M(XII) 13 (graded) and J-I 46; C-II 6 also uses it.
- **27 Derivative of modulus / piecewise functions at a point:** no match. C&D item 50 is only about the derivability of g|f|. Needed by J-I 28, 30, 33.
- **28 f defined through its own derivative values,** e.g. x³+x²f'(1)+xf''(2)+f'''(3): no match. Needed by J-II 29 and 42, J-M(XIII) 1, 6, 15, and QB 145 (graded in both batches).

**Candidates not added** (covered elsewhere, or only needed by Challenger questions):
- **Limits by series expansion** (J-II 33, 35, 37, 39, 40; J-M(XIII) 25; QB 144): covered in Limit / "Standard Expansions" and "Limits based on expansion". These questions sit under the L'Hospital section of the sheet, so they were mapped to item 30 (L'Hospital), which is a valid alternative route.
- **Differentiating a functional equation in x and y** (J-M(XII) 12): covered in Continuity & Differentiability / "Determination of Function" (item 53, partial-derivative approach). Mapped to item 24 (differentiating an identity) + 3.
- **Zeros of f'(x) located graphically / trig zero sets** (J-A 1, 3, 4): this belongs to Application of Derivative / trig equations. Mapped to 4 / 7.
- **Polynomial root or sign conditions from P and P'** (C-I 16, 18, 20, 22) and **change of variable in a differential equation** (C-II 5): needed only by Challenger questions, which are excluded from the coverage check. Change of variable is also covered in Differential Equation item 31.
- **tan3x − tan2x − tanx = tan x tan2x tan3x** (C-I 21): Challenger; trig identity (Trigonometric Ratio).
- **"Trick" f'(0) for tan x · g(x)** (J-M(XIII) 10): this is the product rule (item 4).

## Rephrased items (why)
- **OCR slips corrected:** "ofa", "Whento", "Howto", "Whatis", "Whatare", the stray "|" at line starts, "ly 2" / "a x" garbage (prompt 16), "(f(x))®" (prompt 12 read as (f(x))^{g(x)}), and "0°, «99" (prompt 29 read as 0⁰, ∞⁰).
- **Maths restored:** prompt 16 "value of hk and" was read as "dy/dx and d²y/dx²", per theory sheet section 2.4 (Note: homogeneous function, dy/dx = y/x, d²y/dx² = 0). This is uncertain because the master PDF is not in the repo.
- **Unchecked:** the master PDF is not in the repo, so the printed wording could not be checked against the page image.
- **Other changes:** 21 gives the sheet's example function. 18-19, 26-28 and 2-3 have only wording or grammar changes.

## Questions with no matching item (why)
- **J-II 21:** differentiability of a piecewise function at 0. The RHD is found with L'Hospital, but the question is C&D.
- **J-II 47, C-II 9, C-II 15:** continuity / derivability only.
- **C-II 24:** a monotonicity condition that reduces to the range of f.
- **C-I 14:** pure integration.
- **QB 131:** functional-equation solving (f = K sin(x/2)). The derivative is only a trivial final step; it could be 20;3. It is graded but has no item.

## Uncertain decisions and notes
- **Question numbering:** J-I Q29 is printed "29..", and extract_questions.py stopped at Q28 because of it. A copy of the script that accepts "29.." was run from the scratch folder; the skill was not changed.
- **Counts:** J-I 51, J-II 48, J-M(XII) 16, J-A 6, C-I 24, C-II 25, J-M(XIII) 25, QB 16 (numbered 131-146) = 211 questions.
  - The contents pages give page numbers only.
  - In every exercise the numbering is continuous, and the last number agrees with the PDF.
- **No DPP:** there is no DPP for this chapter; the DPP part was skipped.
- **J-A of XIII:** the XIII sheet's J-A has 8 questions. Q1-6 equal XII's J-A, and Q7 (JEE Adv 2025) and Q8 (JEE Adv 2026) are new.
  - The skill takes every exercise except J-M from the XII sheet, so Q7 and Q8 are not in the index, the grading or the practice map.
  - They would map to Q7 -> 18 (inverse function) with 7, and Q8 -> 20 (higher order derivatives) with 25 (coefficient).
  - If you want them graded for XIII, a later skill version needs a per-batch J-A.
- **Images:** the text layer garbles almost every stem, so every question was read from page images, in seven parallel mapping passes.
- **Main uncertain mapping choices:**
  - J-I 5 -> 8 (could be 15).
  - J-I 10 -> 23 (ITF analysis; could be 14).
  - J-I 45 -> 1 (functional equation, but f' is found by first principle).
  - J-I 50 -> 30 (could be 1).
  - J-II 7, 16, 44 -> 6 (simplify first).
  - J-II 22 -> 24;1 (could be "-").
  - J-II 31 -> 29 (the sheet expands the determinant).
  - J-II 43 -> 20 (a paragraph part that is only a domain count).
  - J-M(XII) 1 and 6 -> 30 (also derivative-in-disguise, item 1).
  - J-M(XII) 9 -> 1;20.
  - J-A 5 -> 4;7 (the printed solution integrates a DE).
  - J-M(XIII) 3 -> 3;6,7.
  - J-M(XIII) 9 -> 3 (mostly a functional equation).
  - J-M(XIII) 20 -> 1;3 (ill-posed question).
  - J-M(XIII) 21 -> 20;4,7.
  - QB 132 -> 29;20 (the solution expands the determinant).
  - QB 142 -> 11;10.
  - C-I 12, 13, 16, 18, 22 and C-II 1, 2, 4, 20, 22 are borderline; see the mapping workbook.
- **Paragraph and matrix-match questions** are mapped once, by their dominant concept: J-A 3/4, J-II 42/43, J-II 47/48, C-II 20-22, 23-24, 25.

## Source errors / oddities found (answers checked; none of the printed final answers is wrong except where stated)
- **Wrong or unjustified working:**
  - **J-I 30:** the printed answer −2 is right, but the solution's piecewise forms are wrong. Near x=−1/2, f = −x; near 1/2, f = x.
  - **J-I 32:** the solution ends "option (1)", while Ans is B (−4).
  - **J-I 50:** the solution is only "Use L'Hospital's rule". This is not strictly justified, because f is differentiable only at x = h.
  - **J-II 36(b):** the answer is printed "does not exist", with no working. The limit tends to +∞ (cot x ~ 1/x dominates), so "does not exist (infinite)" is acceptable, but this is worth a teacher's check.
  - **J-II 46:** the solution writes cos⁻¹(2x²−1) = 2cos⁻¹x for all x. It is 2cos⁻¹|x|, and that is exactly why (B) fails. Ans AC is right.
  - **J-II 47(B):** g' omits the −(ln²(1+x)/x²)cos(1/x) term, which is the term that makes g' discontinuous.
  - **J-II 48(B):** the exponent is inverted and the L'Hospital steps are garbled. The answers are right.
  - **J-II 22:** the solution assumes g is differentiable at 0, which is not given.
  - **J-M(XIII) 3:** the solution solves sin4θ = +√3/2 instead of −√3/2. The θ set and β are wrong (correct β = 5π/8), but f(β) = 5/4 either way, so D stands.
  - **J-M(XIII) 20:** the question is ill-posed; the solution itself says so and gives the NTA answer A.
  - **C-II 20-22:** with g(0) = 1/3 the solution's g = 9/(3−x)³ is increasing, which contradicts "g decreasing", and its extension to x > 3 is unjustified. The intended answers stand only under that assumption.
  - **C-II 24:** the solution puts sec²x = t but needs t = sec x; answer D is right.
  - **C-II 25(D):** valid only for x in (0, π/2).
  - **C-I 11:** the solution is blank. Answer C was checked.
- **Typos:**
  - J-I 2, 26, 29 ("29.."), 35, 37, 40, 47.
  - J-II 5, 6, 14 (tan⁻¹x for 2tan⁻¹x), 19 (1+sin φ for 1+cos φ), 32, 36(a), 39 (ln(1+x) series garbled), 42.
  - J-M(XII) 4, 12 (f'(4)/f'(4) for f'(4)/f'(2)), 14, 15 (cos t for cot t).
  - J-A 3/4 (±(−1)ⁿ).
  - J-M(XIII) 5, 13, 15 / QB 145, 22, 24 / QB 137, 25.
  - QB 131.
  - C-I 10, 15, 16, 17, 18, 19, 24.
  - C-II 1, 12, 17, 19.
- **Garbled option fonts:**
  - J-I 22, 35, 40, 44, 49: the options are printed in a garbled Symbol font, and the answers were read from the solutions.
  - J-I 33: the Hindi options are garbled.
- **Blank Ans lines** (proof questions): J-II 3, 5, 6, 8, 11, 12, 17.
- **Theory sheet:** item 31's example was checked numerically, because the theory's Leibniz page has no example.
  - The theory's section 4 note "f is odd, aperiodic bound" was read as "bounded".

## Examples verified with sympy
Every Ex line was checked with sympy (scratch script checks.py):
- **First principle:**
  - x² -> 2x.
- **Rules:**
  - (2e)^x ln(2e).
  - (fgh)'(0) = 16.
  - x/sin x.
  - (x⁴+x²+1)/(x²+x+1) = x²−x+1.
  - tan²x sin²x/(tan²x−sin²x) = 1.
  - e^{x²}.
  - 2 sin 4.
  - f'(0) = n!·Hₙ (n = 5).
  - x^{sin x}.
- **Parametric, one function w.r.t. another, implicit and inverse:**
  - −tan t.
  - −cot x.
  - Implicit y' = −1 at (2,1).
  - g'(2) = 1/8.
- **Higher order derivatives:**
  - y₂+y = 0.
  - (1−x²)y₂ − xy₁ = 0.
  - Parametric y'' = −1/(2at³).
- **ITF analysis:**
  - Piecewise sin⁻¹(2x/(1+x²)), with the corner ±1 at x = 1.
  - tan⁻¹(2x/(1−x²)) and cos⁻¹((1−x²)/(1+x²)) forms (numerical spot checks).
- **Miscellaneous:**
  - p = −3, q = 2.
  - Σ r·C(n,r) = n2^{n−1}.
  - 1+x+…+x¹⁰⁰ -> f'(1) = 5050 (notes).
- **Determinants:** the determinant derivative.
- **L'Hospital rule:**
  - 1/2.
  - x¹⁰⁰/eˣ -> 0.
  - x^x -> 1.
- **Leibniz rule:** (x−1)/ln x (numerical).
- **Added items:**
  - N1: y = x^y and y = √(x+y).
  - N2: f'(1/2) = 1.
  - N3: a = −5, b = 2, c = 6.
  - N4: −3/32.

## Hindi
- New terms are listed in hindi_glossary_additions.md.
- L'Hospital is written in Devanagari (लोपिताल). ITF is written out (प्रतिलोम त्रिकोणमितीय फलन) in Hindi text.
- The abbreviations LHD and RHD are written inside the mathematics as \text{}, as in the earlier kits.

## Input files used (not modified)
- **chapters/Method_of_Differentiation/Theory.pdf:** theory sheet, 60 pages.
- **chapters/Method_of_Differentiation/XII.pdf:** XII sheet, 142 pages.
  - Exercises: J-I 51 (p2-32), J-II 48 (p33-83), J-M 16 (p84-95), J-A 6 (p96-101), C-I 24 (p102-116), C-II 25 (p117-142).
- **chapters/Method_of_Differentiation/XIII.pdf:** XIII sheet, 151 pages. Only its J-M (25 questions, p84-102) was used.
- **chapters/Method_of_Differentiation/QB.pdf:** JEE Main question bank, questions 131-146 = 16 questions, 13 pages.
- **No DPP** file exists for this chapter.
- **Master prompt list:** .claude/skills/jee-chapter-revision-kit/references/master_index.json.
  - Method of Differentiation, master pages 78-79: 31 prompts in 14 headings.
  - The master PDF is not in the repo; there is no jee-inputs/master_index.json.
