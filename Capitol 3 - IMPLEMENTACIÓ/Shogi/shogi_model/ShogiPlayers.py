import random

import numpy as np
import shogi

from .ShogiGame import who, mirror_board, mirror_move, from_move


class RandomPlayer():
    def __init__(self, game):
        self.game = game

    def play(self, board):
        valids = self.game.getValidMoves(board, who(board.turn))
        moves = np.argwhere(valids == 1)
        return random.choice(moves)[0]


def move_from_usi(board, usi):
    try:
        move = shogi.Move.from_usi(usi)
    except ValueError:
        print("Expected an USI move")
    if move not in board.legal_moves:
        print("Expected a legal move")
        return None
    return move


class HumanShogiPlayer():
    def __init__(self, game):
        pass

    def play(self, board):
        mboard = board
        if board.turn == shogi.BLACK:
            mboard = mirror_board(board)
        print('Valid Moves', end=':')
        for move in mboard.legal_moves:
            print(move.usi(), end=',')
        print()
        human_move = input()
        move = move_from_usi(mboard, human_move.strip())
        if move is None:
            print('Please try again, e.g., %s' % random.choice(list(mboard.legal_moves)).uci())
            self.play(board)
        if board.turn == shogi.BLACK:
            move = mirror_move(move)
        return from_move(move)


class GreedyShogiPlayer():
    def __init__(self, game):
        self.game = game

    def play(self, board):
        valids = self.game.getValidMoves(board, 1)
        candidates = []
        for a in range(self.game.getActionSize()):
            if valids[a] == 0:
                continue
            nextBoard, _ = self.game.getNextState(board, 1, a)
            score = self.game.getScore(nextBoard, 1)
            candidates += [(-score, a)]
        candidates.sort()
        return candidates[0][1]

# TODO: Check engines to run against
