# Originality: every question must be brand new (user's instruction, 18-Oct-2026)

The first two test papers failed this: several questions were close copies of well-known problems
(a published JEE Main equation `tan^-1(x+1)+tan^-1(x-1)=tan^-1(8/31)`, the co-normal "sum of ordinates is zero"
problem, the radical-circle theorem, `x = sec t, y = tan t`, `|sin pi x| + |cos(pi x/3)|`, `(1+tan)/(1+sin)` limits).
"Original" means a new problem, not a known problem with new numbers.

## What counts as new
A question is new when its **mechanism** is new: the object, process or relation the solution turns on is one that
does not appear as a standard exercise, a past-year problem or a textbook example. Standard *ingredients* (a formula,
a theorem) are allowed; a standard *skeleton* with changed constants is not.

Ways to build a new mechanism (pick one per question, and say which):
1. **Iteration / recursion.** A map applied repeatedly (a chain of points, angles, circles) with a clean closed form
   or a clean asymptotic (e.g. normals of a parabola meeting the curve again, then again; theta_{n+1} = arctan(sec theta_n)).
2. **Function defined by a limit or a construction** (a p-norm limit of fractional parts, a max/min of two sawtooth
   functions, a function of a moving point) and then analysed (continuity, corners, counts).
3. **A family defined by two conditions** whose joint property is not a textbook theorem (circles orthogonal to a given
   circle through a given point: common point, concurrency, extremal radius).
4. **A configuration with a hidden symmetry or invariant** that makes an apparently messy quantity clean (a billiard path
   in a wedge by double reflection; a limit where two orders cancel).
5. **A new combination of two ideas** in which the link itself is the discovery.
Constants alone never make a question new. Changing 8/31 to 5/17 does not.

## Known skeletons: do not use as the core of a question
See `known_skeletons.md`. The build script warns on the ones it can pattern-match.

## Process, for every question
1. Name the mechanism (one of 1-5 above) before writing the stem.
2. **Provenance check.** Ask: could a prepared student recognise this as a standard problem within 20 seconds? Would
   it be filed under a familiar title ("normals from a point", "radical centre", "period of |sin|+|cos|",
   "1^infinity with tan - sin")? If yes, change the mechanism, not the numbers.
3. **Web check (when a search tool is available).** Search the distinctive structure in words and symbols, e.g.
   `theta_{n+1} = tan^{-1}(sec theta_n)`, `lim ({x}^n + {1/x}^n)^{1/n}`. If a near-identical problem appears, redesign.
   A search that finds only the ingredient (a textbook relation) but not the construction is acceptable; say so.
4. Verify the answer by code **and** by an independent numerical route (brute force, simulation, high-precision check).
5. Fill `originality_note` in the question file: `New: <the mechanism>. Closest known: <the nearest standard problem>.
   Different because: <what changes the solution>.` and `web_check`: `not found`, `ingredient only` or `not available`.

## In the reply
Report, per question, whether the web check was done and what it found, and flag any question whose ingredient is
standard. Do not claim a question is "new" without having done steps 2 and 3. Perfect novelty cannot be guaranteed; say
so plainly and invite the user to name any question they recognise.
