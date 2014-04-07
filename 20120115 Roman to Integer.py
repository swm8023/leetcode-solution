'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution:
    # @return an integer
    def romanToInt(self, s):
        roval = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roval[s[i]] < roval[s[i+1]]:
                ans -= roval[s[i]]
            else:
                ans += roval[s[i]]
        return ans
