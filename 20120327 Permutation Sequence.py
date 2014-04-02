'''
The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
'''

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        d, ans, use = [0, 1], [], ['0'] * n
        for i in range(2, 10) : d.append( i * d[-1])
        for i in range(n):
            ans.append(0)
            for j in range(n):
                if use[j] == 1:
                    continue;
                ans[i] = chr(ord('0') + j + 1)
                if k <= d[n-i-1]:
                    use[j] = 1
                    break
                k -= d[n-i-1]
        return ''.join(ans)
        