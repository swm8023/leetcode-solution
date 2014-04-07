'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
The solution set must not contain duplicate triplets.
'''

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        dct, ans = {}, []
        for i in range(0, len(num)):
            if (i > 0 and num[i] == num[i-1]):
                continue
            l, r = i + 1, len(num) - 1
            while l < r:
                sum = num[l] + num[r] + num[i]
                if sum == 0:
                    ans.append([num[i], num[l], num[r]])
                    while l < r and num[l] == num[l + 1]: l = l + 1
                    while l < r and num[r] == num[r - 1]: r = r - 1
                    l, r = l + 1, r - 1
                elif sum < 0:
                    l = l + 1
                else:
                    r = r - 1   
        return ans

