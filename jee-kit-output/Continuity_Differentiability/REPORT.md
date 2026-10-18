# Continuity & Differentiability: revision kit report

- Items in the Quick Review: 53
- Batch XII: 64 graded questions, High threshold 6 -> High 6, Medium 16, Low 31
  - High items (numbers): [2, 12, 40, 44, 45, 50]
- Batch XIII: 51 graded questions, High threshold 5 -> High 7, Medium 15, Low 31
  - High items (numbers): [2, 12, 29, 40, 42, 45, 50]

## Added items

## Rephrased items
- 7 (original 7): Comment on continuity of $f+g$, $f-g$, $f\cdot g$, $f/g$ if both $f$ and $g$ are continuous at a point.
- 8 (original 8): Comment on continuity of $f+g$, $f-g$, $f\cdot g$, $f/g$ if both $f$ and $g$ are discontinuous at a point.
- 9 (original 9): Comment on continuity of $f+g$, $f-g$, $f\cdot g$, $f/g$ if $f$ is continuous and $g$ is discontinuous at a point.
- 18 (original 18): What are the different types of removable discontinuity and the condition for each?
- 19 (original 19): What are the different types of non-removable discontinuity and the condition for each?
- 21 (original 21): What are the checkpoints for continuity of $f(g(x))$ if the checkpoints for $f$ and $g$ are known?
- 28 (original 28): Write the expressions of LHD and RHD.
- 29 (original 29): Write all the different ways in which LHD and RHD can be written.
- 35 (original 35): Comment on derivability of $f+g$, $f-g$, $f\cdot g$, $f/g$ if both $f$ and $g$ are derivable at a point.
- 36 (original 36): Comment on derivability of $f+g$, $f-g$, $f\cdot g$, $f/g$ if both $f$ and $g$ are non-derivable at a point.
- 37 (original 37): Comment on derivability of $f+g$, $f-g$, $f\cdot g$, $f/g$ if $f$ is derivable and $g$ is non-derivable at a point.
- 42 (original 42): Comment on continuity and differentiability of $x^p\sin\frac1x$, $x^p\cos\frac1x$ at $x=0$ (value $0$ at $x=0$).
- 51 (original 51): How to define $y=\max\{f(t):a\le t\le x\}$ or $y=\min\{f(t):a\le t\le x\}$?

## Questions with no matching item
- J-I:16
- J-II:41
- QB:114
- QB:115
- QB:116
- C-II:17
- C-II:18
- C-II:20

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [117, 118, 119, 120, 121, 122, 123, 128, 129, 130]

## Validation warnings
- none

## Item numbering
- The final numbers 1-53 are the master prompts 1-53, with the same 10 headings in the same order. No item was added.

## Graded counts and High threshold
- **Batch XII:** J-M(XII) 29 + J-A 17 + QB 18 = 64 graded questions.
  - High threshold = max(2, round(0.091 x 64)) = 6.
- **Batch XIII:** J-M(XIII) 26 + J-A 17 + QB 8 new = 51 graded questions.
  - 10 QB questions are J-M(XIII) questions and are counted once.
  - High threshold = max(2, round(4.64)) = 5.
- QB 114, 115 and 116 are counted as graded questions but are mapped "-": two are 3D-lines questions and one is a linear-system question. They are printed under the Continuity & Differentiability heading of the bank.
- **Low items (0 graded questions)** are mostly definition and statement prompts: 1, 3-6, 10-11, 23, 25, 27, 31, 33-34, 38-39, 46-47 and others. No JM, JA or QB question tests these directly. Low means only "not tested in these questions".

## Question Bank overlap (checked by eye on the page images)
- **XIII**, QB -> J-M(XIII): 117->23, 118->24, 119->12, 120->13, 121->14, 122->15, 123->17, 128->25, 129->26, 130->18.
  - The twin questions have identical mappings.
