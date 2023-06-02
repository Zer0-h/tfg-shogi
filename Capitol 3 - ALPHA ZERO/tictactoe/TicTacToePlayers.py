import numpy as np

class RandomPlayer():
    def __init__(self, game):
        """
        Random player for the game of Tic-Tac-Toe.

        Args:
            game: The Tic-Tac-Toe game instance.
        """
        self.game = game

    def play(self, board):
        """
        Selects a random valid move for the given board.

        Args:
            board: The current board state.

        Returns:
            int: The selected action index.
        """
        valids = self.game.getValidMoves(board, 1)
        a = np.random.choice(np.where(valids == 1)[0])
        return a


class HumanTicTacToePlayer():
    def __init__(self, game):
        """
        Human-interacting player for the game of Tic-Tac-Toe.

        Args:
            game: The Tic-Tac-Toe game instance.
        """
        self.game = game

    def play(self, board):
        """
        Allows a human player to input their move for the given board.

        Args:
            board: The current board state.

        Returns:
            int: The selected action index.
        """
        valid = self.game.getValidMoves(board, 1)
        for i in range(len(valid)):
            if valid[i]:
                print(int(i / self.game.n), int(i % self.game.n))
        while True:
            a = input("Enter your move: ")
            x, y = [int(coord) for coord in a.split(' ')]
            a = self.game.n * x + y if x != -1 else self.game.n ** 2
            if valid[a]:
                break
            else:
                print('Invalid move!')
        return a
