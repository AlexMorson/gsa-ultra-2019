# 13 Across: "Zoinks!"

The Mystery Gang have come face to face with a very real - and very scary - horde of zombies. The Gang have to defeat the zombie horde, but they must be very careful: if a member of the Gang is bitten by a zombie, that member becomes a zombie themselves. The Mystery Gang will only be victorious when every zombie has been destroyed.

The battle proceeds round by round where each side takes turns to attack the other. One side's attack constitutes a full round.

In each of the zombie horde's turns they will turn  $\left \lfloor{m \times T}\right \rfloor$ Gang members into zombies, where $m$ is the number of zombies left in the horde and $T$ is the horde's *zombie turning ratio*. Any Gang members turned by the zombies will join the zombie horde in the next round.

In each of the Mystery Gang's turns they will destroy $\left \lfloor{n \times D}\right \rfloor$ zombies, where $n$ is the number of members left in the Gang and $D$ is the Gang's *zombie destroying ratio*. Any zombies destroyed by the Gang will be permanently removed from the battle.

The zombie horde will start the battle. Provided with the terms described above, what is the minimum number of members the Mystery Gang wins in order to win the battle within *N* rounds?

### Input

- $Z$: an integer denoting the number of zombies in the zombie horde before the battle begins.
- $T$: the horde's *zombie turning ratio* $\frac{a}{b}$, represented as a tuple of two integers $(a, b)$.
- $D$: the Mystery Gang's *zombie destruction ratio* $\frac{a}{b}$, represented as a tuple of two integers $(a, b)$.
- $N$: an integer denoting the total number of rounds within which the Mystery Gang need to destroy all the zombies in the horde.

### Constraints

- $1 \leq N \leq 2 \times 10^5$
- $1 \leq Z, a, b \leq 10^9$

### Example

Consider $Z = 1$, $T = \frac{1}{2}$, $D = \frac{2}{1}$, $N = 2$.

In this case, the Mystery Gang win in two rounds with just a single gang member.

In the first round, the zombies turn at maximum $\left \lfloor{1 \times \frac{1}{2}}\right \rfloor = 0$ Gang members. After the first round, the size of the zombie horde is $1$, and size of the Mystery Gang is $1$.

In the second round, the Gang destroy at maximum $\left \lfloor{1 \times \frac{2}{1}}\right \rfloor = 2$ zombies. After the second round, the size of the zombie horde is $0$, and size of the Mystery Gang is still $1$.
