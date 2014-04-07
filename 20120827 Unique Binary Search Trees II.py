class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    treelist = None
    def generateTrees(self, n):
        return self.dfs(0, n)
    
    def dfs(self, l, r):
        ans = []
        if l == r:
            ans.append(None)
            return ans
        for i in range(l, r):
            lb, rb = self.dfs(l, i), self.dfs(i + 1, r)
            for lc in lb:
                for rc in rb:
                    node = TreeNode(i + 1)
                    node.left = lc
                    node.right = rc
                    ans.append(node)
        return ans

