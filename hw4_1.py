"""
HW 4-1
Напишите функцию для транспонирования матрицы
"""


def isMatrix(value):
    if type(value) is list:
        for i in range(len(value)):
            if type(value[i]) is not list:
                return False
        else:
            return all(len(value[i]) == len(value[i + 1]) for i in range(len(value) - 1))
    else:
        return False


def transpose_matrix(orig_matrix):
    if isMatrix(orig_matrix):
        return [[matrix[row][col] for row in range(len(orig_matrix))] for col in range(len(orig_matrix[0]))]


def show_matrix(value):
    if isMatrix(value):
        print('\n'.join('\t'.join(map(str, row)) for row in value))
    else:
        print('This is not matrix.')


matrix = [[1, 2, 3], [4, 5, 6]]

show_matrix(matrix)
print()
show_matrix(transpose_matrix(matrix))
