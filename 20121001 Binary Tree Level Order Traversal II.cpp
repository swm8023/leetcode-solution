/*
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7]
  [9,20],
  [3],
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
    vector<vector<int> > vec;
    vector<vector<int> > levelOrderBottom(TreeNode *root) {
        vec.clear();
        dfs(root, 0, vec);
        reverse(vec.begin(), vec.end());
        return vec;
    }
    void dfs(TreeNode *root, int dep, vector<vector<int> > &vec) {
        if (root == NULL) return;
        if (vec.size() <= dep) vec.push_back(vector<int>());
        vec[dep].push_back(root->val);
        dfs(root->left, dep+1, vec);
        dfs(root->right, dep+1, vec);
    }
};