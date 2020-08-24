# Chess Engine

This is a python-based chess engine. Currently it runs a negamax algorithm to depth `difficulty`, and makes use of alpha-beta pruning and the principal variation.
Installation requires the python-chess module, which can be installed as
>pip install python-chess

and the pywebview module, as
>pip install pywebview

To run an interactive game with the engine, use 
>python game.py -d [difficulty] -g

or omit the `-g` for a CLI. Difficulty greater than 4 will take longer than you wish to run. Note with graphics, you still need to type moves in the CLI; there is no interactive GUI support as of yet.

There is more to come! I will be implementing some of the practices outlined <a href=http://www.frayn.net/beowulf/theory.html#transposition>here</a>.
