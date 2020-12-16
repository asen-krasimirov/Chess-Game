from project.pieces.abstract_piece import Piece


class Pown(Piece):

    def __init__(self, row: int, column: int, side: str):
        super().__init__(row, column, side)

    @property
    def legal_moves(self):
        moves = {}
        if self.side == 'Black':
            moves['Down'] = [[self.position[0]+1, self.position[1]]]
            if not self.moved_once:
                moves['Down'].append([self.position[0]+2, self.position[1]])
        else:
            moves['Up'] = [[self.position[0]-1, self.position[1]]]
            if not self.moved_once:
                moves['Up'].append([self.position[0]-2, self.position[1]])
        return moves
