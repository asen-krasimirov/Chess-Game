import os

from project.board import Board
from project.piece_initialization import white_pieces, black_pieces


def print_possible_moves(moves: dict):
    for name, positions in moves.items():
        positions = ", ".join([f'{pos[0]}{pos[1]}' for pos in positions]) if not isinstance(positions, str) else positions

        print(f'{name} -> {positions}')


def available_piece(possible_coordinates: dict):
    for direction in possible_coordinates:
        if not isinstance(possible_coordinates[direction], str):
            return True
    return False


def reprint_board():
    os.system('cls')
    print(board.return_board_for_print())
    print()


def alert_king_is_attacked(side):
    if side:
        print(f'{side} King is under attack. Defend the king.')
    else:
        print('NO king is attacked.')


board = Board()

[board.add_piece(piece) for piece in white_pieces]
[board.add_piece(piece) for piece in black_pieces]
reprint_board()

turns = ["White's Turn", "Black's Turn"]
i = 1
while True:
    board.make_every_attacked_cell_attacked()

    attacked_king = None

    if board.is_king_under_attack('White'):
        attacked_king = 'White'

    elif board.is_king_under_attack('Black'):
        attacked_king = 'Black'

    if attacked_king:
        alert_king_is_attacked(attacked_king)

    i += 1
    print(turns[i % len(turns)])
    while True:
        print()
        try:
            piece_coordinates = input('Select piece: ')  # coordinates
            moving_positions = board.possible_moves(piece_coordinates)
        except (ValueError, AttributeError) as exc:
            print(str(exc))
            continue
        if not available_piece(moving_positions):
            print('Piece unavailable.')
            continue

        print_possible_moves(moving_positions)

        place_to_move = input('Select place to move to: ')  # coordinates
        if place_to_move not in [item for elem in moving_positions.values() for item in elem]:
            print('Position unreachable.\n')
            continue

        board.move_piece(piece_coordinates, place_to_move)

        board.make_every_attacked_cell_attacked()

        if board.is_king_under_attack(attacked_king):
            alert_king_is_attacked(attacked_king)
            board.move_piece(place_to_move, piece_coordinates)
            continue

        break
    reprint_board()
