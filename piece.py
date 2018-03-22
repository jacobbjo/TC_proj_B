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

    def move_to(self, coords):
        if self.board.valid_move(coords):
            self.pos_x = coords[0]
            self.pos_y = coords[1]
            self.board.set_visited(coords)
            return True
        return False

    def get_coords(self, dir):
        if dir == "n":
            return [self.pos_x, self.pos_y - 3]
        if dir == "s":
            return [self.pos_x, self.pos_y + 3]
        if dir == "e":
            return [self.pos_x + 3, self.pos_y]
        if dir == "w":
            return [self.pos_x - 3, self.pos_y]
        if dir == "ne":
            return [self.pos_x + 2, self.pos_y - 2]
        if dir == "se":
            return [self.pos_x + 2, self.pos_y + 2]
        if dir == "sw":
            return [self.pos_x - 2, self.pos_y + 2]
        if dir == "nw":
            return [self.pos_x - 2, self.pos_y - 2]

    def get_h(self, coords):
        x = coords[0]
        y = coords[1]

        h = 0
        if self.board.valid_move(x, y - 3): h += 1
        if self.board.valid_move(x, y + 3): h += 1
        if self.board.valid_move(x + 3, y): h += 1
        if self.board.valid_move(x - 3, y): h += 1
        if self.board.valid_move(x + 2, y - 2): h += 1
        if self.board.valid_move(x + 2, y + 2): h += 1
        if self.board.valid_move(x - 2, y - 2): h += 1
        if self.board.valid_move(x - 2, y - 2): h += 1

        return h

    def move_to_best(self):
        moves = ["n","s","e", "w", "ne", "se", "sw", "nw"]
        min_h = 10
        min_move

        for move in moves:
            move_coords = get_coords(move)
            if self.board.valid_move(move_coords) and get_h(move_coords) < min_h:
                min_h = get_h()
                min_move = move

        self.move_to(get_coords(min_move))

        return get_coords(min_move)
