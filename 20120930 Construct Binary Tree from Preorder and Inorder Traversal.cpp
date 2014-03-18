/*
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
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
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        return build(0, preorder.size()-1, 0, inorder.size()-1, preorder, inorder);
    }
    TreeNode *build(int pl, int pr, int il, int ir, vector<int> &pvec, vector<int> &ivec) {
        if (pl > pr) return NULL;
        TreeNode *node = new TreeNode(pvec[pl]);
        int ip;
        for (ip = il; ip <= ir; ip++) {
            if (ivec[ip] == pvec[pl]) break;
        }
        if (il<=ip-1) node->left = build(pl+1, pl+ip-il, il, ip-1, pvec, ivec);
        if (ip+1<=ir) node->right = build(pl+ip-il+1, pr, ip+1, ir, pvec, ivec);
        return node;
    }
};