'''
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.
'''
class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        ans, p, plen = [], 0, 0
        for i in range(len(words)):
            if plen + len(words[i]) + i - p - 1 >= L:
                spc = (L - plen) // (i - p - 1) if i - p > 1 else 0
                sps = (L - plen - spc * (i - p - 1))
                str = words[p]
                for j in range(p + 1, i):
                    if sps > 0:
                        str += ' '
                        sps -= 1
                    str += ' ' * spc + words[j] 
                ans.append(str + ' ' * (L - plen))
                plen, p = 0, i
            if i < len(words):
                plen += len(words[i])
        str = ''
        while p < len(words):
            str += words[p]
            if len(str) < L:
                str += ' '
            p = p + 1
        ans.append(str + ' ' * (L - len(str))) 
        return ans
                    
s = Solution()
print s.fullJustify(["a","b","c","d","e"], 3)
print s.fullJustify(["Here","is","an","example","of","text","justification."], 14)
print s.fullJustify(["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."], 30)
            
        