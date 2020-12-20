from project.board import Board
from project.piece_initialization import white_pieces, black_pieces

board = Board()

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
