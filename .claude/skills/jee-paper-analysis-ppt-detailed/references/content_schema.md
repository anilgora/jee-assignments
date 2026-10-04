# Content file (JSON) - schema and writing rules

The deck is built by `scripts/make_ppt.py` from one JSON file per paper. The file is also the
user's editable record: they may fix a word, a level or an answer in it and simply re-run the
script. Keep it clean and human-readable (UTF-8, `indent=1`, `ensure_ascii=False`).

A working excerpt (Q4, Q10, Q11 of PRT 06: complete solutions, two alternates, results) is
`example_PRT_06_detailed_content.json` in this folder. This is the DETAILED-SOLUTIONS edition: it adds the
fields `solution_source`, `correction_note`, `alternate_solutions` and `useful_results`, and changes what
`solution` must contain.

## Top level

| Key | Required | Meaning |
|---|---|---|
| `title` | yes | Title slide, e.g. `"PRT 06 — Paper Analysis"` (em dash as in the sample) |
| `subtitle` | yes | e.g. `"Paper 01"` |
| `source` | no | File names used; not printed |
| `questions` | yes | List in paper order (see below) |
| `air_marks` | no | List of `[rank, marks]` pairs, e.g. `[["AIR 100", "44 ± 2"], ["AIR 1000", "33 ± 2"]]`. Only when the user supplies them - never invent. If absent, the slide is skipped. |
| `sections` | no | Section dividers: `[{"title": "Single Correct Type", "from": 1, "to": 4, "marking": ["+3 if only the correct option is chosen", "0 if unanswered · −1 otherwise"]}, ...]`. Take the marking lines from the paper's section header, one short line each. If omitted, sections are grouped automatically by type and marks. |
| `reference_indices` | no | Rows for the final comparison slide, e.g. `[["JEE Advanced 2027", 3.10], ...]`. Replaces the built-in list (2021, 2023-2026) entirely, so include every year you want shown. |
| `paper_name` | no | Name of this paper in the comparison table; default is the title before the dash plus the subtitle, e.g. "PRT 06 Paper 01" |
| `level_labels` | no | Overrides for level descriptions, keyed by level as text (`"2.5"`). Defaults are in the script and in SKILL.md. |

## Each question

| Key | Required | Meaning |
|---|---|---|
| `q_no` | yes | Continuous number 1..N, even if the paper restarts numbering per section |
| `type_label` | yes | Printed before `(n Marks)` - use the exact strings in the table below |
| `short_type` | yes | Shorter form for the difficulty table |
| `marks` | yes | Full marks for the question |
| `concepts` | yes | List of 1 or 2 concept strings (rule below) |
| `level` | yes | The **adjusted level** from the jee-advanced-difficulty-calibrated skill (0-5, halves allowed, e.g. 2.5, 3.5) |
| `paragraph` | no | Passage text for paragraph-based questions; printed before the question |
| `question` | yes | Question stem. Use `\n` only for a genuine line break |
| `options` | no | List of option texts without the `(A)` prefix; omit for integer/numerical |
| `answer` | yes | Printed after `Correct Answer:` - e.g. `"(B) 2"`, `"(A, C, D)"`, `"(C)"`, `"4"` |
| `key_idea` | yes | One sentence for the amber "Key idea" strip at the top of the first solution slide (rules below) |
| `solution` | yes | The **complete** primary solution: list of bullet strings, one step each (rules below); never empty |
| `solution_source` | yes | `"pdf"` (PDF working is correct and reproduced as is), `"corrected"` (PDF working was wrong - fixed) or `"written"` (PDF had no usable solution - written from scratch) |
| `correction_note` | only if `corrected` | What was wrong in the PDF (which step, what it said) and what is correct. Goes to the speaker notes of the first solution slide. |
| `alternate_solutions` | only for requested questions | List of `{"idea": "one sentence", "solution": ["bullet", ...]}` (a bare list of bullets is also accepted). Rendered right after the primary solution, tagged "Alternate Solution". Omit the field when no list was given or no elegant alternate exists. |
| `useful_results` | only for requested questions | List of 2-5 bullet strings: general results/patterns helpful for this kind of question. Rendered after the alternates, tagged "Useful Result / Pattern". |

### Type labels

| Paper wording / calibrated-skill type | `type_label` | `short_type` |
|---|---|---|
| Single correct (SCQ) | `Single Correct Type` | `Single Correct` |
| One or more than one correct (MCQ) | `One or more than one Correct Type` | `One or More Correct` |
| Paragraph-based single correct (Para SCQ) | `Paragraph Based Single Correct Type` | `Paragraph Single Correct` |
| Integer 0-9 (INT) | `Integer Type(0 to 9)` | `Integer (0-9)` |
| Numerical value (Numerical) | `Numerical Type ` (note the trailing space) | `Numerical` |
| Matching list (MTC SCQ) | `Matching List Type` | `Matching` |
| Numerical question-stem parts (Q Stem) | `Numerical Type ` | `Numerical` |

## Mathematics: LaTeX between `$...$`

The script converts every `$...$` to a native PowerPoint equation with pandoc, so every piece
of mathematics must be inline LaTeX inside single dollar signs that pandoc understands.

