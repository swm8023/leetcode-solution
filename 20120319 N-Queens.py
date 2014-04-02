'''
The n-queens puzzle is the problem of placing n queens on an n*n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
'''

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.ans, self.dt = [], {}
        self.full = ((1 << n) - 1)
        for i in range(n): self.dt[1<<i] = i
        tmp = [['.'] * n for i in range(n)]
        self.dfs(n, 0, 0, 0, 0, tmp)
        return self.ans
        
    def dfs(self, n, p, lt, rt, nt, tmp):
        if n == p:
            self.ans.append([''.join(s) for s in tmp])
            return
        can = (~(lt | rt | nt) & self.full)
        while can:
           now = can&-can
           tmp[p][self.dt[now]] = 'Q'
           self.dfs(n, p+1, (lt|now)>>1, (rt|now)<<1, nt|now, tmp)
           tmp[p][self.dt[now]] = '.'
           can -= now 
