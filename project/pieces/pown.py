from project.pieces.abstract_piece import Piece
from project.configs import valid_index, FREE_SPACE_SYMBOL
from project.board import Board


class Pown(Piece):

    def __init__(self, row: int, column: int, side: str):
        super().__init__(row, column, side)

    @property
    def legal_moves(self):  # TODO: implement pown's different attacking
        moves = {}

        if self.side == 'Black':
            moves['Down'] = [(self.position[0]+1, self.position[1])]
            if self.times_moves <= 2:
                moves['Down'].append((self.position[0]+2, self.position[1]))
        else:
            moves['Up'] = [(self.position[0]-1, self.position[1])]
            if self.times_moves <= 2:
                moves['Up'].append((self.position[0]-2, self.position[1]))

        self.times_moves += 1

        return moves
