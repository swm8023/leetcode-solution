'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
'''

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        ans, lenh, stk = 0, len(height), []
        for i in range(lenh + 1):
            while len(stk) and (i == lenh or height[stk[-1]] >= height[i]):
                top = stk.pop()
                if len(stk) == 0:
                    ans = max(ans, height[top] * i)
                else:
                    ans = max(ans, height[top] * (i - stk[-1] - 1))
            stk.append(i)
        return ans
