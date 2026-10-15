# RUN REPORT — XII_SHEET_INTEGRATION_FCopy_JM (80 JEE Main questions, Integration)

**Blueprint:** none. **Concepts self-assigned (no blueprint) - please review.**
**Marks assumed:** the paper prints none; 4 marks for every question (single-correct SCQ and numerical), stated in the section dividers.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.01**. No equivalence-relation or multi-correct adjustments (all SCQ/numerical).
- Level 1: 15 questions; Level 2: 49; Level 3: 16; Levels 0, 4, 5: none.
- Levels are my judgement against Advanced anchors (this is a Main sheet); confidence mostly Medium; Q75 Low.

## Solutions with source `corrected` (23) — `written`: none
- Q5: limits printed -pi/4..pi/4 (should be -pi/2..pi/2), log argument garbled, oddness of f not shown.
- Q9: int_1^1 should be int_1^2; "n<=x n+1" missing "<"; label x(x-1)/2 should be n(n-1)/2.
- Q10: PDF gives f'(2-)=2; correct is 5.
- Q12: antiderivative x+ln(x+2) should be x+2ln(x+2).
- Q13: reflected integrand must have e^{-x cos x}.
- Q21: step (t+1)/(t²-t+1) wrong (should be ½(2t-1)+3/2 form); arctan argument and dropped 1/3 fixed.
- Q35: 1-cos t vs 1+cos t, dx=-sin t dt, final matching step added.
- Q41: first bracket typeset as e^{1/(x|x|+1)}, should be 1/(e^{x|x|}+1).
- Q43: sin² vs sin³ on right; f vs f' at 1/√3.
- Q44: sign slip +7(ln(1-1/7)+1/7).
- Q46: denominator cos h should be sin h; L'Hôpital sign.
- Q49: third integrand missing x.
- Q50: several slips; correct f(x)=(18x-4)/13, f(6)=8.
- Q54: ln(49/50) printed where RHS is still ln(49/40).
- Q57: first line equated constant with integral, jumps added.
- Q60: -3e^{-x} should be -6e^{-x}; √2 factor in arctan; constant c inconsistent.
- Q66: bounds on f' over (π/4,π/3) wrongly used as bounds on f(x); f'(x)=8cos x−2cos2x print slip (see answer key below).
- Q68: lower limit -1/2, missing "+", intermediate values added.
- Q69: PDF stopped at n=5; final steps added; sign slip.
- Q71: upper limit 3 should be e³.
- Q75: a₂ should be 15/4, a₃ 82/9 (PDF 9/2, 100/9); n≥5 argument added.
- Q76: sign should be I₂−I₁.
- Q79: factor 15 vs 30, coefficient 2/5 vs 2/3, bracket √3/5.
Minor slips fixed silently but kept `pdf`: Q33, Q34, Q51, Q55, Q70, Q72, Q74, Q80 (see parts/*_notes.md).

## Answer key
- **Q66: the key (C) looks wrong.** True I≈1.5362 > √2π/3≈1.4810; no printed option is fully true (rigorous bounds 1.5155<I<1.5523). `answer` keeps "(C) as keyed" with this caveat.
- All other 79 keys were re-computed numerically and agree.
- Q43: the stated identity fails as x→0+ (holds only up to a constant); differentiating as intended still gives (B). Q40: individual b_n diverge at 0, only differences converge (answer unaffected).

## Alternates / results
- Alternates given for 67 questions. **No alternate (13), no genuinely different method:**
  Q5, Q8 (only parity / reflection idea); Q22, Q26 (only Riemann sum); Q31 (single identity); Q46 (exact derivative, limit step only); Q48 (piecewise graph); Q50 (same linear system); Q52 (degenerate kernel only); Q54 (partial fractions only); Q60 (split + arctan only); Q70 (all routes are t=tan(x/2)); Q75 (term-by-term evaluation).
- Alternates that are partly re-framings (flag for review): Q1, Q2, Q9, Q14, Q15, Q16, Q18, Q24, Q25, Q27, Q29, Q37, Q38, Q40, Q41, Q47, Q49, Q53, Q55, Q58, Q61, Q64, Q66, Q73, Q74, Q79.
- `useful_results` given for all 80 questions (Q70's was added at merge).

## make_ppt.py output
No warnings. 3600 equations converted natively, 534 slides, 80 questions; no "could not convert" messages.

## Skipped / assumed / guessed
- Worked by 8 parallel sub-workers (10 questions each), merged by me; per-part notes kept in parts/.
- Q1 is partial fractions (Algebra) inside an integration sheet; Q9/Q10 span two chapters.
- Slides were not rendered or visually checked (no soffice); layout as produced by the script.
- Sections: consecutive questions grouped by type automatically from the sheet (SCQ / numerical).
