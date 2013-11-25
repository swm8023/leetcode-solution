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
    ListNode *detectCycle(ListNode *head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        ListNode *h1, *h2;
        for(h1 = h2 = head; h1 && h2;){
            if (!h1->next || !h2->next || !h2->next->next)
                return false;
            h1 = h1->next;
            h2 = h2->next->next;
            if (h1 == h2 && h1) break;
        }
        if (!h1 || !h2) return NULL;
        h2 = head;
        while(h1 != h2) h1 = h1->next, h2 = h2->next;
        return h1;
    }
};
