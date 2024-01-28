def validateMatrix(matrix):

    if not isinstance(matrix, list):
        return False

    num_cols = len(matrix[0])
    if not all(len(row) == num_cols for row in matrix):
        return False

    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        return False

    return True

def validateDimensions(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return False
    return True
def MatrixMult(A,B):
    if not validateMatrix(A) or not validateMatrix(B):
        return "Error: Invalid input matrices. Please ensure they are valid matrices with numerical elements."

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
