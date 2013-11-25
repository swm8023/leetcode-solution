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
    vector<int> postorderTraversal(TreeNode *root) {
        stack<TreeNode*> st;
        vec.clear();
        TreeNode *T = root, *last = NULL;
        while (T || !st.empty()) {
            if (T) {
                st.push(T);
                T = T->left;
            } else {
                T = st.top();
                if ((!T->left && !T->right) || (T->left == last && !T->right)
                    || (T->right == last)) {
                    vec.push_back(T->val);
                    last = T, T = NULL;
                    st.pop();
                } else {
                    T = T->right;
                }
            }
        }
        return vec;
    }
};
