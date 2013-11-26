class Solution {
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int remain = 0, totgas = 0, startp = 0;
        for (int i = 0; i < gas.size(); i++) {
            remain += gas[i] - cost[i];
            totgas += gas[i] - cost[i];
            if (remain < 0) remain = 0, startp = i + 1;
        }
        startp %= gas.size();
        return totgas >= 0 ? startp : -1;
    }
};