- One `$...$` per formula; never `$$`, `\(...\)` or `\[...\]`.
- Use standard commands only: `\frac`, `\sqrt`, `\sin`, `\tan^{-1}`, `\left( \right)`,
  `\lfloor \rfloor`, `\{x\}`, `\mathbb{R}`, `\in`, `\cup`, `\cap`, `\setminus`, `\Rightarrow`,
  `\iff`, `\le`, `\ge`, `\neq`, `\binom{n}{r}`, `\sum_{k=1}^{n}`, `\lim_{x\to0}`, `\vec{a}`,
  `\triangle`, `^\circ`. Avoid `\displaystyle`, `\dfrac`, macros and environments.
- Plain words stay outside the dollars: `$f$ is one-one`, not `$f \text{ is one-one}$`.
- In JSON every backslash is doubled: `"$\\frac{1}{2}$"`.
- A literal dollar sign (currency) cannot appear; write "Rs".
- **Matrices and determinants** are supported and become real PowerPoint matrices: `\begin{matrix} a & b \\ c & d \end{matrix}` (no brackets; wrap it as `\left| \begin{matrix} ... \end{matrix} \right|` for a determinant, `\left( ... \right)` or `\left[ ... \right]` for brackets), also `\begin{smallmatrix}`, `\begin{pmatrix} a & b \\ c & d \end{pmatrix}` (round brackets), `\begin{bmatrix}` (square), `\begin{vmatrix}` (determinant bars), `\begin{Vmatrix}` (double bars), `\begin{array}{cc} ... \end{array}` (optionally wrapped in `\left| ... \right|`) and `\begin{cases} ... \end{cases}`. Rows end with `\\`, entries are separated by `&`; in the JSON every backslash is doubled again (`\\begin{pmatrix}` ... `\\\\`). Entries may contain fractions, roots, powers and nested determinants.
- Every converted equation is checked against the OMML (PowerPoint equation) schema rules before it is embedded. If one cannot be made safe, the script keeps it as plain LaTeX text on the slide and prints `could not convert $...$ (reason)` - it never writes XML that would make PowerPoint "repair" the file and empty the slide.

## Concepts rule (the user's instruction)

Start from the blueprint's `Concept1` and `Concept2`. Decide which chapter each concept belongs
to (the blueprint's `Chapter` column is the question's main chapter; the second concept can come
from another chapter, e.g. "Orthogonality of two circles" inside an ITF question).

- **Both concepts in the same chapter:** summarise them into one concept phrase
  (e.g. "Angle between two circles" + "Diametrical form of circle" ->
  "Angle between circles and diametrical form of a circle").
- **Different chapters:** keep both as separate entries. Very long blueprint wording may be
  trimmed to its core, dropping parenthetical lists
  (e.g. "One-one vs many-one: monotonicity, horizontal line and algebraic tests" ->
  "One-one and many-one functions").
- Ignore the blueprint's Difficulty Level column entirely.

## Primary solution = the complete working (this edition)

- **Copy the PDF's working in full**, in its own method and order, one step per bullet. Keep every
  intermediate expression and number the PDF shows; do not condense, merge or skip steps.
  Only the notation changes (into `$...$` LaTeX).
- A bullet can hold one full step including its small calculation, about 250 characters of converted
  text at most (two to three lines at 24 pt). Typical length: 6-15 bullets per question. The script
  spreads them over as many slides as needed (at most 6 per slide; `--max-bullets` lowers this).
- Multi-statement questions: one bullet per option, giving its verdict, e.g. `... (B) correct.`
- The last bullet states the result; the `answer` field repeats it in the green box.
- **Verify before you reproduce.** Re-derive each step; check the final answer by computation where
  possible. Then set `solution_source`:
  `pdf` if everything is correct; `corrected` (+ `correction_note`) if you had to change anything -
  make the smallest change that makes it correct and keep the PDF's structure; `written` if the PDF
  has no usable solution.
- If the paper's answer key looks wrong, keep the correct answer in `answer` and tell the user which
  question and why - do not silently follow a wrong key.

## Alternate solutions (only for the question numbers the user listed)

- Include `alternate_solutions` **only** for the listed questions. No list given = the field never appears.
- Each alternate uses a genuinely different, elegant idea (symmetry, geometric view, substitution,
  identity, counting bijection, limiting case, shortcut formula). Rewording or reordering the PDF's steps
  is not an alternate. If none exists, say so to the user and leave the field out.
- `idea`: one sentence naming the idea (about 120 characters of converted text), shown in the amber
  "Idea" strip. `solution`: complete bullets, one step each, ending at the same answer as the primary
  solution. It must be verified (numerically where possible).
- Usually one alternate; two when both are worth showing (they are numbered "Alternate Solution 1/2").

## Useful results / patterns (only for the question numbers the user listed)

- 2-5 bullets of **general** statements that help with this kind of question: formulas, identities,
  recognition cues, standard patterns, generalisations. State conditions of validity. Add the instance
  from this question where it helps.
- Not a restatement of the solution. Each formula checked on at least one numerical case.

## Key idea (the amber strip)

The strip opens the solution, so students see the decisive move before the working. Write it for
every question.

- One sentence, at most about 110 characters of converted text (one or two lines at 24 pt).
- Name the single step that unlocks the question - the same thing identified as the key step when
  rating difficulty - phrased as an idea a student can reuse on another question:
  "$OP=r\\sqrt{2}$ makes the tangents perpendicular, so $OAPB$ is a square."
  "On the closed interval $[0,2\\pi]$ both endpoints can be solutions."
- No final answer and no restating of the question; no "Key idea:" prefix (the script adds it).
- LaTeX rules as above.
