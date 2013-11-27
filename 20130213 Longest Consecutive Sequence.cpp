 /*
 Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
*/

class Solution {
public:
    int longestConsecutive(vector<int> &num) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        unordered_set<int> uset;
        for (int i = 0; i < num.size(); i++)
            uset.insert(num[i]);
        int ans = 0, tmpAns = 0, now, nowb;
        while (!uset.empty()) {
            now = *uset.begin(), tmpAns = 1;
            uset.erase(now);
            for (nowb = now + 1; uset.count(nowb); uset.erase(nowb), tmpAns++, nowb++);
            for (nowb = now - 1; uset.count(nowb); uset.erase(nowb), tmpAns++, nowb--);
            if (tmpAns > ans) ans = tmpAns;
        }
        return ans;
    }
};
