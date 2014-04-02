'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        a, ans, m, n = matrix, [], len(matrix), len(matrix[0])
        x = [[0] * n for i in range(m)]
        sx, sy = 0, 0
        dx, dy, dn = [0, 1, 0, -1], [1, 0, -1, 0], 0
        for i in range(m * n):
            ans.append(a[sx][sy])
            x[sx][sy] = 1
            nx, ny = sx + dx[dn], sy + dy[dn]
            if nx < 0 or nx < 0 or nx >= m or ny >= n or x[nx][ny]:
                dn = (dn + 1) % 4
                nx, ny = sx + dx[dn], sy + dy[dn]
            sx, sy = nx, ny
        return ans
