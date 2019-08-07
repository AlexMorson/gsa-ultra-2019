# 13 Across: "Zoinks!"

The Mystery Gang have come face to face with a very real - and very scary - horde of zombies. The Gang have to defeat the zombie horde, but they must be very careful: if a member of the Gang is bitten by a zombie, that member becomes a zombie themselves. The Mystery Gang will only be victorious when every zombie has been destroyed.

The battle proceeds round by round where each side takes turns to attack the other. One side's attack constitutes a full round.

In each of the zombie horde's turns they will turn  ![\inline \left \lfloor{m \times T}\right \rfloor](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Cleft%20%5Clfloor%7Bm%20%5Ctimes%20T%7D%5Cright%20%5Crfloor) Gang members into zombies, where ![\inline m](http://latex.codecogs.com/svg.latex?%5Cinline%20m) is the number of zombies left in the horde and ![\inline T](http://latex.codecogs.com/svg.latex?%5Cinline%20T) is the horde's *zombie turning ratio*. Any Gang members turned by the zombies will join the zombie horde in the next round.

In each of the Mystery Gang's turns they will destroy ![\inline \left \lfloor{n \times D}\right \rfloor](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Cleft%20%5Clfloor%7Bn%20%5Ctimes%20D%7D%5Cright%20%5Crfloor) zombies, where ![\inline n](http://latex.codecogs.com/svg.latex?%5Cinline%20n) is the number of members left in the Gang and ![\inline D](http://latex.codecogs.com/svg.latex?%5Cinline%20D) is the Gang's *zombie destroying ratio*. Any zombies destroyed by the Gang will be permanently removed from the battle.

The zombie horde will start the battle. Provided with the terms described above, what is the minimum number of members the Mystery Gang wins in order to win the battle within *N* rounds?

### Input

- ![\inline Z](http://latex.codecogs.com/svg.latex?%5Cinline%20Z): an integer denoting the number of zombies in the zombie horde before the battle begins.
- ![\inline T](http://latex.codecogs.com/svg.latex?%5Cinline%20T): the horde's *zombie turning ratio* ![\inline \frac{a}{b}](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Cfrac%7Ba%7D%7Bb%7D), represented as a tuple of two integers ![\inline (a, b)](http://latex.codecogs.com/svg.latex?%5Cinline%20%28a%2C%20b%29).
- ![\inline D](http://latex.codecogs.com/svg.latex?%5Cinline%20D): the Mystery Gang's *zombie destruction ratio* ![\inline \frac{a}{b}](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Cfrac%7Ba%7D%7Bb%7D), represented as a tuple of two integers ![\inline (a, b)](http://latex.codecogs.com/svg.latex?%5Cinline%20%28a%2C%20b%29).
- ![\inline N](http://latex.codecogs.com/svg.latex?%5Cinline%20N): an integer denoting the total number of rounds within which the Mystery Gang need to destroy all the zombies in the horde.

### Constraints

- ![\inline 1 \leq N \leq 2 \times 10^5](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20N%20%5Cleq%202%20%5Ctimes%2010%5E5)
- ![\inline 1 \leq Z, a, b \leq 10^9](http://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20Z%2C%20a%2C%20b%20%5Cleq%2010%5E9)

### Example

Consider ![\inline Z = 1](http://latex.codecogs.com/svg.latex?%5Cinline%20Z%20%3D%201), ![\inline T = \frac{1}{2}](http://latex.codecogs.com/svg.latex?%5Cinline%20T%20%3D%20%5Cfrac%7B1%7D%7B2%7D), ![\inline D = \frac{2}{1}](http://latex.codecogs.com/svg.latex?%5Cinline%20D%20%3D%20%5Cfrac%7B2%7D%7B1%7D), ![\inline N = 2](http://latex.codecogs.com/svg.latex?%5Cinline%20N%20%3D%202).

In this case, the Mystery Gang win in two rounds with just a single gang member.

In the first round, the zombies turn at maximum ![\inline \left \lfloor{1 \times \frac{1}{2}}\right \rfloor = 0](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Cleft%20%5Clfloor%7B1%20%5Ctimes%20%5Cfrac%7B1%7D%7B2%7D%7D%5Cright%20%5Crfloor%20%3D%200) Gang members. After the first round, the size of the zombie horde is ![\inline 1](http://latex.codecogs.com/svg.latex?%5Cinline%201), and size of the Mystery Gang is ![\inline 1](http://latex.codecogs.com/svg.latex?%5Cinline%201).

In the second round, the Gang destroy at maximum ![\inline \left \lfloor{1 \times \frac{2}{1}}\right \rfloor = 2](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Cleft%20%5Clfloor%7B1%20%5Ctimes%20%5Cfrac%7B2%7D%7B1%7D%7D%5Cright%20%5Crfloor%20%3D%202) zombies. After the second round, the size of the zombie horde is ![\inline 0](http://latex.codecogs.com/svg.latex?%5Cinline%200), and size of the Mystery Gang is still ![\inline 1](http://latex.codecogs.com/svg.latex?%5Cinline%201).
