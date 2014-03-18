/*
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
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
    TreeNode *sortedArrayToBST(vector<int> &num) {
        return dfs(0, num.size()-1, num);
    }
    TreeNode *dfs(int left, int right, vector<int> &num) {
        if (left > right) return NULL;
        int mid = (left + right) >> 1;
        TreeNode *node = new TreeNode(num[mid]);
        node->left = dfs(left, mid-1, num);
        node->right = dfs(mid+1, right, num);
        return node;
    }
};