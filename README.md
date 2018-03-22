# TC_proj_B
A simple representation of a checkerboard and a checker piece that
can move by tree steps in n, s, e, w or two steps diagonally to
ne, nw, se, sw. The goal is to find a path where the piece has visited
every square on the board exactly once.

The problem is similar to the
NP-hard problem "knight's tour". Because of the rather small board size
the problem can be solved with smart moves based on a heuristic.
A brute-fore would be problematic already at this board size because
of the runtime.


## Run

Written in Python 3.6

Run with a suitable Python interpreter

for example:

**python3 main.py**