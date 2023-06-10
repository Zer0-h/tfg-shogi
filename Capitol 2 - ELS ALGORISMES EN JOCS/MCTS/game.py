import numpy as np

def get_init_board():
    """Return an initial Connect Four board."""
    return np.zeros((6, 7))


def place_piece(board, player, action):
    """Place a piece on the board for the specified player at the given action."""
    board_copy = np.copy(board)
    row_index = sum(board_copy[:, action] == 0) - 1
    board_copy[row_index, action] = player
    return board_copy


def get_valid_moves(board):
    """Determine the valid moves that can be played on the board."""
    valid_moves = [0] * 7
    for column in range(7):
        if sum(board[:, column] == 0) > 0:
            valid_moves[column] = 1

    return valid_moves


def is_board_full(board):
    """Check if the board is full (no empty cells remaining)."""
    return sum(board.flatten() == 0) == 0


def is_win(board, player):
    """Check if the specified player has won the game."""
    for column in range(7):
        for row in range(3):
            if board[row, column] == board[row + 1, column] == board[row + 2, column] == board[row + 3, column] == player:
                return True

    for row in range(6):
        for column in range(4):
            if board[row, column] == board[row, column + 1] == board[row, column + 2] == board[row, column + 3] == player:
                return True

    for row in range(3):
        for column in range(4):
            if board[row, column] == board[row + 1, column + 1] == board[row + 2, column + 2] == board[row + 3, column + 3] == player:
                return True

    for row in range(5, 2, -1):
        for column in range(4):
            if board[row, column] == board[row - 1, column + 1] == board[row - 2, column + 2] == board[row - 3, column + 3] == player:
                return True

    return False
