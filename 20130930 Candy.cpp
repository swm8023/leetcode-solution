/*
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
*/
class Solution {
public:
    int candy(vector<int> &ratings) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int size = ratings.size(), ans = 0;
        if (size == 1) return 1;
        vector<int> candies(size, 1);
        for (int i = 0; i < size; i++) {
            if (i == 0 && ratings[i] <= ratings[i + 1] ||
                i == size - 1 && ratings[i] <= ratings[i - 1] ||
                ratings[i] <= ratings[i + 1] && ratings[i] <= ratings[i - 1]) {
                for (int j = i - 1; j >=0 && ratings[j] > ratings[j + 1]; j--)
                    candies[j] = max(candies[j], candies[j + 1] + 1);
                for (int j = i + 1; j < size && ratings[j] > ratings[j - 1]; j++)
                    candies[j] = max(candies[j], candies[j - 1] + 1);
            }
        }
        //for (int i = 0; i < size; i++) printf("%d ", candies[i]);
        for (int i = 0; i < size; i++) ans += candies[i];
        return ans;
    }
};
