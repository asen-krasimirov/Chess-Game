from abc import ABC, abstractmethod


class Piece(ABC):

    @abstractmethod
    def __init__(self, row: int, column: int, side: str):
        self.starting_position = row, column
        self.is_captured = False
        self.side = side

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
