from project.board import Board
from project.pieces.pown import Pown

board = Board()
pieces = [
    Pown(6, 0, 'White')
]

if __name__ == '__main__':
    print(board.return_board_for_print())
    board.add_piece(pieces[0])
    print(board.return_board_for_print())
