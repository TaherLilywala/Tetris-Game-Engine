"""
Made by:
GNU SPOT
Group 3
"""
from sly import Lexer

class GameLexer(Lexer):
    """
    Set of tokens we are exporting to the Parser
    """
    tokens = {START, MOVE, LEFT, RIGHT, ROTATE, CL, ACL, PAUSE, RESTART, DROP,
                BLOCK, EASY, MED, HARD, SPEED, MODE, CB, CC, NEXTQ, ON, OFF,
                SENSITIVITY, NUMBER, SCOREALGO, CUSTOM}

    # Ignore Spaces
    ignore = ' \t'
        
    START = r'START'
    MOVE = r'MOVE'
    LEFT = r'LEFT'
    RIGHT = r'RIGHT'
    ROTATE = r'ROTATE'
    CL = r'CL'
    ACL = r'ACL'
    PAUSE = r'PAUSE'
    RESTART = r'RESTART'
    DROP = r'DROP'
    BLOCK = r'BLOCK'
    EASY = r'EASY'
    MED = r'MED'
    HARD = r'HARD'
    SPEED = r'SPEED'
    MODE = r'MODE'
    CB = r'CB'
    CC = r'CC'
    NEXTQ = r'NEXTQ'
    ON = r'ON'
    OFF = r'OFF'
    SENSITIVITY = r'SENSITIVITY'
    SCOREALGO = r'SCOREALGO'
    CUSTOM = r'CUSTOM'

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')

    def error(self, t):
        print(f"Tetris > Line {t.lineno}.{t.index+1}: Illegal character '{t.value[0]}'")
        self.index += 1

# Main used for testing purposes
if __name__ == '__main__':
    lexer = GameLexer()
    env = {}
    while True:
        try:
            text = input('Tetris > ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)