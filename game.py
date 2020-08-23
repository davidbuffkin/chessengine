#David Buffkin

#This is just a CLI to play with the engine.

import argparse
import chess
from random import choice
from engine import getMove

parser = argparse.ArgumentParser(description='Play a game of chess.')
parser.add_argument('-d', '--difficulty', help='Engine difficulty (0 for random)', type=int, default=0)
parser.add_argument('-b', '--black', help='Play as black', action='store_true')
args = parser.parse_args()

board = chess.Board()

def getPlayerMove():
    moveString = input("What move will you make? Use UCI notation (\'e2e4\' for example)\n").replace(" ","")
    try:
        move = chess.Move.from_uci(moveString)
        if move not in board.legal_moves: 
            raise Exception
        return move
    except:
        print(f"{moveString} is not a valid move. Try again.\n")
        return getPlayerMove()

def getEngineMove():
    if args.difficulty == 0:
        return choice(list(board.legal_moves))
    return getMove(board, args.difficulty)

print("\n" +  str(board) +  "\n")
while not board.is_game_over():
    move = getPlayerMove()
    board.push(move)
    print("\n" +  str(board) + "\n")
    if not board.is_game_over():
        move = getEngineMove()
        print("Engine moves " + move.uci())
        board.push(move)
        print("\n" + str(board) + "\n")

if board.is_stalemate():
    print("Stalemate.")
else:
    if board.is_checkmate():
        print("Checkmate!")
    if board.turn == chess.WHITE:
        print("White wins.")
    else:
        print("Black wins.")


