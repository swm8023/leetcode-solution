'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if len(A) == 0:
            return False
        maxj = A[0]
        for i in range(1, len(A)):
            maxj -= 1
            if (maxj < 0):
                return False
            maxj = max(maxj, A[i])
        return True
            