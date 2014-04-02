'''
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.
'''

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        ans, dt = [], {}
        for i in range(len(strs)):
            lt = list(strs[i])
            lt.sort()
            s = ''.join(lt)
            d = dt.get(s, -2)
            if d == -2:
                dt[s] = i
            elif d == -1:
                ans.append(strs[i])
            else:
                ans.append(strs[i])
                ans.append(strs[d])
                dt[s] = -1
        return ans