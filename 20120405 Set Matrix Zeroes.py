'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if len(matrix) == 0:
            return
        lenn, lenm = len(matrix), len(matrix[0])
        x, y = None, None
        for i in range(lenn):
            for j in range(lenm):
                if matrix[i][j] != 0:
                    continue
                if x is not None:
                    matrix[x][j] = matrix[i][y] = 0
                else:
                    x, y = i, j
        if x is None:
            return
        for i in range(lenn):
            for j in range(lenm):
                if i == x or j == y:
                    continue
                if matrix[x][j] == 0 or matrix[i][y] == 0:
                    matrix[i][j] = 0
        for i in range(lenn):
            matrix[i][y] = 0
        for i in range(lenm):
            matrix[x][i] = 0

            