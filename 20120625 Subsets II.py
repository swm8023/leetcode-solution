'''
Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        bset = []
        for x in range(2**len(S)):
            for i in range(1, len(S)):
                if (S[i] == S[i-1] and (x>>(i-1)&0x03 == 0x01)): break
            else:
                bset.append(x)
        return [[S[x] for x in range(len(S)) if i>>x&1] for i in bset]

S = []
s = Solution()
print s.subsetsWithDup(S)
