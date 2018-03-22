
class Board(object):
    """ Represents a chessboard of size x*y"""
    def __init__(self, size_x, size_y = None):
        self.size_x = size_x  # number of columns
        self.size_y = size_y  # number of rows
        self.squares = [[0 for x in range(self.size_x)] for y in range(self.size_y)]

    @property
    def size_x(self):
        return self._size_x

    @size_x.setter
    def size_x(self, v):
        if not (v > 0):
            raise Exception("Board size_x must be greater than zero")
        self._size_x = v

    @property
    def size_y(self):
        return self._size_y

    @size_y.setter
    def size_y(self, v):
        # Sets y to x if no y was given
        if v is None:
            self.size_y = self.size_x
        elif not(v > 0):
            raise Exception("Board size_y must be greater than zero")
        else:
            self._size_y = v

    def not_visited(self, coords):
        """ Returns whether the specified coordinates have been previously visited"""
        return self.squares[coords[1]][coords[0]] == 0

    def valid_move(self, coords):
        """ Returns whether the specified coordinates are valid"""
        if 0 <= coords[0] < self.size_x and 0 <= coords[1] < self.size_y:
            return self.not_visited(coords)
        return False

    def set_visited(self, coords):
        """ Sets the specified coordinates as visited"""
        self.squares[coords[1]][coords[0]] = 1

    def visited_all(self, path):
        """ Returns whether all squares on the board has been visited """
        return len(path) == self.size_x * self.size_y

    def reset(self):
        """ Resets the board so nothing is marked as visited"""
        self.squares = [[0 for x in range(self.size_x)] for y in range(self.size_y)]




