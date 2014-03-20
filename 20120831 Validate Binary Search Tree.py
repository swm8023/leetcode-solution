class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    val = None
    def isValidBST(self, root):
        if root is None: 
            return True
        res = self.isValidBST(root.left)
        if self.val is None:
            self.val = root.val
        else:
            res = res and (root.val > self.val)
            self.val = root.val
        res = res and self.isValidBST(root.right)
        return res
