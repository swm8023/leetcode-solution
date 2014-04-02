'''
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
'''

class Solution:
    # @return an integer
    def totalNQueens(self, n):
        self.ans = 0
        self.full = ((1 << n) - 1)
        self.dfs(n, 0, 0, 0, 0)
        return self.ans
        
    def dfs(self, n, p, lt, rt, nt):
        if n == p:
            self.ans += 1
            return
        can = (~(lt | rt | nt) & self.full)
        while can:
           now = can&-can
           self.dfs(n, p+1, (lt|now)>>1, (rt|now)<<1, nt|now)
           can -= now 
