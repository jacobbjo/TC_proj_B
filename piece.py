from board import Board
from random import randint


class Piece(object):
    def __init__(self, board, pos_x = None, pos_y = None):
        self.board = board
        self.pos_x = pos_x
        self.pos_y = pos_y

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, b):
        if not type(b) == Board:
            raise TypeError("Board assigned to piece must be of type Board")
        self._board = b
        
    @property
    def pos_x(self):
        return self._pos_x

    @pos_x.setter
    def pos_x(self, v):
        if v is None:
            # If no piece position was given generate one with simple randomization
            self.pos_x = randint(0, self.board.size_x)
        elif not(v >= 0):
            raise Exception("Piece pos_x must be zero or greater")
        else:
            self._pos_x = v

    @property
    def pos_y(self):
        return self._pos_y

    @pos_y.setter
    def pos_y(self, v):
        if v is None:
            # If no piece position was given generate one with simple randomization
            self.pos_y = randint(0, self.board.size_y)
        elif not(v >= 0):
            raise Exception("Piece pos_y must be zero or greater")
        else:
            self._pos_y = v

    def move_to(self, x, y):
        if self.board.valid_move(x, y):
            self.pos_x = x
            self.pos_y = y
            self.board.set_visited(x, y)
            return True
        return False

