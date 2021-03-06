# 8 Across: "Get your fill"

You're given a string ![\inline S](http://latex.codecogs.com/svg.latex?%5Cinline%20S) of length ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N) consisting of digits from ![\inline 0](http://latex.codecogs.com/svg.latex?%5Cinline%200) to ![\inline 9](http://latex.codecogs.com/svg.latex?%5Cinline%209) and the character ![\inline \verb"?"](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Cverb%22%3F%22).

You can *fill* ![\inline S](http://latex.codecogs.com/svg.latex?%5Cinline%20S) by replacing every instance of ![\inline \verb"?"](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Cverb%22%3F%22) with a digit from ![\inline 0](http://latex.codecogs.com/svg.latex?%5Cinline%200) to ![\inline 9](http://latex.codecogs.com/svg.latex?%5Cinline%209). Note that a *filled* version of ![\inline S](http://latex.codecogs.com/svg.latex?%5Cinline%20S) is **not valid** if it has leading zeroes.

Your objective is to find the lexicographically smallest *filled* version of ![\inline S](http://latex.codecogs.com/svg.latex?%5Cinline%20S) that is divisible by ![\inline 8](http://latex.codecogs.com/svg.latex?%5Cinline%208) when converted to an integer, and then return its *value*.

We define the *value* of a string ![\inline S](http://latex.codecogs.com/svg.latex?%5Cinline%20S) of length ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N) as ![\inline (\sum_{i = 1}^{N} 11^{i-1} \times (S[i] + 1)) \mod{10^{9} + 7}](http://latex.codecogs.com/svg.latex?%5Cinline%20%28%5Csum_%7Bi%20%3D%201%7D%5E%7BN%7D%2011%5E%7Bi-1%7D%20%5Ctimes%20%28S%5Bi%5D%20%2B%201%29%29%20%5Cmod%7B10%5E%7B9%7D%20%2B%207%7D).

If no such string can be found, return ![\inline 1000000007](http://latex.codecogs.com/svg.latex?%5Cinline%201000000007).

You may assume that the unfilled version of ![\inline S](http://latex.codecogs.com/svg.latex?%5Cinline%20S) does not have leading zeroes.

### Input

- ![\inline S](http://latex.codecogs.com/svg.latex?%5Cinline%20S): a string of length ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N) consisting of digits from ![\inline 0](http://latex.codecogs.com/svg.latex?%5Cinline%200) to ![\inline 9](http://latex.codecogs.com/svg.latex?%5Cinline%209) and the character ![\inline \verb"?"](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Cverb%22%3F%22).

### Constraints

- ![\inline 1 \le N \le 10^{5}](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cle%20N%20%5Cle%2010%5E%7B5%7D)

## My Solution

This is the first problem I tried to solve, and the last one I ended up actually solving! It felt like an easy enough problem because the remainder of a number when divided by 8 only depends on the last 3 digits, so we know we can set all "?"s before that to 0 (or 1 if it is the first digit). The real problem was sorting out all the edge cases which took a bit of thinking, and even now I wouldn't be surprised if there is an obscure case where my program fails. 

Once I had written a solution I was surprised to find that it ran too slowly! In the end I realised that it was because I was recomputing `11**i` for every iteration of the final sum. Replacing this with a "multiplier" variable which I multiplied by 11 on each iteration fixed this.
