# 7 Down: "The good, the bad and the stringy"

Define a string as a sequence of characters from the lowercase English alphabet.

The length of a string $S$ is represented as the integer $L_S$. A contiguous substring of S, $S_i, S_{i+1}, ..., S_j$, is represented as $S[i..j]$ where $1 \leq i \leq j \leq L_S$.

A string $A$ occurs $p$ times in string $B$ if $A$ exists as a substring in $B$, $p$ times. Note that overlapping occurrences are counted separately.

Given two strings $X$ and $Y$ along with two integers $k_1$ and $k_2$, the *goodness* of some third string $S$ is defined as the number of indices $i$ such that $S[1..i]$ has at most $k_1$ occurrences of $X$ and $S[i+1..L_S]$ has at most $k_2$ occurrences of $Y$, where $0 \le i \le L_S$. When $i = 0$, the string $S[1..i]$ would be considered an empty string. When $i = L_S$, the string $S[i+1..L_S]$ would be considered an empty string.

Given an integer $N$, you are asked to find the sum of the *goodness* of all possible strings of length $N$. Remember that a string may only contain lowercase characters from the English alphabet. Since this value can be large, so give the answer modulo $10^{9}+7$.

### Input

- $N$: an integer.
- $k_1$: an integer.
- $k_2$: an integer.
- $X$: a string of lowercase characters from the English alphabet.
- $Y$: a string of lowercase characters from the English alphabet.

### Constraints

- $1 \le N \le 10^{8}$
- $1 \le k_1 \times len(X) \le 16$
- $1 \le k_2 \times len(Y) \le 16$
