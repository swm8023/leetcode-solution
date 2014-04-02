'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        return [self.lower_bound(A, target), self.upper_bound(A, target)]
    
    def lower_bound(self, A, target):
        l, h, m = 0, len(A), 0
        while l < h:
            m = (l + h) >> 1
            if A[m] < target:
                l = m + 1
            else:
                h = m
        return l if l < len(A) and A[l] == target else -1
            
        
    def upper_bound(self, A, target):
        l, h, m = 0, len(A),  0
        while l < h:
            m = (l + h) >> 1
            if A[m] <= target:
                l = m + 1
            else:
                h = m
        return l-1 if l-1 < len(A) and A[l-1] == target else -1
        
        
        