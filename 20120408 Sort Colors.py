'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
'''

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        s, t, e = 0, 0, len(A) - 1
        while s <= e:
            if A[s] == 0:
                if s != t:
                    A[s], A[t] = A[t], A[s]
                s, t = s + 1, t + 1
            elif A[s] == 1:
                s = s + 1
            elif A[s] == 2:
                if s != e:
                    A[s], A[e] = A[e], A[s]
                e = e - 1
        return A
                
                