'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        num.sort()
        ans = [num[:]]
        while self.next_permutation(num):
            ans.append(num[:])
        return ans
    
    def next_permutation(self, num):
        for i in range(len(num)-2, -1, -1):
            if num[i] < num[i+1]:
                break
        else:
            return False

        for j in range(len(num)-1, i, -1):
            if num[j] > num[i]:
                num[i], num[j] = num[j], num[i]
                break
        for j in range(0, (len(num) - i)//2):
            num[i+j+1], num[len(num)-j-1] = num[len(num)-j-1], num[i+j+1] 
        return True