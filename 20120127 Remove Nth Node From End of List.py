class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
'''
Given a linked list, remove the nth node from the end of list and return its head.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        nHead = ListNode(0)
        nHead.next = head
        p, t = 0, head
        while p < n:
            t = t.next
            p += 1
        pre = nHead
        while t:
            t, pre = t.next, pre.next
        pre.next = pre.next.next
        return nHead.next
    

        