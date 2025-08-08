"""
Tic Tac Toe Player
"""

import math
import copy
from types import new_class

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
        if check_values(values)[0]:
            win = check_values(values)[1]
            return win
    values = []

    #check winner in a column
    for col in range(len(board)):
        for row in range(len(board)):
            values.append(check_box(board[row][col]))
        if check_values(values)[0]:
            win = check_values(values)[1]
            return win
        values = []
    #check winner in first diagonal
    # for col in range(len(board)):
    #     for row in range(len(board)):
    #         if row == col:
    #             values.append(check_box(board[row][col]))
    # return win if (win:= check_values(values)) else None

    values = []
    second_values = []
    #check winner in second diagonal
    for pos in range(len(board)):
        second_values.append(check_box(board[pos][pos]))
        values.append(check_box(board[pos][len(board)-1-pos]))
    if check_values(values)[0]:
        win = check_values(values)[1]
        return win
    if check_values(second_values)[0]:
        win = check_values(second_values)[1]
        return win
    return False


def terminal(board):
    if not winner(board):
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == EMPTY:
                    return False
    else: return True

def utility(board):
    state = winner(board)
    if state == X:
        return 1
    elif state == O:
        return -1
    else:
        return 0


# def minimax(board):
#     """
#     Returns the optimal action for the current player on the board.
#     """
#     raise NotImplementedError

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
            # print(f"ganador")
            if any(values):
                return [True,X]
            else:
                return [True,O]
    return [False, None]

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        print(f"ingreso max: {action}")
        print(f"Max: {aux}")
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move
    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        print(f"ingreso min: {action}")
        print(f"Min: {aux}")
        if aux < v:                 #Return the min value found
            print('min success')
            v = aux
            move = action
            if v == -1:
                return v, move
    return v, move
