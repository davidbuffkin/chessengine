#David Buffkin

#This is inital graphics testing

import argparse
import chess
from random import choice
from engine import getMove
import chess.svg
import webview

parser = argparse.ArgumentParser(description='Play a game of chess.')
parser.add_argument('-d', '--difficulty', help='Engine difficulty (0 for random)', type=int, default=0)
#parser.add_argument('-b', '--black', help='Play as black', action='store_true')
parser.add_argument('-g', '--graphics', help='Display a graphic of the game', action='store_true')
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

def getRandomMove():
    return choice(list(board.legal_moves))

def getEngineMove():
    if args.difficulty == 0:
        return getRandomMove()
    move = getMove(board, args.difficulty)
    if not move:
        return getRandomMove()
    return move

def display_board(window):
    if args.graphics:
        window.load_html(chess.svg.board(board))
    else:
        print("\n" +  str(board) +  "\n")


def game_loop(window):
    if args.graphics:
        window.resize(420, 420)
    display_board(window)
    while not board.is_game_over():
        move = getPlayerMove()
        board.push(move)
        display_board(window)
        move = getEngineMove()
        if not move: break
        board.push(move)
        display_board(window)
        
    if board.is_stalemate():
        print("Stalemate.")
    else:
        if board.is_checkmate():
            print("Checkmate!")
        if board.turn == chess.BLACK:
            print("White wins.")
        else:
            print("Black wins.")


if args.graphics:
    window = webview.create_window('Chess')
    window.on_top = True
    webview.start(game_loop, window)
else:
    game_loop(None)