import numpy as np

def generate_matrix(val, row, col, n):
    matrix = np.zeros((n,n));
    for i in range(len(val)):
        matrix[row[i] - 1, col[i] - 1] = val[i]
    return matrix

def multiply_vector(v1, v2):
    result = 0
    n = v1.shape[0]
    for i in range(n):
        result += v1[i] * v2[i]
    return result

def brute_matrix_mult(matrix1, matrix2):
    # dimension of the square matrix
    n = matrix1.shape[0]
    
    matrix = np.zeros((n,n))
    
    for i in range(n):
        for j in range(n):
            matrix[i,j] = multiply_vector(matrix1[i,:], matrix2[:, j])
    
    return matrix
    
matrix1 = np.array([[4,1,0,0],[0,4,1,0],[0,1,4,0],[0,0,1,4]])
matrix2 = np.array([[25,3,0,1],[0,1,2,0],[1,0,0,0],[0,1,4,0]])
print brute_matrix_mult(matrix1, matrix2)