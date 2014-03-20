'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i > 0 and dp[i-1][j] and s3[i+j-1] == s1[i-1]:
                    dp[i][j] = True
                elif j > 0 and dp[i][j-1] and s3[i+j-1] == s2[j-1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        return dp[len(s1)][len(s2)]
                