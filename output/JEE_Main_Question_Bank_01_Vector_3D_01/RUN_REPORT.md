# RUN REPORT - JEE_Main_Question_Bank_01_Vector_3D_01

Paper: 20 single-correct questions (Vector 3D), deck numbers 1-20 (same as printed numbers).

## Difficulty
- Marks-weighted difficulty index (adjusted levels): **1.75** (140 / 80 marks). No equivalence-relation adjustment or MCQ floor applied (all questions are single correct).
- Questions per level: Level 0: 1 (Q3) | Level 1: 6 (Q1, 2, 8, 9, 10, 16) | Level 2: 10 (Q4, 5, 6, 7, 12, 13, 14, 15, 17, 20) | Level 3: 3 (Q11, 18, 19) | Levels 4 and 5: none.
- Ratings are Medium confidence except where noted High in the ratings file; this is a JEE Main-style bank, so the index sits well below the JEE Advanced range.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed in the paper): JEE Advanced default for single-correct = 4 marks each (stated on the section divider; +4 correct, 0 otherwise assumed).

## Solutions whose source is corrected or written
- Q8 - corrected: the PDF's last line says `2m - 5*sqrt(21)*n = 10`; from area = (1/2)*5*sqrt(21) = m/n the relation is `2m - 5*sqrt(21)*n = 0` (option 1, matching the key). Only that line changed.
- Q11 - corrected: equation (1) is printed `pq + rp + 4q - 1 = 0` (with a stray "z" in the line before); correct is `pq + 8p + 4q - 1 = 0`. Also, (1) and (2) alone admit a spurious pair p=-1/3, q=1 (fails the third proportion) and the PDF jumps to `pq = -3` without showing why. p=-1, q=3 and the answer 8 are right (checked symbolically on all three ratios).
- Q16 - corrected: the PDF expands the dot product wrongly (`2 lambda^2 - 5 lambda + 6 = 0`, "D<0"). Correct: `lambda^2 - 2 lambda - 6 = 0`, roots 1 +- sqrt(7) are real but outside [-1, 3]. Answer 0 (option 4) is unchanged but for a different reason.
- Q18 - corrected (gap, no wrong number): the PDF gets lambda = +-1/6 and writes E(7/6, 2, 1/6) without saying why the + sign is taken. Added the step: E lies on the median segment (0 <= lambda <= 1/2).
- Q19 - corrected: the PDF's figure labels arc AB = 5x and arc BC = x, the reverse of the stated ratio 1/5, although its working uses angle AOB = pi/12 (which is right); and in "dot with OC" it writes `alpha r^2 cos(pi/12)` for OC.OA where it should be `cos(pi/2) = 0`. Corrected the labelling and that term. Answer 2 - sqrt(3) unchanged.
- Q13 (kept as `pdf`): the PDF's labels are inconsistent (it names the foot "A" in its figure, and later uses A, B for the two points); I relabelled so the foot is M and the points are A, B. Numbers unchanged.
- No question is `written`; all others are `pdf` (working verified; trivial notation typos silently fixed, e.g. Q4's cosine simplification written out).

## Answer key
All 20 printed answers were checked by independent computation (sympy / numpy) and none looks wrong. Q18 relies on the vertex C = (2, 1, -1) (the figure and AC = i - j - 2k in the PDF; the printed stem's signs were hard to read in the text layer and the key (3) only agrees with this choice).

## Alternates
Alternate solutions given for 19 of 20 questions: Q1-Q11 and Q13-Q20. Each was verified numerically or symbolically and reaches the same answer. Q18's alternate is option-based (test plane membership and the median segment); it is a different route but only works because options are given.

### Questions with NO alternate
- Q12 (direction cosines with beta = gamma = alpha/2): every route leads to `cos(alpha)(cos(alpha)+1) = 0` (using `l = cos 2*beta`, or squared half-angle, are rewordings of the same step). No genuinely different method; it still has useful_results.

## Useful Result / Pattern
Every one of the 20 questions has a `useful_results` slide.

## make_ppt.py warnings
- `Q9: only 3 solution bullets` - the PDF's working for Q9 is genuinely three lines (de Gua's theorem); the alternate (coordinates) gives the longer derivation. Left as is.
- `Q18: very long question - font reduced to 22 pt` - harmless.
- 844 equations converted to native PowerPoint equations; no "could not convert" notes. 130 slides.

## Skipped / assumed / guessed
- Concepts and levels are self-assigned (nearest anchors cited per question in the ratings file).
- Slides were not rendered or checked visually (no soffice rendering in this environment); the PDF was read from page images.
- Marks assumed 4 per question (not printed in the paper).
