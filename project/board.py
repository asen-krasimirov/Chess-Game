from project.pieces.abstract_piece import Piece
from typing import List, Union
from project.configs import FIELD_SIZE


class Board:
    _SIZE = FIELD_SIZE
    # _LENGTH = 8
    __field = List[Union[str, Piece]]

    def __init__(self):
        self.__field = [['.' for _ in range(self._SIZE)] for _ in range(self._SIZE)]

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
    
    def possible_moves(self, coordinates) -> str:
        piece = self.__field[coordinates[0]][coordinates[1]]
        all_moves = piece.legal_moves
        for direction in all_moves:
            available_positions = []
            for position in all_moves[direction]:
                if self.__field[position[0]][position[1]] == '.':
                    available_positions.append(position)
                else:
                    break
            all_moves[direction] = available_positions if available_positions else 'No spots available.'
        return all_moves
