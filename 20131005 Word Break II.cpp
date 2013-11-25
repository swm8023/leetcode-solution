class Solution {
public:
    vector<string> strRes;
    vector<int> seqRes;
    vector<string> setVec;
    vector<string> wordBreak(string s, unordered_set<string> &dict) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.

        unordered_set<string>::iterator iter;
        vector<vector<int> > dp(s.length(), vector<int>(s.length(), -1));
        setVec.clear();
        strRes.clear();
        seqRes.clear();
        for (iter = dict.begin(); iter != dict.end(); iter++) {
            setVec.push_back(*iter);
            int pos = 0;
            while ((pos = s.find(*iter, pos)) != string::npos)
                dp[pos][pos+(*iter).length()-1] = setVec.size(), pos ++;
        }
        dpit(dp, 0, s.length() - 1);
        dfs_result(dp, 0, s.length()-1);
        return strRes;
    }
    void dfs_result(vector<vector<int> > &dp, int s, int e) {
        if (s > e) {
            string s;
            for (int i = 0; i < seqRes.size(); i++) {
                s.append(setVec[seqRes[i] - 1]);
                if (i != seqRes.size() - 1) s.append(" ");
            }
            strRes.push_back(s);
            return;
        }
        if (dp[s][e] == 0) return;
        for (int i = s; i <= e; i++) {
            if (dp[s][i] > 0) {
                seqRes.push_back(dp[s][i]);
                dfs_result(dp, i + 1, e);
                seqRes.pop_back();
            }
        }
    }
    int dpit(vector<vector<int> > &dp, int l, int r) {
        if (dp[l][r] != -1) return dp[l][r];
        for (int i = l; i < r; i++) {
            if (dpit(dp, l, i) && dpit(dp, i+1, r))
                return dp[l][r] = -2;
        }
        return dp[l][r] = 0;
    }
};
