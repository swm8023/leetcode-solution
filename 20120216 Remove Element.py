'''
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        sz = 0
        for i in range(0, len(A)):
            if A[i] != elem:
                A[sz] = A[i]
                sz += 1
        return sz