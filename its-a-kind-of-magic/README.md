# 10 Across: "It's a kind of magic"

You're given a set $S$ of $N_S$ strings, where each string consists only of digits from $0$ to $9$. The $i^{th}$ string in the set $S$ is assigned a *score* of $x_i$.

For any string $T$, we define its *magic value* to be the sum of the scores of all strings from the set $S$ which are present in $T$ as substrings. Note that if a string occurs in $T$ as a substring multiple times starting at different indices, its score is counted in the sum multiple times, once for each occurrence.

You're given $Q$, a set of $N_Q$ queries of the form $(L, R)$.

For each query $Q_i = (L_i, R_i)$, let $str(j)$ be the string representation (with no leading zeroes) of integer $j$, where $L_i \leq j \leq R_i$.

Let $ans(i)$ be the sum of magic values of $str(j)$ for all $j, L_i \leq j \leq R_i$.

Return $(\sum_{i=1}^{N_Q} 2^i \times ans(i)) \mod{10^9 + 7}$.

### Input

- $S$: A tuple of $N_S$ strings.
- $X$: A tuple of $N_S$ integers where $i^{th}$ denotes $x_i$, the score of the $i^{th}$ string in $S$.
- $Q$: A tuple of $N_Q$ elements $Q_1, Q_2, ..., Q_{N_Q}$. $Q_i$ is a tuple $(L_i, R_i)$ denoting the $i^{th}$ query.

### Constraints

- $1 \leq N_S, N_Q \leq 3 \times 10^3$
- $1 \leq \textrm{length}(S_i) \leq 18$ for all $i$
- $1 \leq x_i \leq 10^{9}$ for all $i$
- $1 \leq L_i, R_i \leq 10^{18}$ for all $i$
