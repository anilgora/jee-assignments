# Run report - SHEET_MATHEMATICAL_REASONING_FCopy_JM

Paper: Exercise J-II (Mathematical Reasoning), 83 AIEEE / JEE Main questions (AIEEE 2008-2012, JEE Main 2013-2023), numbered 1-83 as in the PDF. The PDF has answers and solutions (Hindi text ignored). Date of run: 2026-10-14. Every answer was checked by brute-force truth-table evaluation in Python (all 83 final answers; each option of each question was evaluated), and each step in the written solutions was checked the same way where it is an equivalence.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.** Every question is in one chapter (Mathematical Reasoning), so each question has a single summarised concept.
Marks assumed (none printed; stated in the section dividers): JEE Advanced defaults, 4 marks for every question (single correct Q1-48, 50-64, 66-82; one-or-more-correct Q65; numerical Q49, Q83). Total 332.

## Difficulty
Marks-weighted difficulty index (adjusted): **1.55** (these are JEE Main / AIEEE logic questions; far below the official Advanced range 2.6-3.2).
Level counts: L0 = 0, L1 = 38, L2 = 44, L3 = 1 (Q49), L4 = 0, L5 = 0.
L1: Q1-4, 6-10, 12-15, 17, 18, 20, 21, 23-25, 30, 32, 37, 39, 41, 44, 45, 50, 52, 57, 61-63, 70, 72, 75, 77, 82. All others L2 except Q49 (L3).
No equivalence-relation adjustment and no MCQ floor applied (Q65 is a one-correct-or-more question but involves a single concept, tautology checking). Medium-confidence ratings: Q5, Q28, Q49, Q51, Q78. (Question 49 is the only question with no options and a search over assignments, hence L3.)

## Solutions whose solution_source is "corrected" (18)
- Q1: PDF's step (~p v p) v ~q -> ~p v p v q is not an equivalence step (both are tautologies); rewritten, and options B-D explicitly rejected.
- Q2: PDF defines r as ~p <-> q; r is p <-> q (its own table uses p <-> q).
- Q5: PDF turns the statement into 'brilliant and honest iff rich' and writes ~[(P^~R)<->Q], mixing honest/dishonest; statement is (P^~R)<->Q. Answer B unchanged; steps to B written out.
- Q17: PDF's checks of options (iii) and (iv) are garbled/unfinished; written out (both reduce to ~A v B).
- Q19: PDF's third table header has A^~B where A v B belongs; its value column is that of the real F1.
- Q23: PDF's working for option B uses a disjunction (it is option D's expression); B = (p^q)^(p->q) = p^q was never evaluated and D is not shown. Both written correctly.
- Q37: option (d): PDF says ~(~q v p) = q v ~p; correct is q ^ ~p. Conclusion unchanged.
- Q43: PDF says (p v q) v ~p = p and concludes '~p => p is a tautology' - both wrong. Correct: (p^q) v ~p = ~p v q, and ~p => (~p v q) is the tautology. Answer C unchanged.
- Q45: PDF expands ~(p^q) as ~p ^ ~q in option D; it is ~p v ~q (value F unchanged since X ^ ~X).
- Q46: PDF labels p -> (q v r) as S1; it is S2.
- Q48: PDF's third line prints (~p v q) v (p v ~r) for (~p ^ ~q) v (p v ~r) and stops before simplifying the negation; completed.
- Q56: PDF's check of option A uses (p v q) ^ (p v ~q) = p; with the operations of A it is (p v q) ^ (p ^ ~q) = p ^ ~q. B is proved algebraically instead of by a Venn diagram.
- Q64: PDF's closing line quotes a different expression (premise/conclusion transposed) from the question; its printed columns are right and give option A.
- Q68: ANSWER KEY WRONG (see below); corrected to (C).
- Q69: PDF's first line mis-prints and mis-brackets the statement (p v q, conjunction placed inside the conclusion); also checks only r = ~p and q (r = p and ~q added).
- Q73: PDF's table header for S2 is (p=>q) => (~p^q) instead of (q=>p) => (~p^q); values are those of the correct statement.
- Q78: PDF writes ~r v (~p ^ q) = ~r v (p v ~q) = (p v ~q) => ~r, which is a wrong step; the right step is contraposition. Option A is still right (it is the contrapositive of the converse r => (~p ^ q)).
- Q79: PDF's S2 table labels the (~p ^ q) column as (p ^ ~q).

## Solutions with solution_source "written" (1)
- Q38: the PDF only states 'must be true when Delta = v and =>' with no working; the four-case check is written out. (Answer B = 2 is right.)

Small additions inside "pdf" solutions (nothing wrong in the PDF): Q4, 9, 11, 20, 21, 22, 25, 29, 30, 33, 35, 47, 49, 51, 54, 59, 60, 65, 70, 72, 76, 80, 83 (rejection of the other options, a skipped distribution step, a missing bracket, a stray symbol in an option, etc.; each noted in the content file under source_note).

## Answer key / question problems
- **Q68: the key (A) 'both correct' is wrong.** S2 = ((~p)=>(~q)) ^ ((~p) v q) is p<->q, true at p=q=T and p=q=F (the PDF's own table shows this), so it is not a contradiction. Correct answer: (C) only (S1) is correct. The deck shows (C).
- Q20: options (C) and (D) are printed identically (both modus tollens, both tautologies). Key (NTA) says (C); kept (C), noted in the speaker notes/source_note.
- Q21: options (C) and (D) are printed identically; answer (A) unaffected.
- Q65: one-or-more-correct, answer (A, C, D) agrees with the NTA key (1,3,4).
- Q78: the printed 'converse' option A is only logically equivalent to the converse (it is the contrapositive of r => (~p^q)); no other option is, so the key (A) is kept.
- Q70: option (D) is printed with a stray multiplication sign; irrelevant to the answer.

## Alternates and results
Alternates given for 82 of 83 questions (all except Q25). useful_results given for all 83.
Question with NO alternate:
- Q25: three direct evaluations of conditionals from the definition of '->' (false premise gives true); there is no genuinely different method, anything else would be a reworded copy.
Borderline alternates (technique differs but is close to the main method): Q18 and Q28 (who breaks the promise - semantic form of the negation), Q42 and Q35 (falsifier search instead of case table), Q7/Q39 (the single falsifying row of a conditional). Q49's alternate (case s = T, forcing p=F, r=T, q=T) is a genuinely different route to the same maximum 9.

## make_ppt.py warnings
First build printed 42 "could not convert ... left as LaTeX text" notes (e.g. $\vee$, $\Delta=\wedge$, $*=\vee$). Cause: my formula strings had a space before the closing $ (pandoc will not treat '$..$' with trailing space as maths). Fixed in the generator (whitespace stripped inside every $...$); rebuilt with no notes and no warnings: 1359 equations converted, 464 slides, 83 questions.

## Skipped / assumed / guessed
- Rendering/thumbnail checks were skipped (no soffice); the deck was built without warnings but not visually inspected.
- Concepts, question types and marks are my own assignment (no blueprint). Types: Q49 and Q83 (no options) as 'Numerical'; Q65 as one-or-more-correct (the PDF key lists several options); everything else single correct.
- Question texts were transcribed from page images (small print): the symbols in Q49's nine propositions, Q21's operator options and Q70(D) were checked on zoomed crops.
- Difficulty levels are my estimate on the user's scale; the sheet has no Advanced-level questions, so most anchors used are the easiest official ones (L0-L2); Q5, Q28, Q49, Q51 and Q78 are the least certain.
