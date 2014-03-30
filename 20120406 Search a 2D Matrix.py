'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''
class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        l, h = 0, len(matrix) * len(matrix[0]) - 1
        while (l <= h):
            m = l + ((h-l) >> 2)
            v =  matrix[m/len(matrix[0])][m%len(matrix[0])]
            if v < target:
                l = m + 1
            elif v > target:
                h = m - 1
            else:
                return True
        return False
    

              