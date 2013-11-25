#include <vector>
#include <stack>
using namespace std;
class Solution {
public:
    vector<int> vec;
    vector<int> preorderTraversal(TreeNode *root) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        stack<TreeNode*> st;
        vec.clear();
        TreeNode *T = root;
        while (T || !st.empty()) {
            if (T) {
                vec.push_back(T->val);
                st.push(T);
                T = T->left;
            } else {
                T = st.top(); st.pop();
                T = T->right;
            }
        }
        return vec;
    }
};
