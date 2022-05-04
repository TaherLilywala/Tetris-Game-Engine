# Tetris Game Engine

To test the lexer you can do the following,
```
python3 lexer.py
```

This will allow you to input test statements which will be scanned by our lexer. A few examples are shown below.
```
Tetris > SPEED 5
Tetris > SENSITIVITY 6
Tetris > NEXTQ ON
Tetris > NEXTQ OFF
Tetris > MOVEDEF LEFT A
Tetris > MOVEDEF RIGHT D
```
Use Ctrl + C to exit the program.

NOTE: SLY requires the use of Python 3.6 or greater.  Older versions of Python are not supported.

# Additional Features Added

Set Speed to 5: (Default 0)
```
Tetris > SPEED 5
```
Set Sensitivity to 6: (Default 4)
```
Tetris > SENSITIVITY 6
```

Set if Next block in queue is available or now
```
Tetris > NEXTQ ON
Tetris > NEXTQ OFF
```

Change controls: Replace LEFT with A:
```
Tetris > MOVEDEF LEFT A
```
More examples:
```
Tetris > MOVEDEF RIGHT D
```
