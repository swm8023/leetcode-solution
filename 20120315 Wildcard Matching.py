'''
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "*") -> true
isMatch("aa", "a*") -> true
isMatch("ab", "?*") -> true
isMatch("aab", "c*a*b") -> false
'''

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        ps, pp, lastp, lasts = 0, 0, -1, -1
        while ps < len(s):
            if pp < len(p) and (s[ps] == p[pp] or p[pp] == '?'):
                ps, pp = ps + 1, pp + 1
            elif pp < len(p) and p[pp] == '*':
                pp = pp + 1
                lastp, lasts = pp, ps
            elif lastp != -1:
                lasts = lasts + 1
                pp, ps = lastp, lasts
            else:
                return False
        while pp < len(p) and p[pp] == '*':
            pp = pp + 1
        return ps == len(s) and pp == len(p)
            

