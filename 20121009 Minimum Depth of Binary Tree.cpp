/*
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
*/
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int minDepth(TreeNode *root) {
        if (!root) return 0;
        if (!root->left && !root->right) return 1;
        int ltval = -1, rtval = -1;
        if (root->left) ltval = minDepth(root->left);
        if (root->right) rtval = minDepth(root->right);
        return 1+ (ltval == -1 ? rtval : (rtval == -1 ? ltval : min(ltval, rtval)));
    }
};