- **XII:** no QB question equals a J-M(XII) question.
- **Rejected:** detect_overlaps.py listed some pairs as "possible". All were checked and rejected because they are different questions:
  - QB 124, 126, 127 against XIII.
  - QB 117, 123, 126, 127 against XII.

## Rephrased items (why)
- **Maths restored:** the saved master index lost or garbled the maths in these prompts. The text was restored from the theory sheet:
  - 7-9 and 35-37: "f+g, f-g, f.g, f/g" read as "ftg", "fig".
  - 42: "x^p sin(1/x)" read as "xPsin(1/x)".
  - 51: "max(f(t), a<=t<=x)" read as "a<t<b".
- **Wording only:** 18, 19, 21, 28 and 29 had small wording fixes.
  - 51: the master's "a < t < b" was read as $a\le t\le x$, as in theory sheet section 3 (uncertain).
- **Unchecked:** the master PDF is not in the repo, so the printed wording could not be checked against the page image.
- **OCR slips corrected:** "ifone", "Whatare", "Howto", "dervable", and the stray "|" at the start of the line.

## Coverage check and the cross-chapter rule
- **No item added.** The six mapping passes found no standard method in a non-Challenger question that no item covers. Borderline cases, with the item each was mapped to:
  - **J-A 11:** "f(a)=0, f derivable, g only continuous => fg derivable at a". Mapped to 37 / 50.
    - The fact is also stated in short-notes section 10.
  - **QB 113:** a telescoping functional relation f(2x)-f(x)=x with lim f(x/2^n) = f(0). Mapped to 52.
  - **Limit evaluation inside "find k" questions:** L'Hospital, 1^inf, expansions. These are covered in Limit and in Method of Differentiation, so they were mapped to item 2 for the continuity step.
  - **Rolle / LMVT parts:** C-I 19 (C, D). These belong to the Application of Derivative chapters.
  - **Monotonicity:** J-A 17. Belongs to the Application of Derivative chapters.

## Questions with no matching item (why)
- **J-I 16:** invertibility of (b-x)/(1-bx). Functions chapter.
- **J-II 41:** number of integers in the range of a piecewise GIF function. Functions chapter.
- **QB 114, 115, 116:** 3D lines (two questions) and a linear system. They are misplaced in the bank.
- **C-II 17, 18, 20:** paragraph parts that are a trig equation, a pure limit and a range question.

## Uncertain decisions and notes
- **Exercise names:** the sheets print "Exercise J-1 / J-2 / C - I / C - II", and the J-1 / J-2 forms are not found by extract_questions.py's default patterns. The script was run with a --patterns file that also accepts 1 and 2. The skill was not changed.
- **Counts:** J-I 23, J-II 61, J-M(XII) 29, J-A 17, C-I 23, C-II 23, J-M(XIII) 26, DPP-1 19, DPP-2 18, DPP-3 14, DPP-4 13, QB 18 (numbered 113-130) = 284 questions.
  - The contents pages give page numbers only, not question counts.
  - In every region the numbering is continuous, and the last number agrees with the PDF text.
- **Images:** the text layer garbles almost every stem, so every question was read from the page images. Six parallel mapping passes were used.
  - XII pages were readable everywhere; there were no blank equation boxes this time.
- **Reference sheet:** XIII has the same J-I / J-II / J-A / C-I / C-II as XII. Per the skill, only XIII's J-M was used; the other exercises come from the XII sheet.
- **Multi-part questions:** paragraph, match-the-column and multi-statement questions are mapped once, by their dominant concept, with up to 3 "also used" items. These are:
  - J-II 4, 6, 9, 29, 30, 37-41, 56, 58-61.
  - J-A 3, 7, 9, 16.
  - C-I 1.
  - C-II 21-23.
