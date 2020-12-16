import unittest
from project.board import Board
from project.pieces.pown import Pown
from project.pieces.rook import Rook


class BoardTests(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_adding_pieces_to_field(self):
        self.board.add_piece(
            Pown(6, 0, 'White')
        )
        result = self.board.return_board_for_print()
        expected_result = '''   A B C D E F G H
1  . . . . . . . .
2  . . . . . . . .
3  . . . . . . . .
4  . . . . . . . .
5  . . . . . . . .
6  . . . . . . . .
7  WP . . . . . . .
8  . . . . . . . .
'''  # NOTE: going to be used split no it
        self.assertEqual(expected_result, result)

    def test_display_correct_possible_moves(self):
        pieces = [
            Pown(1, 0, 'Black'),
            Rook(2, 0, 'White')
        ]
        self.board.add_piece(pieces[0])
        self.board.add_piece(pieces[1])
        result = self.board.possible_moves((2, 0))
        self.assertEqual({'Down': [(3, 0), (4, 0), (5, 0), (6, 0), (7, 0)], 'Up': 'No spots available.', 'Right': [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7)], 'Left': 'No spots available.'},
                         result, result)
        result_two = self.board.possible_moves((1, 0))
        self.assertEqual({'Down': 'No spots available.'}, result_two, result_two)


if __name__ == '__main__':
    unittest.main()
