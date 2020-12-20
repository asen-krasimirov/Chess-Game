from project.board import Board
from project.pieces.king import King
from project.pieces.pown import Pown
from project.pieces.queen import Queen
from project.pieces.rook import Rook
from project.pieces.horse import Horse
from project.pieces.officer import Officer


board = Board()


white_pieces = [
    Pown(6, 0, 'White'),
    Pown(6, 1, 'White'),
    Pown(6, 2, 'White'),
    Pown(6, 3, 'White'),
    Pown(6, 4, 'White'),
    Pown(6, 5, 'White'),
    Pown(6, 6, 'White'),
    Pown(6, 7, 'White'),
    Rook(7, 0, 'White'),
    Rook(7, 7, 'White'),
    Horse(7, 1, 'White'),
    Horse(7, 6, 'White'),
    Officer(7, 2, 'White'),
    Officer(7, 5, 'White'),
    Queen(7, 3, 'White'),
    King(7, 4, 'White'),
]

black_pieces = [
    Pown(1, 0, 'Black'),
    Pown(1, 1, 'Black'),
    Pown(1, 2, 'Black'),
    Pown(1, 3, 'Black'),
    Pown(1, 4, 'Black'),
    Pown(1, 5, 'Black'),
    Pown(1, 6, 'Black'),
    Pown(1, 7, 'Black'),
    Rook(0, 0, 'Black'),
    Rook(0, 7, 'Black'),
    Horse(0, 1, 'Black'),
    Horse(0, 6, 'Black'),
    Officer(0, 2, 'Black'),
    Officer(0, 5, 'Black'),
    Queen(0, 3, 'Black'),
    King(0, 4, 'Black'),
]


[board.add_piece(piece) for piece in white_pieces]
[board.add_piece(piece) for piece in black_pieces]
print(board.return_board_for_print())

while True:
    piece_coordinates = list(int(x) for x in input('select piece: '))  # coordinates
    moving_positions = board.possible_moves(piece_coordinates)

    print(moving_positions)

    while True:
        place_to_move = list(int(x) for x in input('select place to move to: '))
        values = [elem for collection in moving_positions.values() for elem in collection]
        if tuple(place_to_move) in values:
            board.move_piece(piece_coordinates, place_to_move)
            board.move_piece(piece_coordinates, place_to_move)
        else:
            print('invalid coordinates')
            continue
        break

    print(board.return_board_for_print())
