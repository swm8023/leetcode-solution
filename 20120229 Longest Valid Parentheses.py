'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stk, p ,ans = [], [0] * len(s), 0
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(i)
            elif s[i] == ')':
                if len(stk) > 0:
                    p[i] = i - stk[-1] + 1
                    if i >= p[i] and p[i - p[i]]:
                        p[i] += p[i-p[i]]
                    ans = max(ans, p[i])
                    stk.pop()
        return ans
