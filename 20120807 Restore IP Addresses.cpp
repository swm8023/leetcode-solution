/*
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
*/
class Solution {
public:
    vector<string> ans;
    vector<string> restoreIpAddresses(string s) {
        ans.clear();
        dfs(ans, s, "", 0, 0);
        return ans;
    }
    void dfs(vector<string> &ans, string s, string str, int pos, int dep) {
        if (dep >= 4) {
            if (dep == 4 && pos == s.length()) ans.push_back(str);
        } else {
            for (int i = pos; i < s.length(); i++) {
                string sub = s.substr(pos, i-pos+1);
                if (sub.length() <= 3 && stoi(sub) >= 0 && stoi(sub) <= 255 &&
                    to_string(stoi(sub)) == sub) {
                    string common = (dep == 3 ? "": ".");
                    dfs(ans, s, str+sub+common, i+1, dep+1);
                }
            }
        }
    }
};