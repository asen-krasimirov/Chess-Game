from project.board import Board
from project.pieces.pown import Pown
from project.pieces.rook import Rook

board = Board()
pieces = [
    Pown(1, 0, 'Black'),
    Rook(2, 0, 'White')
]

print(board.return_board_for_print())
board.add_piece(pieces[0])
board.add_piece(pieces[1])
print(board.return_board_for_print())

piece_coordinates = list(int(x) for x in input('select piece: '))  # coordinates
print(board.possible_moves(piece_coordinates))
