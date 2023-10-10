def transpose_matrix(matrix):
    nRows = len(matrix) 
    nCols = len(matrix[0])

    tMatrix = [[0 for j in range(0,nRows)] for i in range(0,nCols)]

    for j in range(0,nCols):
        for i in range(0,nRows):
            tMatrix[j][i] = matrix[i][j]
    return tMatrix