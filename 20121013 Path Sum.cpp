/*
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
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
    bool hasPathSum(TreeNode *root, int sum) {
        return root && dfs(root, 0, sum) ;
    }
    bool dfs(TreeNode *node, int now, int sum) {
        if (node ->left == NULL && node->right == NULL)
            return now + node->val == sum ;
        if (node->left && dfs(node->left, now + node->val, sum)) return true;
        if (node->right && dfs(node->right, now + node->val, sum)) return true;
        return false;
    }
};