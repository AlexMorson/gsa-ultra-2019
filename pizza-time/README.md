# 3 Across: "Pizza time"

Peter gives Miles a map of New York in the form of a grid ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A) with dimensions ![\inline N \times M](http://latex.codecogs.com/svg.latex?%5Cinline%20N%20%5Ctimes%20M). Rows are numbered ![\inline 1](http://latex.codecogs.com/svg.latex?%5Cinline%201) to ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N) from top to bottom, and columns are numbered ![\inline 1](http://latex.codecogs.com/svg.latex?%5Cinline%201) to ![\inline M](http://latex.codecogs.com/svg.latex?%5Cinline%20M) from left to right. A cell in the grid, which is the intersection of the ![\inline i^{th}](http://latex.codecogs.com/svg.latex?%5Cinline%20i%5E%7Bth%7D) row and ![\inline j^{th}](http://latex.codecogs.com/svg.latex?%5Cinline%20j%5E%7Bth%7D) column, is denoted by ![\inline [i, j]](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Bi%2C%20j%5D).

Each cell ![\inline [i, j]](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Bi%2C%20j%5D) contains ![\inline A_{i,j}](http://latex.codecogs.com/svg.latex?%5Cinline%20A_%7Bi%2Cj%7D) pizzas, where ![\inline A_{i,j}](http://latex.codecogs.com/svg.latex?%5Cinline%20A_%7Bi%2Cj%7D) is an integer. Miles is allowed to move in one of four directions, *up*, *down*, *left*  or *right*, one step at a time. In one step, Miles can move from cell ![\inline [i, j]](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Bi%2C%20j%5D) to one of ![\inline [i + 1, j]](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Bi%20%2B%201%2C%20j%5D), ![\inline [i - 1, j]](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Bi%20-%201%2C%20j%5D), ![\inline [i, j + 1]](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Bi%2C%20j%20%2B%201%5D) and ![\inline [i, j - 1]](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Bi%2C%20j%20-%201%5D), given that he doesn't reach the boundaries of the grid.

Peter adds the restriction that Miles can only move to a neighbouring cell if it has a strictly greater number of pizzas than the cell Miles is currently at. He asks Miles to find the length of the longest path possible in the grid, where length of a path is the number of cells constituting that path. A path starting and finishing at the same cell (i.e. consisting of only one cell) has length ![\inline 1](http://latex.codecogs.com/svg.latex?%5Cinline%201). Can you help Miles to solve this problem?

### Input

- Two integers ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N) and ![\inline M](http://latex.codecogs.com/svg.latex?%5Cinline%20M), denoting the number of rows and columns respectively.
- ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A), a tuple of size ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N). ![\inline A[i]](http://latex.codecogs.com/svg.latex?%5Cinline%20A%5Bi%5D) is a tuple of ![\inline M](http://latex.codecogs.com/svg.latex?%5Cinline%20M) integers, where ![\inline A[i][j]](http://latex.codecogs.com/svg.latex?%5Cinline%20A%5Bi%5D%5Bj%5D) represents the number of pizzas in cell ![\inline [i,j]](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Bi%2Cj%5D).

### Constraints

- ![\inline 1 \leq N \leq 1000](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20N%20%5Cleq%201000)
- ![\inline 1 \leq M \leq 1000](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20M%20%5Cleq%201000)
- ![\inline 0 \leq A_{i_j} \leq 10^9](http://latex.codecogs.com/svg.latex?%5Cinline%200%20%5Cleq%20A_%7Bi_j%7D%20%5Cleq%2010%5E9)
