from project.pieces.abstract_piece import Piece
from typing import List, Union


class Board:
    _HEIGHT = 8
    _LENGTH = 8
    __field = List[Union[str, Piece]]

    def __init__(self):
        self.__field = [['.' for _ in range(self._LENGTH)] for _ in range(self._HEIGHT)]

    def return_board_for_print(self) -> str:
        board_information = "   A B C D E F G H\n"
        current_row = 8
        for row in self.__field:
            board_information += f'{current_row}  ' + ' '.join(str(elem) for elem in row) + '\n'
            current_row -= 1

        return board_information  # NOTE: strip later (.strip('\n'))

    def add_piece(self, piece: Piece):
        row, column = piece.starting_position
        self.__field[row][column] = piece
