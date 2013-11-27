/*
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
*/
class Solution {
public:
    int minCut(string s) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        vector<vector<bool> > isPar(s.length(), vector<bool>(s.length(), false));
        vector<int> minC(s.length(), 0);
        for (int i = 0; i < s.length(); i++) {
            minC[i] = i + 1;
            for (int j = 0; j <= i; j++) {
                if ((j + 2 > i || isPar[j+1][i-1]) && s[j] == s[i]) {
                    isPar[j][i] = true;
                    minC[i] = min(minC[i], j ? (minC[j-1] + 1) : 1);
                }
            }
        }
        return minC[s.length() - 1] - 1;
    }
};
