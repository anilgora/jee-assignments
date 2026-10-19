# Solution of triangle: generation report

Blueprint: `qp_blueprints/Solution_of_triangle.xlsx`. There is no `Solution_of_triangle_config.xlsx`, so the check ran without `--config`.
This scheduled run made the paper on 19-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy, mpmath and python-docx were missing for `python3`. I installed them with `python3 -m pip install pandas openpyxl sympy mpmath python-docx`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- `build_paper.py --blueprint` passed with **no errors and no warnings** on the first build. No script was edited and no check was weakened.
- I rendered page 1 of each of the three PDFs and looked at them. The Hindi is shaped and the equations are typeset in 2D. This paper has no paragraph question.

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the blueprint has only Single Correct and Numerical types and nothing above level 3.
- **Paper:** 14 questions (blueprint Sr No 721-734): 4 Single Correct (Q1-Q4), then 10 Numerical (Q5-Q14).
- **Reorder (`--reorder`):** the rows were not in type order, so they were renumbered (old Sr No -> new Q):
  721->1, 723->2, 724->3, 727->4, 722->5, 725->6, 726->7, 728->8, 729->9, 730->10, 731->11, 732->12, 733->13, 734->14.
- **Answer Plans:** the blueprint had none, so the script drew all 14. Every answer matches its plan; the build checks this.
  - Q1 Option C; Q2 Option A; Q3 Option B; Q4 Option D; Q5 positive 2-digit integer; Q6 negative decimal; Q7 negative integer; Q8 positive decimal;
    Q9 decimal between 0 and 1; Q10 positive 3-digit integer; Q11 negative integer; Q12 positive 2-digit integer; Q13 negative decimal; Q14 decimal between 0 and 1.
- **Cells containing ";":** none.
- **Warnings.** I recorded these and did not fix them, because the blueprint is your decision. There were no errors, and the blueprint file was not edited.
  - Q5 (old row 722) lists 4 concepts in a Main paper. Kept as given; the question uses all 4.
  - Concepts repeated across rows: "Sine Law" (Q1, Q5, Q6, Q8), "Cosine rule" (Q2, Q5), "Half angle formula" (Q5, Q7), "Inradius and incenter based questions" (Q5, Q10), "Orthocenter and Pedal triangle" (Q11, Q14). Each use has a different mechanism, and no setup is reused.

## Answers
| Q | Type | Answer | Level (target) |
|---|---|---|---|
| 1 | SCQ | (C) | 3 (3) |
| 2 | SCQ | (A) | 3 (3) |
| 3 | SCQ | (B) | 3 (3) |
| 4 | SCQ | (D) | 2 (2) |
| 5 | Num | 48 | 3 (3) |
| 6 | Num | -0.25 | 2 (2) |
| 7 | Num | -40 | 2 (2) |
| 8 | Num | 1.28 | 2 (2) |
| 9 | Num | 0.75 | 3 (3) |
| 10 | Num | 336 | 2 (2) |
| 11 | Num | -2 | 3 (3) |
| 12 | Num | 12 | 3 (3) |
| 13 | Num | -0.5 | 3 (3) |
| 14 | Num | 0.24 | 2 (2) |

I recomputed every answer in Python with sympy, separately from the written solutions. Q1: the relation checked at several angles, and the three wrong options shown to fail. Q2: coordinates of C and D, with BD = 17 and tan of the angle. Q3: the 3 : 4 : 2 triangle. Q4: the angle between the vectors directly. Q5: CI as a function of the scale. Q6: solved for c. Q7: a real triangle with b + c = 15, bc = 52. Q8: both values of c (25 and 7). Q9: E and F found, then the circumradius from the side lengths. Q10: Heron. Q11: rebuilt B(6,4) and C(-3,-5), and H checked as A + B + C - 2O. Q12: coordinates A(-1,3). Q13: the bisector length solved for AC, and D checked on the bisector. Q14: the excentres' coordinates.

