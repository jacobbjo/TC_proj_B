# TC_proj_B
A simple representation of a checkerboard and a checker piece that
can move by tree steps in n, s, e, w or two steps diagonally to
ne, nw, se, sw. The goal is to find a path where the piece has visited
every square on the board exactly once.

The problem is similar to the
NP-hard problem "knight's tour". A brute-fore would be problematic
already at this board size of 10x10 because of the runtime. Because
of the rather small board size the problem can be solved with smart
moves based on an heuristic.

This sollution is based on Warnsdorf's
rule [^1] with a random handling of ties. This sollution has also
implemented an increasing randomization based on the amount of
previous unsucsessfull iterations. This makes the algorithm avoid
getting stuck in the same sollution and seems works well on boards
up to about 40x40 squares.



## Run

Written in Python 3.6

Run with a suitable Python interpreter

For example:

**python3 main.py**

## Reference

[^1] [Warnsdorf's rule Wikipedia](https://en.wikipedia.org/wiki/Knight%27s_tour#Warnsdorf's_rule)
