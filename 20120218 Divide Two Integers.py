'''
Divide two integers without using multiplication, division and mod operator.
'''

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        flag, ans = 0, 0
        if dividend < 0:
            flag, dividend = flag^1, -dividend
        if divisor < 0:
            flag, divisor = flag^1, -divisor
        while dividend >= divisor:
            count, newDivisor = 1, divisor
            while newDivisor + newDivisor <= dividend:
                newDivisor = newDivisor + newDivisor
                count = count + count
            dividend -= newDivisor
            ans += count
        return ans if flag == 0 else -ans
    
    