/*
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
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
    vector<vector<int> > ans;
    vector<int> path;
    vector<vector<int> > pathSum(TreeNode *root, int sum) {
        ans.clear();
        path.clear();
        if (root) dfs(root, 0, sum) ;
        return ans;
    }
    void dfs(TreeNode *node, int now, int sum) {
        if (node ->left == NULL && node->right == NULL) {
            if (now + node->val == sum) {
                path.push_back(node->val);
                ans.push_back(path);
                path.pop_back();
            }
            return;
        }
        if (node->left) {
            path.push_back(node->val);
            dfs(node->left, now + node->val, sum);
            path.pop_back();
        }
        if (node->right) {
            path.push_back(node->val);
            dfs(node->right, now + node->val, sum);
            path.pop_back();
        }
    }
};