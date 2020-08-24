#David Buffkin

import chess
import math
from random import random, shuffle


# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str) ...
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()


values = {'P' : 100, 'R' : 500, 'N' : 300, 'B' : 300, 'Q' : 900, 'K' : 0, 'k' : 0,\
          'p' : -100, 'r' : -500, 'n' : -300, 'b' : -300, 'q' : -900, "\n" : 0, "." : 0, " " : 0}


def evaluate(board, black):
    if board.is_checkmate():
        return 1000000 if (board.turn == chess.WHITE) == black else -1000000
    return (-1 if black else 1) * sum([values[c] for c in str(board)])


def search(board : chess.Board, black, depth, alpha, beta, top):

    best = [-10000000, None]

    moves = list(board.legal_moves)
    shuffle(moves) #TODO remove this when evaluate is better and for move ordering
    

    for i, move in enumerate(moves):
        if top:
            printProgressBar(i, len(moves), "Thinking...")

        board.push(move)

        moveScore = None
        if board.is_stalemate():
            board.pop()
            moveScore =  -1000000 if evaluate(board, black) > 0 == black else 0
            board.push(move)
        elif depth <= 0:
            moveScore = evaluate(board, black)
        else:
            moveScore = -search(board, not black, depth - 1, -beta, -alpha, False)[0]
        
        board.pop()

        #print(("    " * depth)+ "Move " + str(move) + " has value " + str(moveScore))
        

        if moveScore > best[0]: best = [moveScore, move]
        if best[0] > alpha: alpha = best[0]
        if alpha >= beta: return [alpha, None]
    if top:
        printProgressBar(1, 1, "Done Thinking!")
        #print("Returning " + str(best))
    return best

def getMove(board, difficulty):
    return search(board, board.turn == chess.BLACK, difficulty, -math.inf, math.inf, True)[1]


