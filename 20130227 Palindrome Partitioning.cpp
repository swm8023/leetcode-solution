/*
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]

*/

class Solution {
public:
    vector<vector<string> > vecResult;
    vector<vector<string> > partition(string s) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        vecResult.clear();
        vector<string> vecStr;
        vector<vector<string> > parStart(s.length());
        for (int i = 0; i < s.length(); i++) {
            for (int j = i; 2*i-j < s.length() && j >= 0 && s[j] == s[2*i-j]; j--)
                parStart[j].push_back(s.substr(j, 2*i-2*j+1));
            for (int j = i; 2*i-j+1 < s.length() && j >= 0 && s[j] == s[2*i-j+1]; j--)
                parStart[j].push_back(s.substr(j, 2*i-2*j+2));
        }
        dfs(parStart, vecStr, 0, s.length());
        return vecResult;
    }
    void dfs(vector<vector<string> > &parStart, vector<string> &vecStr, int sp, int ep) {
        if (sp == ep) {
            vecResult.push_back(vecStr);
        } else {
            for (int i = 0; i < parStart[sp].size(); i++) {
                vecStr.push_back(parStart[sp][i]);
                dfs(parStart, vecStr, sp + parStart[sp][i].length(), ep);
                vecStr.pop_back();
            }
        }
    }
};
