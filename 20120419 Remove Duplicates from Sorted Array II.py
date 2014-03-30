'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
'''

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i = 2;
        while i < len(A):
            if A[i] == A[i-1] and A[i] == A[i - 2]:
                A.pop(i)
            else:
                i = i + 1 
        return len(A)
        