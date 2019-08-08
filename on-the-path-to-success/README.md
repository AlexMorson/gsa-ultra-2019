# 5 Down: "On the path to success"

Laura gives Dale an undirected tree with ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N) nodes numbered ![\inline 1](http://latex.codecogs.com/svg.latex?%5Cinline%201) to ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N), rooted at node ![\inline 1](http://latex.codecogs.com/svg.latex?%5Cinline%201). In this tree, node ![\inline i](http://latex.codecogs.com/svg.latex?%5Cinline%20i) has a value ![\inline V_i](http://latex.codecogs.com/svg.latex?%5Cinline%20V_i) associated with it.

A path in the tree is defined as a sequence of distinct nodes ![\inline x_1, x_2, ..., x_k](http://latex.codecogs.com/svg.latex?%5Cinline%20x_1%2C%20x_2%2C%20...%2C%20x_k) such that for all ![\inline j](http://latex.codecogs.com/svg.latex?%5Cinline%20j), ![\inline x_j](http://latex.codecogs.com/svg.latex?%5Cinline%20x_j) and ![\inline x_{j+1}](http://latex.codecogs.com/svg.latex?%5Cinline%20x_%7Bj%2B1%7D) are connected by a direct edge and ![\inline 1 \leq x_j \leq N](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20x_j%20%5Cleq%20N), where ![\inline k \geq 1](http://latex.codecogs.com/svg.latex?%5Cinline%20k%20%5Cgeq%201). Laura considers two paths to be different if and only if there is a node in one of the paths that's not present in the other.

Laura defines the *value* of a path as the bitwise AND of the values of nodes on that path, and the *score* of a path as the number of set bits in the value of the path.

Laura wants Dale to find ![\inline f(k)](http://latex.codecogs.com/svg.latex?%5Cinline%20f%28k%29), the number of paths with *score* ![\inline k](http://latex.codecogs.com/svg.latex?%5Cinline%20k), for each ![\inline k](http://latex.codecogs.com/svg.latex?%5Cinline%20k) from 0 to 8. You need to help Dale by returning ![\inline \sum_{i = 0}^{8} f(i) \times 2^i](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Csum_%7Bi%20%3D%200%7D%5E%7B8%7D%20f%28i%29%20%5Ctimes%202%5Ei). Since this number may be large, output it modulo ![\inline 10^9 + 7](http://latex.codecogs.com/svg.latex?%5Cinline%2010%5E9%20%2B%207).

### Input

- ![\inline P](http://latex.codecogs.com/svg.latex?%5Cinline%20P): a tuple of ![\inline N-1](http://latex.codecogs.com/svg.latex?%5Cinline%20N-1) elements ![\inline P_1, P_2, ..., P_{N-1}](http://latex.codecogs.com/svg.latex?%5Cinline%20P_1%2C%20P_2%2C%20...%2C%20P_%7BN-1%7D) where ![\inline P_i](http://latex.codecogs.com/svg.latex?%5Cinline%20P_i) denotes the parent of node ![\inline i+1](http://latex.codecogs.com/svg.latex?%5Cinline%20i%2B1).
- ![\inline V](http://latex.codecogs.com/svg.latex?%5Cinline%20V): a tuple of ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N) integers ![\inline V_1, V_2, ..., V_{N}](http://latex.codecogs.com/svg.latex?%5Cinline%20V_1%2C%20V_2%2C%20...%2C%20V_%7BN%7D) where ![\inline V_i](http://latex.codecogs.com/svg.latex?%5Cinline%20V_i) denotes the value of node ![\inline i](http://latex.codecogs.com/svg.latex?%5Cinline%20i).

### Constraints

- ![\inline 2 \le N \le 40000](http://latex.codecogs.com/svg.latex?%5Cinline%202%20%5Cle%20N%20%5Cle%2040000)
- ![\inline 0 \le V_i < 2^{8}](http://latex.codecogs.com/svg.latex?%5Cinline%200%20%5Cle%20V_i%20%3C%202%5E%7B8%7D), for all ![\inline i](http://latex.codecogs.com/svg.latex?%5Cinline%20i)

## My Solution

This problem had me worried until I read "bitwise AND" because I realised that `0 & x = 0`, so we can just loop through every node in the tree, do a tree search from that node - keeping track of the value of the path to each node along the way - until the value hits 0. We then know that after this point, the value of the paths to every node that has not been seen will be 0 as well, so we can stop exploring. The problem statement defines paths to be the same if they have the same pair of start/end nodes, so I actually count every path twice, meaning that I need to halve the values I get for f(i).

I have a feeling that a test case with every node having value 255 would take too long for my program, but fortunately the test cases that were given must have been reasonable because my program had no trouble finishing in time.
