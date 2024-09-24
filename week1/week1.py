"""
Tic Tac Toe Player
"""

# import math
import copy

X = "X"
O = "O"
EMPTY = None


# def initial_state():
#     """
#     Returns starting state of the board.
#     """
#     return [[EMPTY, EMPTY, EMPTY],
#             [EMPTY, EMPTY, EMPTY],
#             [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    nx = sum([i.count("X") for i in board])
    no = sum([i.count("O") for i in board])
    if nx > no:
        return "O"
    else:
        return "X"

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ls = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                ls.add((i, j))
    return ls
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    ls = actions(board)
    if action not in ls:
        raise Exception("Invalid action")
    boardcopy = copy.deepcopy(board)
    if player(board) == "X":
        boardcopy[action[0]][action[1]] = "X"
    elif player(board) == "O":
        boardcopy[action[0]][action[1]] = "O"

    return boardcopy

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    diagonal1 = set([board[i][i] for i in range(3)])
    diagonal2 = set([board[i][2 - i] for i in range(3)])
    rows = [set([board[i][0], board[i][1], board[i][2]]) for i in range(3)]
    columns = [set([board[0][i], board[1][i], board[2][i]]) for i in range(3)]
    if diagonal1 == {'X'} or diagonal2 == {'X'} or {"X"} in rows or {'X'} in columns:
        return 'X'
    elif diagonal1 == {'O'} or diagonal2 == {'O'} or {"O"} in rows or {'O'} in columns:
        return "O"
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    def max_value(board):
        if terminal(board):
            return (utility(board), None)

        value = float('-inf')
        action = None
        for move in actions(board):
            # v = max(v, min_value(result(board, action)))
            v, act = min_value(result(board, move))
            if v > value:
                value = v
                action = move
                if v == 1:
                    return (v, action)

        return (v, action)

    def min_value(board):
        if terminal(board):
            return utility(board), None

        value = float('inf')
        action = None
        for move in actions(board):
            # v = max(v, min_value(result(board, action)))
            v, act = max_value(result(board, move))
            if v < value:
                value = v
                action = move
                if value == -1:
                    return (value, action)

        return (value, action)

    if player(board) == "X":
        return max_value(board)[1]
    else:
        return min_value(board)[1]

    raise NotImplementedError

def display(board):
    for i in range(3):
        print(f"{board[i][0]}\t{board[i][1]}\t{board[i][2]}", end="\n\n")
        

def main():
    board = [[None for _ in range(3)] for _ in range(3)]
    while not terminal(board):
        current_player = player(board)
        if current_player == O:
            move = int(input("Enter possible cell to enter in (0 - 8): "))
            action = (move//3, move%3)
            if action in actions(board):
                board[action[0]][action[1]] = O
            else:
                print("Enter a valid move")
                move = int(input("Enter possible cell to enter in (0 - 8): "))
                action = [move//3, move%3]
        else:
            move = minimax(board)
            board[move[0]][move[1]] = X
        
        display(board)
        if winner(board) is not None:
            print(f"{winner(board)} wins!")

main()
