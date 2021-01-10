from project.pieces.king import King
from project.pieces.pown import Pown
from project.pieces.queen import Queen
from project.pieces.rook import Rook
from project.pieces.officer import Officer
from project.pieces.horse import Horse


white_pieces = [
    Pown(6, 0, 'White'),
    Pown(6, 1, 'White'),
    Pown(6, 2, 'White'),
    Pown(6, 3, 'White'),
    Pown(6, 4, 'White'),
    Pown(6, 5, 'White'),
    Pown(6, 6, 'White'),
    Pown(6, 7, 'White'),
    Rook(7, 0, 'White'),
    Rook(7, 7, 'White'),
    Horse(7, 1, 'White'),
    Horse(7, 6, 'White'),
    Officer(7, 2, 'White'),
    Officer(7, 5, 'White'),
    Queen(7, 3, 'White'),
    King(7, 4, 'White'),
]

black_pieces = [
    Pown(1, 0, 'Black'),
    Pown(1, 1, 'Black'),
    Pown(1, 2, 'Black'),
    Pown(1, 3, 'Black'),
    Pown(1, 6, 'Black'),
    Pown(1, 7, 'Black'),
    Rook(0, 0, 'Black'),
    Rook(0, 7, 'Black'),
    Horse(0, 1, 'Black'),
    Horse(0, 6, 'Black'),
    Officer(0, 2, 'Black'),
    Officer(0, 5, 'Black'),
    Queen(0, 3, 'Black'),
    King(0, 4, 'Black'),
]

