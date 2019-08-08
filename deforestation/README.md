# 12 Across: "Deforestation"

Take an undirected tree ![\inline T](http://latex.codecogs.com/svg.latex?%5Cinline%20T) with ![\inline N_T](http://latex.codecogs.com/svg.latex?%5Cinline%20N_T) nodes and consider one of its nodes, ![\inline x](http://latex.codecogs.com/svg.latex?%5Cinline%20x). To find a *subtree* of ![\inline x](http://latex.codecogs.com/svg.latex?%5Cinline%20x) relative to some other node ![\inline r](http://latex.codecogs.com/svg.latex?%5Cinline%20r) we first root the tree ![\inline T](http://latex.codecogs.com/svg.latex?%5Cinline%20T) at ![\inline r](http://latex.codecogs.com/svg.latex?%5Cinline%20r). The *subtree* of ![\inline x](http://latex.codecogs.com/svg.latex?%5Cinline%20x) relative to ![\inline r](http://latex.codecogs.com/svg.latex?%5Cinline%20r) is then defined as the set of all nodes ![\inline n](http://latex.codecogs.com/svg.latex?%5Cinline%20n) for which ![\inline x](http://latex.codecogs.com/svg.latex?%5Cinline%20x) lies on the path from ![\inline n](http://latex.codecogs.com/svg.latex?%5Cinline%20n) to ![\inline r](http://latex.codecogs.com/svg.latex?%5Cinline%20r). The *size* of a subtree is the number of nodes this set contains.

You're given a tree ![\inline T](http://latex.codecogs.com/svg.latex?%5Cinline%20T) along with a list ![\inline Q](http://latex.codecogs.com/svg.latex?%5Cinline%20Q) of integers ![\inline Q_1, Q_2, ..., Q_i, ..., Q_{N_Q}](http://latex.codecogs.com/svg.latex?%5Cinline%20Q_1%2C%20Q_2%2C%20...%2C%20Q_i%2C%20...%2C%20Q_%7BN_Q%7D). Each element in ![\inline Q](http://latex.codecogs.com/svg.latex?%5Cinline%20Q) is a *query*.

For each query  ![\inline Q_i](http://latex.codecogs.com/svg.latex?%5Cinline%20Q_i),

- Determine the probability that, for nodes ![\inline x](http://latex.codecogs.com/svg.latex?%5Cinline%20x) and ![\inline r](http://latex.codecogs.com/svg.latex?%5Cinline%20r) chosen uniformly at random, the subtree size of ![\inline x](http://latex.codecogs.com/svg.latex?%5Cinline%20x) relative to ![\inline r](http://latex.codecogs.com/svg.latex?%5Cinline%20r) is ![\inline Q_i](http://latex.codecogs.com/svg.latex?%5Cinline%20Q_i).

Represent this probability as a fraction ![\inline \frac{A}{B}](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Cfrac%7BA%7D%7BB%7D).

- Compute the answer for this query, which is the multiplicative product of ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A) and ![\inline B^{-1} \mod{10^9 + 7}](http://latex.codecogs.com/svg.latex?%5Cinline%20B%5E%7B-1%7D%20%5Cmod%7B10%5E9%20%2B%207%7D) (where the latter term is the modular multiplicative inverse of ![\inline B](http://latex.codecogs.com/svg.latex?%5Cinline%20B) with respect to ![\inline 10^9 + 7](http://latex.codecogs.com/svg.latex?%5Cinline%2010%5E9%20%2B%207)). Represent this value as ![\inline ans(i)](http://latex.codecogs.com/svg.latex?%5Cinline%20ans%28i%29).

Output the sum of ![\inline i \times ans(i)](http://latex.codecogs.com/svg.latex?%5Cinline%20i%20%5Ctimes%20ans%28i%29) for all ![\inline i](http://latex.codecogs.com/svg.latex?%5Cinline%20i), where ![\inline 1 \leq i \leq N_Q](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20i%20%5Cleq%20N_Q). Since this number might be large, output it modulo ![\inline 10^9 + 7](http://latex.codecogs.com/svg.latex?%5Cinline%2010%5E9%20%2B%207).

### Input

- ![\inline T](http://latex.codecogs.com/svg.latex?%5Cinline%20T): a tuple of ![\inline N_T-1](http://latex.codecogs.com/svg.latex?%5Cinline%20N_T-1) elements ![\inline E_1, E_2, ..., E_{N-1}](http://latex.codecogs.com/svg.latex?%5Cinline%20E_1%2C%20E_2%2C%20...%2C%20E_%7BN-1%7D), where ![\inline E_i](http://latex.codecogs.com/svg.latex?%5Cinline%20E_i) is a tuple of two integers ![\inline u](http://latex.codecogs.com/svg.latex?%5Cinline%20u) and ![\inline v](http://latex.codecogs.com/svg.latex?%5Cinline%20v), denoting an undirected edge between nodes ![\inline u](http://latex.codecogs.com/svg.latex?%5Cinline%20u) and ![\inline v](http://latex.codecogs.com/svg.latex?%5Cinline%20v).
- ![\inline Q](http://latex.codecogs.com/svg.latex?%5Cinline%20Q): a tuple of ![\inline N_Q](http://latex.codecogs.com/svg.latex?%5Cinline%20N_Q) integers denoting the queries.

### Constraints

- ![\inline 1 \leq N_T, N_Q \leq 5 \times 10^5](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20N_T%2C%20N_Q%20%5Cleq%205%20%5Ctimes%2010%5E5)
- ![\inline 1 \leq u, v, Q_i \leq N_T](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20u%2C%20v%2C%20Q_i%20%5Cleq%20N_T)

## My Solution

At first I didn't read the problem carefully enough and was under the impression that the queries being given were subtrees, rather than sizes of subtrees (which would have made the problem quite a bit easier)! I had thought of a way to solve this problem, then when I was ready to start coding up the solution I realised my mistake and went back to the drawing board.

I eventually realised that if I knew the size of each subtree out of every node, I would have enough information to calculate the required probabilities. This is because we can calculate the number of nodes with subtrees of a given size, and the number of ways of getting that subtree relative to another node is equal to the number of nodes *not* in that subtree.

To calculate the size of each subtree in every direction took a bit of graph searching hackery, because to calculate the size of a subtree you first want to calculate the size of the subtrees of the children, and just sum them up. So in the end my program effectively roots the tree at every node, and for each of them does some sort of bottom up traversal of the tree, calculating subtree sizes as it goes.
