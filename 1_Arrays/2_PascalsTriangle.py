#2
""" 
LEETCODE: 118- Pascals Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above

Example1
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
[[1],
 [1,1],
 [1,2,1],
 [1,3,3,1],
 [1,4,6,4,1]]
Example2
Input: numRows = 1
Output: [[1]]
"""
"""
APPROACH:
1. Initialize each row with ones, keep increementing the counter in every iteration.
2. Current number will be addition previous rows digits:
    row[j] = triangle[i-1][j-1] + triangle[i-1][j]
"""

def generate(numRows):   
    # complexity On^2
    triangle = []

    for i in range(numRows):
        row = [1] * (i+1)

        for j in range(1,i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        triangle.append(row)

    return triangle

numRows = 5
result = generate(numRows)
print(result)