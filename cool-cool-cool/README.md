# 6 Across: "Cool, cool, cool"

Troy recently learned about *bitonic sequences*.

Let $S$ be a sequence of $L_S$ integers. A contiguous subsequence of $S$, $S_i, S_{i+1}, ..., S_j$, can be represented as $S[i..j]$ where $1 \leq i,j \leq L_S$. A sequence $S$ is *bitonic* if for some $i$ the subsequence $S[1..i]$ is strictly increasing and the subsequence $S[i..L_S]$ is strictly decreasing. Note that either subsequence could be of length $1$.

Abed gets tired of Troy's constant bragging about this new knowledge. He decides to test his friend with a challenge.

Abed gives Troy an array $A$ of $L_A$ integers. In one operation, Troy can increment the value of a single element of $A$ by $1$. Abed asks Troy to convert $A$ into a bitonic sequence in as few operations as possible, and then tell Abed the number of operations it took him to do so.

Troy knows his stuff, but being put on the spot by his best friend has really undermined his confidence. Can you help Troy with this task?

### Input

- $A$: a tuple of $N$ integers, where $i^{th}$ integer denotes $A_i$.

### Constraints

- $1 \leq N \leq 2 \times 10^6$
- $1 \leq A_i \leq 10^9$
