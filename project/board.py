from project.pieces.abstract_piece import Piece
from typing import List, Union
from project.configs import FIELD_SIZE, valid_index, FREE_SPACE_SYMBOL


class Board:
    _SIZE = FIELD_SIZE
    # _LENGTH = 8
    __field = List[Union[str, Piece]]

    def __init__(self):
        self.__field = [[FREE_SPACE_SYMBOL for _ in range(self._SIZE)] for _ in range(self._SIZE)]

    def return_board_for_print(self) -> str:
        board_information = "   A B C D E F G H\n"
        current_row = 1
        for row in self.__field:
            board_information += f'{current_row}  ' + ' '.join(str(elem) for elem in row) + '\n'
            current_row += 1

        return board_information  # NOTE: strip later (.strip('\n'))

    def add_piece(self, piece: Piece):
        row, column = piece.position
        self.__field[row][column] = piece

    def remove_piece(self, piece: Piece):
        row, column = piece.position
        self.__field[row][column] = FREE_SPACE_SYMBOL

    def __find_piece_in_field(self, coordinates: list):
        piece = self.__field[coordinates[0]][coordinates[1]]
        if isinstance(piece, str):
            raise ValueError('No piece on this position.')
        return self.__field[coordinates[0]][coordinates[1]]

    def possible_moves(self, coordinates: list) -> dict:
        piece = self.__find_piece_in_field(coordinates)
        all_moves = piece.legal_moves
        for direction in all_moves:
            available_positions = []
            for position in all_moves[direction]:
                cur_row, cur_column = position
                if not valid_index(cur_row) or not valid_index(cur_column):
                    break
                if self.__field[position[0]][position[1]] != FREE_SPACE_SYMBOL:
                    break
                available_positions.append(position)

            all_moves[direction] = available_positions if available_positions else 'No spots available.'
        return all_moves

    def move_piece(self, piece_coordinates: list, new_coordinates: list) -> Union[None, str]:
        # self.__find_piece_in_field(piece_coordinates)
        try:
            piece = self.__find_piece_in_field(piece_coordinates)
            self.remove_piece(piece)
            piece.position = new_coordinates
            self.add_piece(piece)
        except ValueError as exc:
            return str(exc)
