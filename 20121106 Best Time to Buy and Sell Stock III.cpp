/*
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).*/
class Solution {
public:
    int maxProfit(vector<int> &prices) {
        int size = prices.size(), ans = 0;
        if (size <= 1) return 0;
        vector<int> p(size, 0);
        int minv = prices[0], maxv;
        for (int i = 1; i < size; i++)
            p[i] = prices[i] - minv,
            minv = min(prices[i], minv);
        ans = max(ans, p[size-1]);
        minv = prices[size-1], maxv = 0;
        for (int i = size-2; i >= 0; i--)
            maxv = max(maxv, minv - prices[i]),
            ans = max(ans, p[i] + maxv),
            minv = max(prices[i], minv);
        return ans;
    }
};
