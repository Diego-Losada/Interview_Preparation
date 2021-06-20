#Reference: https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/chapter_01/p07_rotate_matrix.py

def rotateMatrix(matrix):
    n = len(matrix)
    arr = [[0]*n for i in range(n)]
    for i,j in zip(range(n), range(n-1,-1,-1)):
        for k in range(n):
            arr[k][i] = matrix[j][k]
    print(arr)
    return arr
             


print(rotateMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]) ==
      [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]])
