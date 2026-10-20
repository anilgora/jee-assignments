# Vector_3D: generation report

Blueprint: `qp_blueprints/Vector_3D.xlsx`. There is no `Vector_3D_config.xlsx`, so the check ran without `--config`.
This paper was made by a scheduled run on 20-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly). This was the last blueprint without an output folder.

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy, mpmath and python-docx were missing for `python3` (/usr/local/bin/python3). I installed them with `python3 -m pip install ...`; plain `pip` installs into a different Python. One writer also installed scipy for its numerical cross-checks.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- The final `build_paper.py --blueprint` run had **no errors and no warnings**. No script was edited and no check was weakened.
- I rendered page 1 of each of the three PDFs and looked at it. The Hindi is shaped, the equations are 2D, and the solutions are laid out correctly. This paper has no paragraph question.

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the blueprint has only Single Correct and Numerical types and nothing above level 3.
- **Paper:** 66 questions (blueprint Sr No 735-800). Q1-Q12 are Single Correct and Q13-Q66 are Numerical.
- **Reorder (`--reorder`):** old Sr No -> new Q:
  743->1, 760->2, 764->3, 766->4, 767->5, 773->6, 780->7, 782->8, 793->9, 794->10, 798->11, 799->12, 735->13, 736->14, 737->15, 738->16, 739->17, 740->18, 741->19, 742->20, 744->21, 745->22, 746->23, 747->24, 748->25, 749->26, 750->27, 751->28, 752->29, 753->30, 754->31, 755->32, 756->33, 757->34, 758->35, 759->36, 761->37, 762->38, 763->39, 765->40, 768->41, 769->42, 770->43, 771->44, 772->45, 774->46, 775->47, 776->48, 777->49, 778->50, 779->51, 781->52, 783->53, 784->54, 785->55, 786->56, 787->57, 788->58, 789->59, 790->60, 791->61, 792->62, 795->63, 796->64, 797->65, 800->66.
- **Answer Plans:** the blueprint had none, so the script drew all 66. Every answer matches its plan; the build checks this.
  - SCQ: Q1 C, Q2 A, Q3 B, Q4 D, Q5 A, Q6 B, Q7 D, Q8 C, Q9 A, Q10 C, Q11 B, Q12 D (A, B, C and D three times each).
  - Numerical: the styles are those printed by the check (see `_source/blueprint.json`, field `answer_plan`). The answers are in the table below.
- **Cells containing ";":** "Range of a.sin(x) + b.cos(x); maximum and minimum" (Q17) and "Coordinates in space; distance and section formulae" (Q60, Q61). There was no config, so each was kept as **one** concept. Both read as single concepts.
- **Warnings** (recorded, not fixed; the blueprint was not edited; there were no errors):
  - Q2, Q25, Q33 and Q41 list 3 concepts and Q32 lists 4, which is unusual for the Main pattern. All were kept, and every question uses all of its concepts.
  - Concepts repeat across rows (about 80 "concept used in Qx and Qy" warnings), as expected in a one-chapter paper of 66 rows. Every use has its own mechanism. A cross-paper check (below) removed the setups that were reused.

## Level distribution and index
- Level 2: 33 questions. Level 3: 33 questions. These match the blueprint targets exactly; **no question is one level off its target**.
- Marks-weighted index (SCQ 3 marks, Numerical 4 marks): **about 2.50**. There are no equivalence relations and no MCQs, so neither adjustment applies. This is a JEE Main pattern chapter test, so the index follows the blueprint.
- **Consistency pass** (sorted by level, neighbours compared):
  - **Low confidence:** Q10 (bisector plane selecting one of two tangent circles) and Q28 (third vertex from an area / projected-area ratio) are rated 3, but either could be read as 2.
  - **Could be read lower:** Q19 and Q24 are the borderline Level 3 numericals.
  - **Could be read higher:** Q38 (images in a pencil of planes lie on a circle) and the redesigned Q52 (r x (r x a) = c, solved by dotting with c) could be read as 4.
  - Most anchors come from Vector 3D: 2023-P1-Q16 (L3), 2026-P1-Q6 (L3), 2021-P1-Q19 (L3), 2026-P2-Q1 (L2), 2021-P2-Q5 (L2).

