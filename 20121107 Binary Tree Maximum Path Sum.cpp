/*
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
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
    int maxPathSum(TreeNode *root) {
        int ans = root->val;
        dfsTree(root, ans);
        return ans;
    }
    int dfsTree(TreeNode *fa, int &ans) {
        if (fa == NULL) return 0;
        int tmp = fa->val, lmax, rmax;
        if ((lmax = dfsTree(fa->left, ans)) > 0) tmp += lmax;
        if ((rmax = dfsTree(fa->right, ans)) > 0) tmp += rmax;
        ans = max(ans, tmp);
        return max(fa->val, max(fa->val+lmax, fa->val+rmax));
    }
};
