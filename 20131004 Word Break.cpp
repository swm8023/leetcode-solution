class Solution {
public:
    bool wordBreak(string s, unordered_set<string> &dict) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        vector<vector<int> > dp(s.length(), vector<int>(s.length(), -1));
        return dpit(dp, s, dict, 0, s.length() - 1);
    }
    bool dpit(vector<vector<int> > &dp, string &s, unordered_set<string> &dict, int l, int r) {
        if (dp[l][r] != -1) return dp[l][r];
        if (dict.find(s.substr(l, r - l + 1)) != dict.end()) return dp[l][r] = 1;
        for (int i = l; i < r; i++) {
            if (dpit(dp, s, dict, l, i) && dpit(dp, s, dict, i+1, r))
                return dp[l][r] = 1;
        }
        return dp[l][r] = 0;
    }
};
