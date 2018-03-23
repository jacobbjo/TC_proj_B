from unittest import TestCase
from board import Board
from piece import Piece

class Test(TestCase):
    """ Some simple tests for the piece and board class"""

    def test_board(self):
        board = Board(10)
        piece = Piece(board, 0, 0)
        self.assertFalse(board.valid_move([-1, 2]))
        self.assertFalse(board.valid_move([2, -1]))
        self.assertTrue(board.valid_move([1, 2]))
        self.assertTrue(board.valid_move([1, 5]))
        self.assertTrue(board.not_visited([3, 3]))
        piece.move_to([1,2])
        piece.move_to([5,5])
        self.assertFalse(board.not_visited([1, 2]))
        self.assertFalse(board.visited_all([]))
        board.reset()
        self.assertTrue(board.not_visited([1, 2]))

    def test_piece(self):
        board = Board(10)
        piece = Piece(board, 0, 0)

        self.assertEqual(piece.get_coords("s"), [0, 3])
        self.assertEqual(piece.get_coords("se"), [2, 2])

        self.assertEqual(piece.get_h([0, 0]), 3)
        self.assertEqual(piece.get_h([5, 5]), 8)

        self.assertIsNotNone(piece.move_to_best())

        self.assertFalse(piece.move_to([-1, 2]))
        self.assertTrue(piece.move_to([2, 2]))
