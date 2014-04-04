'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
'''
class Solution:
    # @return an integer
    def reverse(self, x):
        a = 0
        b = x if x > 0 else -x
        while b:
            a, b = a * 10 + b % 10, b / 10 
        return a if x > 0 else -a