- **Main uncertain mapping choices:**
  - J-I 4 -> 9 (could be 12).
  - J-I 13 -> 40.
  - J-I 22 and J-II 34 -> 29 (could be 52).
  - J-II 22 and J-II 52 -> 44 (could be 30).
  - J-II 31 -> 32;12.
  - J-II 43 -> 29.
  - J-II 55 -> 12.
  - J-A 2 -> 50 (could be 42).
  - J-A 5 -> 49.
  - J-A 14 -> 10 (mostly counting).
  - "count m discontinuities and n non-derivable points" (XII JM 15, XIII JM 7, QB 127) -> 40;12,45.
  - [g(x)] non-derivability (XII JM 28, XIII JM 8) -> 40;14.
  - XIII JM 18 / QB 130 -> 52;29.
  - DPP-2:5 -> 21.
  - DPP-3:5 -> 43.
  - DPP-4:10 -> 49.

## Source errors / oddities found
- **Printed answer or solution wrong:**
  - **J-II 31:** the printed answer "continuous but not derivable at √2" looks wrong. For 1<x<2 the degree is constantly 2, so f is constant near √2, and so continuous and derivable there. The solution only repeats the answer.
  - **J-II 61:** the solution is incomplete and garbled; it ends "π00" and part (D) is not worked. The printed answer (A) PQRST includes x = ±π, yet the solution shows LHL ≠ RHL there.
  - **J-A 17:** two answers are printed, "Ans. C" (official) and "By Matrix B". The Matrix argument (f increasing on the left and decreasing on the right of 0) is wrong: f' oscillates in sign near 0+. C is correct.
  - **C-II 11:** the printed answer and solution analyse f, not f(f(x)). The correct result for f(f(x)) is continuous but not derivable at x=1, and discontinuous at x=2 and at x=3. This was found during mapping and is worth a teacher's check.
  - **C-II 21 (C):** max({x+1},{5-x}) is even with period 1, so T also fails. The answer should probably be C -> P only.
  - **DPP-4:12:** the Ans line is blank and the solution is wrong. The correct g = min f(t) stays 6 up to x = (9-√21)/2 ≈ 2.21, and g is not derivable there, not at x=1. This was found during mapping and is worth a teacher's check.
  - **DPP-3:2:** the reasoning for option (D) is wrong. f(1) = cos 2π = 1, but LHL = -1, so (D) is false. The printed answer C stands.
  - **DPP-4:6:** the solution drops the factor 1/2 and ends "= 4". The printed answer 2 is correct.
  - **J-II 53:** the solution says jump = 1 and then calls (C) correct, but (C) states 1/2. The printed BD is right.
- **J-M(XIII) 2:** printed answer "Drop" (officially dropped). The solution gives 10, which is option (B).
- **J-M(XII) 11:** options are labelled A, B, C, C, and the solution says "x = -183" (garbled). It should be x = 3, -1, giving Ans C.
- **Wrong working, correct answer:**
  - J-I 12: f(0-) and f(2+) are wrong in the solution.
  - J-I 23: uses L'Hospital without justification.
  - J-II 13: expands e^{nx} inside an n -> ∞ limit.
  - J-II 22: claims the one-sided derivatives are ±∞; they are ±π/2.
  - J-II 25: the x<0 piece should be -x.
  - J-II 30: f'(0-) for a>1 should be -1.
- **Typos (answers unaffected):**
  - J-II 42: x ≤ -π/2.
  - J-II 58(A): f(3±h²).
  - J-II 59(B): -2x+2.
  - XII JM 29: count 39+39+1.
  - XIII JM 13 / QB 120: f'(x)<0.
  - XIII JM 19: the +2b is dropped.
  - XIII JM 26 / QB 129: e^{b/a}.
  - C-I 10: the solution ends with (D) where Ans is C.
  - C-I 18: the solution ends with (A) where Ans is AC.
  - C-I 22: should read x ≤ -1.
  - C-II 7 and C-II 13: sign slips.
  - DPP-1:4, 6, 8: limit labels.
  - DPP-2:16: LHL and RHL swapped.
  - DPP-2:15: "ND" should be ∞.
  - DPP-4:13: piece domain mistyped.
