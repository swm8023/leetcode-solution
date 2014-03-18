/*
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
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
    bool isBalanced(TreeNode *root) {
        bool ans = true;
        dfs(root, ans);
        return ans;

    }
    int dfs(TreeNode *root, bool &ans) {
        if (!root) return 0;
        int ltval = dfs(root->left, ans);
        int rtval = dfs(root->right, ans);
        if (!(ltval - rtval <= 1 && ltval - rtval >= -1))
            ans = false;
        return max(ltval, rtval) + 1;
    }
};