#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    columns = len(matrix[0])
    if columns == 0:
        print()
        return
    for i in range(rows):
        delimiter = ' '
        for w in range(columns):
            if w == columns - 1:
                delimiter = '\n'
            print("{:d}".format(matrix[i][w]), end=delimiter)
