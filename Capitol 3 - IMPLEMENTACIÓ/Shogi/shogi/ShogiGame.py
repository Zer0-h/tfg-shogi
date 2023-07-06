from __future__ import print_function
import sys
sys.path.append('..')
from Game import Game
from ShogiLogic import Board
import numpy as np
import shogi

SHOGI_BOARD_SQUARES = 81

def who(turn):
  return 1 if turn else -1

def to_move(action):
  to_sq = action % SHOGI_BOARD_SQUARES
  from_sq = int(action / SHOGI_BOARD_SQUARES)
  return shogi.Move(from_sq, to_sq)

def mirror_move(move):
  return shogi.Move(shogi.square_mirror(move.from_square), shogi.square(move.to_square))

class ShogiGame(Game):
    square_content = {
        -1: "X",
        +0: "-",
        +1: "O"
    }

    @staticmethod
    def getSquarePiece(piece):
        return ShogiGame.square_content[piece]

    def __init__(self, n=9):
        self.n = n

    def getInitBoard(self):
        # return initial board (numpy board)
        return shogi.Board()
        #b = Board(self.n)
        #return np.array(b.pieces)

    def getBoardSize(self):
        # (a,b) tuple
        return (self.n, self.n)

    def getActionSize(self):
        # return number of actions
        return SHOGI_BOARD_SQUARES * SHOGI_BOARD_SQUARES
        # return self.n*self.n + 1

    def getNextState(self, board, player, action):
        # if player takes action on board, return next (board,player)
        # action must be a valid move
        assert(who(board.turn) == player)
        move = to_move(action)
        if not board.turn:
            # Assume that the move comes from the canonical board
            move = mirror_move(move)
        if move not in board.legal_moves:
            # It can be a piece promotion, which would have an extra letter (+) in USI format
            move = shogi.Move.from_usi(move.usi()+'+')
            if move not in board.legal_moves:
                assert False, "%s not in %s" % (str(move), str(list(board.legal_moves)))
        board = board.copy()
        board.push(move)
        return (board, who(board.turn))

    def getValidMoves(self, board, player):
        # return a fixed size binary vector
        valids = [0]*self.getActionSize()
        b = Board(self.n)
        b.pieces = np.copy(board)
        legalMoves =  b.get_legal_moves(player)
        if len(legalMoves)==0:
            valids[-1]=1
            return np.array(valids)
        for x, y in legalMoves:
            valids[self.n*x+y]=1
        return np.array(valids)

    def getGameEnded(self, board, player):
        # return 0 if not ended, 1 if player 1 won, -1 if player 1 lost
        # player = 1
        b = Board(self.n)
        b.pieces = np.copy(board)
        if b.has_legal_moves(player):
            return 0
        if b.has_legal_moves(-player):
            return 0
        if b.countDiff(player) > 0:
            return 1
        return -1

    def getCanonicalForm(self, board, player):
        # return state if player==1, else return -state if player==-1
        return player*board

    def getSymmetries(self, board, pi):
        # mirror, rotational
        assert(len(pi) == self.n**2+1)  # 1 for pass
        pi_board = np.reshape(pi[:-1], (self.n, self.n))
        l = []

        for i in range(1, 5):
            for j in [True, False]:
                newB = np.rot90(board, i)
                newPi = np.rot90(pi_board, i)
                if j:
                    newB = np.fliplr(newB)
                    newPi = np.fliplr(newPi)
                l += [(newB, list(newPi.ravel()) + [pi[-1]])]
        return l

    def stringRepresentation(self, board):
        return board.tostring()

    def stringRepresentationReadable(self, board):
        board_s = "".join(self.square_content[square] for row in board for square in row)
        return board_s

    def getScore(self, board, player):
        b = Board(self.n)
        b.pieces = np.copy(board)
        return b.countDiff(player)

    @staticmethod
    def display(board):
        n = board.shape[0]
        print("   ", end="")
        for y in range(n):
            print(y, end=" ")
        print("")
        print("-----------------------")
        for y in range(n):
            print(y, "|", end="")    # print the row #
            for x in range(n):
                piece = board[y][x]    # get the piece to print
                print(OthelloGame.square_content[piece], end=" ")
            print("|")

        print("-----------------------")
