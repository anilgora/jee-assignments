# Taxonomy and Exact Strings

These strings must match the user's generation pipeline character for character, because the
Blueprint sheet is read directly by their script and the values are interpolated into the prompt
sent to the model. A mismatch silently changes what gets generated.

## Question types

Use exactly one of these in the `Q Type` / `question_type` field:

- `Single Correct Type`
- `One or More Than One Correct Type`
- `Numerical Type`
- `Integer Type (0 to 9)`
- `Paragraph Based (Two Single Correct)`
- `Paragraph Based (Two Numerical)`
- `Matrix Match`

Mapping from formats that appear in real assignments:

| Printed in the assignment | Record as |
|---|---|
| MCQ, single option correct, "only one option is correct" | `Single Correct Type` |
| Multiple correct, "one or more options" | `One or More Than One Correct Type` |
| Assertion-Reason (Statement 1 / Statement 2) | `Single Correct Type` |
| Subjective / prove-that / show-that | `Numerical Type` if the answer reduces to a value, otherwise record as `Numerical Type` and note the conversion in the justification |
| Fill in the blank with a number | `Numerical Type` |
| Answer is a single digit 0-9 | `Integer Type (0 to 9)` |
| Comprehension / passage with 2 MCQs | `Paragraph Based (Two Single Correct)` |
| Comprehension with 2 numerical answers | `Paragraph Based (Two Numerical)` |
| Comprehension with 3+ questions | Record each sub-question on its own row with the nearest paragraph type, and note the count in the justification |
| Column I / Column II matching, List-I / List-II | `Matrix Match` |

## Difficulty level labels

The numeric level drives the analysis; the label string is what the generation script feeds back
into the prompt. Both go in the report.

| Level | Label string |
|---|---|
| 0 | `Easier than JEE Main Level(Level 0)` |
| 1 | `JEE Main Level(Level 1)` |
| 2 | `A little easier than JEE Advanced(Level 2)` |
| 3 | `JEE Advanced(Level 3)` |
| 4 | `A little more difficult than JEE Advanced(Level 4)` |
| 5 | `Very difficult than JEE Advanced(Level 5)` |

Note the absent space before each opening parenthesis - that is how the source prompt is written.

## Blueprint sheet columns

The generation script reads these column names. Two of them are inconsistently spaced in the
original (`Concept1` with no space, `Concept 2` with one). Preserve that inconsistency exactly, or
`pandas` will raise a `KeyError` when the script runs.

| Column | Contents |
|---|---|
| `Sr No` | Integer, starting at 1 |
| `Chapter` | Chapter name, from the list below |
| `Concept1` | Primary concept - no space in the header |
| `Concept 2` | Secondary concept, blank if the question is single-concept - one space in the header |
| `Q Type` | One of the question-type strings above |
| `Difficulty Level` | The label string above |

## Chapter names

Prefer these standard names so tagging stays consistent across assignments. If a question does not
fit, use the name printed in the assignment rather than forcing it into this list.

**Algebra** - Quadratic Equations · Complex Numbers · Sequences and Series · Permutations and
Combinations · Binomial Theorem · Matrices · Determinants · Probability · Mathematical Reasoning

**Calculus** - Functions · Limits · Continuity and Differentiability · Methods of Differentiation ·
Application of Derivatives · Indefinite Integration · Definite Integration · Area Under Curves ·
Differential Equations

**Coordinate Geometry** - Straight Lines · Circles · Parabola · Ellipse · Hyperbola

**Trigonometry** - Trigonometric Ratios and Identities · Trigonometric Equations · Inverse
Trigonometric Functions · Solution of Triangles

**Vectors and 3D** - Vector Algebra · Three Dimensional Geometry

## Concept tagging

Concepts are narrower than chapters and should name the specific technique or property being
tested. Two examples of the intended granularity:

- Chapter `Definite Integration`, Concept1 `King's rule (a+b-x property)`, Concept 2
  `Periodic functions`
- Chapter `Circles`, Concept1 `Radical axis`, Concept 2 `Family of circles`

Leave `Concept 2` blank rather than padding it with something vague. A blank cell is honest
information: it says the question is single-concept, which is itself a difficulty signal (see
override rule 4 in the rubric).
