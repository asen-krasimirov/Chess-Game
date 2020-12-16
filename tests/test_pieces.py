import unittest
from project.pieces.pown import Pown


class BoardTests(unittest.TestCase):
    def setUp(self):
        self.piece = Pown(6, 1, 'White')

    def test_init_creates_proper_attrs(self):

        self.assertEqual((6, 1), self.piece.position)
        self.assertEqual('White', self.piece.side)

    def test_raises_exception_when_piece_received_invalid_side(self):
        with self.assertRaises(ValueError) as exc:
            Pown(1, 1, 'Green')
        self.assertEqual('Invalid piece side given -> Green', str(exc.exception))


if __name__ == '__main__':
    unittest.main()
