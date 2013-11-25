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
    ListNode *sortList(ListNode *head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if (head == NULL) return head;
        ListNode *tail = head;
        int size = 0;
        for (; tail!= NULL; tail = tail->next, size++);
        MergeSort(head, tail, size);
        return head;
    }
    void MergeSort(ListNode *l, ListNode *r, int size) {
        if (l->next == r) return;
        ListNode *m = l;
        for (int i = 0; i < size / 2; i++, m = m->next);
        MergeSort(l, m, size / 2);
        MergeSort(m, r, size - size / 2);
        ListNode *lp = l, *rp = m, *s;
        if (l->val > m-> val) {
            swap(l->val, m->val);
            for (ListNode *t = m; t->next != r && t->val > t->next->val;
                swap(t->val, t->next->val), t = t->next);
        }
        s = lp, lp = lp->next;
        for (int i = 1; i < size; i++) {
            if (rp == r || (lp !=m && lp->val < rp->val))
                s->next = lp, lp = lp->next;
            else
                s->next = rp, rp = rp->next;
            s = s->next;
        }
        s->next = r;
    }
    void swap (int &x, int &y) {
        x^=y^=x^=y;
    }
};
