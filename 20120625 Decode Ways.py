'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        dp = [1] + [0] * len(s)
        ok = lambda x: x[0] != '0' and  int(x) >= 1 and int(x) <= 26;
        for i in range(1, len(s) + 1):
            dp[i] = dp[i-1] if ok(s[i-1:i]) else 0
            if i >= 2:
                dp[i]+= dp[i-2] if ok(s[i-2:i]) else 0
        return dp[len(s)]

s = Solution()
print s.numDecodings("23")
