import unittest
from project.board import Board
from project.pieces.pown import Pown


class BoardTests(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_adding_pieces_to_field(self):
        self.board.add_piece(
            Pown(6, 0, 'White')
        )
        result = self.board.return_board_for_print()
        expected_result = '''. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
WP . . . . . . .
. . . . . . . .'''
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
