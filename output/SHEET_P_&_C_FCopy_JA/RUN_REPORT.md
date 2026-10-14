# RUN REPORT - SHEET_P_&_C_FCopy_JA (Permutations & Combinations, Exercise J-A, 21 questions)

**Blueprint:** none was available. Concepts self-assigned (no blueprint) - please review.
Marks assumed (none printed): Single Correct 3, Paragraph single correct 3, Matching 3, One-or-more-correct 4, Numerical/integer 4. Stated in the section dividers.

## Difficulty
- Marks-weighted difficulty index (adjusted = unadjusted; no equivalence-relation or multi-concept adjustment applied): **2.68**
- Levels: L1 x2 (Q6, Q9); L2 x8 (Q1, 2, 8, 10, 11, 14, 15, 16); L3 x7 (Q3, 4, 5, 12, 13, 17, 21); L4 x3 (Q7, 18, 19); L5 x1 (Q20).
- Q16, Q19, Q20, Q21 are official JEE Advanced questions (2021, 2024, 2025, 2026) that already exist in the anchor bank, so their levels follow the user's own ratings (2, 4, 5, 3).

## Solutions that are corrected or written
- Q5 (corrected): the PDF's "Alternative" table of the 7 tuples has three wrong rows (1,2,4,5,7 sums to 19; 1,2,4,6,8 and 1,3,4,6,7 sum to 21). Replaced with the correct list. The main method and answer 7 are right.
- Q16 (corrected): the PDF writes n3 = 8C4 = 70 and n4 = 10C4 = 210 and crosses out (D), contradicting its own key ABD. Correct: n3 = C(10,4) = 210 (so (C) 220 is false) and n4 = 5040, n4/12 = 420. The n2 table was garbled and is rewritten as 2+3+...+9 = 44.
- No question was "written" from scratch.
- Small clarifications (still source "pdf"): Q3 gains an explicit step b15 = c16 for option (C); Q8 and Q12 have missing intermediate numbers filled in; Q18 is restated in the question's own colours (the PDF's diagrams label the 3-ball colour "B"); Q10's "x = 10" in the PDF is 10! (lost in extraction).

## Answer key
Every answer was checked by brute force (itertools) and all agree with the PDF key: Q1 B, Q2 B, Q3 A, Q4 C, Q5 7, Q6 5, Q7 5, Q8 A, Q9 D, Q10 5, Q11 625, Q12 C, Q13 30, Q14 495, Q15 1080, Q16 ABD, Q17 569, Q18 A, Q19 665, Q20 762, Q21 206. No wrong key found.

## Alternates and results
- Alternate solutions were produced for all 21 questions (Q15 has two). Each was checked numerically/symbolically against the answer.
- Questions with NO alternate: none.
- Weakest alternates (genuine but close in spirit): Q6 (degree count vs direct count), Q10 (multiset view), Q9 (complement/Vandermonde).
- Every question has a useful_results slide.

## make_ppt.py output
- "Q12: very long question - font reduced to 20 pt." - harmless; the matching question has a long paragraph.
- An early "could not convert $\\neq$" was my typo (double backslash); fixed and rebuilt. No remaining conversion warnings.
- 649 equations converted to native PowerPoint equations; 141 slides.

## Skipped / assumed / guessed
- No rendering or thumbnail check was done (no soffice); the deck was not viewed visually.
- Concepts and section marking are assumptions (no blueprint, no printed marks).
- The paper's printed symbols were partly garbled in the text layer; Q16's definitions were checked on the page image. Q3's "≠" signs were confirmed on the page image.
