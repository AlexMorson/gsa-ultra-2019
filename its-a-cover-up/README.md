# 2 Down: "It's a cover up"

For an array ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A) of ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N) integers ![\inline A_1, A_2, ..., A_N](http://latex.codecogs.com/svg.latex?%5Cinline%20A_1%2C%20A_2%2C%20...%2C%20A_N), we define a *subarray* of ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A) as a contiguous set of elements from ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A). The *value* of a subarray is defined as the sum of the elements in the subarray.

A *cover* of an array ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A) is defined as a set of disjoint and exhaustive subarrays. No subarrays should overlap and the whole of ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A) should be covered. The *score* of a cover is defined as the sum of pairwise products of the values of the subarrays. The score of a cover consisting of only one subarray will be ![\inline 0](http://latex.codecogs.com/svg.latex?%5Cinline%200).

For example, if a cover is formed from four subarrays with respective values ![\inline x, y, z, a](http://latex.codecogs.com/svg.latex?%5Cinline%20x%2C%20y%2C%20z%2C%20a), then the score of the cover is ![\inline xy + yz + xz + xa + ya + za](http://latex.codecogs.com/svg.latex?%5Cinline%20xy%20%2B%20yz%20%2B%20xz%20%2B%20xa%20%2B%20ya%20%2B%20za).

Given an array ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A), your objective is to find the cover of ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A) with the highest possible score. The output of your function should be this score.

### Input

- ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A): a tuple of ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N) integers, where the ![\inline i^{th}](http://latex.codecogs.com/svg.latex?%5Cinline%20i%5E%7Bth%7D) integer denotes ![\inline A_i](http://latex.codecogs.com/svg.latex?%5Cinline%20A_i).

### Constraints

- ![\inline 1 \leq N \leq 100000](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20N%20%5Cleq%20100000)
- ![\inline -10000 \leq A_i \leq 10000](http://latex.codecogs.com/svg.latex?%5Cinline%20-10000%20%5Cleq%20A_i%20%5Cleq%2010000)
