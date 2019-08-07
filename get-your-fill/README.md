# 8 Across: "Get your fill"

You're given a string $S$ of length $N$ consisting of digits from $0$ to $9$ and the character $\verb"?"$.

You can *fill* $S$ by replacing every instance of $\verb"?"$ with a digit from $0$ to $9$. Note that a *filled* version of $S$ is **not valid** if it has leading zeroes.

Your objective is to find the lexicographically smallest *filled* version of $S$ that is divisible by $8$ when converted to an integer, and then return its *value*.

We define the *value* of a string $S$ of length $N$ as $(\sum_{i = 1}^{N} 11^{i-1} \times (S[i] + 1)) \mod{10^{9} + 7}$.

If no such string can be found, return $1000000007$.

You may assume that the unfilled version of $S$ does not have leading zeroes.

### Input

- $S$: a string of length $N$ consisting of digits from $0$ to $9$ and the character $\verb"?"$.

### Constraints

- $1 \le N \le 10^{5}$
