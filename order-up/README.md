# 9 Down: "Order up!"

You are the owner of a well-reviewed but remote gastropub which prides itself on the satisfaction of its many customers. Unfortunately, a recent spate of heavy snow has made the long and windy path to your delivery entrance unsafe and so you will have to try to serve dinner with the meagre supplies left in the kitchen pantry.

Tonight you have ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N) guests of varying appetites. A nifty pre-dinner survey has informed you of the appetite of each guest.

You have managed to scrape together ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N) variously-sized servings of a surprisingly decent-looking dish. You consider speaking with a strong accent to fend off queries about what the dish actually has in it, but decide it could cause offence.

You must distribute the servings in such a way that the total food consumption is maximised. Every guest in the pub must be served with exactly one serving of food.

Given the appetites of your guests and the sizes of your servings, return the maximum possible total food consumption in food units (you can worry about the TripAdvisor reviews another time).

### Input

- ![\inline C](http://latex.codecogs.com/svg.latex?%5Cinline%20C): a tuple ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N) of integers ![\inline C_1, C_2, ..., C_N](http://latex.codecogs.com/svg.latex?%5Cinline%20C_1%2C%20C_2%2C%20...%2C%20C_N) where ![\inline C_i](http://latex.codecogs.com/svg.latex?%5Cinline%20C_i) denotes the consumption capacity of the ![\inline i^{th}](http://latex.codecogs.com/svg.latex?%5Cinline%20i%5E%7Bth%7D) guest, in food units.
- ![\inline D](http://latex.codecogs.com/svg.latex?%5Cinline%20D): a tuple ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N) of integers ![\inline D_1, D_2, ..., D_N](http://latex.codecogs.com/svg.latex?%5Cinline%20D_1%2C%20D_2%2C%20...%2C%20D_N) where ![\inline D_i](http://latex.codecogs.com/svg.latex?%5Cinline%20D_i) denotes the size of the ![\inline i^{th}](http://latex.codecogs.com/svg.latex?%5Cinline%20i%5E%7Bth%7D) serving, in food units.

### Constraints

- ![\inline 1 \leq N \leq 10^6](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20N%20%5Cleq%2010%5E6)
- ![\inline 1 \leq C_i, D_i \leq 10^9](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20C_i%2C%20D_i%20%5Cleq%2010%5E9)
