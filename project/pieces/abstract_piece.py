from abc import ABC, abstractmethod


class Piece(ABC):

    @abstractmethod
    def __init__(self, row: int, column: int, side: str):
        self.position = row, column
        self.is_captured = False
        self.is_attacking = False
        self.attacked_pieces = []
        self.side = side
        self.moved_once = False

    def gather_attacked_pieces(self, pieces: list):
        self.attacked_pieces = pieces

    def move_piece(self, new_row, new_column):
        self.position = new_row, new_column

    @abstractmethod
    def legal_moves(self):
        pass
    
    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        if value not in {'Black', 'White'}:
            raise ValueError(f'Invalid piece side given -> {value}')
        self.__side = value

    def __str__(self):
        return f'{self.side[0]}{self.__class__.__name__[0]}'  # example White Pown -> WP
