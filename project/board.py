from project.pieces.abstract_piece import Piece
from typing import List, Union
from project.configs import FIELD_SIZE, valid_index, FREE_SPACE_SYMBOL


class Board:
    _SIZE = FIELD_SIZE
    __field = List[Union[str, Piece]]

    def __init__(self):
        self.__field = [[FREE_SPACE_SYMBOL for _ in range(self._SIZE)] for _ in range(self._SIZE)]

    def return_board_for_print(self) -> str:
        board_information = "   A  B  C  D  E  F  G  H\n"
        current_row = 1
        for row in self.__field:
            board_information += f'{current_row}  ' + ' '.join(str(elem) for elem in row) + f'  {current_row}' + '\n'
            current_row += 1
        board_information += "   A  B  C  D  E  F  G  H"
        return board_information

    def add_piece(self, piece: Piece):
        row, column = piece.position
        self.__field[row][column] = piece

    def remove_piece(self, piece: Piece):
        row, column = piece.position
        self.__field[row][column] = FREE_SPACE_SYMBOL

    def __find_piece_in_field(self, coordinates: list):
        piece = self.__field[coordinates[0]][coordinates[1]]
        if isinstance(piece, str):  # NOTE: change validation when doing a graphic version
            raise ValueError('No piece on this position.')
        return self.__field[coordinates[0]][coordinates[1]]

    @staticmethod
    def __convert_coordinates(coordinates: str):
        column_coordinates = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        row_coordinates = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}

        new_coordinates = [row_coordinates[coordinates[1]], column_coordinates[coordinates[0]]]
        return new_coordinates

    @staticmethod
    def __reverse_convert_coordinates(coordinates: str):
        column_coordinates = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H'}
        row_coordinates = {'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7, '7': 8}

        new_coordinates = [row_coordinates[str(coordinates[0])], column_coordinates[str(coordinates[1])]]
        return new_coordinates

    def possible_moves(self, coordinates: str) -> dict:  # getting information as coordinates (1, 0 -> A2)
        coordinates = self.__convert_coordinates(coordinates)  # converting from coordinates (A2 -> 0, 1)

        piece = self.__find_piece_in_field(coordinates)
        piece_type = piece.__class__.__name__

        all_moves = piece.legal_moves
        pieces_attacked = []
        for direction in all_moves:
            available_positions = []
            for position in all_moves[direction]:
                cur_row, cur_column = position
                if not valid_index(cur_row) or not valid_index(cur_column):
                    break
                if self.__field[position[0]][position[1]] != FREE_SPACE_SYMBOL:
                    pieces_attacked.append(position)
                    break
                available_positions.append(position)

            all_moves[direction] = available_positions if available_positions else 'No spots available.'

        if piece_type == 'Pown' and piece.side == 'Black':
            pieces_attacked = [(coordinates[0]+1, coordinates[1]-1), (coordinates[0]+1, coordinates[1]+1)]
            pieces_attacked = [position for position in pieces_attacked if valid_index(position[0]) and valid_index(position[1]) and self.__field[position[0]][position[1]] != FREE_SPACE_SYMBOL]

        elif piece_type == 'Pown' and piece.side == 'White':
            pieces_attacked = [(coordinates[0]-1, coordinates[1]-1), (coordinates[0]-1, coordinates[1]+1)]
            pieces_attacked = [position for position in pieces_attacked if valid_index(position[0]) and valid_index(position[1]) and self.__field[position[0]][position[1]] != FREE_SPACE_SYMBOL]

        pieces_attacked = [position for position in pieces_attacked if self.__field[position[0]][position[1]].side != self.__field[coordinates[0]][coordinates[1]].side]
        all_moves['Attacking Pieces'] = pieces_attacked if pieces_attacked else 'Not attacking any piece.'
        # converting to coordinates (0, 1 -> A2)
        for name, moves in all_moves.items():
            if not isinstance(moves, str):
                # print([self.__reverse_convert_coordinates(move) for move in moves])
                all_moves[name] = [self.__reverse_convert_coordinates(move) for move in moves]
        return all_moves

    def move_piece(self, piece_coordinates: str, new_coordinates: str) -> Union[None, str]:

        piece_coordinates = self.__convert_coordinates(piece_coordinates)
        new_coordinates = self.__convert_coordinates(new_coordinates)

        try:
            piece = self.__find_piece_in_field(piece_coordinates)
            self.remove_piece(piece)
            piece.position = new_coordinates
            self.add_piece(piece)
        except ValueError as exc:
            return str(exc)
