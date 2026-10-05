# RUN REPORT – JEE_Main_Question_Bank_01_Algebra_17 (Q321–Q340: Complex Numbers)

**Blueprint:** none. Concepts self-assigned (no blueprint) - please review.
**Marks assumed:** no marks printed; 4 marks for every question (all 20 are single-correct, PDF 321..340 = deck 1..20), as in the earlier Algebra runs; stated in the section divider.

## Difficulty
Marks-weighted difficulty index (all 4 marks, no equivalence-relation or MCQ-floor adjustment applies): **1.95**.
Levels: L1 = 4 questions (Q2, Q11, Q16, Q20), L2 = 13 questions, L3 = 3 questions (Q7, Q15, Q17). No L0, L4, L5. Confidence Medium (JEE Main-style questions rated on the Advanced scale).

## Solutions corrected / written (solution_source)
- Q1 (321) corrected: PDF gives Im z2 = (2√6 − √3); the product (√3+2√2 i)(√3+i) has imaginary part √3 + 2√6 (its next line z1−z2 is already right). Added |z1−z2|² = 11/3 = |z2|² and the area check for (C), (D).
- Q7 (327) corrected: PDF's expansion begins with |z2|² where |z1|² is meant; missing "=" in the squaring line.
- Q13 (333) corrected: PDF says "the roots of z^1985+z^100+1=0 be ω and ω²" (that degree-1985 equation has many other roots). Rewritten as: factor the cubic, test ω, ω², and −1 (−1 fails). Answer unchanged.
- Q17 (337) corrected: PDF's line "(a²−b²)(z+z̄)=2(a²−b²)" should have z²+z̄²; "1+1²=−1" replaced by −2|z|²=2. The PDF's own a = −b case shows an infinite set (see answer key).
- Q11 (331) written: the PDF has only a sketch of the lines; full algebraic solution written.
- All others: pdf (reproduced; verified). Small bridging lines added without changing the PDF's method: Q2, Q4 (angle of the sector), Q9 (n! multiple of 4), Q15 (which point is z1, z2), Q19 (excluded point).

## Answer key
- All 20 PDF answers verified numerically/exactly and agree with the key.
- Q17 (337): key (D) 0 is true only for a ≠ ±b. The question says only a ≠ b; for a = −b the set is infinite (the PDF itself shows this), and no option says so. Kept answer (D) with the caveat in the answer text.
- Q16 (336): key "Bonus" is right: min is 0 (the point −(3+4i)/2 has modulus 5/2 ≥ 1); no option is 0. (With |z| ≤ 1 the answer would be 3/2.)

## Alternates and Useful Results
- Alternates given for 19 of 20 questions (all except Q16).
- **No alternate for Q16 (336):** the answer is "the centre of the distance function lies in the allowed region, so the minimum is 0"; no genuinely different method exists.
- Useful Result / Pattern given for all 20 questions.
- Weaker alternates (partly the same core idea) – flagged for review: Q2 (triangle-inequality chain vs. centre-distance rule), Q4 (complement sector vs. direct sector), Q9 (residue count and Σ = m − Σ i^{n!}), Q7 (standard identity packaging the same expansion), Q17 (sum/difference of the two equations instead of elimination), Q13 (divisibility argument, though it ends with the same test of z = −1).

## make_ppt.py warnings
- "Q5: very long question - font reduced to 22 pt" – harmless, automatic.
- During development two LaTeX "could not convert" notes appeared because a "\ne" inside Q17's question text was turned into a line break by my own generator script; fixed in the generator and rebuilt. The final build prints no "could not convert" notes (752 equations converted).

## Skipped / assumed
- Slides were not rendered or visually inspected (no soffice step in this environment).
- Concepts and the nearest anchors self-assigned; anchors are only indicative (the anchor bank has few elementary complex-number questions).
- Q10 (330): the point z = 2i (quotient 0, real part 0) is on the circle |z| = 2 and counted; z = −2i is excluded. The maximum is unaffected.
- Q16 answer recorded as "Bonus (none of the options: the minimum is 0)".
