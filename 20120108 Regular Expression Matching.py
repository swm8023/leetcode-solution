'''
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "a*") -> true
isMatch("aa", ".*") -> true
isMatch("ab", ".*") -> true
isMatch("aab", "c*a*b") -> true
'''

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        s, p = ' ' + s, ' ' + p
        dp = [[False] * (len(p)) for i in range(len(s))]
        dp[0][0] = True
        ind = 2
        while ind < len(p) and p[ind] == '*':
            dp[0][ind], ind = True, ind + 2
        for i in range(1, len(s)):
            for j in range(1, len(p)):
                if (s[i] == p[j] or p[j] == '.') and dp[i-1][j-1]:
                    dp[i][j] = True
                if p[j] == '*' and (dp[i][j-2] or ((p[j-1] == '.' or p[j-1] == s[i]) and (dp[i-1][j-2] or dp[i-1][j]))):
                    dp[i][j] = True
        return dp[len(s) - 1][len(p) - 1]
            
s = Solution()
print s.isMatch("aa", "a")              # False
print s.isMatch("aa", "aa")             # True
print s.isMatch("aaa","aa")             # False
print s.isMatch("aa", "a*")             # True
print s.isMatch("aa", ".*")             # True
print s.isMatch("ab", ".*")             # True
print s.isMatch("aab", "c*a*b")         # True
print s.isMatch("aaa", "ab*a")          # Fasle
print s.isMatch("aaba", "ab*a*c*a")     # False
print s.isMatch("", ".*")               # True
print s.isMatch("bbab", "b*a*")         # False
print s.isMatch("aab", "b.*")           # False    
        
        
        