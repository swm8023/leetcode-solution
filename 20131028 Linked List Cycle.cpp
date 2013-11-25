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
    bool hasCycle(ListNode *head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        ListNode *h1, *h2;
        for(h1 = h2 = head; h1 && h2;){
            if (!h1->next || !h2->next || !h2->next->next)
                return false;
            h1 = h1->next;
            h2 = h2->next->next;
            if (h1 == h2 && h1) return true;
        }
        return false;
    }
};
