class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return head
        nHead = ListNode(0)
        nHead.next, head = head, nHead
        while head:
            if (head.next and head.next.next and head.next.next.val == head.next.val):
                head.next = head.next.next
            else:
                head = head.next
        return nHead.next