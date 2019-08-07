# 7 Down: "The good, the bad and the stringy"

Define a string as a sequence of characters from the lowercase English alphabet.

The length of a string ![\inline S](http://latex.codecogs.com/svg.latex?%5Cinline%20S) is represented as the integer ![\inline L_S](http://latex.codecogs.com/svg.latex?%5Cinline%20L_S). A contiguous substring of S, ![\inline S_i, S_{i+1}, ..., S_j](http://latex.codecogs.com/svg.latex?%5Cinline%20S_i%2C%20S_%7Bi%2B1%7D%2C%20...%2C%20S_j), is represented as ![\inline S[i..j]](http://latex.codecogs.com/svg.latex?%5Cinline%20S%5Bi..j%5D) where ![\inline 1 \leq i \leq j \leq L_S](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20i%20%5Cleq%20j%20%5Cleq%20L_S).

A string ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A) occurs ![\inline p](http://latex.codecogs.com/svg.latex?%5Cinline%20p) times in string ![\inline B](http://latex.codecogs.com/svg.latex?%5Cinline%20B) if ![\inline A](http://latex.codecogs.com/svg.latex?%5Cinline%20A) exists as a substring in ![\inline B](http://latex.codecogs.com/svg.latex?%5Cinline%20B), ![\inline p](http://latex.codecogs.com/svg.latex?%5Cinline%20p) times. Note that overlapping occurrences are counted separately.

Given two strings ![\inline X](http://latex.codecogs.com/svg.latex?%5Cinline%20X) and ![\inline Y](http://latex.codecogs.com/svg.latex?%5Cinline%20Y) along with two integers ![\inline k_1](http://latex.codecogs.com/svg.latex?%5Cinline%20k_1) and ![\inline k_2](http://latex.codecogs.com/svg.latex?%5Cinline%20k_2), the *goodness* of some third string ![\inline S](http://latex.codecogs.com/svg.latex?%5Cinline%20S) is defined as the number of indices ![\inline i](http://latex.codecogs.com/svg.latex?%5Cinline%20i) such that ![\inline S[1..i]](http://latex.codecogs.com/svg.latex?%5Cinline%20S%5B1..i%5D) has at most ![\inline k_1](http://latex.codecogs.com/svg.latex?%5Cinline%20k_1) occurrences of ![\inline X](http://latex.codecogs.com/svg.latex?%5Cinline%20X) and ![\inline S[i+1..L_S]](http://latex.codecogs.com/svg.latex?%5Cinline%20S%5Bi%2B1..L_S%5D) has at most ![\inline k_2](http://latex.codecogs.com/svg.latex?%5Cinline%20k_2) occurrences of ![\inline Y](http://latex.codecogs.com/svg.latex?%5Cinline%20Y), where ![\inline 0 \le i \le L_S](http://latex.codecogs.com/svg.latex?%5Cinline%200%20%5Cle%20i%20%5Cle%20L_S). When ![\inline i = 0](http://latex.codecogs.com/svg.latex?%5Cinline%20i%20%3D%200), the string ![\inline S[1..i]](http://latex.codecogs.com/svg.latex?%5Cinline%20S%5B1..i%5D) would be considered an empty string. When ![\inline i = L_S](http://latex.codecogs.com/svg.latex?%5Cinline%20i%20%3D%20L_S), the string ![\inline S[i+1..L_S]](http://latex.codecogs.com/svg.latex?%5Cinline%20S%5Bi%2B1..L_S%5D) would be considered an empty string.

Given an integer ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N), you are asked to find the sum of the *goodness* of all possible strings of length ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N). Remember that a string may only contain lowercase characters from the English alphabet. Since this value can be large, so give the answer modulo ![\inline 10^{9}+7](http://latex.codecogs.com/svg.latex?%5Cinline%2010%5E%7B9%7D%2B7).

### Input

- ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N): an integer.
- ![\inline k_1](http://latex.codecogs.com/svg.latex?%5Cinline%20k_1): an integer.
- ![\inline k_2](http://latex.codecogs.com/svg.latex?%5Cinline%20k_2): an integer.
- ![\inline X](http://latex.codecogs.com/svg.latex?%5Cinline%20X): a string of lowercase characters from the English alphabet.
- ![\inline Y](http://latex.codecogs.com/svg.latex?%5Cinline%20Y): a string of lowercase characters from the English alphabet.

### Constraints

- ![\inline 1 \le N \le 10^{8}](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cle%20N%20%5Cle%2010%5E%7B8%7D)
- ![\inline 1 \le k_1 \times len(X) \le 16](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cle%20k_1%20%5Ctimes%20len%28X%29%20%5Cle%2016)
- ![\inline 1 \le k_2 \times len(Y) \le 16](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cle%20k_2%20%5Ctimes%20len%28Y%29%20%5Cle%2016)
