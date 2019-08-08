# 10 Across: "It's a kind of magic"

You're given a set ![\inline S](http://latex.codecogs.com/svg.latex?%5Cinline%20S) of ![\inline N_S](http://latex.codecogs.com/svg.latex?%5Cinline%20N_S) strings, where each string consists only of digits from ![\inline 0](http://latex.codecogs.com/svg.latex?%5Cinline%200) to ![\inline 9](http://latex.codecogs.com/svg.latex?%5Cinline%209). The ![\inline i^{th}](http://latex.codecogs.com/svg.latex?%5Cinline%20i%5E%7Bth%7D) string in the set ![\inline S](http://latex.codecogs.com/svg.latex?%5Cinline%20S) is assigned a *score* of ![\inline x_i](http://latex.codecogs.com/svg.latex?%5Cinline%20x_i).

For any string ![\inline T](http://latex.codecogs.com/svg.latex?%5Cinline%20T), we define its *magic value* to be the sum of the scores of all strings from the set ![\inline S](http://latex.codecogs.com/svg.latex?%5Cinline%20S) which are present in ![\inline T](http://latex.codecogs.com/svg.latex?%5Cinline%20T) as substrings. Note that if a string occurs in ![\inline T](http://latex.codecogs.com/svg.latex?%5Cinline%20T) as a substring multiple times starting at different indices, its score is counted in the sum multiple times, once for each occurrence.

You're given ![\inline Q](http://latex.codecogs.com/svg.latex?%5Cinline%20Q), a set of ![\inline N_Q](http://latex.codecogs.com/svg.latex?%5Cinline%20N_Q) queries of the form ![\inline (L, R)](http://latex.codecogs.com/svg.latex?%5Cinline%20%28L%2C%20R%29).

For each query ![\inline Q_i = (L_i, R_i)](http://latex.codecogs.com/svg.latex?%5Cinline%20Q_i%20%3D%20%28L_i%2C%20R_i%29), let ![\inline str(j)](http://latex.codecogs.com/svg.latex?%5Cinline%20str%28j%29) be the string representation (with no leading zeroes) of integer ![\inline j](http://latex.codecogs.com/svg.latex?%5Cinline%20j), where ![\inline L_i \leq j \leq R_i](http://latex.codecogs.com/svg.latex?%5Cinline%20L_i%20%5Cleq%20j%20%5Cleq%20R_i).

Let ![\inline ans(i)](http://latex.codecogs.com/svg.latex?%5Cinline%20ans%28i%29) be the sum of magic values of ![\inline str(j)](http://latex.codecogs.com/svg.latex?%5Cinline%20str%28j%29) for all ![\inline j, L_i \leq j \leq R_i](http://latex.codecogs.com/svg.latex?%5Cinline%20j%2C%20L_i%20%5Cleq%20j%20%5Cleq%20R_i).

Return ![\inline (\sum_{i=1}^{N_Q} 2^i \times ans(i)) \mod{10^9 + 7}](http://latex.codecogs.com/svg.latex?%5Cinline%20%28%5Csum_%7Bi%3D1%7D%5E%7BN_Q%7D%202%5Ei%20%5Ctimes%20ans%28i%29%29%20%5Cmod%7B10%5E9%20%2B%207%7D).

### Input

- ![\inline S](http://latex.codecogs.com/svg.latex?%5Cinline%20S): A tuple of ![\inline N_S](http://latex.codecogs.com/svg.latex?%5Cinline%20N_S) strings.
- ![\inline X](http://latex.codecogs.com/svg.latex?%5Cinline%20X): A tuple of ![\inline N_S](http://latex.codecogs.com/svg.latex?%5Cinline%20N_S) integers where ![\inline i^{th}](http://latex.codecogs.com/svg.latex?%5Cinline%20i%5E%7Bth%7D) denotes ![\inline x_i](http://latex.codecogs.com/svg.latex?%5Cinline%20x_i), the score of the ![\inline i^{th}](http://latex.codecogs.com/svg.latex?%5Cinline%20i%5E%7Bth%7D) string in ![\inline S](http://latex.codecogs.com/svg.latex?%5Cinline%20S).
- ![\inline Q](http://latex.codecogs.com/svg.latex?%5Cinline%20Q): A tuple of ![\inline N_Q](http://latex.codecogs.com/svg.latex?%5Cinline%20N_Q) elements ![\inline Q_1, Q_2, ..., Q_{N_Q}](http://latex.codecogs.com/svg.latex?%5Cinline%20Q_1%2C%20Q_2%2C%20...%2C%20Q_%7BN_Q%7D). ![\inline Q_i](http://latex.codecogs.com/svg.latex?%5Cinline%20Q_i) is a tuple ![\inline (L_i, R_i)](http://latex.codecogs.com/svg.latex?%5Cinline%20%28L_i%2C%20R_i%29) denoting the ![\inline i^{th}](http://latex.codecogs.com/svg.latex?%5Cinline%20i%5E%7Bth%7D) query.

### Constraints

- ![\inline 1 \leq N_S, N_Q \leq 3 \times 10^3](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20N_S%2C%20N_Q%20%5Cleq%203%20%5Ctimes%2010%5E3)
- ![\inline 1 \leq \textrm{length}(S_i) \leq 18](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20%5Ctextrm%7Blength%7D%28S_i%29%20%5Cleq%2018) for all ![\inline i](http://latex.codecogs.com/svg.latex?%5Cinline%20i)
- ![\inline 1 \leq x_i \leq 10^{9}](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20x_i%20%5Cleq%2010%5E%7B9%7D) for all ![\inline i](http://latex.codecogs.com/svg.latex?%5Cinline%20i)
- ![\inline 1 \leq L_i, R_i \leq 10^{18}](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20L_i%2C%20R_i%20%5Cleq%2010%5E%7B18%7D) for all ![\inline i](http://latex.codecogs.com/svg.latex?%5Cinline%20i)

## My Solution

My first solution was a simple brute force algorithm, looping over every string from L to R for every query and sliding the given strings over the number to see what matched. Obviously this was waaaay too slow for the hidden test cases and I had to think of something else.

First I played with the idea of using smarter string searching algorithms, but I realised that any solution that looped over the values between L and R was doomed to fail. So my solution tries to calculate the number of times each string will appear between L and R without doing any string searching. It does this by first counting how many times it would appear in the least significant part of the numbers, then (recursively) moves on to counting the occurences in the next column, and so on. This was very tricky to think about (especially when trying to handle leading 0s correctly) and I had to make a lot of tweaks until I got an algorithm that even gave the same output as the brute force solution. I would not be surprised if this was a source of a lot of failed test cases.
