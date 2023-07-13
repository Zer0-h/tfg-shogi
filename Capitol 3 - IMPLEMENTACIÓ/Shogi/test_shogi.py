""""

    This is a Regression Test Suite to automatically test all shogi_model and its ML framework. Each test
    plays two quick games using an untrained neural network (randomly initialized) against a random player.

"""

import unittest

import numpy as np

import Arena
from MCTS import MCTS
from shogi_model.ShogiGame import ShogiGame
from shogi_model.ShogiPlayers import RandomPlayer
from shogi_model.pytorch.NNet import NNetWrapper as ShogiPytorchNNet
from utils import *


class TestChess(unittest.TestCase):

    @staticmethod
    def execute_game_test(game, neural_net):
        rp = RandomPlayer(game).play

        args = dotdict({'numMCTSSims': 25, 'cpuct': 1.0})
        mcts = MCTS(game, neural_net(game), args)
        n1p = lambda x: np.argmax(mcts.getActionProb(x, temp=0))

        arena = Arena.Arena(n1p, rp, game)
        print(arena.playGames(2, verbose=False))

    def test_chess_pytorch(self):
        self.execute_game_test(ShogiGame(), ShogiPytorchNNet)


if __name__ == '__main__':
    unittest.main()
