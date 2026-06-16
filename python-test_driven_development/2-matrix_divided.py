#!/usr/bin/python3
"""Defines matrix_divided, a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides a matrix by a given number.

    Parameters:
        matrix (list[list[float, int]]): The matrix to divide.
        div (int, float) The divisor.
    
    Returns:
        (list[list[float, int]]): The divided matrix.
    """

    validate_matrix(matrix)
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = []

    for r in range(0, len(matrix)):
        row = []
        for col in range(0, len(matrix[r])):
            row.append(matrix[r][col] / div)
        new_matrix.append(row)
    
    return new_matrix

def validate_matrix(matrix):
    """Validates the given matrix.
    
    Parameters:
        matrix (list[list[int, float]]): The matrix to validate.
    """

    row_length = -1
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if row_length == -1:
            row_length = len(row)
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")