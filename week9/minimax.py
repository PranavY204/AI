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
