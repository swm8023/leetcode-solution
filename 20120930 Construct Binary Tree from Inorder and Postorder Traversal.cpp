/*
Given inorder and postorder traversal of a tree, construct the binary tree.

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
    TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) {
        return build(0, inorder.size()-1, 0, postorder.size()-1, inorder, postorder);
    }
    TreeNode *build(int il, int ir, int pl, int pr, vector<int> &ivec, vector<int> &pvec) {
        if (pl > pr) return NULL;
        TreeNode *node = new TreeNode(pvec[pr]);
        int ip;
        for (ip = il; ip <= ir; ip++) {
            if (ivec[ip] == pvec[pr]) break;
        }
        if (il<=ip-1) node->left = build(il, ip-1, pl, pl+ip-il-1, ivec, pvec);
        if (ip+1<=ir) node->right = build(ip+1, ir, pl+ip-il, pr-1, ivec, pvec);
        return node;
    }
};