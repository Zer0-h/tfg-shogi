from __future__ import print_function

import sys

sys.path.append('..')
from Game import Game
import numpy as np
import shogi
import typing

SHOGI_BOARD_SQUARES = len(shogi.SQUARES)
TOTAL_PIECES = len(shogi.PIECE_TYPES_WITHOUT_KING) + 1


def piece_map(board):
    result = {}
    for square in range(81 - 1, -1, -1):
        piece = board.piece_at(square)
        if piece is not None:
            result[square] = typing.cast(shogi.Piece, piece)
    return result


def to_np(board):
    a = [0] * (SHOGI_BOARD_SQUARES * TOTAL_PIECES)
    for sq, pc in piece_map(board).items():
        if pc is not None:
            a[sq * TOTAL_PIECES + pc.piece_type - 1] = 1 if pc.color == shogi.WHITE else -1
    return np.array(a)


def from_move(move):
    return move.from_square * SHOGI_BOARD_SQUARES + move.to_square


def to_move(action):
    to_sq = action % SHOGI_BOARD_SQUARES
    from_sq = int(action / SHOGI_BOARD_SQUARES)
    return shogi.Move(from_sq, to_sq)


def who(turn):
    return 1 if turn == shogi.WHITE else -1


def square_mirror(square):
    return SHOGI_BOARD_SQUARES - square - 1


def mirror_move(move):
    return shogi.Move(square_mirror(move.from_square), square_mirror(move.to_square))


def change_piece_color(color):
    return 0 if color == 1 else 1


def mirror_board(board):
    new_board = shogi.Board()
    new_board.reset()

    # Mirror pieces in board
    for i in range(SHOGI_BOARD_SQUARES):
        piece = board.piece_at(i)
        new_board_square = SHOGI_BOARD_SQUARES - i - 1
        if piece is None:
            new_board.remove_piece_at(new_board_square)
        else:
            piece.color = change_piece_color(piece.color)
            new_board.set_piece_at(new_board_square, piece)

    # Mirror pieces in hand
    for piece_type in range(shogi.PROM_PAWN):
        if piece_type < shogi.PROM_PAWN:
            if board.has_piece_in_hand(piece_type, shogi.BLACK):
                piece_count = board.pieces_in_hand[shogi.BLACK][piece_type]
                new_board.add_piece_into_hand(piece_type, shogi.WHITE, piece_count)
            if board.has_piece_in_hand(piece_type, shogi.WHITE):
                piece_count = board.pieces_in_hand[shogi.WHITE][piece_type]
                new_board.add_piece_into_hand(piece_type, shogi.BLACK, piece_count)

    return new_board


class ShogiGame(Game):
    def __init__(self, n=9):
        self.n = n

    def getInitBoard(self):
        # return initial board
        return shogi.Board()
        # return np.array(b.pieces)

    def getBoardSize(self):
        # (n, n, pieces) tuple
        return self.n, self.n, TOTAL_PIECES

    def getActionSize(self):
        # We assume every piece can be moved
        # return len(board.legal_moves) ?
        return SHOGI_BOARD_SQUARES * SHOGI_BOARD_SQUARES
        # return self.n*self.n + 1

    def getNextState(self, board, player, action):
        # if player takes action on board, return next (board,player)
        # action must be a valid move
        assert (who(board.turn) == player)
        move = to_move(action)
        if board.turn == shogi.BLACK:
            # Assume that the move comes from the canonical board
            move = mirror_move(move)
        if move not in board:
            # It can be a piece promotion, which would have an extra letter (+) in USI format
            move = shogi.Move.from_usi(move.usi() + '+')
            if move not in board.legal_moves:
                assert False, "%s not in %s" % (str(move), str(list(board.legal_moves)))
        board = board.copy()
        board.push(move)
        return board, who(board.turn)

    def getValidMoves(self, board, player):
        # return a fixed size binary vector
        assert (who(board.turn) == player)
        acts = [0] * self.getActionSize()
        for move in board.get_legal_moves():
            acts[from_move(move)] = 1
        return np.array(acts)

    def getGameEnded(self, board, player):
        # return 0 if not ended, 1 if player 1 won, -1 if player 1 lost
        if not board.is_game_over():
            if board.is_stalemate() or board.is_fourfold_repetition():
                # draw, return very little value
                return 1e-4
            else:
                # The current turn will be the one of the losing player
                return -1 if who(board.turn) == player else 1
        return 0

    def getCanonicalForm(self, board, player):
        # return state if player==1, else return -state if player==-1
        assert (who(board.turn) == player)
        if board.turn == shogi.WHITE:
            return board
        else:
            return mirror_board(board)

    def getSymmetries(self, board, pi):
        # mirror, rotational
        return [(board, pi)]

    def stringRepresentation(self, board):
        return board.sfen()

    @staticmethod
    def display(board):
        print(board)
