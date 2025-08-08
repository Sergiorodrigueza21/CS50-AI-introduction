import tictactoe.tictactoe.tictactoe as ttt

tablero = [[ttt.EMPTY, ttt.EMPTY, ttt.X],
            [ttt.O, ttt.X, ttt.EMPTY],
            [ttt.O, ttt.O, ttt.O]]

print(ttt.utility(tablero))
