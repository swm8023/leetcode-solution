'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
'''
class Solution:
    # @return an integer
    def maxArea(self, height):
        l, r, ans = 0, len(height) - 1, 0
        while l <= r:
            ans = max(ans, (r - l) * min(height[r], height[l]))
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
        return ans
        