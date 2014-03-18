/*
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
*/

class Solution {
public:
    int numTrees(int n) {
        int *dp = new int[n+1];
        for (int i = 0; i <= n; i++)
            dp[i] = (i <= 1 ? 1 : -1);
        return dpit(dp, n);
    }
    int dpit(int dp[], int n) {
        if (dp[n] != -1) return dp[n];
        dp[n] = 0;
        for (int i = 0; i < n; i++)
            dp[n] += dpit(dp, i) * dpit(dp, n-i-1);
        return dp[n];
    }
};