- **Incomplete solutions:**
  - C-I 3: the solution is cut off.
  - C-II 23: parts (C) and (D) are missing; the printed answers were checked and are right.
  - DPP-4:3: the solution is only a hint.
  - DPP-4:5: the solution is blank.
  - DPP-2:11: the Ans line is blank.
- **Theory sheet:**
  - In the "type of discontinuity" examples (1/cosec x, x sin(1/x), e^{-tan²x}), "f(0) = Not differentiable" should read "not defined".
  - Section 1.2 example 5 (theory p.30): the text layer shows a = 1/4. The page image shows a = -1/4, which is used and verified.

## Examples verified with sympy
Every Ex line was checked with sympy (scratch script checks.py):
- **Continuity at a point:**
  - k = 4.
  - √x at 0⁺: limit 0.
  - sin⁻¹x at 1⁻: π/2.
  - [x]+[-x] at 0: limits -1, value 0.
  - [x] at 1: limits 0 and 1.
  - [x]{x} at 1: 0, 0, 0; at 0: limits -1 and 0.
  - x[x] at 0: 0, 0; at 1: 0 and 1.
- **Intervals and special functions:**
  - sgn(x-2)+[x-1/2]+[ln x] on [1,3]: jumps exactly at 3/2, 2, 5/2, e (numerical).
  - x²+6 = 5x gives x = 2, 3.
  - [sin x] at π/2.
  - Built-in limit: a = 0, b = 1.
- **Types of discontinuity:**
  - (x²-4)/(x-2) -> 4.
  - tan⁻¹(1/x) -> ±π/2.
  - |sin x|/x -> ±1.
  - [x]/x at 2: 1 and 1/2.
  - f(f(x)) = (x-1)/x for f = 1/(1-x).
- **Theorems:**
  - x³+x-1 at 0, 1: -1 and 1.
  - (x-1)(x-3)-(x-2)(x-4) at 2, 4: -1 and 3.
- **Derivability:**
  - |x| at 0: one-sided derivatives -1 and 1.
  - a = -1/4, b = 1.
  - √x at 0: RHD ∞; x^{3/2} at 0: RHD 0.
  - [x] at 1: RHD 0.
  - (x+1)|x| at 0: 1 and -1.
  - x² sin(1/x): f'(0) = 0.
  - 9 = 9 and f'(1⁺) = 450.
  - Item 48 piece at 1: value 2, slope -1.
  - (x²-1)|x²-3x+2|: derivable at 1 (both slopes 0); at 2 the slopes are ±3.
  - ||x-1|-1|: corners at 0, 1, 2.
- **Functional equations:**
  - f = x²+4x+1 satisfies the rule identically.
  - f = 3 ln x satisfies f(xy) = f(x)+f(y).

## Hindi
- New terms are listed in hindi_glossary_additions.md.
- The abbreviations IMVT, LHL, RHL, LHD and RHD are written inside the mathematics as \text{}, as in the Limit kit.

## Input files used (not modified)
- chapters/Continuity_Differentiability/Theory.pdf (theory sheet, 34 pages)
- chapters/Continuity_Differentiability/XII.pdf: XII sheet, 157 pages.
  - Exercises: J-1 23, J-2 61, J-M 29, J-A 17, C-I 23, C-II 23.
- chapters/Continuity_Differentiability/XIII.pdf: XIII sheet, 161 pages. Only its J-M (26 questions, pages 65-86) was used.
- chapters/Continuity_Differentiability/DPP.pdf: Special DPP on Continuity & Differentiability # 1-4, 19 + 18 + 14 + 13 = 64 questions, 50 pages.
- chapters/Continuity_Differentiability/QB.pdf: JEE Main question bank (Differential Calculus, Continuity & Differentiability), questions 113-130 = 18 questions, 16 pages.
- Master prompt list: .claude/skills/jee-chapter-revision-kit/references/master_index.json.
  - Continuity & Differentiability, master pages 76-77: 53 prompts in 10 headings.
  - The master PDF is not in the repo; there is no jee-inputs/master_index.json.
