"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    xturns = 0
    oturns = 0

    for row in board:
        for position in row:
            if position == X:
                xturns += 1
            if position == O:
                oturns += 1
    if xturns > oturns:
        return O
    else:
        return X

def actions(board):
    posible_moves = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                position = (row,col)
                posible_moves.add(position)

    return posible_moves
def result(board, action):
    if action not in actions(board):
        raise Exception("Not valid action")
    row,col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)

    return board_copy

def winner(board):
    win = False
    #check winner in a row
    for i,row in enumerate(board):
        values= [check_box(v) for v in row]
        if "-" not in values:
            if all(values) or all(not x for x in values):
                win = True
                print(f"ganador horizontal {i}")
    values = []
    #check winner in a column
    for col in range(len(board)):
        for row in range(len(board)):
            values.append(check_box(board[row][col]))
        if "-" not in values:
            if all(values) or all(not x for x in values):
                win = True
                print(f"ganador vertical {col}" )
        values = []
    #check winner in first diagonal
    for col in range(len(board)):
        for row in range(len(board)):
            if row == col:
                values.append(check_box(board[row][col]))
    if "-" not in values:
        if all(values) or all(not x for x in values):
            win = True
            print(f"ganador diagonal" )
    values = []
    #check winner in second diagonal
    for pos in range(len(board)):
        values.append(check_box(board[pos][len(board)-1-pos]))
    if "-" not in values:
        if all(values) or all(not x for x in values):
            win = True
            print(f"ganador diagonal" )
    values = []


    return win


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

def check_box(data: str):
    if data == X:
        return True
    elif data == O:
        return False
    else:
        return "-"

def check_values(values):
    if "-" not in values:
        if all(values) or all(not x for x in values):
            print(f"ganador ganador" )
            values = []