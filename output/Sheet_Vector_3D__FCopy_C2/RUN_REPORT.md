# Run report - Sheet_Vector_3D__FCopy_C2 (Exercise C-II, Vector & 3D Geometry, 47 questions)

**Blueprint:** none used. **Concepts self-assigned (no blueprint) - please review.**
**Marks assumed (none printed):** 4 for Q1-33 (numerical / subjective / prove-type), 3 for the paragraph questions Q34-42 and 3 for matching Q43-47 (stated in the section dividers). Total 174 marks. Q40-42 have no options, so they are labelled "Numerical Type" (3 marks) although they belong to a paragraph. Q10, 16, 25, 26, 27, 29, 30 are "Subjective Type" (my labelling).

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.29** (no equivalence-relation or multi-correct adjustments apply). Low versus JEE Advanced (about 2.6-3.2): the sheet is mostly routine vector/3D exercises.
- Levels: L0 = 1 (Q18); L1 = 5 (Q1, 10, 17, 21, 23); L2 = 22; L3 = 16; L4 = 3 (Q26, 36, 45); L5 = 0.
- Ratings are my judgement against the anchors (workers rated their own chunk; a consistency pass was not done across chunks). Workbook: Sheet_Vector_3D__FCopy_C2_difficulty.xlsx (no recalc.py, so formula values are cached only after opening in Excel).

## Solutions corrected / written (no question needed `written`)
- Q9 - (iii) PDF wrote |2+24-10|=16 giving 8√10/15; plane is x+8y-5z+2=0, numerator 18, distance 3√10/5 (key was right). Also slips in (i) (AP written as point P) and (iv) (cross product 4,4,-2 then 4,14,-2; √120 instead of √216).
- Q14 - PDF's Case I misses the λ=|b|² branch and never works the α=0 part; both added (α=0 gives -60(2i+k)).
- Q16 - PDF part (1) lines garbled; same logic rewritten; part (2) restated in the form asked.
- Q21 - PDF wrote a-b=(3,4,-1) (should be (3,-4,-1)) and printed the area without the factor 1/2.
- Q22 - determinant expansion had slips (5(8-λ) instead of 5(8-3λ)); cubic/roots inconsistent. Correct polynomial -λ(λ²+4λ-25); non-zero check added.
- Q26 - PDF proves only P-N ≤ L³ with V taken without modulus; case N-P added.
- Q32 - PDF stops at "use Heron's formula"; final area (altitude 5a/6, area 5a²/(12√3)) added.
- Q33 - PDF writes x in open interval (-2,2); must be closed [-2,2] for m=3 to be attained (answer 34 unchanged).
- Q37 - typo "-2 - 2/5 = -8/3" corrected to -2 - 2/3 (answer unchanged).
- Q43 - PDF correct but incomplete (roots in (A) not listed, jump check in (B) missing, typo "2ab+cosθ" in (D)); written out in full.
- Q44 - PDF working stops at 3cos²α = 1+2cosθ and never evaluates rows; completed (see answer key below).
- Q45 - row C: PDF's own working rejects μ=5, so only μ=0 (see key below).
- Q46 - PDF solution blocks mislabelled (block "(A)" is D, "(C)" is A, "(D)" is C); row D used ax-y=1 instead of 4 (a0=1; correct a0=2).
- Q47 - PDF has no working for row A; written (n1×n2, plane x-y+z=0, distance 1).
- Notation-only fixes kept as `pdf`: Q2 (stray j, lost minus signs), Q4 (line BA labelled AC), Q36/Q41 (one explanatory bullet added), Q18/Q31 (steps filled in), Q10 (blank key; wrote "(n³+1)[a b c]").

## Answer key problems
- **Q44 row D:** key says (D)→(r); cosθ=5/8 gives 3cos²α=9/4, α=π/6, i.e. (s). Kept (D)→(s).
- **Q45 row C:** key says (C)→(q,s); μ=5 is impossible (would need λ₂²=-λ₁²). Kept (C)→(q).
- Q10 key blank; proofs Q25, 26, 27, 29, 30 have no printed answer (answer recorded as "Proved"/"Shown"). All other answers checked by computation.

## Alternates and results
- Alternates for 41 of 47 questions. Partial coverage: Q43 (rows A, C, D), Q44 (projection argument, weakly different), Q45 (rows A, C, D; second alternate is the PDF's own "Aliter" for D), Q46 (row D only), Q47 (rows B, D).
- **No alternate (no genuinely different method):** Q2 (only other route is the same oblique-distance formulas); Q13 (only variants are the same idea reworded); Q20 (same - Vandermonde variant is a rewording); Q25 (IVT on the cross-product function is the only route); Q27 (every route uses [x×y y×z z×x]=[x y z]²); Q28 (any other route is the same substitution into the same conditions).
- Every question has useful_results.

## make_ppt.py output
- 2194 equations converted to native equations; 323 slides, 47 questions. No "could not convert" warnings.
- Notes: Q45 and Q47 "very long question - font reduced to 22 pt" (harmless).
- build_report.py first failed on a form-feed character (a "\f" of \frac in a ratings text); fixed by escaping control characters in the ratings JSON.

## Skipped / assumed / guessed
- Concepts, chapter names and ratings self-assigned; no rendering check (no PowerPoint/LibreOffice). Q38 option (C) is cut off in the PDF ("indeterminate, as [p q r]") and kept verbatim. Q15's figure and Q32's DE:EA / BF:FD = 2:1 reading came from page images. Q7 assumes the new vector has a positive x-component. Q28 and Q30 state angle conditions in words.
- The work was split between five parallel sub-workers (one per question range); the lead merged their output.
