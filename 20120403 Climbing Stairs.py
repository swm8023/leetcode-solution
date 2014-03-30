'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        f = [1, 1]
        while len(f) <= n:
            f.append(f[-1] + f[-2])
        return f[n]