/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode *head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int len = 0, i;
        ListNode *p, *last, *pnext, *tmp;
        for (p = head; p; p = p->next, len++);
        if (len <= 2) return;
        for (p = head, i = 0; i < len/2; p = p->next, i++);
        tmp = p, p = p->next, tmp->next = NULL;
        for (pnext = p->next, p->next = NULL; pnext;) {
            tmp = pnext;
            pnext = pnext->next;
            tmp->next = p;
            p = tmp;
        }
        last = p;
        for (p = head; p; p = tmp){
            tmp = p->next;
            if (last) {
                p->next = last;
                last = last->next;
                p->next->next = tmp;
            }
        }
    }
};

