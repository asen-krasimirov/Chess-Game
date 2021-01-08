from abc import ABC, abstractmethod
from project.configs import ALLOWED_COLORS
from project.pieces.cell import Cell


class Piece(ABC, Cell):
    attacked_pieces: list

    @abstractmethod
    def __init__(self, row: int, column: int, side: str):
        super().__init__(row, column)
        # self.position = row, column
        # self.is_captured = False
        # self.is_attacking = False
        self.attacked_pieces = []
        self.side = side
        # self.moved_once = []  # gets set to false on initialization
        self.times_moves = 0

    # def gather_attacked_pieces(self, pieces: list):
    #     self.attacked_pieces = pieces

    def move_piece(self, new_row, new_column):
        self.position = new_row, new_column

    @abstractmethod
    def legal_moves(self) -> dict:
        pass
    
    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        if value not in ALLOWED_COLORS:
            raise ValueError(f'Invalid piece side given -> {value}')
        self.__side = value

    def __eq__(self, val):
        return str(self) == val

    def __str__(self):
        return f'{self.side[0]}{self.__class__.__name__[0]}'  # example White Pown -> WP
