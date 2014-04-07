/*
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <= b <= c <= d)
The solution set must not contain duplicate quadruplets.
For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

A solution set is:
(-1,  0, 0, 1)
(-2, -1, 1, 2)
(-2,  0, 0, 2)
*/
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int> > fourSum(vector<int> &num, int target) {
        vector<vector<int> > ans;
        sort(num.begin(), num.end());
        for (int i = 0; i < num.size(); i++) {
            if (i > 0 && num[i] == num[i-1]) continue;
            for (int j = i + 1; j < num.size(); j++) {
                if (j > i + 1 && num[j] == num[j - 1]) continue;
                int l = j + 1, r = num.size() - 1;
                while (l < r) {
                    int sum = num[i] + num[j] + num[l] + num[r];
                    if (sum == target) {
                        ans.push_back({num[i], num[j], num[l], num[r]});
                        while (l < r && num[l] == num[l + 1]) l++; l++;
                        while (l < r && num[r] == num[r - 1]) r--; r--;
                    } else if (sum < target) {
                        l++;
                    } else {
                        r--;
                    }
                }
             }
        }
        return ans;
    }
};
