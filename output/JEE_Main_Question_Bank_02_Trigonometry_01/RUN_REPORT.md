# Run report — JEE_Main_Question_Bank_02_Trigonometry_01

Paper: `papers/JEE_Main_Question_Bank_02_Trigonometry_01.pdf` (14 pages, 18 maths questions: Q1–Q15 single correct, Q16–Q18 integer type).

Files in this folder:
- `JEE_Main_Question_Bank_02_Trigonometry_01_Analysis.pptx` (114 slides)
- `JEE_Main_Question_Bank_02_Trigonometry_01_content.json`
- `JEE_Main_Question_Bank_02_Trigonometry_01_ratings.json`
- `JEE_Main_Question_Bank_02_Trigonometry_01_difficulty.xlsx`

## Blueprint and marks
- **No blueprint was used** (`blueprints/JEE_Main_Question_Bank_02_Trigonometry_01.xlsx` does not exist). **Concepts self-assigned (no blueprint) - please review.**
- The paper prints no marking scheme. Marks assumed (JEE Advanced defaults, as instructed): **4 marks for every single-correct question (Q1–Q15) and 4 marks for every integer question (Q16–Q18)**. This is stated on both section dividers.

## Difficulty (jee-advanced-difficulty-calibrated)
- Marks-weighted difficulty index (adjusted): **1.83** (all questions carry 4 marks, so it equals the mean level).
- Questions per level: Level 1 — 7 (Q1, Q4, Q5, Q7, Q10, Q13, Q18); Level 2 — 7 (Q2, Q3, Q6, Q8, Q11, Q12, Q14); Level 3 — 4 (Q9, Q15, Q16, Q17); Levels 0, 4, 5 — none.
- No equivalence-relation adjustment and no multi-correct floor applied (no such questions). This is a JEE Main question bank, so the index sits well below the official JEE Advanced range (2.59–3.21), as expected.
- Excel built with `build_report.py`; `recalc.py` was skipped (no `/mnt/skills`), so formula cells have no cached values until the workbook is opened in Excel.

## Solutions: corrected / written (none were `written`)
- **Q9 — corrected:** PDF keeps cos β = ±1/√2 without rejecting the negative sign (the right side must equal 4 > 0), and its last line reads −2√2 although the previous line gives −2·(1/√2) = −√2. Fixed to −√2 (option B, matching the key).
- **Q11 — corrected:** PDF line 4 has a sign error, 2sin²θ(sin⁴θ − 1) instead of 2sin²θ(1 − sin⁴θ), and line 5 ends with a stray "… cos²θ − 1" instead of "= 0". The answer 9 is unaffected.
- **Q12 — corrected:** PDF writes the denominator of tan(α+β) as 1 − tanα + tanβ instead of 1 − tanα·tanβ. Its numeric result (λ/√2) was right.
- **Q14 — corrected:** PDF line reads (log sin x)² − 4 log sin x log cos x + 4(log cos x)² = **1**; it must be **0**, otherwise the next step does not follow. I also added the rejection of the negative root.
- **Q15 — corrected:** typo 2cos((x+5)/2) for 2cos((x+y)/2), and the PDF stops at "put x = y = π/3" without working out sin x + cos y. I added that final step.
- **Q16 — corrected:** the PDF solution is incomplete and mislabelled. It writes "x = 60°, y = 30°" where x, y are tan θ₁, tan θ₂ (the intended case is θ₁ = 30°, θ₂ = 60°), and it stops at θ₂/θ₁ = 2 without using the area or finding the perimeter. I added the missing steps: AC = a/√3, the area gives a = 3 − √3, and the perimeter is (3 − √3)(3 + √3) = 6.
- **Q17 — corrected:** "tan θ − 1" should read tan θ = −1; I added a check that both tangents are defined at all six solutions.
- **Q18 — corrected:** the compound-angle line is labelled tan(α+β) instead of tan(α+2β).
- All other questions (Q1–Q8, Q10, Q13) — `pdf`: the working was checked step by step and reproduced as printed.

## Answer key
- Every printed answer was checked by direct numerical evaluation (Python) and is correct: A, C, C, D, B, D, D, A, B, B, A, C, D, C, A, 6, 2, 1. No answer key errors were found.
- Note on Q5: the printed solution's value of L, 1/(2√2) − ½cos(π/8), matches neither option A nor D. That is correct: only option B (about M) is true.

## Alternate solutions and useful results
- **Alternates: all 18 questions (Q1–Q18) have one alternate each.** Each one uses a genuinely different method and was checked against the answer. Examples: Q1 uses the cosine rule in sine form; Q3 uses the identity cos³θcos3θ + sin³θsin3θ = cos³2θ; Q9 writes the equation as a sum of squares; Q12 uses the a cos 2x + b sin 2x = k form; Q13 uses complex numbers; Q18 uses arg[(7+i)(3+i)²].
- Questions with NO alternate: **none**.
- Two alternates are weaker in originality and are noted here for review:
  - **Q4** uses special-value elimination (θ = π/3), which only works because the question is single-correct.
  - **Q6** uses a different factorisation, (2cosθ+1)(2cosθ−1) with half-angle telescoping. It is still a telescoping argument.
- **Useful Result / Pattern: all 18 questions have 4–5 bullets each.** The formulas were checked numerically on sample values.

## make_ppt.py warnings
- The build printed no warnings: "Equations: 717 converted to native PowerPoint equations. Saved … (114 slides, 18 questions)". No "could not convert" notes, so no equation was left as LaTeX text.
- Checked inside the .pptx XML that all 18 "Correct Answer" boxes and all 18 "Same answer" boxes are present.

## Skipped, assumed or guessed
- Skipped (not available in this environment): `recalc.py`, thumbnail and soffice rendering, and visual inspection of the rendered slides.
- **Q16 has a figure.** The deck cannot show the image, so the question text describes it in brackets: ABDC is a rectangle, E lies on BD produced, θ₁ = ∠CBA and θ₂ = ∠ECD. I read this layout from the PDF figure and the PDF solution.
- Q16–Q18 are labelled "Integer Type(0 to 9)" because the paper's header says "INTEGER TYPE QUESTIONS" and all three answers are single digits.
- Levels are my calibrated judgement. Confidence is Medium for Q2, Q3, Q6, Q9, Q11, Q14, Q15, Q16 and Q17 (details in the Excel workbook).
- The Hindi translations in the PDF were left out. The deck uses the English text only.