## How the paper was made, and the cross-paper check
The 66 questions were written in six parallel batches. Each batch was verified in sympy plus an independent numerical route: brute force, explicit coordinate reconstruction, random sampling or minimisation. I then compared every question's mechanism and objects across the whole paper. Five questions clashed with another question or with published material, so I redesigned them (the versions in the table are the final ones):
- **Q52:** the original (r fixed by r x a = b and r x c = d) was the same setup as Q7. The new version is r x (r x a) = c.
- **Q59:** the original was a weighted-centroid sum of squared distances, the same mechanism as Q56. The new version is a tetrahedron with two pairs of perpendicular opposite edges, using the cosine rule in three faces.
- **Q62:** the original was "lines coplanar for exactly two k (quadratic determinant)", the same as Q6 and also the JEE Main 2012 skeleton. The new version is a transversal through O fixed by two coplanarity determinants, then compared with the shortest distance.
- **Q64:** the original was the PA.PB = k sphere, a published exercise. The new version is "sum of squared distances from the three axes = 3 PA^2".
- **Q66:** the original used the same sphere centre and the same "tangents to a section circle" frame as Q12. The new version is a chord of a section circle and the inscribed-angle theorem.

The writers also redesigned during writing:
- **Q9:** the first version was a standard origin-side bisector question.
- **Q11:** the first version's correct answer equalled a given radius.
- **Q24:** the first version was the setup of 2006 AIME I #14.
- **Q43:** the first version was a common JEE Main item.
- **Q58:** the first version was the "three equal forces along the sides of a triangle" result.
- **Q63:** the first version was a published PA^2+PB^2 = 2PC^2 plane.
- **Q22:** components were removed from the stem.
- **Q33:** "skew" was added, because the lines meet at mu = 7.

## Problems found while verifying (all fixed)
- **Q5:** a sign slip in the full solution's check line was fixed; the plane is 4x-4y-7z+4 = 0.
- **Q11:** a distance in the full solution was corrected to sqrt(27/2).
- **Q33:** the first design was degenerate (L1 met the z-axis for every mu).
- **Q46:** the first solution used the cubic discriminant formula. It was replaced by the product f'(alpha) f'(beta) f'(gamma) = -81.
- **Second roots and branches** are removed by conditions in the stem:
  - c > 0 in Q28;
  - a < 0 in Q32;
  - "right-handed" in Q43;
  - 0 < x < 1 in Q45;
  - "in the plane of the triangle" in Q53;
  - the mirror perpendicular to the xy-plane in Q55.
- **Uniqueness checks:**
  - Q52 has two solutions, r = +/-(3i - j + 4k), and both give |r|^2 = 26.
  - Q38's family misses one plane, but the maximum is still attained.
  - Q59's tetrahedron exists (Gram determinant > 0).

## Rows whose concepts were hard to combine naturally
- **Q15** (direction cosines + complex number): joined through w = l + i m with |w|^2 = 1 - n^2. This is the least natural pairing.
- **Q55** (vector angle bisector + straight-line angle bisectors): a reflection problem in the xy-plane, so it is a 2D question in a 3D paper.
- **Q65** (3D locus + "Locus based questions"): the second concept only reads off the intercepts of a 2D line.
- **Q58** (vectors + compound angles): the trigonometric part is a short cos(phi1 - phi2) step.
- **Q32** (four concepts): the coplanarity determinant is itself a scalar triple product. The concepts are separated by using the triple product for the distance.
- **Q31 and Q33:** the answer is asked as a sum (d + beta + gamma, mu - d^2), in JEE Main style but less natural.
- **Q51:** at lambda = 1/4, v and w coincide. This is correct but makes the coplanarity visible.

