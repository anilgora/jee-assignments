# Run report - SHEET_SET_&_RELATION_FCopy_JM (Set & Relation, Exercise III: JEE Main PYQs, 73 questions)

Files: `_content.json`, `_Analysis.pptx` (427 slides, 73 questions), `_ratings.json`, `_difficulty.xlsx`, `per_question_notes.md` (one line per question: key status, source, alternate remarks).

## Difficulty
- Marks-weighted difficulty index (adjusted levels): **1.76** (292 marks; every question 4 marks).
- Adjusted level counts: 1 -> 25 (Q1-5, 9, 10, 11, 15, 17, 20, 23, 32, 40, 46, 47, 49, 56, 57, 59, 60, 64, 65, 68, 69); 1.5 -> 6 (Q13, 14, 16, 28, 36, 37); 2 -> 28; 2.5 -> 7 (Q18, 24, 25, 29, 41, 42, 71); 3 -> 7 (Q31, 34, 43, 53, 54, 62, 72); levels 0, 4, 5: none.
- +0.5 equivalence-relation adjustment applied where the key step is an equivalence-relation check/classes; judgement calls flagged by workers: Q21 (set false), Q37 and Q47 (set true, borderline). No multi-correct questions, so the 2.5 floor never applies.
- JEE Main PYQ sheet, so far below the Advanced range (2.6-3.2); reported as it is.

## Blueprint / marks
- No blueprint: **Concepts self-assigned (no blueprint) - please review.**
- No marks printed. Assumed 4 for single-correct and 4 for numerical (JEE Advanced defaults); stated in the section dividers. No matching/paragraph questions.

## Solutions corrected (source = corrected) / written
Corrected (21): Q2 (symmetry counterexamples filed under Reflexive, typo (8,3)); Q6 (vague symmetry line; fails only at w=0, counterexample (0,1)); Q7 (garbled symmetry step, no counterexample); Q9 (typo'd case list); Q10 (n(B)=8 / 2^8=250 should be n(AxB)=8, 256); Q11 (typo x-2sqrt(x)+12 should be x-8sqrt(x)+12); Q14 (symmetry/transitivity steps invalid); Q17 (wrong roots, should be (-1±sqrt73)/2); Q23 (typos A-B=(1,1), stray P); Q27 (omits prime 19: n(R1)=36, n(R2)=28, difference 8 unchanged); Q35 (symmetry claim ignores 2a≠b, transitivity untested; counterexamples supplied); Q44 (invalid step a/b>-2 => b/a<-1/2; counterexample (2,-5)); Q48 (pair (2,4) should be (2,8)); Q53 (printed key wrong, see below); Q56, Q61, Q63, Q64 (see per_question_notes.md); Q62 (printed key wrong, see below); Q67 (printed implications false as written, (II) never stated false); Q72 (14-x should be 40-x, labels m/n swapped; answer 45 right).
Written from scratch (4): Q5 (PDF only asserts B=C), Q8 (PDF stops after "Reflexive;"), Q15 (PDF one line), Q21 (PDF one-line verdict).
Small gap-fills kept as source pdf: Q12, Q13, Q19, Q20, Q46, Q47, Q49, Q51, Q54 and others (see per_question_notes.md).

## Answer key
- **Q53**: printed key 4 is wrong; brute force gives 3 (the PDF itself lists only 3 relations). Answer recorded as 3.
- **Q62**: printed key 11 is wrong; correct maximum is 10 (the PDF's own working and the official key give 10). Recorded 10.
- All other keys verified (brute force/numerical; Q7, Q8, Q21, Q23, Q25 by hand only; Q15 from figures at higher resolution).

## Alternates and results
- Alternates given for 51 of 73 questions, each verified. Every question has useful_results (2-5 bullets).
- **No alternate (22), no genuinely different method:** Q1, Q3 (single property check/counterexample; other route is option elimination); Q2 (finite check); Q8 (same three-axiom proof); Q10 (complement count is the same count); Q15 (single figure observation); Q16 (only natural method is listing (4k,3k)); Q28, Q30, Q31 (single natural method; others are the same enumeration/counterexample); Q34 (same row-by-row lattice count); Q35 (counterexample disproof only); Q40 (reciprocal-conjugate trick is the only short route); Q47, Q48, Q54 (see notes); Q56 (only option elimination); Q61 (other routes are the same mod-4/mod-8 idea); Q66, Q67, Q68, Q70 (no different method).
- Weak/close alternates: Q13 and Q21 (shortcut-type), Q38 (same facts, different route).

## make_ppt.py notes
- First build: `could not convert $qm=pn\right\}$` (unbalanced \left...\right\} in Q6's question after `$` splitting). Fixed by using plain `\{ ... \}`; rebuilt with no warnings. 2494 equations converted.

## Skipped / assumed
- No visual rendering of the deck (no soffice); fit judged from script output only.
- Maths text from pdftotext was garbled in places, so workers read from page images (seven parallel workers by block; Q21 was covered by two blocks, the first copy was kept). A first worker launched with an empty prompt by mistake was stopped and did nothing.
- Q15's figures are not reproduced; described in words in the question text. Hindi duplicates ignored.
