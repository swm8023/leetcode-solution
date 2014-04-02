'''
Implement pow(x, n).
'''
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1
        xx = pow(x, n >> 1)
        xx *= xx
        if n & 1: xx *= x
        return xx