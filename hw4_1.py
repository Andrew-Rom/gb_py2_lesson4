"""
HW 4-1
Напишите функцию для транспонирования матрицы
"""


def transpose(orig_matrix: list):
    if all(len(orig_matrix[i]) == len(orig_matrix[i + 1]) for i in range(len(orig_matrix) - 1)):
        return [[matrix[row][col] for row in range(len(orig_matrix))] for col in range(len(orig_matrix[0]))]


def show_matrix(value: list):
    if type(value) is list:
        print('\n'.join('\t'.join(map(str, row)) for row in value))
    else:
        print('This is not matrix.')


matrix = [[1, 2, 3], [4, 5, 6]]

show_matrix(matrix)
print()
show_matrix(transpose(matrix))
