
class Board(object):
    def __init__(self, size_x, size_y = None):
        self.size_x = size_x
        self.size_y = size_y
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

    def not_visited(self, x, y):
        return self.squares[y][x] == 0

    def valid_move(self, x, y):
        if 0 <= x < self.size_x and 0 <= y < self.size_y:
            return self.not_visited(x, y)

    def set_visited(self, x,y):
        self.squares[y][x] = 1

