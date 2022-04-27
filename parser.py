"""
Made by:
GNU SPOT
Group 3
"""
import sys

from zmq import NULL
from sly import Parser
from lexer import GameLexer

class GameParser(Parser):
    tokens = GameLexer.tokens

    def error(self, p):
        """
        Syntax error handler.
        Checks for syntax errors i.e. incorrect token and prints location and incorrect token.
        """
        if not p:
            print("Tetris > Syntax Error Encountered.")
            return NULL
        
        print(f"Tetris > Line {p.lineno}.{p.index+1}: Syntax Error: \"{p.value}\"")

    """ main commands """
    @_('move')
    def command(self, p):
        return ('command', p.move)
    
    @_('mode')
    def command(self, p):
        return ('command', p.mode)

    @_('rotate')
    def command(self, p):
        return ('command', p.rotate)  
    
    @_('block')
    def command(self, p):
        return ('command', p.block)
    
    @_('speed')
    def command(self, p):
        return ('command', p.speed)
    
    @_('sensitivity')
    def command(self, p):
        return ('command', p.sensitivity)
    
    @_('nextq')
    def command(self, p):
        return ('command', p.nextq)

    @_('START')
    def command(self, p):
        return ('command', p.START)

    @_('PAUSE')
    def command(self, p):
        return ('command', p.PAUSE)

    @_('RESTART')
    def command(self, p):
        return ('command', p.RESTART)
    
    @_('droplr')
    def command(self, p):
        return ('command', p.droplr)

    @_('DROP')
    def command(self, p):
        return ('command', p.DROP)

    """ H.O. Grammar """   
    @_('MOVE move_param')
    def move(self, p):
        return ('move', p.move_param)

    @_('MODE mode_param')
    def mode(self, p):
        return ('mode', p.mode_param)

    @_('ROTATE rotate_param')
    def rotate(self, p):
        return ('rotate', p.rotate_param)
    
    @_('BLOCK block_param')
    def block(self, p):
        return ('block', p.block_param)

    @_('SPEED NUMBER')
    def speed(self, p):
        return ('speed', p[1])
    
    @_('SENSITIVITY NUMBER')
    def sensitivity(self, p):
        return ('sensitivity', p[1])
    
    @_('DROP move_param')
    def droplr(self, p):
        return ('droplr', p.move_param)

    @_('NEXTQ nextq_param')
    def nextq(self, p):
        return ('nextq', p.nextq_param)

    """ Parameters """
    @_('LEFT', 'RIGHT')
    def move_param(self, p):
        return ('move_param', p[0])

    @_('CL', 'ACL')
    def rotate_param(self, p):
        return ('rotate_param', p[0])

    @_('EASY', 'MED', 'HARD')
    def block_param(self, p):
        return ('block_param', p[0])

    @_('CB', 'CC')
    def mode_param(self, p):
        return ('mode_param', p[0])

    @_('ON', 'OFF')
    def nextq_param(self, p):
        return ('nextq_param', p[0])

if __name__ == '__main__':
    lexer = GameLexer()
    parser = GameParser()
    while True:
        try:
            text = input('Tetris > ')
            result = parser.parse(lexer.tokenize(text))
            print(f'Parser > {result}')
        except EOFError:
            break