# RUN REPORT – JEE_Main_Question_Bank_01_Algebra_15 (Q281–Q300, Binomial Theorem)

**Blueprint:** none. Concepts self-assigned (no blueprint) - please review.
**Marks assumed:** no marks printed; 4 marks for every question (single correct Q1–Q8 = PDF 281–288, numerical Q9–Q20 = PDF 289–300).
Deck numbering 1..20 = PDF 281..300.

## Difficulty
Marks-weighted difficulty index (all 4 marks, no adjustments applied): **2.20**.
Levels: L1 = 1 question (Q9), L2 = 14 questions, L3 = 5 questions (Q8, Q10, Q14, Q15, Q19). No L0, L4, L5.
No equivalence-relation adjustment or MCQ floor applies. Ratings are Medium confidence (JEE Main-style questions rated on the Advanced scale).

## Solutions corrected / written (solution_source)
- Q2 (282) corrected: PDF's last lines drop the first coefficient and show only "…=32 ⇒ 729ab=32"; both coefficients now written out and equated.
- Q5 (285) corrected: see answer-key note below.
- Q6 (286) corrected: index typos (C9 instead of C49, ending at C99 instead of C49) and a skipped cancellation.
- Q13 (293) corrected: typos "3768" for 3762 and "2023–z" for 2023–2.
- Q18 (298) corrected: PDF working is garbled and drops the factor 289^2023 (≡ –1 mod 5); rewritten with 2023 = 7·289.
- Q19 (299) corrected: final simplification line mis-signed as printed; correct contribution of second sum is –1/e.
- All others: pdf (reproduced; verified). No question was "written".

## Answer key
- **Q5 (PDF 285): key looks wrong / statement mismatch.** For the statement as printed (1011th term from the end = 1024 × 1011th from beginning) |x| = 5/16 (the PDF's own working also reaches 5/16), which is not an option. The key (C) 10 fits the reversed statement (beginning term = 1024 × end term). Answer box shows 5/16 with this note.
- All other answers verified by computation (sympy / exact integer arithmetic) and agree with the key.

## Alternates and Useful Results
- Alternates given for 19 of 20 questions (Q1–Q15, Q17–Q20).
- **No alternate for Q16 (PDF 296):** the only route is solving 1–3n+9C(n,2)=376 for n and reading off the r=2 term; any other method (e.g. re-expressing as x^10(1–3x^-3)^10) is the same steps reworded.
- Useful Result / Pattern slides given for all 20 questions.
- Weaker alternates (same core idea, different organisation): Q1, Q2, Q7, Q8, Q14 – flagged for review.

## make_ppt.py warnings
None. The script printed only "761 converted to native PowerPoint equations" (no "could not convert" messages).

## Skipped / assumed
- Slides were not rendered or visually inspected (no soffice step in this environment).
- Concepts and chapters self-assigned; Q19 chapter set to "Exponential Series" (listed under Algebra in the paper).
- The Q5 answer is displayed as 5/16 (not an option) rather than following the key.
