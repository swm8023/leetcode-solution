class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(cmp = lambda x, y: cmp(x.start, y.start) or (x.start == y.start and cmp(x.end,y.end)))
        ans, p, maxr = [], 0, 0
        for i in range(len(intervals) + 1):
            if i > 0 and (i == len(intervals) or intervals[i].start > maxr):
                ans.append(Interval(intervals[p].start, maxr))
                p = i
            if i < len(intervals):
                maxr = max(maxr, intervals[i].end)
        return ans
    