## Other notes
- **Repeated numerical answers:**
  - -3 appears three times (Q13, Q23, Q65);
  - 113 twice (Q36, Q44);
  - 3.5 twice (Q19, Q29);
  - 0.25 twice (Q16, Q51).

  The plan styles were followed, but you may want to vary one of them.
- **Hindi:** the Hindi is my own translation; please review the specialised terms.
- **Stem review:** a self-check. I read every English stem as a student would (symbols, domains, conditions, one reading, uniqueness, option forms) and found nothing further to change beyond the redesigns above. An independent reader may still find things.

## Originality report
Every question was web-checked with web search on its distinctive structure. Perfect novelty cannot be guaranteed; please tell me if you recognise any question.

Ratings were made on the calibrated rubric.

| Q | Type | Answer | Level (target) | Confidence | Mechanism | Web check | Closest known |
|---|---|---|---|---|---|---|---|
| 1 | SCQ | C | 2 (2) | High | the line is never given; it is defined as the locus of points equidistant from three points (two perpendicular-bisector planes, way 3) and then cut by a plane | ingredient only | the textbook exercise of a point on a coordinate plane equidistant from three points |
| 2 | SCQ | A | 3 (3) | Medium | the plane of the family is fixed by a non-incidence property (the only member that misses M), and the answer uses a hidden invariant: for perpendicular members through l, distance from l equals distance from the other plane, which is constant along M (way 4) | not found | plane through the line of intersection of two planes parallel to a given line, and its distance from the line |
| 3 | SCQ | B | 2 (2) | Medium | a double reflection in two perpendicular planes (way 4: a composite map with a hidden half-turn about their common line) | ingredient only | the image of a point in one plane |
| 4 | SCQ | D | 2 (2) | High | one vertex of the tetrahedron runs along a parabola, so the scalar triple product becomes a quadratic in the parameter whose minimum gives the least volume (way 2: a function of a moving point) | not found | the volume of a tetrahedron with four given vertices, or a parameter fixed by a given volume |
| 5 | SCQ | A | 3 (3) | Medium | the base is given only by three lines of the xy-plane (2D area of a triangle), the apex is located on a given line through the origin by the volume, and the volume is reused with a different face as base to give an altitude (way 5) | not found | volume of a tetrahedron with given vertices, or altitude from a vertex |
| 6 | SCQ | B | 3 (3) | Medium | a one-parameter family of lines in which coplanarity with a fixed line happens for exactly two parameters; the two meeting points and the two base points then span a tetrahedron (way 3: a family defined by two conditions) | not found | the value of k for which two given lines are coplanar |
| 7 | SCQ | D | 2 (2) | High | two vector equations of the form r x a = p, each of which alone describes a line, are imposed together, so r is the intersection point of two lines given only through their moment vectors (way 5) | ingredient only | the published problem r x a = b x a, r x b = a x b, where adding the equations gives r parallel to a+b |
| 8 | SCQ | C | 2 (2) | Medium | a tetrahedron given only by its edge lengths and angles at one vertex, with a cyclic sum of dot products of face-normal vectors evaluated through the four-vector identity without coordinates (way 5) | ingredient only | evaluating (a x b).(c x d) for given vectors, or the dihedral angle of a regular tetrahedron |
| 9 | SCQ | A | 3 (3) | Medium | the plane is picked out of the family through l by a point, and only then recognised as a bisector by its parameter (/k/ = /n1///n2/), with the acute/obtuse decision made from unit normals (way 5) | ingredient only | the equation of the plane bisecting the acute angle between two given planes |
| 10 | SCQ | C | 3 (3) | Low | the bisector plane of two planes is used to choose between the two circles that touch the traces of the planes, so the 3D bisector and the 2D angle bisectors of the traces meet in one configuration (way 5) | not found | the plane bisecting the angle containing the origin, and separately the circle touching two lines with centre on an axis |
| 11 | SCQ | B | 3 (3) | Medium | the spheres through a fixed circle form a one-parameter family with centres on the normal through the circle centre, and the member is fixed by tangency to a line (way 3: a family with a second condition) | not found | the sphere through the circle S + lambda P = 0 that touches a given plane, or passes through a point |
| 12 | SCQ | D | 3 (3) | Medium | a hidden invariant (way 4): the tangent length from P to the circle cut from the sphere by any plane through P equals the tangent length from P to the sphere, so the messy section circle is not needed | ingredient only | the radius and centre of the circle of section of a sphere by a plane; the power of a point for a circle |
| 13 | Num | -3 | 2 (2) | Medium | a vector fixed only by its integer length 7 and three inequalities on its direction angles, so the solver must first find the unique decomposition 49 = 4+9+36 into non-zero squares and then sort signs and order from the angle conditions (way 3, an object defined by several conditions) | not found | 'find the vector of magnitude 7 along 2i+3j+6k' or 'direction cosines of a vector' |
| 14 | Num | 83 | 2 (2) | High | a walk whose step lengths grow 1,2,3,4,5 while the directions cycle through three non-unit vectors; the solver must normalise, group the steps by direction and add (way 1, a repeated process). The three vectors are hidden mutually perpendicular vectors of equal length, which makes the answer clean | not found | 'resultant of displacements' exercises |
| 15 | Num | -0.68 | 2 (2) | Medium | the first two direction cosines of a unit vector are packed into a complex number w = l + i m, and w is fixed by its modulus and by a conjugate-argument condition ((3-4i) times conj(w) negative real); the third direction cosine then comes from l^2+m^2+n^2 = 1 with /w/^2 = l^2+m^2 (way 5, link of two chapters) | not found | 'find z with arg((3-4i) z) = pi' or 'direction cosines from two given ones' |
| 16 | Num | 0.25 | 2 (2) | Medium | a simultaneous averaging map on three vectors iterated three times; the invariant sum S and the factor -1/2 on c_n - S/3 make the coefficients clean (way 1, iteration with an invariant) | not found | 'express a vector in terms of three non-coplanar vectors' and the medial-triangle iteration for points |
| 17 | Num | 226 | 3 (3) | Medium | a vector curve c + (cos t) a + (sin t) b in which a and b are hidden perpendicular vectors of equal length, so /r/^2 collapses to 65 + 36 cos t + 48 sin t; the restriction t in [0, pi/2] then makes the minimum an end-point value (way 4, hidden invariant) | ingredient only | 'maximum of a cos t + b sin t + c' as a plain trigonometric exercise |
| 18 | Num | 2.5 | 2 (2) | High | a segment with one end on each of two non-intersecting lines is fixed by its mid-point; three mid-point equations in two parameters must be consistent and give the ends (way 3, an object defined by two conditions) | not found | in two dimensions, 'line through a point bisected between two lines' |
| 19 | Num | 3.5 | 3 (3) | Medium | the point where a coordinate plane cuts AB is paired with its harmonic conjugate, and the product of their distances from the mid-point is asked; the answer is MA^2 whatever plane is used (way 4, hidden invariant) | ingredient only | 'ratio in which the xy-plane divides AB' and, in plane geometry, the harmonic-division lemma MP.MQ = MA^2 |
| 20 | Num | -2.8 | 3 (3) | Medium | a triangle in space whose vertices are equidistant from the origin and coplanar with it, so the origin is the circumcentre and the orthocentre is simply a + b + c through the Euler-line section ratio; nothing in the stem names the circumcentre (way 4, hidden configuration) | ingredient only | 'if the circumcentre is the origin then the orthocentre is a + b + c' as a stated result |
| 21 | Num | 42 | 3 (3) | Medium | lattice points on a space line whose symmetric equation has coefficients on x and y, so the integrality of all coordinates becomes a pair of congruences on the parameter (way 5, linking the line equation with integrality) | not found | 'number of integer points on a segment in the plane' (gcd count) |
| 22 | Num | 196 | 2 (2) | High | the vectors a and b are given only through lengths and the angle (no components), and r is fixed by its two scalar projections; the coefficients come from a 2x2 Gram system and /r/^2 = x (r.a) + y (r.b) (way 5) | ingredient only | 'vector in the plane of a and b whose projection on c is given' (published JEE problems, with components) |
| 23 | Num | -3 | 3 (3) | Medium | two vectors are known only through their sum, their cross product and equal length; the rhombus diagonals s and d are perpendicular, /s//d/ = 2/a x b/ gives /d/, and a.b = (/s/^2 - /d/^2)/4 (way 4, hidden configuration) | ingredient only | 'diagonals of a parallelogram are given, find its area' and 'solve r x a = b with r.c given' |
| 24 | Num | 0.4 | 3 (3) | Medium | in a right regular triangular pyramid known only by its lateral edge 5 and height 3, the angle between a lateral edge and the base median from another vertex (skew lines) is asked; the solver must place the foot at the centroid and set up coordinates (way 5) | ingredient only | angles between edges and faces of a regular tetrahedron; the 2006 AIME I Problem 14 tripod uses legs 5 and height 4 but asks a different question |
| 25 | Num | -32 | 3 (3) | Medium | the cross product of two linear combinations reduces to -5 a x b, and Lagrange's identity together with /a+b/ collapses to a perfect square (p+9)^2 = 0, so a.b and /b/ are both forced although /b/ is never given (way 4, hidden invariant) | not found | given /a/, /b/ and /a x b/, find a.b |
| 26 | Num | -1.25 | 2 (2) | Medium | two lines given only through position vectors in the basis a, b (one through two points, one through a point with a given direction); the intersection is found purely by comparing coefficients in the plane (way 5) | not found | intersection of two cevians of a triangle in vector form |
| 27 | Num | 900 | 3 (3) | Medium | an iterated cross-product sequence c_{n+1} = a x c_n; from the second term on it lies in the plane perpendicular to a, so the map squares to -/a/^2 and the four-term sum collapses to -3(c2+c3) with c2 perpendicular to c3 (way 1, iteration) | not found | a x (a x b) expansion and /a x b/ from Lagrange |
| 28 | Num | 0.48 | 3 (3) | Low | the third vertex is fixed only through the ratio of the triangle's area to the area of its shadow on the xy-plane (2D coordinate area formula), and the cross-product components then give the inclination to a different coordinate plane (way 5) | not found | area of a triangle from its vertices by the cross product; projection of an area onto a plane |
| 29 | Num | 3.5 | 2 (2) | High | the angle is not given; the difference a.b - /a x b/ together with Lagrange's identity gives a quadratic in /a x b/ whose negative root must be rejected (way 5) | not found | area from /a/, /b/ and a.b |
| 30 | Num | 66 | 2 (2) | High | a quadratic in a.b built from a cross-product magnitude and a dot-product magnitude, maximised over the angle; the vertex must be checked to lie in the attainable range (way 5) | ingredient only | maximum of /pa + qb/ or of 3/3a+2b/+4/3a-2b/ (JEE Main 2026) |
| 31 | Num | 8.5 | 2 (2) | Medium | the common perpendicular of two specific skew lines is extended until it crosses the coordinate plane x = 0, and its length is combined with that crossing point (way 5) | not found | shortest distance between two given skew lines; feet of the common perpendicular |
| 32 | Num | -1.6 | 3 (3) | Medium | three lines in a chain: the position of L2 is fixed by its meeting L3 (coplanarity determinant), the position of L1 by the value of the shortest distance (scalar triple product, two roots, sign condition), and only then is the common perpendicular located (way 5) | not found | shortest distance and feet for two fully given skew lines |
| 33 | Num | -29 | 3 (3) | Medium | the line L2 slides with a parameter, and the parameter is fixed by asking that the common perpendicular cut the z-axis, a coplanarity condition on a line that itself depends on mu (way 3, a family with a second condition) | not found | shortest distance between given skew lines; lines meeting the coordinate axes |
| 34 | Num | 38 | 2 (2) | Medium | one line is given only as the intersection of two planes and the other only through two points, so the directions must be built (cross product of normals, difference of points) before the common perpendicular is found (way 5) | not found | feet of the common perpendicular of two lines in symmetric form |
| 35 | Num | 0.44 | 3 (3) | Medium | the points of a line lying in a plane from which a fixed external point is seen at a fixed angle to the plane; since the height is constant along the line, the angle condition becomes a fixed distance AP = 5, and the answer is the apex angle of the isosceles triangle ABC (way 5: line-plane angle combined with the line of intersection) | not found | angle between a given line and a given plane; line of intersection of two planes |
| 36 | Num | 113 | 2 (2) | High | the sum of the squared distances of a point from the two bisecting planes of a pair of planes, which by a hidden invariant (perpendicular bisectors through the common line) equals the squared distance from the line of intersection (way 4) | not found | equation of the bisecting planes and the bisector containing a given point |
| 37 | Num | 27 | 2 (2) | Medium | the plane is not given; it is fixed only by the requirement that the image of a point lies on a given line (the image moves along the normal through A as d varies, and the line picks one position), after which the same line is cut by the plane (way 5) | not found | image of a point in a given plane; point of intersection of a line and a plane |
| 38 | Num | 2.8 | 3 (3) | Medium | the images of one point in all members of a family of planes through a line lie on a circle centred on the line (reflections fix the line pointwise), so the greatest distance between two images is a diameter (way 4, hidden invariant) | ingredient only | in two dimensions, the locus of the image of a point in a pencil of lines is a circle (a published JEE problem); in three dimensions, the image of a point in one given plane |
| 39 | Num | 0.6 | 3 (3) | Medium | the traces of a family of planes on the xy-plane form a family of lines through a fixed point; the two-dimensional extremal property of that pencil (farthest line from a point is perpendicular to the joining segment) selects the plane, whose inclination is then asked (way 5: the link between the two families is the discovery) | not found | the line of a family through a fixed point at maximum distance from a given point (2D); plane through the line of intersection satisfying a condition (3D) |
| 40 | Num | -8 | 2 (2) | Medium | a plane is fixed by requiring that it reflects a point to the same place as a given line does, so the plane is the perpendicular bisector of the point and its line image (way 5) | not found | image of a point in a line; image of a point in a plane |
| 41 | Num | 154 | 3 (3) | Medium | the dot products of the edge vectors of a tetrahedron are not given; they are encoded in two vector triple product identities, then the tetrahedron spanned by the face-normal cross products is measured through [a x b, b x c, c x a] = [a b c]^2 and the dot-product determinant (way 5) | ingredient only | [a x b, b x c, c x a] = [a b c]^2 as a textbook identity; volume of a tetrahedron from edge lengths and angles |
| 42 | Num | -0.25 | 2 (2) | Medium | an angle between two edges of an oblique parallelepiped is recovered from the lengths of two of its body diagonals, which form a diagonal parallelogram ODGC (way 4: the parallelogram law removes the unknown dot products with the third edge) | ingredient only | angle between two body diagonals of a rectangular box |
| 43 | Num | -2 | 2 (2) | Medium | the third edge is hidden in the opposite vertex G = A + B + C, and the sign of the box product (right-handed orientation) chooses between the two parameter values that give the volume (way 5) | ingredient only | unknown parameter in an edge vector fixed by a given volume |
| 44 | Num | 113 | 2 (2) | High | the tetrahedron on four mutually non-adjacent vertices of an oblique parallelepiped given by four vertices, whose volume is one third of the parallelepiped (way 4) | ingredient only | the regular tetrahedron inside a cube with one third of its volume (a known geometric fact) |
| 45 | Num | 0.5 | 3 (3) | Medium | a parallelepiped whose edges are cyclic combinations a + x b + x^2 c, ..., so the volume ratio is a circulant determinant that factorises by row-sum and row operations into (1 - x^3)^2 (way 5) | ingredient only | edges a + b, b + c, c + a giving twice the volume |
| 46 | Num | 4.5 | 3 (3) | Medium | the vertices are points (1, t, t^3) at the three roots of a cubic, so the volume is a generalized Vandermonde determinant (a-b)(b-c)(c-a)(a+b+c) whose size is fixed by the discriminant and the sum of roots (way 5) | ingredient only | volume of a tetrahedron from given position vectors; the textbook factorisation of the (1, a, a^3) determinant |
| 47 | Num | 75 | 2 (2) | High | a linear vector equation r + a x (a x r) = c in which the triple product turns r into a combination of r and a, and one dot product with a collapses the unknown scalar a.r (way 5) | not found | the standard equation x + (x x a) = b solved by dotting and crossing with a |
| 48 | Num | -3.5 | 3 (3) | Medium | a triply nested cross product dotted with c x d, evaluated from dot-product data only; one triple-product expansion reduces it to two four-vector scalar products whose values need /c/, /d/ and c.d (way 5) | not found | evaluating (a x b).(c x d) from given dot products, or simplifying a x (b x (c x d)) |
| 49 | Num | 121 | 2 (2) | High | the basis is a, a x b, a x (a x b), which is orthogonal, so the coefficients of the linear combination come from single dot products instead of a 3x3 system (way 4: hidden orthogonality) | ingredient only | expressing a vector as x a + y b + z c for three given vectors |
| 50 | Num | -0.5 | 3 (3) | Medium | a point fixed by two cevians in a face of a tetrahedron is projected from the mid-point of an edge onto the opposite face; both steps are coefficient matching, once in the plane ABC and once in space (way 5) | not found | intersection of two cevians of a triangle by vectors; centroid of a tetrahedron |
| 51 | Num | 0.25 | 3 (3) | Medium | the non-uniqueness of a linear combination is turned into a parametric system whose determinant has two roots, one giving an inconsistent system and one a consistent one (way 5) | ingredient only | values of lambda for which three vectors are coplanar |
| 52 | Num | 26 | 3 (3) | Medium | a quadratic vector equation r x (r x a) = c; after the triple-product expansion m r - s a = c, the dot products with r and with c give r.c = 0 and /c/^2 = -s(a.c), so /r/^2 is fixed without solving for r (way 4: hidden invariant) | not found | linear vector equations r x a = b x a with r.c = 0, or x + a x x = b |
| 53 | Num | -9 | 2 (2) | High | the point is described by its bisectors (one internal, two external) instead of by name, so the student must recognise the excentre and use the signed-weight vector formula for a triangle in space with integer sides 8, 7, 9 (way 5) | ingredient only | incentre of a triangle from its vertices in 3D |
| 54 | Num | 4.8 | 2 (2) | High | a space triangle with integer sides 9 and 6 at P whose bisector foot happens to lie directly 'above' P, so the bisector length is read off one coordinate after the section formula (way 5) | ingredient only | length of an angle bisector of a triangle by the formula 2bc cos(A/2)/(b+c) |
| 55 | Num | -2.75 | 2 (2) | Medium | the mirror is not given; it is recovered from the incident and reflected rays, and the decision between the two angle bisectors is made by the vector sum of unit vectors (way 5) | not found | equation of the reflected ray for a given mirror; bisector of the angle containing a given point |
| 56 | Num | 29.5 | 2 (2) | Medium | a weighted sum of squared distances with weights 1, 1, 2 is minimised by moving the origin to the weighted centroid; the minimum is then turned into side lengths by the vector identity /a + b + 2c/^2 = 0 (way 4) | ingredient only | PA^2 + PB^2 + PC^2 = 3PG^2 + GA^2 + GB^2 + GC^2 (Leibniz) with equal weights |
| 57 | Num | 28 | 3 (3) | Medium | four sides and one diagonal of a skew quadrilateral plus only the angle between the diagonals; the vector identity AB^2+CD^2-BC^2-DA^2 = 2 DB.AC recovers the missing diagonal, then the midpoint identity gives MN (way 5) | ingredient only | perpendicular diagonals iff sums of squares of opposite sides are equal; Euler's quadrilateral theorem (both used in USAMO 1977 P4 style proofs) |
| 58 | Num | 0.8 | 2 (2) | High | two directions given by elevation and azimuth (as in lines of sight); the dot product yields the vector form cos(psi) = cos t1 cos t2 cos(p1 - p2) + sin t1 sin t2, and the compound-angle formula evaluates the azimuth difference (way 5) | ingredient only | proving cos(A - B) by the dot product of two unit vectors in a plane |
| 59 | Num | 256 | 3 (3) | Medium | a tetrahedron with two pairs of perpendicular opposite edges; the vector proof that then a.b = b.c = c.a (and the third pair is perpendicular) turns one face angle into all three face angles at O, and the cosine rule in each face gives the edges (way 5) | ingredient only | the textbook vector proof that two pairs of perpendicular opposite edges force the third pair |
| 60 | Num | -6 | 2 (2) | Medium | the line AB is cut by the condition PC = PD; the quadratic terms of the two distance formulas cancel to give the parameter, which the section formula turns into a signed ratio that comes out external (way 5) | not found | ratio in which a coordinate plane divides a segment |
| 61 | Num | -1.5 | 3 (3) | Medium | a cutting plane of a tetrahedron through a mid-point, a trisection point and a vertex meets the median AG of the tetrahedron; coordinates of three section points, a plane through them and its intersection with the median (way 5) | not found | ratio in which a plane divides a segment joining two given points |
| 62 | Num | 2.25 | 3 (3) | Medium | the transversal through the origin to two skew lines is found from two coplanarity determinants (one for each line), and the length it cuts off is compared with the shortest distance; the origin turns out to divide AB in the ratio 1:2 (way 5) | ingredient only | the line through a given point meeting two given lines (textbook exercise) and the shortest-distance formula |
| 63 | Num | 36 | 2 (2) | High | the set of mid-points of all segments joining two skew lines is a plane parallel to both, found by eliminating the two parameters; the plane is then read through its intercepts (way 3) | ingredient only | locus of a point at a fixed relation to fixed points (PA^2 - PB^2 = k, a plane) |
| 64 | Num | 174 | 2 (2) | High | the locus compares the sum of squared distances from the coordinate axes with a multiple of the squared distance from a fixed point; the coefficients 2 and 3 leave one square, so the locus is a sphere centred at 3A (way 5) | ingredient only | 'sum of squares of distances from the axes is a constant' (a sphere about the origin), a published exercise |
| 65 | Num | -3 | 3 (3) | Medium | points of a coordinate plane equidistant from two skew lines whose directions are mirror images in that plane; the quadratic parts of the two point-line distances cancel, so the planar locus is a straight line (way 4: hidden symmetry) | not found | locus of points equidistant from two given points (perpendicular bisector) or from two intersecting lines in a plane |
| 66 | Num | 0.75 | 2 (2) | Medium | a chord of a sphere's section circle is cut out by a second plane perpendicular to the section plane; the distance of the circle's centre from the chord comes from a point-plane distance, and the inscribed-angle theorem turns it into the angle at the circumference (way 5) | ingredient only | angle subtended by a chord at a point of the major arc of a given circle |

**Closest to published material:**
- Q7: near the published r x a = b x a, r x b = a x b pair.
- Q9: the acute/obtuse bisector rule is standard.
- Q22: "a vector in the plane of a, b with given projections".
- Q38: the 2D version, where images in a pencil of lines lie on a circle, is published.
- Q41: [a x b, b x c, c x a] = [abc]^2.
- Q44: the tetrahedron on alternate vertices is V/3.
- Q57: the identity AB^2+CD^2-BC^2-DA^2 = 2 DB.AC appears in a 1977 USAMO solution.
- Q64: the "sum of squared distances from the axes = constant" version is published.

Replace any of these if you want more distance.
