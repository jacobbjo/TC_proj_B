from board import Board
from piece import Piece

def main():
    print("Test")
    brade = Board(10,5)
    print("x: ", brade.size_x)
    print("y: ", brade.size_y)
    print(brade.squares)

    pjas = Piece(brade)

    print("pjas x: ", pjas.pos_x)
    print("pjas y: ", pjas.pos_y)

    pjas.move_to(9,10)

    print("pjas x: ", pjas.pos_x)
    print("pjas y: ", pjas.pos_y)



if __name__ == "__main__":
    main()