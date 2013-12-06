/*
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

*/
class Solution {
public:
    vector<int> ans;
    vector<int> getRow(int rowIndex) {
        ans.resize(rowIndex + 1);
        ans[0] = 1;
        for (int i = 1; i <= rowIndex; i++)
            ans[i] = (long long)ans[i-1] * (rowIndex - i + 1) / i;
        return ans;
    }
};
