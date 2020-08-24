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





def evaluate(board, black):
    if board.is_checkmate():
        return 1000000 if (board.turn == chess.WHITE) == black else -1000000
    #return (-1 if black else 1) * sum([values[c] for c in str(board)])
    boardString = str(board).replace(" ","").replace("\n", "")
    value = 0
    for i in range(64):
        piece = str(boardString)[i]
        if piece == ".": continue
        number = 8 - i // 8
        letter = i % 8 + 1
        if piece == "P":
            value += 100 + number * 1.5
        elif piece == "p":
            value -= 100 + (9 - number) * 1.5
        elif piece == "R":
            value += 500
        elif piece == "r":
            value -= 500
        elif piece == "N":
            if letter > 4:
                letter = 9 - letter
            if number > 4:
                number = 9 - number
            value += 300 + (letter + number) * 3
        elif piece == "n":
            if letter > 4:
                letter = 9 - letter
            if number > 4:
                number = 9 - number
            value -= 300 + (letter + number) * 3
        elif piece == "B":
            value += 300
            if(letter + number) % 2 == 0:
                #light square. implement better later
                if letter == number:
                    value += 50
            else:
                #dark square
                if abs(letter - number) == 7:
                    value += 50
        elif piece == "b":
            value -= 300
            if(letter + number) % 2 == 0:
                #light square. implement better later
                if letter == number:
                    value -= 50
            else:
                #dark square
                if abs(letter - number) == 7:
                    value -= 50
        elif piece == "Q":
            value += 900
        elif piece == "q":
            value -= 900
        elif piece == "K":
            letter = abs(letter - 4)
            if number == 1:
                value += 5 * letter
            elif number == 2:
                value += 3 * letter
        elif piece == "k":
            letter = abs(letter - 5)
            if number == 8:
                value -= 5 * letter
            elif number == 7:
                value -= 3 * letter
        else:
            raise NameError(f"Piece \'{piece}\' not recognized.")
        
    return value * (-1 if black else 1)



lastBest = None
def search(board : chess.Board, black, depth, alpha, beta, top):
    global lastBest

    best = [-10000000, []]

    moves = list(board.legal_moves)
    if len(moves) == 0: return [evaluate(board, black), []]
    
    #Ordering
    if lastBest:
        if lastBest in moves:
            moves.remove(lastBest)
            #shuffle(moves)
            moves = [lastBest] + moves
    

    for i, move in enumerate(moves):
        if top:
            printProgressBar(i, len(moves), "Thinking...")

        board.push(move)

        moveScore = None
        pv = None
        if board.is_stalemate():
            board.pop()
            moveScore =  -1000000 if evaluate(board, black) > 0 == black else 0
            board.push(move)
        elif depth <= 0:
            moveScore = evaluate(board, black)
            pv = []
        else:
            moveScore, pv = search(board, not black, depth - 1, -beta, -alpha, False)
            moveScore *= -1
        
        board.pop()

        if moveScore > best[0]: best = [moveScore, [move] + pv]
        if best[0] > alpha: alpha = best[0]
        if alpha >= beta: return [alpha, []]
    if top:
        printProgressBar(1, 1, "Done Thinking!")
        #print("Returning " + str(best))
    return best

def getMove(board, difficulty):
    global lastBest
    bestScore, PV =  search(board, board.turn == chess.BLACK, difficulty, -math.inf, math.inf, True)
    if len(PV) >= 3:
        lastBest = PV[2]
    #print([str(m) for m in PV])
    return PV[0]


