 /*
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
*/

class Solution {
public:
    int ladderLength(string start, string end, unordered_set<string> &dict) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        queue<string> q;
        unordered_map<string, int> vis;
        int len = start.length();
        q.push(start);
        vis[start] = 1;
        while (!q.empty()) {
            string s = q.front(); q.pop();
            int step = vis[s];
            for (int i = 0; i < len; i++) {
                string news = s;
                for (char c = 'a'; c <= 'z'; c++) {
                    if (s[i] == c) continue;
                    news[i] = c;
                    if (news == end) return step + 1;
                    if (dict.count(news) && !vis[news]) {
                        vis[news] = step + 1;
                        q.push(news);
                    }
                }
            }
        }
        return 0;
    }
};
