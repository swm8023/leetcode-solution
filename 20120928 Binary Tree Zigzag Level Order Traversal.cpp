/*
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.


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
    vector<vector<int> > zigzagLevelOrder(TreeNode *root) {
        vec.clear();
        dfs(root, 0, vec);
        for (int i = 1; i < vec.size(); i += 2)
            reverse(vec[i].begin(), vec[i].end());
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