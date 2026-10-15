# Run report - XII_SHEET_CONTINUITY_&_DIFFERENTIBILITY_FCopy_JM (Exercise J-M, 29 questions)

**Blueprint:** none was used. **Concepts self-assigned (no blueprint) - please review.**
**Marks assumed:** the sheet prints no marks, so JEE Advanced defaults were used: 4 marks for every question (Q1-5, Q10-12, Q15-19, Q22-27 single correct; Q6-9, Q13-14, Q20-21, Q28-29 numerical). Stated in the section dividers. Total 116 marks.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.07** (60/29; all questions 4 marks; no equivalence-relation adjustment, no multi-correct floor). These are JEE Main questions, so this is below the Advanced range.
- Levels: Level 1 = 9 (Q1, Q4, Q8, Q11, Q12, Q13, Q22, Q23, Q27); Level 2 = 10 (Q2, Q3, Q5, Q6, Q7, Q9, Q10, Q17, Q24, Q26); Level 3 = 9 (Q14, Q15, Q16, Q18, Q19, Q20, Q25, Q28, Q29); Level 4 = 1 (Q21); Levels 0 and 5 = none. All ratings Medium confidence (anchors for the limit chapters are loose).
- Workbook: `..._difficulty.xlsx` (recalc.py not available; cached values appear when opened in Excel).

## Solutions corrected / written (solution_source)
- **Q4 (corrected)** - PDF swaps the sides (takes the $(1+|\sin x|)^{3a/|\sin x|}$ branch as $x\to0^+$ although it is the $x<0$ piece) and states $\tan2x/\tan4x\to1/2$ without showing it. Answer unchanged.
- **Q6 (corrected)** - PDF gives $g'(x)=4$ on $3<x\le4$; derivative of $4-x$ is $-1$. Conclusion (1 point) unchanged.
- **Q11 (corrected)** - PDF working is garbled and cut off ("Not differentiable at x = -183", should be $x=-1,3$) and never justifies why $|9x^2-12x+4|$ can be dropped; rewritten. Key (C) correct.
- **Q12 (corrected)** - PDF labels the left limit as $f(0^+)$ and has a stray fragment "(9sqrt2, 2)"; fixed. Answer -5 unchanged.
- **Q14 (corrected)** - PDF piece intervals $(-2,-1]$ / $(-1,0)$ put $x=-1$ in the wrong piece (value happens to agree); no continuity check at $-1$. Added. Answer 2 unchanged.
- **Q16 (corrected)** - PDF includes $x=-3$ in the piece $-3\le x<0$, but $f(-3)=0$ so $g(f(-3))=k_2$; isolated point, answer unaffected.
- **Q19 (corrected)** - PDF leaves the middle piece as $[(x-1)^2-1]$ (it is the constant $-1$) and does not test $x=2$ against $f(g(2))=1$. Added.
- **Q21 (corrected)** - PDF part (ii) writes $2(2x-3)^2$ (should be $2(2x+3)^2$) and never checks $x=0$ where $g$ jumps. Fixed; count 62 unchanged.
- **Q26 (corrected)** - PDF factors out $|x-1|$ and concludes "x=1, 4" without justification (bracket still contains $\sin|x-1|$, $|x-4|$; $x=2$ not discussed). Replaced by the even-function/simple-zero argument; answer 2 unchanged.
- **Q28 (corrected)** - PDF assigns $x_0=\frac{2-\sqrt2}{2}$ to the "2" piece, but $h(x_0)=3$ so $f(x_0)=3$ (3 on $(\frac14,x_0]$). Count 3 unchanged.
- **Q29 (corrected)** - PDF counts 39 half-integers (misses -19.5; there are 40) and adds $x=-3/2$ separately although it is a half-integer; the slips cancel, total 79 correct. Fixed.
- No question needed `written`. Kept as `pdf` with small added justification bullets (no error): Q2, Q13, Q15, Q18 (PDF only states the three conditions; reasons why x=1 is always discontinuous added), Q22, Q25, Q8, Q24, Q9, Q10.

## Answer key
All 29 keys (D, B, D, D, B, 1, 4, 39, 5, D, C, B, 14, 2, C, D, B, C, B, 7, 62, A, D, B, B, B, D, 3, 79) agree with my own derivations; checked by sympy (limits Q2, Q12, Q13, Q22, Q24, Q27) and brute-force numerics (Q6, Q7, Q9, Q10, Q14, Q20, Q21, Q26, Q28, Q29). No key is wrong. The English option list of Q11 labels two options "(C)"; the Hindi list shows C = two points, consistent with the key.

## Alternates and results
- Alternates for **22 of 29 questions**: Q2, Q4-Q10, Q12-Q17, Q19, Q20, Q21, Q22, Q24, Q26, Q27, Q29 (note: Q2 and Q22 and Q12 Taylor-expansion vs standard-limit routes, Q13 Taylor, Q15 `max(2x,0)=x+|x|`, Q20 even-symmetry count are milder variants - different technique but short).
- **No alternate (7): Q1** (two joint equations, only one way to impose continuity), **Q3** (one-sided limits are the whole solution), **Q11** (modulus times positive smooth factor - the rule is the solution), **Q18** (statement checking is forced), **Q23** (fix a,b then substitute), **Q25** (three regimes of $x^{2n}$ is the only method), **Q28** (staircase analysis is the method).
- Every question (1-29) has `useful_results`.

## make_ppt.py warnings
- One: "Q27: only 3 solution bullets" - fixed by splitting the PDF's short working into 5 bullets and rebuilt; no remaining warnings. No "could not convert" messages (1120 equations converted; 180 slides).

## Skipped / assumed / guessed
- Only the English text was read (Hindi text ignored). The PDF is bilingual; figures (graphs in Q5-Q10, Q17, Q19, Q28) are described in words, not reproduced.
- No visual rendering check of the deck (no soffice here).
- Question types: Q6-9, Q13-14, Q20-21, Q28-29 treated as numerical-value (no options printed); the rest single correct.
- Difficulty chapter labels: "Limit" for Q2, Q4, Q12, Q13, Q22, Q24, Q27; "Continuity & Differentiability" otherwise. Nearest anchors are loose.
