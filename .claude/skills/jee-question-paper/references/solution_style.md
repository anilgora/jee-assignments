# Style guide for shortened solutions

## Reader
A student at about the 90th percentile who **knows the concept** the question tests but has not
seen this question. Every line must be followable by that student without filling in a gap of more
than one routine step.

## Approved level of detail (user feedback, 7-Oct-2026)
The first version, compressed as far as possible (about 2 pages for 17 questions), was rejected as
too short. The approved version was about 4 pages for 17 questions, roughly 35-45% of the
original solutions. Aim for that.

Keep:
- The key idea in words where it is not obvious ("Adding 3: ... so $b_n$ is a GP").
- The reason for each non-routine step (why $I$ and $N$ commute, why parallel planes are disjoint,
  why a value is included in a set).
- Intermediate results of computations: one line of determinant expansion, the discriminant
  simplification, values of power sums, endpoint values of a function.
- For one-or-more-correct questions: each statement on its own line ending
  "so (X) is correct" / "so (X) is wrong", using **this file's option letters**.
- Interval-by-interval checks when counting roots, each with its reason.

Drop:
- Restating the question or given data.
- "We know that", "Now", "Thus we get", "Final Answer:" duplicates inside the body.
- Separate lines for single arithmetic moves; merge with $\Rightarrow$.
- Decimal approximations unless they settle a comparison.

Method:
- Use a shorter method only if it is **standard** for the reader (e.g. Newton's power sums instead
  of the cubic discriminant formula). Never replace with a trick the reader is unlikely to know.
- If the original solution makes an arbitrary or unjustified choice, keep it honest ("Taking ...")
  and flag the question in chat.

Questions without a source solution:
- Write the solution at exactly the same level of detail as the shortened ones; do not make it
  longer because there was nothing to shorten.

## Notation
- Inline maths `$...$`, displayed maths `$$...$$` (only for matrices, cases, telescoping identities
  or other wide expressions).
- Standard LaTeX only: `\frac`, `\dfrac`, `\sqrt`, `\begin{pmatrix}`, `\begin{vmatrix}`,
  `\begin{cases}`, `\Rightarrow`, `\in`, `\cup`, `\setminus`, `\mathrm{tr}`, `\mathrm{adj}`.
- Prose in plain text outside the dollar signs. No bullets, no bold inside solutions (except the
  paragraph sub-headings that the Master format already uses).

## Worked examples (approved)

Recurrence question. Original: 21 lines. Shortened:
```
Adding 3: $a_{n+1}+3=2(a_n+3)$, so $b_n=a_n+3$ is a GP with $b_1=4,\ r=2$
$\Rightarrow b_n=4\cdot 2^{n-1}=2^{n+1}$
$k,m,n$ in AP $\Rightarrow k+n=2m$; with $k+m+n=9$: $3m=9\Rightarrow m=3$
$b_k,b_m,b_n$ in GP with ratio 4: $\dfrac{b_m}{b_k}=2^{m-k}=4\Rightarrow m-k=2\Rightarrow k=1$, and $n=2m-k=5$
$a_n=a_5=b_5-3=2^{6}-3=61$

Correct Option: (B)
```

Determinant question:
```
Non-trivial solution $\Rightarrow |(AB)^T|=0$
$|(AB)^T|=|AB|=|A||B|=0$
$|B|=1(1-0)-2(2-0)+1(0-1)=-4\neq 0\Rightarrow |A|=0$
$|A|=1(\lambda-0)-0+1(2-0)=\lambda+2=0\Rightarrow \lambda=-2$

Correct Option: (B)
```

Multi-correct statement lines:
```
(C) $n=12$: entries $12\sin\theta=6,\ 12\cos\theta=6\sqrt{3},\ 12\cdot\frac{1}{2\sqrt{3}}+33\cdot\frac{\sqrt{3}}{2}=\frac{37\sqrt{3}}{2}$
Sum of all elements $=3+6+6\sqrt{3}+\frac{37\sqrt{3}}{2}=9+\frac{49\sqrt{3}}{2}\neq 73+27\sqrt{3}$, so (C) is wrong
```

Too short (rejected) - do not write like this:
```
$|(AB)^T|=|A||B|=0$; $|B|=-4\neq0\Rightarrow|A|=\lambda+2=0\Rightarrow\lambda=-2$
```
