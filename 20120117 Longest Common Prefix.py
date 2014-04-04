'''
Write a function to find the longest common prefix string amongst an array of strings.
'''
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) <= 1:
            return strs[0] if len(strs) == 1 else ""
        end, minl = 0, min([len(s) for s in strs])
        while end < minl:
            for i in range(1, len(strs)):
                if strs[i][end] != strs[i-1][end]:
                    return strs[0][:end]
            end = end + 1
        return strs[0][:end]