from src.MatrixMultEC530.MatrixMult import validateMatrix, validateDimensions, MatrixMult

def testValidateMatrixValid():
    matrix = [[1, 2, 3], [4, 5, 6]]
    assert validateMatrix(matrix) == True

def testValidateMatrixInvalidType():
    matrix = "invalid"
    assert validateMatrix(matrix) == False

def testValidateMatrixInvalidElement():
    matrix = [[1, 'a', 3], [4, 5, 6]]
    assert validateMatrix(matrix) == False

# Test validate_dimensions function
def testValidateDimensionsValid():
    matrix1 = [[1, 2, 3], [4, 5, 6]]
    matrix2 = [[7, 8], [9, 10], [11, 12]]
    assert validateDimensions(matrix1, matrix2) == True

def testValidateDimensionsInvalid():
    matrix1 = [[1, 2, 3], [4, 5, 6]]
    matrix2 = [[7, 8], [9, 10], [11, 12], [13, 14]]
    assert validateDimensions(matrix1, matrix2) == False

# Test matrix_multiply function
def testMatrixMultiplyValid():
    matrix_A = [[1, 2, 3], [4, 5, 6]]
    matrix_B = [[7, 8], [9, 10], [11, 12]]
    result = MatrixMult(matrix_A, matrix_B)
    assert result == [[58, 64], [139, 154]]

def testMatrixMultiplyInvalidInput():
    matrix_A = [[1, 'a', 3], [4, 5, 6]]
    matrix_B = [[7, 8], [9, 10], [11, 12]]
    result = MatrixMult(matrix_A, matrix_B)
    assert isinstance(result, str)

def testMatrixMultiplyInvalidDimensions():
    matrix_A = [[1, 2, 3], [4, 5, 6]]
    matrix_C = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = MatrixMult(matrix_A, matrix_C)
    assert isinstance(result, str)
