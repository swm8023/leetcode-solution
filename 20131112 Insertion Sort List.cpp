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
    ListNode *insertionSortList(ListNode *head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if (head == NULL) return head;
        ListNode *newHead = new ListNode(0);
        ListNode *nextHead = head->next, *now;
        newHead->next = head, head->next = NULL;
        while (nextHead != NULL){
            now = nextHead, nextHead = nextHead->next;
            for (ListNode *h = newHead; h != NULL; h = h->next) {
                if (h->next == NULL || now->val < h->next->val) {
                    ListNode *tmp = h->next;
                    h->next = now, now->next = tmp;
                    break;
                }
            }
        }
        head = newHead->next;
        delete newHead;
        return head;
    }
};
