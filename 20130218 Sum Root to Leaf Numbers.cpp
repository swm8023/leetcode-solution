 /*

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3

The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
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
    int sumNumbers(TreeNode *root) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int ans = 0;
        if (!root) return 0;
        dfsTree(root, root->val, ans);
        return ans;
    }
    void dfsTree(TreeNode *fa, int now, int &ans) {
        if (!(fa->left || fa->right)) ans += now;
        else {
            if (fa->left) dfsTree(fa->left, now*10+fa->left->val, ans);
            if (fa->right)dfsTree(fa->right,now*10+fa->right->val,ans);
        }
    }
};
