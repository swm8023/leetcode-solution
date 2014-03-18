/*
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
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
    TreeNode *sortedListToBST(ListNode *head) {
        int len = 0;
        for (ListNode *p = head; p; p = p->next, len++);
        return dfs(head, len);
    }
    TreeNode *dfs(ListNode *head, int len) {
        if (len <= 0) return NULL;
        int mid = (len + 1) >> 1;
        ListNode *rhead = head;
        for (int i = 1; i < mid; rhead=rhead->next, i++);
        TreeNode *node = new TreeNode(rhead->val);
        node->left = dfs(head, mid - 1);
        node->right = dfs(rhead->next, len - mid);
        return node;
    }
};