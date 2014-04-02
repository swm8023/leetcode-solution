'''
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2,... , ak) must be in non-descending order.
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 
'''

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        self.ans, tmp = [], []
        self.dfs(candidates, target, 0, 0, tmp)
        return self.ans
    
    def dfs(self, candidates, target, p, now, tmp):
        if now == target:
            self.ans.append(tmp[:])
            return
        for i in range(p, len(candidates)):
            if now + candidates[i] <= target:
                tmp.append(candidates[i])
                self.dfs(candidates, target, i, now+candidates[i], tmp)
                tmp.pop()

        