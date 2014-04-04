'''
Implement strStr().
Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.
'''
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        lenh, lenn = len(haystack), len(needle)
        if lenn == 0:
            return haystack
        next, p = [-1] * (lenn), -1
        for i in range(1, lenn):
            while p >= 0 and needle[i] != needle[p + 1]:
                p = next[p]
            if needle[i] == needle[p + 1]:
                p  = p + 1
            next[i] = p
        p = -1
        for i in range(lenh):
            while p >= 0 and haystack[i] != needle[p + 1]:
                p = next[p]
            if haystack[i] == needle[p + 1]:
                p = p + 1
            if p + 1 == lenn:
                return haystack[i - p:] 
        return None
            