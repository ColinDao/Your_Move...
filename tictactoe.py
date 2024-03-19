"""
Tic Tac Toe Player
"""

import copy

# Players
X = "X"
O = "O"

# Starting cell for board
EMPTY = None

# Infinity bounds
POS_INF = float('inf')
NEG_INF = float('-inf')


def initial_state():
    """
    Returns starting state of the board.
    """
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    spaces = 0
    for i in range(3):

        # Count number of empty cells
        spaces += board[i].count(EMPTY)

    # Since X moves first, return X if there are an odd amount of empty cells
    return X if spaces % 2 == 1 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    # Loop through the entire board
    for i in range(3):
        for j in range(3):

            # Empty spot is an available move
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Deconstruct row and column coordinates
    x, y = action

    # Invalid move
    if board[x][y] != EMPTY:
        raise Exception("Not empty space")
    
    # Make a copy state of the board with the new move
    copy_board = copy.deepcopy(board)
    copy_board[x][y] = player(board)
    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if winner_helper(board, X):
        return X
    elif winner_helper(board, O):
        return O
    return None


def winner_helper(board, player):
    """
    Find winner if there is one.
    """

    # Diagonal win
    if board[1][1] == player and (
        (board[0][0] == player and board[2][2] == player) or 
        (board[0][2] == player and board[2][0] == player)
    ):
        return True
    
    # Horizontal and vertical wins
    for i in range(3):

        # Horizontal win
        if board[i].count(player) == 3:
            return True
        
        # Vertical win
        count = 0
        for j in range(3):
            if board[j][i] == player:
                count += 1
        if count == 3:
            return True
        
    # No win
    return False


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) or len(actions(board)) == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # Get player who has won
    winning_player = winner(board)

    if winning_player == X:
        return 1
    elif winning_player == O:
        return -1
    
    # No winner
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    _, move = minimax_helper(board, None, NEG_INF, POS_INF, player(board))
    return move


def minimax_helper(board, move, alpha, beta, p):
    """
    Returns the evaluation and optimal action for the current player on the board.
    """

    # There's a winner
    if terminal(board):
        return utility(board), move

    # Best current outcome and target depending on the player
    best_value = NEG_INF if p == X else POS_INF
    target = 1 if p == X else -1

    # Go through all the possible actions to find the most optimal one
    for action in actions(board):

        # New board after this action
        new_board = result(board, action)

        # Get the evaluation of this move based on how the other player responds
        current_value, _ = minimax_helper(new_board, action, alpha, beta, O if p == X else X)

        # Update best outcome and move if the new evaluation is better for the current player
        if (p == X and current_value > best_value) or (p == O and current_value < best_value):
            best_value = current_value
            move = action

            # Update limits to include the best value
            if p == X:
                alpha = max(alpha, best_value)
            else:
                beta = min(beta, best_value)

            # Exit if opponent has stronger move than current best move or 
            # if current player is in a winning position
            if beta <= alpha or best_value == target:
                break

    # Return the best evaluation and move
    return best_value, move