'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        maxl, maxr, maxv, ans = [], [], 0, 0
        for i in range(len(A)):
            if A[i] > maxv: maxv = A[i]
            maxl.append(maxv)
        maxv = 0
        for i in range(len(A)-1, -1, -1):
            if A[i] > maxv: maxv = A[i]
            maxr.append(maxv)
        for i in range(len(A)):
            minh = min(maxl[i], maxr[len(A) - i - 1]) - A[i]
            ans += minh if minh > 0 else 0
        return ans
    
s = Solution()
print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
            