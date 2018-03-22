from board import Board
from piece import Piece

def dfs(piece, path):
    piece.board.print_board()
    print(" ")

    if piece.board.visited_all(path):
        print("ALLLL VISITEDDDDDD!!!!!!!******************************************")
        return path

    path.append([piece.pos_x, piece.pos_y])

    if piece.move_n():
        #print("n")
        path = dfs(piece, path)
        #print("north out")

    if piece.move_se():
        #print("se")
        path = dfs(piece, path)

    if piece.move_w():
        #print("w")
        path = dfs(piece, path)

    if piece.move_ne():
        #print("ne")
        path = dfs(piece, path)

    if piece.move_s():
        #print("s")
        path = dfs(piece, path)

    if piece.move_nw():
        #print("nw")
        path = dfs(piece, path)

    if piece.move_e():
        #print("e")
        path = dfs(piece, path)

    if piece.move_sw():
        #print("sw")
        path = dfs(piece, path)







    #print(path)
    if(len(path) > 1):
        piece.board.unset_visited(path[-1][0], path[-1][1])
        piece.move_to(path[-2][0], path[-2][1])
        return path[:-1]
    else:
        piece.move_to(path[0][0], path[0][1])
        return path

def main():
    print("Test")
    brade = Board(10)
    print("x: ", brade.size_x)
    print("y: ", brade.size_y)
    print(brade.squares)


    pjas = Piece(brade)

    print("pjas x: ", pjas.pos_x)
    print("pjas y: ", pjas.pos_y)

    print("pjas x: ", pjas.pos_x)
    print("pjas y: ", pjas.pos_y)

    print(brade.squares)




    vag = dfs(pjas, [])
    print(vag)

    print("len(vag)", len(vag))
    print("squares on board", brade.size_x*brade.size_y)





if __name__ == "__main__":
    main()