/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if (!head) return NULL;
        RandomListNode *bhead, *anow, *bnow;
        for (anow = head; anow; anow = anow->next) {
            bnow = new RandomListNode(anow->label);
            bnow->next = anow->random;
            anow->random = bnow;
        }
        for(anow = head; anow; anow = anow->next) {
            bnow = anow->random;
            bnow->random = bnow->next?bnow->next->random:NULL;
        }
        bhead = head->random;
        for(anow = head; anow; anow = anow->next) {
            bnow = anow->random;
            anow->random = bnow->next;
            bnow->next = anow->next?anow->next->random:NULL;
        }
        return bhead;
    }
};
