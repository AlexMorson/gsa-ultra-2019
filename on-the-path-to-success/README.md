# 5 Down: "On the path to success"

Laura gives Dale an undirected tree with $N$ nodes numbered $1$ to $N$, rooted at node $1$. In this tree, node $i$ has a value $V_i$ associated with it.

A path in the tree is defined as a sequence of distinct nodes $x_1, x_2, ..., x_k$ such that for all $j$, $x_j$ and $x_{j+1}$ are connected by a direct edge and $1 \leq x_j \leq N$, where $k \geq 1$. Laura considers two paths to be different if and only if there is a node in one of the paths that's not present in the other.

Laura defines the *value* of a path as the bitwise AND of the values of nodes on that path, and the *score* of a path as the number of set bits in the value of the path.

Laura wants Dale to find $f(k)$, the number of paths with *score* $k$, for each $k$ from 0 to 8. You need to help Dale by returning $\sum_{i = 0}^{8} f(i) \times 2^i$. Since this number may be large, output it modulo $10^9 + 7$.

### Input

- $P$: a tuple of $N-1$ elements $P_1, P_2, ..., P_{N-1}$ where $P_i$ denotes the parent of node $i+1$.
- $V$: a tuple of $N$ integers $V_1, V_2, ..., V_{N}$ where $V_i$ denotes the value of node $i$.

### Constraints

- $2 \le N \le 40000$
- $0 \le V_i < 2^{8}$, for all $i$
