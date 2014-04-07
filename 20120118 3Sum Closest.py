'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        ans = None
        for i in range(len(num)):
            l, r = i + 1, len(num) - 1
            while (l < r):                    
                sum = num[l] + num[r] + num[i]
                if ans is None or abs(sum- target) < abs(ans - target):
                    ans = sum
                if sum <= target:
                    l = l + 1
                else:
                    r = r - 1
        return ans
    