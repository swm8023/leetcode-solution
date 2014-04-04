'''
Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.
'''

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return [""]
        self.dglist = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.ans, tmp = [], []
        self.dfs(digits, 0, tmp)
        return self.ans
    
    def dfs(self, digits, p, tmp):
        if (p == len(digits)):
            self.ans.append(''.join(tmp))
            return
        for c in self.dglist[ord(digits[p]) - ord('0')]:
            tmp.append(c)
            self.dfs(digits, p + 1, tmp)
            tmp.pop()
    