'''
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
'''

class Solution:
    # @return a list of integers
    def grayCode(self, n):
        self.res = [0]
        for i in [2**x for x in range(0, n)]:
            self.res.append(self.res[-1] + i)
            self.res.extend([i + v for v in self.res[-3:None:-1]])
        return self.res;
    
s = Solution()
print s.grayCode(3)