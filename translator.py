"""
Made by:
GNU SPOT
Group 3
"""
import sys

class GameTranslator:
    def __init__(self, tree, game):
        self.game = game
        result = self.walkTree(tree)

    def speed(self, speed):
        self.game.setSpeed(speed)

    def sensitivity(self, sens):
        self.game.setSensitivty(sens) 

    def nextq(self, check):
        if check[1] == 'ON':
            self.game.setDisplayPiece(True) 
        else:
            self.game.setDisplayPiece(False)
        
    def startGame(self):
        self.game.begin()

    def walkTree(self, node):
        if node is None:
            return None

        if node == 'START':
            self.startGame()
            return None
        
        if node[0] == 'command':
            return self.walkTree(node[1])

        if node[0] == 'speed':
            self.speed(node[1])
            return None   

        if node[0] == 'sensitivity':
            self.sensitivity(node[1])   
            return None

        if node[0] == 'nextq':
            self.nextq(node[1])
            return None
