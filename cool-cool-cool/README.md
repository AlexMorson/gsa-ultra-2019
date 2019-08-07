# 6 Across: "Cool, cool, cool"

Troy recently learned about *bitonic sequences*.

Let ![\inline S](http://latex.codecogs.com/svg.latex?%5Cinline%20S) be a sequence of ![\inline L_S](http://latex.codecogs.com/svg.latex?%5Cinline%20L_S) integers. A contiguous subsequence of ![\inline S](http://latex.codecogs.com/svg.latex?%5Cinline%20S), ![\inline S_i, S_{i+1}, ..., S_j](http://latex.codecogs.com/svg.latex?%5Cinline%20S_i%2C%20S_%7Bi%2B1%7D%2C%20...%2C%20S_j), can be represented as ![\inline S[i..j]](http://latex.codecogs.com/svg.latex?%5Cinline%20S%5Bi..j%5D) where ![\inline 1 \leq i,j \leq L_S](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20i%2Cj%20%5Cleq%20L_S). A sequence ![\inline S](http://latex.codecogs.com/svg.latex?%5Cinline%20S) is *bitonic* if for some ![\inline i](http://latex.codecogs.com/svg.latex?%5Cinline%20i) the subsequence ![\inline S[1..i]](http://latex.codecogs.com/svg.latex?%5Cinline%20S%5B1..i%5D) is strictly increasing and the subsequence ![\inline S[i..L_S]](http://latex.codecogs.com/svg.latex?%5Cinline%20S%5Bi..L_S%5D) is strictly decreasing. Note that either subsequence could be of length ![\inline 1](http://latex.codecogs.com/svg.latex?%5Cinline%201).

Abed gets tired of Troy's constant bragging about this new knowledge. He decides to test his friend with a challenge.

Abed gives Troy an array ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A) of ![\inline L_A](http://latex.codecogs.com/svg.latex?%5Cinline%20L_A) integers. In one operation, Troy can increment the value of a single element of ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A) by ![\inline 1](http://latex.codecogs.com/svg.latex?%5Cinline%201). Abed asks Troy to convert ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A) into a bitonic sequence in as few operations as possible, and then tell Abed the number of operations it took him to do so.

Troy knows his stuff, but being put on the spot by his best friend has really undermined his confidence. Can you help Troy with this task?

### Input

- ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A): a tuple of ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N) integers, where ![\inline i^{th}](http://latex.codecogs.com/svg.latex?%5Cinline%20i%5E%7Bth%7D) integer denotes ![\inline A_i](http://latex.codecogs.com/svg.latex?%5Cinline%20A_i).

### Constraints

- ![\inline 1 \leq N \leq 2 \times 10^6](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20N%20%5Cleq%202%20%5Ctimes%2010%5E6)
- ![\inline 1 \leq A_i \leq 10^9](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20A_i%20%5Cleq%2010%5E9)
