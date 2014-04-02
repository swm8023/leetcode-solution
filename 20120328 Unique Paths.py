'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        g = [[0] * n for i in range(m)]
        for i in range(m): g[i][0] = 1
        for j in range(n): g[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                g[i][j] = g[i][j-1] + g[i-1][j]
        return g[m-1][n-1]