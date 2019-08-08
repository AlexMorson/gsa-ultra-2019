# 11 Down: "One-ing streak"

You're given an array ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A) of ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N) elements ![\inline A_1, A_2, ..., A_N](http://latex.codecogs.com/svg.latex?%5Cinline%20A_1%2C%20A_2%2C%20...%2C%20A_N), where ![\inline A_i](http://latex.codecogs.com/svg.latex?%5Cinline%20A_i) is either ![\inline 0](http://latex.codecogs.com/svg.latex?%5Cinline%200) or ![\inline 1](http://latex.codecogs.com/svg.latex?%5Cinline%201), for ![\inline 1 \leq i \leq N](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20i%20%5Cleq%20N). A subarray of array ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A) is defined as a non-empty sequence of contiguous elements from array ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A).

Your objective is to find the longest subarray in which every element is a ![\inline 1](http://latex.codecogs.com/svg.latex?%5Cinline%201). Output the index of the first element in the subarray. If there are multiple such subarrays, select the one which has smallest such index. If no such subarray exists, output ![\inline -1](http://latex.codecogs.com/svg.latex?%5Cinline%20-1).

### Input

- ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A): a tuple of ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N) integers ![\inline A_1, A_2, .., A_N](http://latex.codecogs.com/svg.latex?%5Cinline%20A_1%2C%20A_2%2C%20..%2C%20A_N).

### Constraints

- ![\inline 1 \leq N \leq 10^7](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20N%20%5Cleq%2010%5E7)

## My Solution

I just loop through the array, keeping track of the longest sequence of 1s and where it started, and the current number of 1s in a row and where that started.
