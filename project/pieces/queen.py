from project.pieces.abstract_piece import Piece
from project.configs import FIELD_SIZE, valid_index


class Queen(Piece):

    def __init__(self, row: int, column: int, side: str):
        super().__init__(row, column, side)

    @property
    def legal_moves(self):
        moves = {'Down-Right': [], 'Down-Left': [], 'Up-Right': [], 'Up-Left': [], 'Down': [], 'Up': [], 'Right': [], 'Left': []}

        # going down-right
        for i in range(1, FIELD_SIZE + 1):
            new_row, new_column = self.position[0] + i, self.position[1] + i
            if valid_index(new_row):
                moves['Down-Right'].append((new_row, new_column))

        # going down-left
        for i in range(1, FIELD_SIZE + 1):
            new_row, new_column = self.position[0] + i, self.position[1] - i
            if valid_index(new_row):
                moves['Down-Left'].append((new_row, new_column))

        # going up-right
        for i in range(1, FIELD_SIZE + 1):
            new_row, new_column = self.position[0] - i, self.position[1] + i
            if valid_index(new_column):
                moves['Up-Right'].append((new_row, new_column))

        # going up-left
        for i in range(1, FIELD_SIZE + 1):
            new_row, new_column = self.position[0] - i, self.position[1] - i
            if valid_index(new_column):
                moves['Up-Left'].append((new_row, new_column))

        # going down
        for i in range(1, FIELD_SIZE + 1):
            new_row, new_column = self.position[0] + i, self.position[1]
            if valid_index(new_row):
                moves['Down'].append((new_row, new_column))

        # going up
        for i in range(1, FIELD_SIZE + 1):
            new_row, new_column = self.position[0] - i, self.position[1]
            if valid_index(new_row):
                moves['Up'].append((new_row, new_column))

        # going right
        for i in range(1, FIELD_SIZE + 1):
            new_row, new_column = self.position[0], self.position[1] + i
            if valid_index(new_column):
                moves['Right'].append((new_row, new_column))

        # going left
        for i in range(1, FIELD_SIZE + 1):
            new_row, new_column = self.position[0], self.position[1] - i
            if valid_index(new_column):
                moves['Left'].append((new_row, new_column))

        return dict(moves)
