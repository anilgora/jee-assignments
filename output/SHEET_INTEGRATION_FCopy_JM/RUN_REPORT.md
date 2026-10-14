# Run report - SHEET_INTEGRATION_FCopy_JM

Paper: Integration sheet, 100 JEE Main questions (numbered 1-100 as in the PDF; options A-D or numerical answer). Run date 2026-10-14. Work was split over five sub-agents (Q1-20, 21-40, 41-60, 61-80, 81-100); results were merged and built here.

## Blueprint
No blueprint used. **Concepts self-assigned (no blueprint) - please review.** Marks assumed: 4 for every question (single-correct and numerical alike; none printed), stated in the section divider.

## Difficulty
Marks-weighted index (adjusted): **2.07** (chapter sheet of JEE Main questions; no expected distribution).
Level counts: L0 = 1, L1 = 23, L2 = 47, L3 = 26, L4 = 3, L5 = 0. No equivalence-relation adjustment, no MCQ floor.
Low/Medium confidence ratings are flagged in the ratings JSON (e.g. Q27 Low; Q72 is close to anchor 2021-P2-Q19 (L4) but rated 3 since only two breakpoints matter - please review).

## solution_source = corrected (27)
- Q6: PDF stops before multiplying by 16; mistyped lines fixed.
- Q9: limits after x=1/t inconsistent (sign of reversed limits dropped).
- Q14: typos (ln(1-f) for ln(1-t); garbled last line).
- Q19: garbled notation; initial condition f(0)=e added.
- Q22: dropped outer minus sign; ln(9/2) should be ln(9/e). Answer 20 right.
- Q24: PDF writes I=2*int g; correct is I=int g, so value 13 not 26 (see key problems).
- Q25: sign after by-parts (+ should be -); final line -pi should be -pi^2/16.
- Q27: PDF working incomplete; completed (see key problems).
- Q31: x=1/t valid only for x>0 (|x| mishandled); f(0)=0 used as limit x->0+.
- Q36: antiderivative wrong in PDF; correct is t ln(t+sqrt(t^2+1)) - sqrt(t^2+1). Answer B right.
- Q40: partial-fraction line limits 0..inf should be 1..inf.
- Q41: statement typed in the intended form (e^{-pi/4} + integral in numerator), matching the PDF's working and answer 50.
- Q46: coefficient +10 should be +18.
- Q58: stray n^3; (x^2-1) should be (x^2+1).
- Q59: derivative of e^{x^2}(2x) missing a factor 2.
- Q64: c/1=d/1=e/1 should be e/4.
- Q66: theta limits 0..pi/4 should be 0..pi/2 and result is 2I; the two slips cancel, answer right.
- Q67: limits after t=2x-1 should be +-1, not +-1/2; answer 0 right.
- Q68: pi/2 + 7sqrt3/64 should be pi/8 + 7sqrt3/64.
- Q75: -pi/(2x2) should be -pi^2/(2x2); skipped reflection step added.
- Q80: option (D) printed as 7 (same as C); treated as misprint of 4 (see key problems).
- Q81: log coefficient 3/2 should be 3/8.
- Q83: antiderivative -x^2/22 should be -x^2/2.
- Q85: skipped 0/0 stage between L'Hopital steps; sign of sin term reversed (no effect on answer).
- Q93: cot^-1(tan theta)=pi/2-theta step missing, minus sign dropped then restored.
- Q97: inner integral lines wrong (cos^2 t should be cot^2 t; 1/cos t should be tan t); result and answer right.
- Q100: last line pi/sqrt2 = pi/K should be pi/(4 sqrt2); K=4sqrt2, K^2=32 right.
No question has solution_source "written". Short PDF solutions (e.g. Q38, Q4) were expanded with missing intermediate steps while staying "pdf".

## Answer key problems
- **Q24: key says 26, correct answer is 13** (numerically 16I/pi = 13.000). `answer` shows 13.
- **Q27: printed key "B / Bonus"; no option is a correct antiderivative** (integrand has log_2 x, substitution gives ln(ex/2)). `answer` reads "Bonus: no option is correct". Low confidence in rating.
- Q69: numerical question but key printed as "B"; working gives alpha = 2, answer set to 2.
- Q80: option D misprinted as 7 (same as C); key D, value 4 - shown as 4.
- Q100: statement prints a numerator "8" in the second term (general term 2nr^2 gives 8n); typed as printed, a typo with no effect on the answer.
- Q52 option (C) was garbled in the PDF; typed as 2 cosec(theta) (a guess, does not affect answer D). Q56 exponent typed as sin^2023 x.

## Alternate solutions
Given for 92 of 100 questions, each verified numerically. Questions with NO alternate:
- Q4: only a restatement via cos^-1.
- Q10: other route is the same split t^4+1=(t^4-t^2+1)+t^2.
- Q11: interval splitting gives the same step-function sum.
- Q18: half-angle route is the same symmetry plus arctan finish.
- Q20: any alternate is the king property in another variable.
- Q27: question has no correct option.
- Q38: only content is simplifying min and greatest integer; no different method.
- Q48: pure five-stage recursion; every other route tried was a reworded copy.
Weaker alternates (viewpoint/shortcut variants, please review): Q3, Q25, Q26, Q35, Q37, Q62, Q73, Q75, Q78, Q84, Q89, Q92, Q93.

## Useful Result / Pattern
Every question (1-100) has useful_results.

## make_ppt.py warnings
None. 4055 equations converted to native PowerPoint equations; 629 slides, 100 questions. No equation was left as LaTeX text.

## Skipped / assumed / guessed
- No rendering/thumbnail check (no soffice); the deck was built but not viewed. Difficulty xlsx not recalculated (recalc.py unavailable).
- Figures were not reproduced. Concepts and levels are self-assigned; marks of 4 assumed.
