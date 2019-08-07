# 12 Across: "Deforestation"

Take an undirected tree $T$ with $N_T$ nodes and consider one of its nodes, $x$. To find a *subtree* of $x$ relative to some other node $r$ we first root the tree $T$ at $r$. The *subtree* of $x$ relative to $r$ is then defined as the set of all nodes $n$ for which $x$ lies on the path from $n$ to $r$. The *size* of a subtree is the number of nodes this set contains.

You're given a tree $T$ along with a list $Q$ of integers $Q_1, Q_2, ..., Q_i, ..., Q_{N_Q}$. Each element in $Q$ is a *query*.

For each query  $Q_i$,

- Determine the probability that, for nodes $x$ and $r$ chosen uniformly at random, the subtree size of $x$ relative to $r$ is $Q_i$.

Represent this probability as a fraction $\frac{A}{B}$.

- Compute the answer for this query, which is the multiplicative product of $A$ and $B^{-1} \mod{10^9 + 7}$ (where the latter term is the modular multiplicative inverse of $B$ with respect to $10^9 + 7$). Represent this value as $ans(i)$.

Output the sum of $i \times ans(i)$ for all $i$, where $1 \leq i \leq N_Q$. Since this number might be large, output it modulo $10^9 + 7$.

### Input

- $T$: a tuple of $N_T-1$ elements $E_1, E_2, ..., E_{N-1}$, where $E_i$ is a tuple of two integers $u$ and $v$, denoting an undirected edge between nodes $u$ and $v$.
- $Q$: a tuple of $N_Q$ integers denoting the queries.

### Constraints

- $1 \leq N_T, N_Q \leq 5 \times 10^5$
- $1 \leq u, v, Q_i \leq N_T$
