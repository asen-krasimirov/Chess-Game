from project.configs import FREE_SPACE_SYMBOL


class Cell:
    def __init__(self, row: int, column: int):
        self.__is_attacked = False
        self.side = 'Neutral'
        self.position = row, column

    @property
    def is_attacked(self):
        return self.__is_attacked

    @is_attacked.setter
    def is_attacked(self, new_val):
        self.__is_attacked = new_val

    def __eq__(self, val):
        return val == FREE_SPACE_SYMBOL

    def __str__(self):
        return FREE_SPACE_SYMBOL
