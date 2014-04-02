'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
'''
class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        num1 = [ord(i) - ord('0') for i in num1][::-1]
        num2 = [ord(i) - ord('0') for i in num2][::-1]
        ans = [0] * (len(num1) + len(num2) + 1)
        for i in range(len(num1)):
            for j in range(len(num2)):
                ans[i + j] += num1[i] * num2[j]
                ans[i + j + 1] += ans[i + j]
                #ans[i + j]
        while len(ans) > 1 and ans[len(ans) - 1] == 0:
            ans.pop()
        return ''.join([chr(i + ord('0')) for i in ans][::-1])
    