## Level distribution and index
- Level 2: 6 questions (Q4, Q6, Q7, Q8, Q10, Q14). Level 3: 8 questions (Q1, Q2, Q3, Q5, Q9, Q11, Q12, Q13).
- Marks-weighted index (SCQ 3 marks, Numerical 4 marks): **2.56**. No question is about equivalence relations, and there is no MCQ, so neither adjustment applies.
- **No question is one level off its target.** Each rated level equals the blueprint level.
- Consistency pass: I sorted the questions by level and compared neighbours. Q10 (incircle/excircle touch points) and Q7 are the hardest Level 2s. Q3 (Napier's analogy plus the half-angle identity) is the easiest Level 3 and is close to 2. Q12 and Q13 are the hardest Level 3s. Most ratings are Medium confidence, because the anchor bank has few Solution of Triangle questions (nearest anchors: 2021-P1-Q18 at L2, 2021-P2-Q2 at L3, and 2021-P1-Q1 at L3 for the coordinate questions).

## Originality report
The web checks used web search. I searched each question's distinctive structure in words and symbols. Perfect novelty cannot be guaranteed. Please tell me if you recognise any question.

| Q | Mechanism | Web check | Standard ingredient |
|---|---|---|---|
| 1 | B - C = π/2 parametrised by C = θ; sine law gives sides k cos 2θ, k cos θ, k sin θ; eliminating θ gives (b²-c²)² = a²(b²+c²). | ingredient only | **yes**: the identity (b²-c²)/a² = sin(B-C)/sin A is a textbook result, and the relation follows from it quickly |
| 2 | Second triangle ABD across AB, fixed by AD and ∠CAD = 90°; BD comes from the complement angle; tan∠CBD is the tan of a sum (obtuse). | not found | cosine rule on a common base |
| 3 | tan(A/2) recovered from tan(B/2)tan(C/2), xy+yz+zx = 1 and Napier's analogy as a small system; then tan((B-C)/2). | not found | Napier's analogy exercises |
| 4 | Triangle given by 3D position vectors; the cevian point given as (b+2c)/3; cot B and cot C from dot products; m-n theorem. | not found | m-n theorem |
| 5 | Sine ratio fixes the shape; the vertex-to-incentre distance CI = (s-c)/cos(C/2) fixes the scale. | not found | incentre distance formula |
| 6 | The projections c cos B and b cos C given separately with sin B = 2 sin C; projection formulae used three times. | not found | a(b cos C - c cos B) = b²-c² is a textbook identity |
| 7 | Incircle data (r, AF) give tan(A/2) = r/(s-a); the t-formulae give sin A and cos A; the area gives bc; the answer needs only bc and cos A. | not found | r = (s-a) tan(A/2) |
| 8 | Ambiguous case: the two angles C are π-A-B₁ and B₁-A, so the sum of their sines is 2 sin B₁ cos A. | not found | c₁+c₂ = 2b cos A type results |
| 9 | The circle on BC (diametric form) meets the sides at the feet of altitudes, so the circumcircle of AEF is the circle on AH. | not found | **yes**: AEF ~ ABC with ratio cos A, circumradius R cos A (pedal-triangle fact) |
| 10 | The distance between the incircle and A-excircle touch points on BC is \|b-c\|; with r r₁ = (s-b)(s-c) and r₁/r = s/(s-a). | not found | r r₁ = (s-b)(s-c) |
| 11 | Foot of the altitude from A recovered from A, O, H: G on the Euler line, then the midpoint of BC, then BC ⟂ AH. | not found | G divides OH in 1:2 |
| 12 | PQ between the feet of the internal and external bisectors (harmonic conjugates) gives AB : AC = 1 : 3; the median length fixes the scale. | not found | Apollonius median formula |
| 13 | The bisector of the obtuse angle between two given lines gives cos(A/2); the bisector-length formula is solved for AC. | not found | bisector equations and bisector length |
| 14 | ABC is the pedal triangle of its excentral triangle; the pedal area ratio 2 cos cos cos becomes r/(2R). | ingredient only | **yes**: "incentre = orthocentre of the excentral triangle" and "area of the excentral triangle = 2Rs" are known results |

## Problems found while verifying
- **Q1 redesigned after the web check.** The first design (∠B = 3∠A, giving a c² = (a+b)(b-a)²) turned out to be a published problem (a Socratic answer, "if α = 3β prove (a-b)²(a+b) = bc²"). I replaced it with the ∠B - ∠C = π/2 version. The search found only the general identity for that version, not the problem.
- Q14: my first full-solution draft had a wrong coordinate check (wrong excentres). I recomputed the excentres as (0,-6), (5,4), (-5,4), giving Δ₂ = 50 and 12/50 = 0.24, and corrected the line before the build.
- Q12: a web-search summary said PQ and AD alone do not fix the area. That is true, but the stem also gives BC = 8, and with it the area is fixed. Both k = 1/3 and k = 3 give area 12.
- Stem review (a self-check; an independent reader may still find things): in Q14 I replaced a worded fraction inside the maths with Δ₁ / Δ₂, defined in words in both languages. In Q9 I state F ≠ B and E ≠ C so that the points are unique. In Q13 the obtuse condition fixes which side of A the point C lies on.

## Rows whose concepts were hard to combine naturally
- **Q5 (old row 722, four concepts):** all four are used in one chain (sine law, then cosine rule, then half-angle formula, then the incentre distance). The cosine rule and the half-angle formula give the same cos(C/2) by two routes, so one of them is partly redundant.
- **Q4 (m-n theorem + position vectors):** the direct vector route (the angle between DA and DC) gives the answer without the m-n theorem. The m-n theorem is the intended route, but a student can bypass it.
- **Q13 (bisector length + angle bisectors):** a pure coordinate route (D divides BC in the ratio 2 : 1) is also available.

## Notes
- The Hindi is my own translation. Please review the specialised terms (अन्तःकेन्द्र, बाह्यकेन्द्र, बाह्यवृत्त, लम्बकेन्द्र, परित्रिज्या, आन्तरिक/बाह्य समद्विभाजक, असर्वांगसम).
- `_source/` holds `blueprint.json`, `meta.json` and `q01.json`-`q14.json`. To fix a question, edit its JSON and rerun `build_paper.py`.
- Web-search sources consulted include socratic.com/answers/601023 (the B = 3A problem), allen.in/dn/qna/130349 (the (b²-c²)/a² identity), and repository.unri.ac.id (excentral triangle area ratio).
