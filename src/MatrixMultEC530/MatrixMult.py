def validateMatrix(matrix):
    """
    Validate if the given matrix is valid:
   - Check if the matrix is a list.
   - Ensure all rows have the same number of columns.
   - Verify that all elements are numerical.

    :param matrix:
    - (List) The matrix to be validated.
    :return:
    - bool: True if the matrix is valid, False otherwise.
    """
    if not isinstance(matrix, list):
        return False

    num_cols = len(matrix[0])
    if not all(len(row) == num_cols for row in matrix):
        return False

    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        return False

    return True

def validateDimensions(matrixA, matrixB):
    """
    Validate if the dimensions of two matrices allow for matrix multiplication.

    :param matrix1: The first matrix. (List)
    :param matrix2: The second matrix. (List)
    :return: bool - True if the dimensions are valid, False otherwise.
    """
    if len(matrixA[0]) != len(matrixB):
        return False
    return True

def MatrixMult(A,B):
    """
    Perform matrix multiplication.

    :param A: The first matrix.
    :param B: The second matrix.
    :return: list or str: The result of matrix multiplication if successful,
    or an error message if invalid input or dimensions.
    """
    if not validateMatrix(A) or not validateMatrix(B):
        return "Error: Invalid input matrices. Please ensure they are valid matrices with only numerical elements."

    if not validateDimensions(A, B):
        return "Error: Invalid matrix dimensions for multiplication."

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            element_sum = sum(A[i][k] * B[k][j] for k in range(len(B)))
            row.append(element_sum)
        result.append(row)

    return result


"""if __name__ == "__main__":
    A = [[2, 1],
         [1, 2]]

    B = [[1, 'a'],
         [0, 1]]
    C = MatrixMult(A,B)
    print(C)"""
