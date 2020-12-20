from project.pieces.abstract_piece import Piece
from project.configs import FIELD_SIZE, valid_index


class Horse(Piece):

    def __init__(self, row: int, column: int, side: str):
        super().__init__(row, column, side)

    @property
    def legal_moves(self):
        moves = {'Down': [], 'Up': [], 'Right': [], 'Left': []}
        allowed_moves = {
            'down': [(-2, -1), (-2, 1)],  # going down
            'up': [(2, -1), (2, 1)],  # going up
            'right': [(-1, 2), (1, 2)],  # going right
            'left': [(-1, -2), (1, -2)]  # going left
        }
        # going down
        for delta in allowed_moves['down']:
            new_row, new_column = self.position[0] + delta[0], self.position[1] + delta[1]
            if valid_index(new_row) and valid_index(new_column):
                moves['Down'].append((new_row, new_column))

        # going up
        for delta in allowed_moves['up']:
            new_row, new_column = self.position[0] + delta[0], self.position[1] + delta[1]
            if valid_index(new_row) and valid_index(new_column):
                moves['Up'].append((new_row, new_column))

        # going right
        for delta in allowed_moves['right']:
            new_row, new_column = self.position[0] + delta[0], self.position[1] + delta[1]
            if valid_index(new_row) and valid_index(new_column):
                moves['Right'].append((new_row, new_column))

        # going left
        for delta in allowed_moves['left']:
            new_row, new_column = self.position[0] + delta[0], self.position[1] + delta[1]
            if valid_index(new_row) and valid_index(new_column):
                moves['Left'].append((new_row, new_column))

        return moves
