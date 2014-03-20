'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
'''
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join([word[::-1] for word in s[::-1].split()])

    


