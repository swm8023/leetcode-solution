'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''

class Solution:
    # @return a string
    def countAndSay(self, n):
        s, now = [str(1), ''], 0
        for i in range(1, n):
            now, pre, tot = now^1, now, 0
            s[now], p = "", 0
            while p  < len(s[pre]):
                tot, v, p = 1, s[pre][p], p + 1
                while p < len(s[pre]) and v == s[pre][p]:
                    p += 1
                    tot += 1
                s[now] += str(tot) +  v
        return s[now]
