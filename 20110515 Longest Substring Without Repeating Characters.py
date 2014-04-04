'''
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
'''
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        dict, ans, p1, p2 = {}, 0, 0, 0
        while p2 < len(s):
            p = dict.get(s[p2], None)
            if p == None:
                dict[s[p2]] = p2
                p2 += 1
                ans = max(ans, p2 - p1)
            else:
                while p1 <= p: 
                    dict.pop(s[p1])
                    p1 += 1
                p1 = p + 1
        return ans
        
        
