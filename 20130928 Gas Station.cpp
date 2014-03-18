/*
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
*/

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
