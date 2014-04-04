'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution:
    # @return a boolean
    def isValid(self, s):
        dct = {'(':')', '[':']', '{':'}'}
        stk = []
        for c in s:
            if dct.get(c, None):
                stk.append(c)
            elif len(stk) == 0 or dct[stk[-1]] != c:
                return False
            else:
                stk.pop()
        return True if len(stk) == 0 else False
                