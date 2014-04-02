'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example given the array [-2,1,-3,4,-1,2,1,-5,4]
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        ans, sum = A[0], A[0]
        for i in range(1, len(A)):
            if (sum < 0):
                sum = A[i]
            else:
                sum += A[i]
            ans = max(ans, sum)
        return ans
        