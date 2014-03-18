/*
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
*/
/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    TreeLinkNode *next(TreeLinkNode* p) {
        while (p && !p->left && !p->right) p = p->next;
        return p;
    }
    void connect(TreeLinkNode *root) {
        TreeLinkNode *nextHead, *preHead, *nextPreHead;
        for (TreeLinkNode *head = root; head; preHead = head, head = nextHead) {
            head = next(head);
            if (head != NULL)
                nextHead = head->left ? head->left : head->right;
            else
                break;
            for (preHead = NULL; head; preHead = head, head = next(head->next)) {
                if (head->left && head->right) head->left->next = head->right;
                if (preHead) {
                    nextPreHead = head->left ? head->left : head->right;
                    if (preHead->right == NULL)
                        preHead->left->next = nextPreHead;
                    else
                        preHead->right->next = nextPreHead;
                }
            }
        }
    }
};