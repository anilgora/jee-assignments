# RUN REPORT - B1 Assignment Differential Calculus 02

Blueprint used: NO. **Concepts self-assigned (no blueprint) - please review.** No marks are printed in the paper; JEE Advanced defaults assumed: single correct 4, one-or-more correct 4, integer 4, numerical / multi-part subjective 4, paragraph-based single correct 3, matching 3 (stated in the section dividers). Q46-49 (proofs / multi-part) are labelled "Numerical Type" with 4 marks.

## Difficulty
Marks-weighted difficulty index (adjusted levels): **2.34** over 51 questions (198 marks).
Questions per level: L0: 1, L1: 8, L2: 19, L2.5: 1, L3: 17, L4: 5.
Q21 has the multi-concept multi-correct floor (2.5); no equivalence-relation adjustments. Low-confidence ratings: Q28, Q43, Q46, Q47 (garbled / reconstructed / few anchors). Q31 and Q41 are debatable levels. Ratings were produced by sub-agents using the calibrated rubric.

## Solutions marked corrected / written
- Q1 (corrected): question prints f(x)=dy/dx but the working/key use (dy/dx)/(2x)=tan^-1 x; remark added, answer B kept.
- Q2 (corrected): working and key right, but (1,1) is not on the curve (32 vs 16); y''=0 holds at every point of the curve. Remark added.
- Q3 (corrected): question prints the product y''(y')^n, working uses the quotient; as printed n=-4. Key D kept (assumed misprint), remark added.
- Q4 (corrected): PDF asserts extremum at 0 and 2 extrema for x>0 without proof; added f'(0)!=0 and the roots of f'. Answer unchanged.
- Q10 (corrected): PDF f'(t)=(t-1)(2t+1) is wrong; correct (t-1)(3t+1), f'(-1)=4. Answer D unchanged.
- Q12 (corrected): PDF proves only (A); added MVT steps, elimination of B and counterexample for (C),(D).
- Q14 (corrected): PDF never evaluates statements (i)-(iii); completed. Key B right.
- Q17 (corrected): concavity sketch replaced by MVT bound f(x)>=f(0)+x/2017.
- Q19 (corrected): working had a typo and omitted max check/value; added. KEY WRONG (below).
- Q20 (corrected): PDF writes g''(2)=1/f'(0) (should be g'(2)); f''(0) and invertibility added.
- Q22 (corrected): d/dx(f^3)>=0 not >0 (zero where f=0); conclusion unchanged.
- Q24 (corrected): LMVT written with f instead of g=f^n, and GM exponent 1+..+n should be 0+..+(n-1); answer unchanged.
- Q28 (written): PDF has no solution. KEY WRONG (below).
- Q29 (written): PDF has no solution.
- Q32 (corrected): PDF sets g'(x)=0 for g=x+1/x, which finds stationary points of g not f; redone via h(g). Answer 16 right.
- Q34 (corrected): PDF's Rolle count on f''' unjustified and last Rolle step skipped; fixed. Answer 12 right.
- Q36 (corrected): PDF proves only "at most one" solution; existence (x=2) added.
- Q39 (corrected): PDF garbled, omits k=6, f(0)=1/3 and f'(0)=4/3; added.
- Q40 (corrected): PDF f(0)=sin1+(-1) should be sin1+1; condition is sin(lambda)<=sin 1; left-side monotonicity added.
- Q42 (corrected): PDF lists f(+-1) as candidates though outside the domain; endpoints only.
- Q43 (corrected): QUESTION GARBLED in the PDF (h printed as (a+bx^2)/x^(5/3), target quantity missing). Reconstructed h=(a+bx^{3/2})/x^{5/4} and the asked quantity to match the PDF working and key 5 - please review.
- Q45 (corrected): result right; justifications for the root counts added.
- Q47 (corrected): duplicated garbled fragment dropped; reason for the concave-down stretch added.
- Q48 (corrected): PDF solution is cut off in case (3i) and runs into unrelated text; remainder written and checked (289>288, minimum 0.08579).
- Q49 (corrected): denominator exponent should be 2/3 and the unit is per hour, not per second. Answer 19/27 m/h.
- Small transcription fixes (not corrections of maths): Q21(D) garbled exponents read from the PDF's own working; Q25 stem f'(0)=0 read as f'(r)=0; Q28-29 paragraph "lim x->2" read as x->infinity and "R-P{3}" as R-{3}; Q26-27 figure described in words; Q11, Q13, Q15, Q16, Q18, Q33, Q38, Q41 got extra explanatory bullets but are marked pdf.

## Answer keys that look wrong
- Q19: key (A, D) is wrong; options (C) and (D) are the identical expression, so the correct answer is (A, C, D).
- Q28: key (A) lambda+1 is wrong; lambda=3 and there are exactly 5 solutions, i.e. (C) 2*lambda-1 (depends on reading the paragraph's limit as x->infinity; Low confidence).
- Q3's key D is consistent only with the quotient reading (see above). Q41: answer 4 holds only for (1+sqrt2)/2 in lowest terms. Q16(D) is true only as a containment.

## Alternates
Alternate solutions given for 37 questions. NO alternate (reason):
- Q1: only product rule + identity. Q8: only chain rule. Q10: "not necessarily true" is settled only by a counterexample.
- Q21: only partial fractions + parity. Q24: AM-GM/Jensen step is the same convexity idea. Q27: one-step endpoint check of a convex function.
- Q28: other routes are the same region-by-region count. Q29: geometric reflection is the same reasoning as the one-sided derivatives. Q30: no genuinely different elegant method found.
- Q40: every route reduces to f(0) vs f(0+) plus left monotonicity. Q43: only one sensible route. Q45: Rolle interlacing is the only route. Q47: parts (a)-(c) are direct reading, (d) has one argument. Q51: only a partial shortcut for part (d).
Useful results (2-5 bullets) given for ALL 51 questions.

## make_ppt.py output
- "Equations: 1967 converted to native PowerPoint equations." No "could not convert" warnings.
- Notes: Q47, Q50, Q51 "very long question - font reduced to 20 pt" - harmless, the script's designed behaviour.
- Deck: 331 slides.

## Skipped / assumed / guessed
- No rendering or thumbnails (no soffice/skills mount). Equations not visually checked in PowerPoint.
- Q26-27 rates taken as railway 1, highway 2; Q40 "maximum at 0" taken as local max; Q29 assumes a genuine corner at x=-2.
- Concepts and marks self-assigned; sections set by consecutive question type (Q30-34 and Q46-49 "Numerical", Q35-45 "Integer").
