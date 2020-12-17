

FIELD_SIZE = 8
FREE_SPACE_SYMBOL = '.'

def valid_index(number, matrix_length=FIELD_SIZE):
    if -1 < number < matrix_length:
        return True
    return False
