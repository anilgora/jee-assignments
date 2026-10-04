# Calibrated Rubric - the user's 0-5 scale

This rubric was reverse-engineered from the user's own ratings of 172 official JEE Advanced
maths questions (2021, 2023, 2024, 2025, 2026). It describes how *this user* grades, which differs
in important ways from a generic "how hard is this" judgement. Where this file and your own
instinct disagree, this file wins, because it was built from the user's actual decisions.

## Contents
1. The reference student
2. What the scale means
3. The factors that decide the level (in order of weight)
4. Level descriptors with anchors
5. Decision procedure
6. Known quirks of this user's scale
7. Reference statistics
8. Calibration history
9. Equivalence relations and the multi-correct floor (read this)

Every question gets an integer **level** (0-5) on the user's scale, judged with sections 1-6
(question format is already part of that judgement, exactly as in the user's own ratings), and an
**adjusted level** from the two rules in section 9. The marks-weighted difficulty index is computed
on the adjusted level.

---

## 1. The reference student

Judge every question against a strong JEE Advanced aspirant working under exam conditions: knows
the whole syllabus, has solved thousands of coaching-style problems, is good but not exceptional,
and has about 3 minutes per mark. Never rate by how easy the question is for you. A model finds
almost every question easy; rating that way collapses everything to Level 1-2, which is exactly
the error the first version of this rubric made (it ran half a level too low on the 2026 blind test).

## 2. What the scale means

| Level | User's label | What it means in practice | Share of official questions |
|---|---|---|---|
| 0 | Easier than JEE Main | Direct evaluation or a single formula; no decision at all | 2% |
| 1 | JEE Main level | One well-known trick or result, applied once | 10% |
| 2 | Easier than Advanced | Routine but multi-step: several standard results chained, no real insight | 23% |
| 3 | Average Advanced | Two ideas linked, or several statements each needing a genuine check | 27% |
| 4 | Slightly difficult | A non-routine key idea, or careful counting / casework where one slip gives a wrong answer | 32% |
| 5 | Very difficult | Hardest ~6% of real Advanced questions (see section 4) | 6% |

Two consequences that surprise people:

- **The scale is anchored inside JEE Advanced, not above it.** Level 4 is the user's most common
  rating for official Advanced questions. Level 5 is *not* Olympiad territory: it is the top slice
  of real Advanced papers. Do not reserve 5 for RMO/INMO-grade problems.
- **Level 1 is rare for Advanced-style work.** A question needs only one familiar move to be
  Level 1 (the king property on a simple integrand, "row-equivalent to I means invertible").
  As soon as the student must chain three or more routine steps, it is Level 2, even if nothing in
  it is hard (2026-P2-Q1 vector area, 2026-P2-Q2 perpendicular tangents, 2026-P2-Q17 angle
  between tangents were all rated 2, not 1).

## 3. The factors that decide the level (in order of weight)

**F1. Idea availability - the strongest factor.** Ask whether the key idea is one a prepared
student has practised many times. The user rates by *how likely the student is to have met the
idea*, not by how short the solution is once you know it.
- A familiar single trick keeps the question at 1-2.
- An idea outside the usual coaching pattern pushes the question up by 1-2 levels even when the
  solution is three lines. Examples: 2026-P2-Q9 (Mobius map preserving the upper half-plane,
  order of a 2x2 matrix) rated **5**; 2026-P1-Q15 (orthogonal matrix, MM^T = I, columns as
  orthonormal vectors) rated **4** even as a matching question; 2026-P2-Q5 (Leibniz on
  (x-1)^10 (x+1)^10 hidden in a 10th derivative) rated 4.

**F2. Precision risk.** Counting, casework or a long exact computation where a single slip gives
a wrong final answer, with no options to check against. This is the main road to 4 and 5 in
numerical questions: 2025-P1-Q10 (overlapping digit casework) 5, 2026-P1-Q9 (partitions of 10 with
sum of squares 42, then counting with equal-size blocks) 5, 2023-P2-Q12 (counting invertible
matrices) 5, 2026-P2-Q14 (discontinuity counting with cancellations) 4.

**F3. Chain length.** Number of distinct stages the student must get through. Three or more
genuine stages with an insight somewhere is typically 4; with heavy execution on top, 5.

**F4. Heavy computation - it counts.** Unlike many rubrics, this user lets long precise
computation reach Level 5 in numerical format: 2021-P1-Q10 (locus distance), 2023-P1-Q10
(7 5...5 7 sum), 2023-P2-Q14 (triangle area with heavy trig). Do not cap "grind" at Level 3.
In option-based questions the same grind usually lands at 3-4, because options let the student
check.

**F5. Format - a moderate nudge inside the level, not a cap.** The user's official-paper
ratings already reflect format, so judge it the same way (there is no separate format adjustment).
- Numerical / integer answers and one-or-more-correct questions are harder to score than the same
  mathematics as single-correct: no options to check against, or every option to judge with
  negative risk. Numericals average about half a level higher than option-based questions.
- Matching (MTC) questions average about 2.1: four short items with elimination possible.
  But an MTC with an unfamiliar idea still reaches 4 (2026-P1-Q15). Never cap by format.
- Any format can reach 5: 2026-P2-Q9 is a multi-correct question at Level 5.
- A one-or-more-correct question involving several concepts never ends below 2.5 (section 9).

**F6. Number of chapters or concepts - weak.** Multi-chapter questions average higher (about
3.5 vs 2.8), but 2025-P1-Q15 spans three chapters and was rated 1. Use it only as a tie-breaker.

## 4. Level descriptors with anchors

Use `anchors.md` for the full bank; these are the clearest examples per level.

- **Level 0** - one formula, no decision. 2024-P2-Q1 (tan of an inverse-trig combination),
  2024-P2-Q11 (dot with p x q gives gamma), 2023-P1-Q15 (mean/median/mean deviation of a table).
- **Level 1** - one familiar move. 2021-P2-Q17 (inclusion-exclusion), 2024-P2-Q3 (1^infinity
  limit), 2025-P1-Q7 (Apollonius circle), 2026-P1-Q3 (invertibility), 2026-P2-Q4 (king property).
- **Level 2** - routine chain, no insight. 2023-P2-Q9 (linear DE then maximum), 2021-P1-Q18
  (cot ratio via cosine rule), 2026-P2-Q3 (separable DE with quartic finish), 2026-P2-Q12
  (recover two observations from means and variances).
- **Level 3** - two ideas linked or statements needing genuine checks. 2021-P1-Q15 (telescoping
  cot^-1 statements), 2023-P2-Q2 (toss until two consecutive match), 2026-P1-Q7 (g = x f(x)
  implications with counterexamples), 2026-P1-Q11 (bounded distribution count).
- **Level 4** - non-routine key idea or high-precision casework. 2021-P2-Q9 (parity of exponents
  decides extrema), 2023-P2-Q13 (radical axis through tangent midpoints), 2025-P2-Q16 (king-type
  substitution with tan^-1), 2026-P2-Q6 ((r+2)(s+2) = 3 factoring), 2026-P1-Q12 (telescoping
  product via cos 3a / cos a).
- **Level 5** - top slice. Either (a) an unfamiliar idea plus several stages (2026-P2-Q9,
  2023-P2-Q11 octagon product via z^8 - 2^8), or (b) a long chain with heavy, exact execution or
  delicate overlapping casework and no options (2025-P1-Q10, 2026-P1-Q9, 2023-P2-Q12,
  2021-P1-Q10, 2023-P1-Q10, 2023-P1-Q12, 2023-P2-Q14, 2024-P1-Q13).

## 5. Decision procedure

For each question:

1. Solve it completely. You need the real route to judge it; the printed solution can be
   clumsier or slicker than what a strong student would find.
2. Name the key step - the single thing that decides whether the student gets it.
3. Find 2-3 nearest anchors in `anchors.md`: same chapter first, then same kind of demand
   (same trick, same counting style, same format). Note how they were rated.
4. Place the question relative to those anchors, then check it against F1-F6:
   - Unfamiliar idea? Move up 1-2 from where the solution length alone would put it.
   - Only one familiar move? Level 1 (or 0 if there is no decision at all).
   - Three or more routine steps with no insight? Level 2, not 1.
   - Numerical answer with casework or long exact computation? Consider 4-5.
5. Record the nearest anchor and a confidence (High / Medium / Low). Use Low when the anchors
   point in different directions or the question type has no close anchor.

## 6. Known quirks of this user's scale

- **Question-stem and paragraph parts** are rated separately and tend to be high: 17 of the 24
  question-stem parts in 2021-2025 were Level 4. The second part is not automatically harder
  (harder in 4 of 10 pairs, equal in 4, easier in 2).
- **Recent ratings run higher.** The 2026 ratings sit about half a level above what the
  2021-2025-based rubric predicted, and a routine planes question (2026-P1-Q6) was rated 3 while
  a similar one in 2024 (2024-P2-Q6) was rated 1. When anchors from different years conflict,
  lean towards the more recent year.
- **A few 2021 ratings are unexplained** (2021-P1-Q5/Q6 complement probabilities at 4; 2021-P1-Q7
  at 1 but 2021-P1-Q8 at 4 from the same consistency condition). Do not generalise from them.

## 7. Reference statistics (user's ratings)

Marks-weighted difficulty index = sum(marks x level) / sum(marks). These are the user's ratings as
given; they already include format and topic, so no adjustment is applied to them. Compare a new
paper's **adjusted** index with them.

| Year | Weighted index | Mean level | Marks at Level 0-1 | Marks at Level 4-5 | Level-5 questions |
|---|---|---|---|---|---|
| 2021 | 2.76 | 2.89 | 16 | 34 | 1 |
| 2023 | 3.19 | 3.15 | 13 | 47 | 5 |
| 2024 | 2.59 | 2.56 | 28 | 40 | 1 |
| 2025 | 3.21 | 3.19 | 8 | 65 | 1 |
| 2026 | 3.02 | 2.94 | 6 | 38 | 2 |

Average level by type (all 172): SCQ 2.4, MCQ 2.9, MTC 2.1, INT 3.0, Numerical 3.6,
Q Stem 3.5, Para SCQ 3.8.

These numbers describe **official JEE Advanced papers**. A full mock in the Advanced pattern
should usually land between about 2.6 and 3.2. Coaching assignments, DPPs and chapter sheets have
no expected distribution - do not force their spread to match these numbers; report it as it is.

## 8. Calibration history

- **v1 (built from 2021-2025 only)**, blind-tested on 2026: exact match on 12 of 34 questions,
  within one level on 31 of 34, but on average 0.56 levels too low, with no Level 5 at all. The
  three 2-level misses were 2026-P1-Q6, 2026-P1-Q15 and 2026-P2-Q9.
- **v2** adds: idea availability as the lead factor (F1), removal of all format caps,
  a raised floor (routine multi-step = Level 2), and the 2026 questions in the anchor bank.
  v2 has not yet been blind-tested; the next set of user ratings is its first real test.
- **v2 check (27-Sep-2026):** the user accepted every level v2 gave for two coaching
  tests (RPT 02 Paper 2, PRT 06 Paper 1; 17 questions each).
- **v3 (this file):** adds the two user rules in section 9 (equivalence-relation adjustment,
  multi-correct floor). A proposed +0.3-0.5 format adjustment was withdrawn by the user because the
  official-paper ratings already include format; format stays inside the level (F5).

## 9. Equivalence relations and the multi-correct floor

**Adjusted level = min(5, max(level + equivalence adjustment, multi-correct floor))**

**Equivalence adjustment: +0.5.** Set `eq_relation` when the key step needs any of: deciding
whether a relation is an equivalence relation (reflexive, symmetric, transitive checks framed around
equivalence), finding or describing equivalence classes, counting equivalence relations
(partitions, Bell numbers), or decoding a condition into an equivalence relation. Why: these topics
are newly added to the JEE Advanced syllabus, little practice material exists, and students are
relatively weak in them. Do not set it for relation questions that never touch equivalence (e.g.
counting relations with a size condition only). Do not also raise the integer level for the same
unfamiliarity - the adjustment already carries it - but other unfamiliar elements (such as
composition of relations) still count under F1.

**Multi-correct floor: 2.5.** A one-or-more-correct (MCQ) question that involves two or more
distinct concepts never ends below 2.5, however routine each statement is. Set `multi_concept`
when the statements draw on at least two different concepts (e.g. an equivalence relation plus a
bijection check, or range plus inverse plus IVT). Several older anchors sit below this
(2021-P2-Q6 at 1; 2021-P1-Q11, 2021-P2-Q1, Q3, Q5 at 2); the rule overrides them for new ratings.

The official-paper ratings already reflect all of this, so these rules apply only to new papers
you rate, never to the anchors.
