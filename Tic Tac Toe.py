import tictactoe.tictactoe.tictactoe as ttt

tablero = [[ttt.EMPTY, ttt.O, ttt.EMPTY],
            [ttt.X, ttt.EMPTY, ttt.EMPTY],
            [ttt.EMPTY, ttt.O, ttt.EMPTY]]
entrada = tablero[0][2]

print(ttt.winner(tablero))
