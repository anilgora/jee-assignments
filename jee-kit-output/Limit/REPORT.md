# Limit: revision kit report

- Items in the Quick Review: 62
- Batch XII: 59 graded questions, High threshold 5 -> High 12, Medium 26, Low 24
  - High items (numbers): [16, 20, 25, 28, 30, 33, 34, 38, 42, 54, 57, 58]
- Batch XIII: 49 graded questions, High threshold 4 -> High 13, Medium 24, Low 25
  - High items (numbers): [16, 20, 26, 27, 28, 33, 34, 38, 42, 46, 54, 57, 58]

## Added items
- 62: How to find a geometrical limit (length or area of a figure as an angle $\to0$ or $n\to\infty$)?  [source: J-II:37 (theory sheet 10.2)]

## Rephrased items
- 31 (original 31): What is the value of limit $\lim_{x\to a}\dfrac{x^n-a^n}{x-a}$?
- 34 (original 34): What is the value of limit $\lim_{x\to0}\dfrac{1-\cos x}{x^2}$?
- 35 (original 35): What is the value of limit of $x^p\sin\frac1x$, $x^p\cos\frac1x$ as $x\to0$?
- 43 (original 43): Write result of $f'(x)$, $f''(x)$, $f'''(x)$, $f''''(x)$ as limits.

## Questions with no matching item

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [98, 99, 100, 101, 102, 103, 104, 105, 106, 110, 111, 112]

## Validation warnings
- none

## Item numbering
- Final numbers 1-61 = master prompts 1-61 (same headings, same order). Final 62 = added item N1 (geometrical limits), placed at the end of "Miscellaneous".
- Master prompt 54 ("How to find limit when numerator and denominator are expressed as expansion of x") sits under the heading "Limits of Composite Function" in the saved master index (probably a column slip in the scan). It was kept where the index puts it, so that the master order is unchanged.

## Graded counts and High threshold
- Batch XII: J-M(XII) 22 + J-A 14 + QB 23 = 59 graded; High threshold max(2, round(0.091 x 59)) = 5.
- Batch XIII: J-M(XIII) 24 + J-A 14 + QB 11 new = 49 graded (12 QB questions are J-M(XIII) questions, counted once); High threshold max(2, round(4.46)) = 4.
- The graded sets are small, so High needs only 4-5 questions. The Low items (0 graded questions) are mostly definition and "what to keep in mind" prompts (1, 3, 6-9, 12-13 and others). No JM, JA or QB question tests these directly.

## Question Bank overlap (checked by eye on the page images)
- XIII: QB -> J-M(XIII): 98->19, 99->20, 100->21, 101->12, 102->14, 103->15, 104->16, 105->7, 106->8, 110->22, 111->23, 112->24.
  - detect_overlaps.py marked 102 only as "possible" and missed 106; both pairs have the same stem and answer.
- XII: no QB question equals a J-M(XII) question. QB 107 is similar to J-A 1 but is not the same question.

## Rephrased items (why)
- 31, 34, 35, 43: the saved master index lost the mathematics in these prompts ("What is the value of limit lim ? x-a", "1-cos x ... lim", "x? sin(1/x)", "f'(x), f"(x) ..."). The formulas were restored from the theory sheet (3.1, 3.2, section 4). The master PDF is not in the repo, so the printed wording could not be checked against the page image.
- Prompt 30 ("What to replace if (s^n - 1) appears") is answered as in theory sheet 3.1: s -> 1 gives s^n - 1 ~ n(s - 1).
- Other prompts: only OCR slips were corrected ("ofa", "Howto", "fig" -> f+g, "co -co" -> infinity - infinity, "trigonometrix").

## Coverage check and the cross-chapter rule
- Added N1 (geometrical limits): the theory sheet has this as section 10.2, but no master prompt covers it. search_master.py found no match for "geometrical limit". Questions: J-II 37 (non-Challenger) and C-II 17, 18, 19, 26, 27, 28 (Challenger).
- Not added, because another chapter covers them:
  - Telescoping sums and products before n -> infinity: covered in Sequence & Progression, "Miscellaneous Sequence Type 3" (method of difference, prompts 48-49) and "Miscellaneous" (continued product form, prompt 55).
    - Questions: J-I 9, DPP-1 13, DPP-2 10, DPP-2 14 (mapped to 26, n -> infinity simplification), plus J-II 8, J-II 16, J-M(XII) 13, J-A 10, J-M(XIII) 7, QB 105, QB 108 (mapped to the item for their limit step).
  - L'Hospital's rule: covered in Method of Differentiation, "L'Hospital Rule". Several printed solutions (J-I 13, C-II 8, J-M(XIII) 22) use it; these were mapped to the item for the form instead.
  - Definite integral as a limit of a sum: covered in Definite Integration.
- Loose fits, recorded but not added (uncertain):
  - Bounded function divided by a quantity tending to infinity (sin x / x as x -> infinity; DPP-1 16, DPP-4 8, DPP-4 21) was mapped to 35. Sandwich (50) would also fit.
  - Trigonometric transformation to cancel the zero factor (J-A 9, J-M(XII) 11) was mapped to 16 / 57.
  - Product of cosines cos(x/2)cos(x/4)...cos(x/2^n) (DPP-2 6, C-II 3, 10, 14) was mapped to 33.

## Questions with no matching item
- None is mapped "-". Questions that are hardly limit questions were mapped to their one limit step (uncertain):
  - J-M(XII) 19: functional equation, mapped to 60.
  - QB 96: functional equation, then a finite limit, mapped to 58.
  - J-A 4: mostly range and composition, mapped to 33.
  - J-II 40: number of solutions of e^(-x^2/2) = x^2, mapped to 42.
  - J-II 54: properties of cos(sin x), mapped to 14.
  - J-M(XII) 4: finite sum, mapped to 14.

## Uncertain decisions and notes
- extract_questions.py did not find J-I, J-II, C-I or C-II, because the sheets print "Exercise J-1 / J-2 / C-1 / C-2". It was run with a --patterns file that also accepts 1 and 2; the skill was not changed.
  - Counts: J-I 36, J-II 58, J-M(XII) 22, J-A 14, C-I 29, C-II 34, J-M(XIII) 24, DPP-1 18, DPP-2 20, DPP-3 13, DPP-4 21, DPP-5 23, QB 23 (numbered 90-112 in the bank) = 335.
  - The contents pages give no question counts. In every region the numbering was checked to be continuous, and the last number agrees with the PDF text.
- The text layer garbles almost every stem, so every question was read from the page images during mapping.
- In XII.pdf every equation from page 119 onwards (C-II 13-34) is printed as a blank grey box. These questions were read from the same Challenger set in XIII.pdf (pages 120-140).
- XIII has its own exercises, but per the skill only its J-M was used. All other exercises come from the XII (reference) sheet.
- Multi-part and match-the-column questions are mapped once, by their dominant concept, with up to 3 "also used" items:
  - DPP-1 3: 9 parts.
  - J-II 4, 19, 22, 52, 56, 57, 58.
  - C-I 18, 25, 26.
- Mapping is judgement. The main uncertain choices:
  - J-I 13 -> 16 (could be 43).
  - J-I 21 -> 9 (the base is exactly 1).
  - J-II 9 -> 25.
  - J-II 13 -> 20.
  - J-M(XIII) 1 -> 26;59.
  - J-M(XIII) 4 -> 49;34.
  - J-M(XIII) 15 / QB 103 -> 50;46.
  - J-M(XIII) 22 / QB 110 -> 21;20.
  - J-A 3 -> 58.
  - J-A 13 -> 61;33.
  - C-II 1 -> 1 (recursive sequence; no item fits; Challenger).
  - C-II 12 -> 27.
  - DPP-4 2, 3, 10, 12, 13, 14, 16.
- Hindi uses $\text{LHL}$ / $\text{RHL}$ inside the mathematics (they are standard abbreviations). "JEE" appears once in the Hindi answer to item 5.

## Source errors / oddities found
- J-M(XIII) 16 = QB 104, lim_{x->12} (|x|^3/12 - [x/12]): LHL = 144 but RHL = 143, so the limit does not exist. The printed answer 144 (and the solution) ignore the RHL.
- QB 94: the solution shows both statements true (option C), but the printed answer is B.
- J-A 3: the answer is printed as 0, with a remark that a = 2 may also be accepted (a JEE 2014 ambiguity).
- J-I 9: the printed solution is the one for J-I 11.
- J-II 17: the printed solution belongs to J-II 19(b); the answer 0 is still correct.
- J-II 1: no solution is printed.
- J-II 16: the exponent in the solution should be 2^(n+1) - 1; the answer is unaffected.
- J-II 41-43 solution: the parts are labelled 4, 5, 6.
- J-II 37: the last step drops an x.
- J-II 49: the solution's denominator should be 3x - 6.
- C-I 3: the solution ends "a = 26"; it should be 36.
- C-I 21: the printed solution belongs to another question.
- C-I 29: the solution ends "L = 1/16"; it should be 1/64, which matches the printed answer.
- DPP-5 11: the last line of the solution reads e^{1/2} = √3 (typo). The answer B (√e) is right.
- J-M(XIII) 20 = QB 99 and J-M(XIII) 24 = QB 112 have small typos in the stem; the answers are unaffected.
- Theory sheet 1.2, Ex.1 (sgn x at 0): the text layer shows "LHL = 1, RHL = 1" (a lost minus sign). The kit uses LHL = -1, RHL = 1.

## Examples verified with sympy
Every Ex line was checked with sympy (scratch script checks.py):
- (x²-4)/(x-2) -> 4; sgn at 0: -1, 1; sin⁻¹x at 1⁻: π/2; sin x/x + eˣ -> 2.
- Factorisation and rationalisation:
  - (x²-2x-3)/(x²-4x+3) -> 2; (x⁴-3x+2)/(x⁵-4x+3) -> 1; 1/(x-1) - 3/(x³-1) -> 1.
  - (√(1+x) - √(1-x))/x -> 1; √(x²+x) - x -> 1/2; ((1+x)^{1/3} - 1)/x -> 1/3; eˣ(√(1+x) - 1)/x -> 1/2.
- Substitution and infinity/infinity: √(x²+1)/x at -∞ -> -1; x sin(1/x) -> 1; (π/2 - x)tan x -> 1; (2x²+3x)/(5x²-1) -> 2/5.
- Standard limit type 1: ((1+x)^{1/7} - 1)/(x⁴+4x) -> 1/28; (x^{1/9} - 1)/(x²-3x+2) -> -1/9; (x⁵-32)/(x-2) -> 80.
- Trigonometric:
  - sin 2x/sin 3x -> 2/3; sin x²/(x tan 2x) -> 1/2; (1 - cos 4x)/x² -> 8; x² sin(1/x) -> 0.
  - tan⁻¹2x/sin⁻¹3x -> 2/3; cos⁻¹(1-x)/√x -> √2.
- Exponential and logarithmic: (eˣ - e³)/(x-3) -> e³; (5ˣ - 3ˣ)/x -> ln(5/3); ln(1+3x)/x -> 3; ln x/(x-1) -> 1.
- 1^∞: (cos x)^{1/x²} -> e^{-1/2}; (1 + tan²√x)^{5/x} -> e⁵.
- Special signs and sandwich: sin x/|x|: LHL -1; x[1/x] -> 1; Σ[kx]/n² -> x/2 (numerical); Σ1/√(n²+r) -> 1 (numerical).
- Expansions and constants:
  - (x⁷+3x³)/(x⁵-2x³) -> -3/2; (cos x - 1)(cos x - eˣ)/x³ -> 1/2.
  - The four standard limits 1/6, 1/3, 1/2, -1/2.
  - a = c = 1, b = 2 gives a + b + c = 4 with limit 2.
- Miscellaneous: ln(sin x/x) -> 0; x¹⁰e^{-x} -> 0; x ln x -> 0⁺; lim xⁿ/(xⁿ+1) = 0, 1/2, 1; geometric A/B -> 2.

## Hindi
- New terms are listed in hindi_glossary_additions.md.

## Input files used (not modified)
- chapters/Limit/Theory.pdf (theory sheet, 51 pages)
- chapters/Limit/XII.pdf: XII sheet, 140 pages.
  - Exercises: J-I 36, J-II 58, J-M 22, J-A 14, C-I 29, C-II 34.
- chapters/Limit/XIII.pdf: XIII sheet, 142 pages.
  - Only its J-M (24 questions) was used, plus its C-II pages to read C-II 13-34, whose equations are blank in XII.pdf.
- chapters/Limit/DPP.pdf: Special DPP on Limit # 1-5, 18 + 20 + 13 + 21 + 23 = 95 questions, 64 pages.
- chapters/Limit/QB.pdf: JEE Main question bank (Differential Calculus, Limit), questions 90-112 = 23 questions, 19 pages.
- Master prompt list: .claude/skills/jee-chapter-revision-kit/references/master_index.json.
  - Limit, master pages 73-75: 61 prompts in 25 headings.
  - The master PDF is not in the repo; there is no jee-inputs/master_index.json.
