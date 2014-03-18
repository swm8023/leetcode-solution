/*
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
*/
class Solution {
public:
    int numDistinct(string S, string T) {
        int lent = T.length(), lens = S.length();
        vector<vector<int> > dp(lent+1, vector<int>(lens+1, 0));
        for (int i = 0; i <= lens; i++) dp[0][i] = 1;
        for (int i = 1; i <= lent; i++) {
            for (int j = 1; j <= lens; j++) {
                dp[i][j] = dp[i][j-1];
                if (S[j-1] == T[i-1])
                    dp[i][j] += dp[i-1][j-1];
            }
        }
        return dp[lent][lens];
    }
};