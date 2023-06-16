class Board():
    """
    Board class for the game of Tic-Tac-Toe.
    Default board size is 3x3.
    Board data:
        1=white(O), -1=black(X), 0=empty
        First dimension is column, second is row:
        pieces[0][0] is the top-left square,
        pieces[2][0] is the bottom-left square.
    Squares are stored and manipulated as (x, y) tuples.

    Author: Evgeny Tyurin, github.com/evg-tyurin
    Date: Jan 5, 2018.
    Based on the board for the game of Othello by Eric P. Nichols.
    """

    __directions = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]

    def __init__(self, n=3):
        """
        Set up initial board configuration.

        Args:
            n (int): The size of the board (default is 3x3).
        """
        self.n = n
        self.pieces = [[0] * self.n for _ in range(self.n)]

    def __getitem__(self, index):
        """
        Allows indexing the board using the [][], syntax.

        Args:
            index: The index for accessing the board.

        Returns:
            list: The row of the board corresponding to the index.
        """
        return self.pieces[index]

    def get_legal_moves(self, color):
        """
        Returns all the legal moves for the given color.

        Args:
            color (int): The color of the player (1 for white, -1 for black).

        Returns:
            list: A list of legal move coordinates as (x, y) tuples.
        """
        moves = []
        for y in range(self.n):
            for x in range(self.n):
                if self[x][y] == 0:
                    moves.append((x, y))
        return moves

    def has_legal_moves(self):
        """
        Checks if there are any legal moves left on the board.

        Returns:
            bool: True if there are legal moves, False otherwise.
        """
        for y in range(self.n):
            for x in range(self.n):
                if self[x][y] == 0:
                    return True
        return False

    def is_win(self, color):
        """
        Checks whether the given player has won the game by forming a triplet in any direction.

        Args:
            color (int): The color of the player (1 for white, -1 for black).

        Returns:
            bool: True if the player has won, False otherwise.
        """
        win = self.n

        # Check y-strips
        for y in range(self.n):
            count = 0
            for x in range(self.n):
                if self[x][y] == color:
                    count += 1
            if count == win:
                return True

        # Check x-strips
        for x in range(self.n):
            count = 0
            for y in range(self.n):
                if self[x][y] == color:
                    count += 1
            if count == win:
                return True

        # Check two diagonal strips
        count = 0
        for d in range(self.n):
            if self[d][d] == color:
                count += 1
        if count == win:
            return True

        count = 0
        for d in range(self.n):
            if self[d][self.n - d - 1] == color:
                count += 1
        if count == win:
            return True

        return False

    def execute_move(self, move, color):
        """
        Performs the given move on the board.

        Args:
            move (tuple): The move to execute as an (x, y) tuple.
            color (int): The color of the player (1 for white, -1 for black).
        """
        (x, y) = move
        assert self[x][y] == 0
        self[x][y] = color
