# 14 Across: "Hopping mad"

Fergal the Frog can't believe his luck - he's just turned the corner onto his favourite patch of grass and spotted ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N) flies sitting in a perfect horizontal line, each spaced one centimetre apart.

Fergal eats the first fly on the left. To remain unpredictable, he then hops to the rightmost uneaten fly and gobbles it up. Then he hops back to the leftmost uneaten fly and eats that one too. He repeats this process until there are no flies left (probably for the best, as he now feels uncomfortably full).

Output the total distance Fergal covered, in centimetres.

### Input

- ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N): the number of flies in the line.

### Constraints

- ![\inline 2 \le N \le 10^{9}](http://latex.codecogs.com/svg.latex?%5Cinline%202%20%5Cle%20N%20%5Cle%2010%5E%7B9%7D)

## My Solution

This was a nice easy problem. Walking through a small example shows that the first hop has length N-1 and each subsequent hop decreases in length by 1, so the answer is simply the sum of the integers from 1 to N-1.
