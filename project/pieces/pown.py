from project.pieces.abstract_piece import Piece


class Pown(Piece):

    def __init__(self, row: int, column: int, side: str):
        super().__init__(row, column, side)

    @property
    def legal_moves(self):  # TODO: implement pown's different attacking
        moves = {}
        if self.side == 'Black':
            moves['Down'] = [(self.position[0]+1, self.position[1])]
            if not self.moved_once:
                moves['Down'].append((self.position[0]+2, self.position[1]))
                self.moved_once = True
        else:
            moves['Up'] = [(self.position[0]-1, self.position[1])]
            if not self.moved_once:
                moves['Up'].append((self.position[0]-2, self.position[1]))
                self.moved_once = True
        return moves
