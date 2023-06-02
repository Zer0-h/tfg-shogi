from __future__ import print_function
import sys
sys.path.append('..')
from Game import Game
from .TicTacToeLogic import Board
import numpy as np

class TicTacToeGame(Game):
    """
    Game class implementation for the game of Tic-Tac-Toe.
    Based on the OthelloGame, then getGameEnded() was adapted to new rules.

    Author: Evgeny Tyurin, github.com/evg-tyurin
    Date: Jan 5, 2018.
    Based on the OthelloGame by Surag Nair.
    """

    def __init__(self, n=3):
        self.n = n

    def getInitBoard(self):
        """
        Returns the initial board configuration.

        Returns:
            numpy.array: The initial board state (numpy array).
        """
        b = Board(self.n)
        return np.array(b.pieces)

    def getBoardSize(self):
        """
        Returns the size of the game board.

        Returns:
            tuple: A tuple representing the size of the game board (n, n).
        """
        return (self.n, self.n)

    def getActionSize(self):
        """
        Returns the number of possible actions in the game.

        Returns:
            int: The number of actions.
        """
        return self.n * self.n + 1

    def getNextState(self, board, player, action):
        """
        Returns the next state (board, player) after applying the given action on the current board.

        Args:
            board (numpy.array): The current board state.
            player (int): The player making the move (1 for white, -1 for black).
            action (int): The action to be applied.

        Returns:
            tuple: A tuple representing the next state (next_board, next_player).
        """
        if action == self.n * self.n:
            return (board, -player)
        b = Board(self.n)
        b.pieces = np.copy(board)
        move = (int(action / self.n), action % self.n)
        b.execute_move(move, player)
        return (b.pieces, -player)

    def getValidMoves(self, board, player):
        """
        Returns a binary vector indicating the valid moves for the given player on the current board.

        Args:
            board (numpy.array): The current board state.
            player (int): The player for whom to check valid moves (1 for white, -1 for black).

        Returns:
            numpy.array: A binary vector representing the valid moves.
        """
        valids = [0] * self.getActionSize()
        b = Board(self.n)
        b.pieces = np.copy(board)
        legalMoves = b.get_legal_moves(player)
        if len(legalMoves) == 0:
            valids[-1] = 1
            return np.array(valids)
        for x, y in legalMoves:
            valids[self.n * x + y] = 1
        return np.array(valids)

    def getGameEnded(self, board, player):
        """
        Returns the game result for the given player on the current board.

        Args:
            board (numpy.array): The current board state.
            player (int): The player for whom to check the game result (1 for white, -1 for black).

        Returns:
            float: 1 if the player won, -1 if the player lost, or 0 if the game is not ended.
        """
        b = Board(self.n)
        b.pieces = np.copy(board)

        if b.is_win(player):
            return 1
        if b.is_win(-player):
            return -1
        if b.has_legal_moves():
            return 0
        return 1e-4

    def getCanonicalForm(self, board, player):
        """
        Returns the canonical form of the board with respect to the player.

        Args:
            board (numpy.array): The current board state.
            player (int): The player for whom to calculate the canonical form (1 for white, -1 for black).

        Returns:
            numpy.array: The canonical form of the board.
        """
        return player * board

    def getSymmetries(self, board, pi):
        """
        Returns the symmetries of the board and policy vector.

        Args:
            board (numpy.array): The current board state.
            pi (list): The policy vector.

        Returns:
            list: A list of (board, pi) pairs representing the symmetries of the board and policy vector.
        """
        assert len(pi) == self.n ** 2 + 1  # 1 for pass
        pi_board = np.reshape(pi[:-1], (self.n, self.n))
        symmetries = []

        for i in range(1, 5):
            for j in [True, False]:
                newB = np.rot90(board, i)
                newPi = np.rot90(pi_board, i)
                if j:
                    newB = np.fliplr(newB)
                    newPi = np.fliplr(newPi)
                symmetries.append((newB, list(newPi.ravel()) + [pi[-1]]))
        return symmetries

    def stringRepresentation(self, board):
        """
        Returns a string representation of the board.

        Args:
            board (numpy.array): The current board state.

        Returns:
            str: A string representation of the board.
        """
        return board.tostring()

    @staticmethod
    def display(board):
        """
        Displays the current board state.

        Args:
            board (numpy.array): The current board state.
        """
        n = board.shape[0]

        print("   ", end="")
        for y in range(n):
            print(y, "", end="")
        print("")
        print("  ", end="")
        for _ in range(n):
            print("-", end="-")
        print("--")
        for y in range(n):
            print(y, "|", end="")  # print the row #
            for x in range(n):
                piece = board[y][x]  # get the piece to print
                if piece == -1:
                    print("X ", end="")
                elif piece == 1:
                    print("O ", end="")
                else:
                    if x == n:
                        print("-", end="")
                    else:
                        print("- ", end="")
            print("|")

        print("  ", end="")
        for _ in range(n):
            print("-", end="-")
        print("--")
