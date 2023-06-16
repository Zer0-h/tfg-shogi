from .TicTacToeNNet import TicTacToeNNet as onnet
from NeuralNet import NeuralNet
from utils import *
import os
import time
import numpy as np
import sys
sys.path.append('..')

args = DotDict({
    'lr': 0.001,
    'dropout': 0.3,
    'epochs': 10,
    'batch_size': 64,
    'cuda': False,
    'num_channels': 512,
})

class NNetWrapper(NeuralNet):
    """
    Neural network wrapper class for Tic-Tac-Toe.

    Author: Evgeny Tyurin, github.com/evg-tyurin
    Date: Jan 5, 2018.
    Based on (copy-pasted from) the NNet by SourKream and Surag Nair.
    """

    def __init__(self, game):
        """
        Initializes the NNetWrapper.

        Args:
            game (Game): The game object.
        """
        self.nnet = onnet(game, args)
        self.board_x, self.board_y = game.getBoardSize()
        self.action_size = game.getActionSize()

    def train(self, examples):
        """
        Trains the neural network model using provided examples.

        Args:
            examples (list): List of examples, each example is of form (board, pi, v).
        """
        input_boards, target_pis, target_vs = list(zip(*examples))
        input_boards = np.asarray(input_boards)
        target_pis = np.asarray(target_pis)
        target_vs = np.asarray(target_vs)
        self.nnet.model.fit(x=input_boards, y=[target_pis, target_vs], batch_size=args.batch_size, epochs=args.epochs)

    def predict(self, board):
        """
        Performs a prediction using the neural network model.

        Args:
            board (np.array): The board state.

        Returns:
            tuple: A tuple containing the predicted policy and value.
        """
        # Timing
        start = time.time()

        # Preparing input
        board = board[np.newaxis, :, :]

        # Run prediction
        pi, v = self.nnet.model.predict(board)

        #print('PREDICTION TIME TAKEN: {0:.3f}'.format(time.time() - start))
        return pi[0], v[0]

    def save_checkpoint(self, folder='checkpoint', filename='checkpoint.pth.tar'):
        """
        Saves the model weights as a checkpoint.

        Args:
            folder (str): Folder path to save the checkpoint.
            filename (str): Filename of the checkpoint.
        """
        filepath = os.path.join(folder, filename)
        if not os.path.exists(folder):
            print("Checkpoint Directory does not exist! Making directory {}".format(folder))
            os.mkdir(folder)
        else:
            print("Checkpoint Directory exists!")
        self.nnet.model.save_weights(filepath)

    def load_checkpoint(self, folder='checkpoint', filename='checkpoint.pth.tar'):
        """
        Loads the model weights from a checkpoint.

        Args:
            folder (str): Folder path of the checkpoint.
            filename (str): Filename of the checkpoint.

        Raises:
            IOError: If the checkpoint file does not exist.
        """
        filepath = os.path.join(folder, filename)
        if not os.path.exists(filepath):
            raise IOError()
        self.nnet.model.load_weights(filepath)
