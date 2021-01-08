

FIELD_SIZE = 8
FREE_SPACE_SYMBOL = 'OO'
WHITE_KING_STARTING_POSITION = 7, 4
BLACK_KING_STARTING_POSITION = 0, 4
ALLOWED_COLORS = ['White', 'Black', 'Neutral']


def valid_index(number, matrix_length=FIELD_SIZE):
    if -1 < number < matrix_length:
        return True
    return False
