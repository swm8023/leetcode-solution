/*
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
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
    bool isSymmetric(TreeNode *root) {
        vector<TreeNode *> now, next;
        if (root) now.push_back(root);
        bool flag = true;
        while(now.size() > 0) {
            next.clear();
            int size = now.size();
            for (int l = 0, r = size - 1; l <= r; l++, r--) {
                if (!nodeeql(now[l]->left, now[r]->right) ||
                    !nodeeql(now[l]->right, now[r]->left))
                    flag = false;
            }
            if (!flag) break;
            for (int i = 0; i < size; i++) {
                if (now[i]->left) next.push_back(now[i]->left);
                if (now[i]->right)next.push_back(now[i]->right);
            }
            now = next;
        }
        return flag;
    }
    bool nodeeql(TreeNode *l1, TreeNode *l2) {
        if ((!l1 && l2) || (l1 && !l2)) return false;
        return !l1 && !l2 || l1->val == l2->val;
    }
};