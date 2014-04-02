'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        l, h = 0, len(A) - 1
        while (l <= h):
            m = l + ((h - l) >> 1)
            if A[m] == target:
                return m
            elif (A[m] > A[l] and target < A[m] and target >= A[l]) or (A[m] < A[l] and not (target <= A[h] and target > A[m])):
                h = m - 1
            else:
                l = m + 1
        return -1 
