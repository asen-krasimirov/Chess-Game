from project.board import Board
from project.pieces.pown import Pown
from project.pieces.rook import Rook
from project.pieces.horse import Horse
from project.pieces.officer import Officer


board = Board()
pieces = [
    Pown(1, 0, 'Black'),
    Rook(2, 0, 'White'),
    Horse(2, 1, 'White'),
    Officer(1, 1, 'Black')
]

board.add_piece(pieces[0])
board.add_piece(pieces[1])
board.add_piece(pieces[2])
board.add_piece(pieces[3])
print(board.return_board_for_print())

while True:
    piece_coordinates = list(int(x) for x in input('select piece: '))  # coordinates
    moving_positions = board.possible_moves(piece_coordinates)
    # attacking_positions = board.possible_attacks(piece_coordinates) TODO: implement attacking

    print(moving_positions)
    # print(attacking_positions)

    while True:
        place_to_move = list(int(x) for x in input('select place to move to: '))
        values = [elem for collection in moving_positions.values() for elem in collection]
        if tuple(place_to_move) in values:
            board.move_piece(piece_coordinates, place_to_move)
            board.move_piece(piece_coordinates, place_to_move)
        # elif place_to_move in attacking_positions: TODO: --.--
        #     pass
        else:
            print('invalid coordinates')
            continue
        break

    print(board.return_board_for_print())
