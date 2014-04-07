'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        L = len(A)
        for i in range(L):
            while A[i] > 0 and A[i] <= L and A[i] != A[A[i] - 1] and i != A[i] - 1:
                A[A[i] - 1], A[i] = A[i], A[A[i] - 1]
                #A[i], A[A[i] - 1] = A[A[i] - 1], A[i]  dosen't work
        for i in range(L):
            if i != A[i] - 1:
                return i + 1
        return L + 1