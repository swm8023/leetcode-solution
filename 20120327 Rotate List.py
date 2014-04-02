class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head:
            return head
        p, len = head, 1
        while p.next:
            p, len = p.next, len + 1
        k = len - k % len
        if k == len:
            return head
        pp, len = head, 1
        while len < k:
            pp, len = pp.next, len + 1
        p.next, head, pp.next = head, pp.next, None
        return head

        