# TC project B
# Jacob Björkman

from board import Board
from piece import Piece


def warnsdorf(piece):
    """ Based on Warnsdorf's rule for the knights tour problem but with an addition of a
    incresing random weight as the number of unsuccessfull paths increases"""

    start = [piece.pos_x, piece.pos_y]
    path = []
    fails = 0

    while not piece.board.visited_all(path):
        piece.board.reset()
        piece.move_to(start)
        path = [start]

        for _ in range(piece.board.size_x * piece.board.size_y):
            new_pos = piece.move_to_best(fails % 100)

            if new_pos is None:
                fails += 1
                break
            path.append(new_pos)

    return path


def main():
    while True:
        inputa = input("\nEnter anything to run or \"q\" to quit")
        if inputa == "q" or inputa == "Q":
            break

        print("#############################################################")
        board = Board(10)
        piece = Piece(board)

        print("\nFinding path from [", piece.pos_x, ",", piece.pos_y,
              "] to all other", board.size_x*board.size_y-1, "squares\n")


        vag = warnsdorf(piece)

        print("Length of found path:", len(vag))
        print("Found path:")

        print(vag)


if __name__ == "__main__":
    main()