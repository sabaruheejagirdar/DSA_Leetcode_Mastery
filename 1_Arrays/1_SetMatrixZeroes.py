# 01
""" 
LEETCODE: 73- Set Matrix Zeroes
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

TC:O(2*N*M)
SC: O(N) + O(M)

1   1   1           1    0    1
1   0   1    =>     0    0    0
1   1   1           1    0    1

Example1
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example2
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""
"""
APPROACH:
1.  To the matrix, create and extra row and column, initialize it with 0's,
    Update it to "1" if atleast one zero is found in respective row/ column
2.  Finally mark arr[i][j] = 0 if row[i] or col[j] is marked with "1"
"""

def zeroMatrix(matrix):     
    n = len(matrix) #row count
    m = len(matrix[0]) #col count

    row = [0] * n
    col = [0] * m

    #Traverse the matrix:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # mark ith index of row with 1
                row[i] = 1
                # mark jth index of col with 1
                col[j] = 1

    # Finally mark arr[i][j] = 0 if row[i] or col[j] is marked with "1"
    for i in range(n):
        for j in range(m):
            if row[i] == 1 or col[j]==1:
                matrix[i][j] = 0

    return matrix

# matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
result = zeroMatrix(matrix)
print(result)