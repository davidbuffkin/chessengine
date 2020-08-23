#David Buffkin

import chess
import math
from random import random

values = {'P' : 100, 'R' : 500, 'N' : 300, 'B' : 300, 'Q' : 900, 'K' : 0, 'k' : 0,\
          'p' : -100, 'r' : -500, 'n' : -300, 'b' : -300, 'q' : -900, "\n" : 0, "." : 0, " " : 0}

def evaluate(board, black):
    if board.is_game_over():
        return math.inf if (board.turn == chess.WHITE) == black else -math.inf
    return (-1 if black else 1) * sum([values[c] for c in str(board)])


def search(board : chess.Board, black, depth, alpha, beta):

    best = [-math.inf, None]

    for move in board.legal_moves:

        board.push(move)

        moveScore = None
        if depth <= 0:
            moveScore = evaluate(board, black)
        else:
            moveScore = -search(board, not black, depth - 1, -beta, -alpha)[0]
        
        board.pop()

        moveScore += random()  - .5

        if moveScore > best[0]: best = [moveScore, move]
        if best[0] > alpha: alpha = best[0]
        if alpha >= beta: return [alpha, None]

    return best

def getMove(board, difficulty):
    return search(board, board.turn == chess.BLACK, difficulty, -math.inf, math.inf)[1]


