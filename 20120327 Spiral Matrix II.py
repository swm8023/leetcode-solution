'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        a = [[0] * n for i in range(n)]
        sx, sy = 0, 0
        dx, dy, dn = [0, 1, 0, -1], [1, 0, -1, 0], 0
        for i in range(n * n):
            a[sx][sy] = i + 1
            nx, ny = sx + dx[dn], sy + dy[dn]
            if nx < 0 or nx < 0 or nx >= n or ny >= n or a[nx][ny]:
                dn = (dn + 1) % 4
                nx, ny = sx + dx[dn], sy + dy[dn]
            sx, sy = nx, ny
        return a
