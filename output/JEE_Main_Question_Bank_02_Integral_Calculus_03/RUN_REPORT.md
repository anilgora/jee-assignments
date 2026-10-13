# Run report - JEE_Main_Question_Bank_02_Integral_Calculus_03

Paper: `papers/JEE_Main_Question_Bank_02_Integral_Calculus_03.pdf` (17 pages, Matrix JEE Academy; 20 single-correct questions with printed solutions, English + Hindi). Printed numbers are 41-60; deck numbers are 1-20 (deck Qn = printed Q(n+40)).
Files: `_Analysis.pptx` (126 slides), `_content.json`, `_ratings.json`, `_difficulty.xlsx`, this report.

## Blueprint and marks
- **Concepts self-assigned (no blueprint) - please review.** No blueprint was used.
- No marks printed. Assumed **4 marks per Single Correct question**, no negative marking (stated in the section divider). Total 80 marks.

## Difficulty
- **Marks-weighted difficulty index: 1.95** (equal marks; no equivalence-relation or multi-correct adjustments apply).
- Level 1: 5 (Q2, Q5, Q12, Q15, Q16); Level 2: 12 (Q1, Q3, Q4, Q8, Q9, Q10, Q11, Q13, Q14, Q17, Q18, Q20); Level 3: 3 (Q6, Q7, Q19); Levels 0, 4, 5: none.

## Solutions whose source is corrected
- Q8 (printed 48): working g(alpha)=pi/12 (constant) is right, but the PDF never examines the options. The question asks which statement is INCORRECT and the key says (A); for a constant function (A) "even" is TRUE and (B), (C), (D) are all incorrect. Option verdicts added; see answer-key note.
- Q9 (printed 49): PDF writes y-3x (in the DE and the final line) and dt/dx = dy/dx - 3; the question has y+3x, so t = y+3x and dt/dx = dy/dx + 3. Method and result unchanged; answer (B) right.
- Kept as `pdf` with small notes (typos only): Q10 (printed 50) has stray limits/"ds" typos and a missing $\sqrt{}$ simplification step, written out; Q1 (printed 41), Q4, Q7, Q11, Q13 extended with the PDF's skipped lines (f(3)=2 derivation, simplifications).

## Solutions whose source is written
- None.

## Answer key
- All 20 keys verified (mpmath numerical integration / sympy; DE solutions checked by substitution). All keys correct except as noted below.
- **Q8 (printed 48): key (A) looks wrong for the wording "incorrect".** g is constant = pi/12, so (A) is the only TRUE statement and (B), (C), (D) are all incorrect - the question has no unique answer as worded; key (A) fits a "which is correct" wording. The answer box says so.
- Q10 and Q17 fine; Q17 asks for "a possible choice" (f is determined up to a constant; only (B) has the right derivative).

## Alternates
- Given for 19 of 20 questions (all except Q11).
- **No alternate:** Q11 (printed 51): after [x]=1 and x^3=t the only route is summing a G.P. over unit intervals; telescoping the G.P. is the same computation reworded.
- Weaker alternates (flagging for review): Q6 (substitution u = tan x sin 3x is the same idea as the exact-derivative recognition), Q14 (definite integral from 2 to 4 instead of finding C), Q17 (testing the options' derivatives, a check not a derivation), Q9 (inverse-function view of the same separation), Q8 (explicit g(0)=g(1) check rather than a derivation).
- Useful results: all 20 questions have `useful_results`.

## make_ppt.py warnings
- First build crashed (control character): two concept strings were not raw strings in my generator script and `\f`/`\t` were turned into control characters; fixed by making them raw. Final build: no warnings; 769 equations converted to native PowerPoint equations; no "could not convert" notes.

## Skipped / assumed
- No rendering or thumbnails (no soffice); the deck was not visually inspected. Hindi text not transcribed.
- Concepts and levels are my own judgement (Medium confidence; the rubric's anchors are Advanced-level, so for this Main-level bank I placed questions relative to the lowest anchors).
- Numbering: deck numbers 1-20 differ from printed 41-60; the question text itself does not show printed numbers.
