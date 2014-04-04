'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        self.ans, tmp = [], []
        lb = 0
        self.dfs(lb, 0, n, tmp)
        return self.ans
    
    def dfs(self, lb, p, n, tmp):
        if p == n * 2:
            self.ans.append(''.join(tmp))
            return
        if lb < n:
            tmp.append('(')
            self.dfs(lb + 1, p + 1, n, tmp)
            tmp.pop()
        if p - lb < lb:
            tmp.append(')')
            self.dfs(lb, p + 1, n, tmp)
            tmp.pop()
