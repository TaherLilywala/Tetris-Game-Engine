"""
Made by:
GNU SPOT
Group 3
"""
from game import Game
from lexer import GameLexer
from parser import GameParser
from translator import GameTranslator
import sys

if __name__ == '__main__':       
    print('Tetris > Hi, I am the Tetri-game Engine.')
    lexer = GameLexer()
    parser = GameParser()
    game = Game()

    while True:
        try:
            print('Tetris > Please type a command.')
            print('------ > ', end = "")
            text = input()
        except EOFError:
            print("")
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            GameTranslator(tree, game)