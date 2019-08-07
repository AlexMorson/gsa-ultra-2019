# 3 Across: "Pizza time"

Peter gives Miles a map of New York in the form of a grid $A$ with dimensions $N \times M$. Rows are numbered $1$ to $N$ from top to bottom, and columns are numbered $1$ to $M$ from left to right. A cell in the grid, which is the intersection of the $i^{th}$ row and $j^{th}$ column, is denoted by $[i, j]$.

Each cell $[i, j]$ contains $A_{i,j}$ pizzas, where $A_{i,j}$ is an integer. Miles is allowed to move in one of four directions, *up*, *down*, *left*  or *right*, one step at a time. In one step, Miles can move from cell $[i, j]$ to one of $[i + 1, j]$, $[i - 1, j]$, $[i, j + 1]$ and $[i, j - 1]$, given that he doesn't reach the boundaries of the grid.

Peter adds the restriction that Miles can only move to a neighbouring cell if it has a strictly greater number of pizzas than the cell Miles is currently at. He asks Miles to find the length of the longest path possible in the grid, where length of a path is the number of cells constituting that path. A path starting and finishing at the same cell (i.e. consisting of only one cell) has length $1$. Can you help Miles to solve this problem?

### Input

- Two integers $N$ and $M$, denoting the number of rows and columns respectively.
- $A$, a tuple of size $N$. $A[i]$ is a tuple of $M$ integers, where $A[i][j]$ represents the number of pizzas in cell $[i,j]$.

### Constraints

- $1 \leq N \leq 1000$
- $1 \leq M \leq 1000$
- $0 \leq A_{i_j} \leq 10^9$
