/*
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
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
    vector<int> vec;
    vector<int> inorderTraversal(TreeNode *root) {
        stack<TreeNode*> st;
        vec.clear();
        TreeNode *T = root;
        while (T || !st.empty()) {
            if (T) {
                st.push(T);
                T = T->left;
            } else {
                T = st.top(); st.pop();
                vec.push_back(T->val);
                T = T->right;
            }
        }
        return vec;
    }
};