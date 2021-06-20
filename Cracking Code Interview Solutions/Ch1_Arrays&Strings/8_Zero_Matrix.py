#[[1,2,3],
# [4,0,6],
# [7,8,9]

#O(n^2)
def zeroMatrix(matrix):
    row0 = set()
    col0 = set()
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if (matrix[i][j] == 0):
                row0.add(i)
                col0.add(j)

    for i in range(rows):
        for j in range(cols):
            if (i in row0 or j in col0):
                matrix[i][j] = 0

    return matrix
                
                



print(zeroMatrix([[1,2,3],[4,0,6],[7,8,9]]) == [[1,0,3],[0,0,0],[7,0,9]])
