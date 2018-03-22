from board import Board
from random import randint


class Piece(object):
    """ Represents a piece on the chessboard """

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
            self.pos_x = randint(0, self.board.size_x-1)
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
            self.pos_y = randint(0, self.board.size_y-1)
        elif not(v >= 0):
            raise Exception("Piece pos_y must be zero or greater")
        else:
            self._pos_y = v

    def move_to(self, coords):
        """ Moves the piece to the specified coordinates"""

        if self.board.valid_move(coords):
            self.pos_x = coords[0]
            self.pos_y = coords[1]
            self.board.set_visited(coords)
            return True
        return False

    def get_coords(self, dir):
        """ Returns the coordinates if the piece does a certain move"""

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
        """ Returns the heuristic for the given coordinates based on how many valid moves
        there is from those coordinates """

        x = coords[0]
        y = coords[1]
        h = 0

        if self.board.valid_move([x, y - 3]): h += 1
        if self.board.valid_move([x, y + 3]): h += 1
        if self.board.valid_move([x + 3, y]): h += 1
        if self.board.valid_move([x - 3, y]): h += 1
        if self.board.valid_move([x + 2, y - 2]): h += 1
        if self.board.valid_move([x + 2, y + 2]): h += 1
        if self.board.valid_move([x - 2, y - 2]): h += 1
        if self.board.valid_move([x - 2, y - 2]): h += 1

        return h

    def move_to_best(self, weight = 0):
        """ Moves the piece in the direction that is deemed best based on the Warnsdof's rule where
        the position with the lowest amount of possible moves is prioritized.
        Returns the new position. """

        moves = ["n", "s", "e", "w", "ne", "se", "sw", "nw"]
        min_h = 10
        min_move = None

        for move in moves:
            move_coords = self.get_coords(move)

            # Randomly add a weight to the heuristic based on amount of errors in previous runs
            h_move_coords = self.get_h(move_coords) + randint(0, weight)

            if self.board.valid_move(move_coords) and h_move_coords != 0:
                if h_move_coords < min_h:
                    min_h = h_move_coords
                    min_move = move
                elif h_move_coords == min_h:
                    # Solve ties randomly
                    if randint(0, 1) == 1:
                        min_h = h_move_coords
                        min_move = move

        if min_move is not None:
            new_pos = self.get_coords(min_move)
            self.move_to(new_pos)
            return new_pos

        return None
