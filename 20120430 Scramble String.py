'''
iven a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
'''

class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if len(s1) == 0:
            return True
        self.s1, self.s2 = s1, s2
        lens = len(s1)
        self.dp = [[[-1] * lens for i in range(lens)] * lens for i in range(lens)]
        return self.dfs(0, 0, len(s1))
    
    def dfs(self, lp, rp, len):
        if self.dp[lp][rp][len - 1] >= 0:
            return True if self.dp[lp][rp][len - 1] == 1 else False
        if len == 1:
            return self.s1[lp] == self.s2[rp]
        for i in range(1, len):
            if self.dfs(lp, rp, i) and self.dfs(lp + i, rp + i, len - i) \
                    or self.dfs(lp, rp + i, len - i) and self.dfs(lp + len - i, rp, i):
                self.dp[lp][rp][len - 1] = 1
                return True
        self.dp[lp][rp][len - 1] = 0 
        return False
        
        