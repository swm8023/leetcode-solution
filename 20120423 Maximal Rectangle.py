'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
'''
class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if len(matrix) == 0:
            return 0
        ans = 0;
        for i in range(len(matrix)):
            stk = []
            for j in range(len(matrix[0]) + 1):
                if j < len(matrix[0]): matrix[i][j] = int(matrix[i][j])
                if i > 0 and j < len(matrix[0]) and matrix[i][j]:
                    matrix[i][j] += matrix[i-1][j]
                while len(stk) and (j == len(matrix[0]) or matrix[i][stk[-1]] >= matrix[i][j]):
                    top = stk.pop()
                    if len(stk) == 0:
                        ans = max(ans, matrix[i][top]*j)
                    else:
                        ans = max(ans, matrix[i][top]*(j-stk[-1]-1))
                stk.append(j)
        return ans
                       