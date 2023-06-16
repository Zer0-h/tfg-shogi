import numpy as np
from tictactoe.TicTacToeGame import TicTacToeGame
from tictactoe.TicTacToePlayers import *
from tictactoe.keras.NNet import NNetWrapper as NNet
from utils import dotdict
from MCTS import MCTS
import Arena

"""
Use this script to play Tic Tac Toe games between different agents.
"""

human_vs_cpu = True
game = TicTacToeGame()

# Define players
random_player = RandomPlayer(game).play
human_player = HumanTicTacToePlayer(game).play

# Load and configure neural network player
nnet = NNet(game)
nnet.load_checkpoint('./pretrained_models/tictactoe/keras/', 'best-25eps-25sim-10epch.pth.tar')
nnet_args = dotdict({'numMCTSSims': 50, 'cpuct': 1.0})
mcts = MCTS(game, nnet, nnet_args)
nnet_player = lambda x: np.argmax(mcts.getActionProb(x, temp=0))

if human_vs_cpu:
    player2 = human_player
else:
    nnet2 = NNet(game)
    nnet2.load_checkpoint('./pretrained_models/tictactoe/pytorch/', '8x8_100checkpoints_best.pth.tar')
    nnet2_args = dotdict({'numMCTSSims': 50, 'cpuct': 1.0})
    mcts2 = MCTS(game, nnet2, nnet2_args)
    nnet_player2 = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))
    player2 = nnet_player2

# Create an arena to play games
arena = Arena.Arena(nnet_player, player2, game, display=TicTacToeGame.display)

print(arena.playGames(2, verbose=True))
