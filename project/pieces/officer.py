from project.pieces.abstract_piece import Piece


class Officer(Piece):

    def __init__(self, row: int, column: int, side: str):
        super().__init__(row, column, side)