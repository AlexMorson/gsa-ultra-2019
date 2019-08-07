# 2 Down: "It's a cover up"

For an array $A$ of $N$ integers $A_1, A_2, ..., A_N$, we define a *subarray* of $A$ as a contiguous set of elements from $A$. The *value* of a subarray is defined as the sum of the elements in the subarray.

A *cover* of an array $A$ is defined as a set of disjoint and exhaustive subarrays. No subarrays should overlap and the whole of $A$ should be covered. The *score* of a cover is defined as the sum of pairwise products of the values of the subarrays. The score of a cover consisting of only one subarray will be $0$.

For example, if a cover is formed from four subarrays with respective values $x, y, z, a$, then the score of the cover is $xy + yz + xz + xa + ya + za$.

Given an array $A$, your objective is to find the cover of $A$ with the highest possible score. The output of your function should be this score.

### Input

- $A$: a tuple of $N$ integers, where the $i^{th}$ integer denotes $A_i$.

### Constraints

- $1 \leq N \leq 100000$
- $-10000 \leq A_i \leq 10000$
