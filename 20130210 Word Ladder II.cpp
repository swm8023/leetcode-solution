 /*
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
*/

class Solution {
public:
    vector<vector<string> > ans;
    vector<vector<string> > findLadders(string start, string end, unordered_set<string> &dict) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        dict.insert(end);
        int dsize = dict.size(), len = start.length();
        unordered_map<string, vector<string> > next;
        unordered_map<string, int> vis;
        queue<string> q;
        vector<string> path;
        ans.clear();
        q.push(start);
        vis[start] = 0;
        while (!q.empty()) {
            string s = q.front(); q.pop();
            if (s == end) break;
            int step = vis[s];
            vector<string> snext;
            for (int i = 0; i < len; i++) {
                string news = s;
                for (char c = 'a'; c <= 'z'; c++) {
                    news[i] = c;
                    if (c == s[i] || dict.find(news) == dict.end()) continue;
                    auto it = vis.find(news);
                    if (it == vis.end()) {
                        q.push(news);
                        vis[news] = step + 1;
                    }
                    snext.push_back(news);
                }
            }
            next[s] = snext;
        }
        path.push_back(start);
        dfspath(path, next, vis, start, end);
        return ans;
    }
    void dfspath(vector<string> &path,  unordered_map<string, vector<string> > &next,
                 unordered_map<string, int> &vis, string now, string end){
       //cout << now << endl;
        if (now == end) ans.push_back(path);
        else {
            auto vec = next[now];
            int visn = vis[now];
            for (int i = 0; i < vec.size(); i++) {
                if (vis[vec[i]] != visn + 1) continue;
                path.push_back(vec[i]);
                dfspath(path, next, vis, vec[i], end);
                path.pop_back();
            }
        }
    }
};
