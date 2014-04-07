'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        y0, y1 = 0, 1
        while int(y0) != int(y1):
            y0 = y1
            y1 = 1.0/2.0 * (y0 + x / y0)
        return int(y0)
    
