import os

from project.board import Board
from project.piece_initialization import white_pieces, black_pieces


def print_possible_moves(moves: dict):
    for name, positions in moves.items():
        positions = ", ".join([f'{pos[1]}{pos[0]}' for pos in positions]) if not isinstance(positions, str) else positions

        print(f'{name} -> {positions}')


def available_piece(possible_coordinates: dict):
    for direction in possible_coordinates:
        if not isinstance(possible_coordinates[direction], str):
            return True
    return False


def reprint_board():
    os.system('cls')
    print(board.return_board_for_print())


board = Board()

[board.add_piece(piece) for piece in white_pieces]
[board.add_piece(piece) for piece in black_pieces]
print(board.return_board_for_print())

turns = ["White's Turn", "Black's Turn"]
i = 1
while True:
    i += 1
    # White Turn
    print(turns[i % len(turns)])
    while True:
        piece_coordinates = input('Select piece: ')  # coordinates
        moving_positions = board.possible_moves(piece_coordinates)
        if not available_piece(moving_positions):
            print('Piece unavailable.\n')
            continue

        print_possible_moves(moving_positions)

        place_to_move = input('Select place to move to: ')  # coordinates
        board.move_piece(piece_coordinates, place_to_move)
        board.move_piece(piece_coordinates, place_to_move)
        break
    reprint_board()

    #
    # # Black Turn
    # print("Black's Turn")
    # piece_coordinates = input('Select piece: ')  # coordinates
    # moving_positions = board.possible_moves(piece_coordinates)
    #
    # print_possible_moves(moving_positions)
    #
    # place_to_move = input('Select place to move to: ')  # coordinates
    #
    # board.move_piece(piece_coordinates, place_to_move)
    # board.move_piece(piece_coordinates, place_to_move)
    #
    # reprint_board()
