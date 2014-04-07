'''
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
'''

class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        l, h = 0, len(A) - 1
        while (l <= h):
            m = l + ((h - l) >> 1)
            if A[m] == target:
                return True
            if A[m] == A[l] and A[m] == A[h]:
                l, h = l + 1, h - 1
            elif (A[m] > A[l] and target < A[m] and target >= A[l]) or (A[m] < A[l] and not (target <= A[h] and target > A[m])):
                h = m - 1
            else:
                l = m + 1
        return False