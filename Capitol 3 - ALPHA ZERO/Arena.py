import logging
from tqdm import tqdm

log = logging.getLogger(__name__)

class Arena():
    """
    An Arena class where any 2 agents can be pit against each other.
    """

    def __init__(self, player1, player2, game, display=None):
        """
        Initializes the Arena.

        Args:
            player1: Function representing player 1. Takes the board as input and returns an action.
            player2: Function representing player 2. Takes the board as input and returns an action.
            game: Game object representing the game being played.
            display: Function that takes the board as input and displays it (optional).
        """
        self.player1 = player1
        self.player2 = player2
        self.game = game
        self.display = display

    def playGame(self, verbose=False):
        """
        Executes one episode of a game.

        Returns:
            The winner: 1 if player1 wins, -1 if player2 wins.
            or
            The draw result returned by the game (neither 1, -1, nor 0).
        """
        players = [self.player2, None, self.player1]
        curPlayer = 1
        board = self.game.getInitBoard()
        it = 0
        while self.game.getGameEnded(board, curPlayer) == 0:
            it += 1
            if verbose:
                assert self.display
                print("Turn", str(it), "Player", str(curPlayer))
                self.display(board)
            action = players[curPlayer + 1](self.game.getCanonicalForm(board, curPlayer))

            valids = self.game.getValidMoves(self.game.getCanonicalForm(board, curPlayer), 1)

            if valids[action] == 0:
                log.error(f'Action {action} is not valid!')
                log.debug(f'valids = {valids}')
                assert valids[action] > 0
            board, curPlayer = self.game.getNextState(board, curPlayer, action)

        if verbose:
            assert self.display
            print("Game over: Turn", str(it), "Result", str(self.game.getGameEnded(board, 1)))
            self.display(board)

        return curPlayer * self.game.getGameEnded(board, curPlayer)

    def playGames(self, num, verbose=False):
        """
        Plays a specified number of games, where player1 starts num/2 games and player2 starts num/2 games.

        Returns:
            oneWon: Number of games won by player1.
            twoWon: Number of games won by player2.
            draws: Number of games resulting in a draw.
        """

        num = int(num / 2)
        oneWon = 0
        twoWon = 0
        draws = 0

        for _ in tqdm(range(num), desc="Arena.playGames (1)"):
            gameResult = self.playGame(verbose=verbose)
            if gameResult == 1:
                oneWon += 1
            elif gameResult == -1:
                twoWon += 1
            else:
                draws += 1

        self.player1, self.player2 = self.player2, self.player1

        for _ in tqdm(range(num), desc="Arena.playGames (2)"):
            gameResult = self.playGame(verbose=verbose)
            if gameResult == -1:
                oneWon += 1
            elif gameResult == 1:
                twoWon += 1
            else:
                draws += 1

        return oneWon, twoWon, draws
