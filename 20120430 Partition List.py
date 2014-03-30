class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head is None:
            return head
        sHead, bHead = ListNode(0), ListNode(0)
        sTail, bTail = sHead, bHead
        while head is not None:
            if head.val < x:
                sTail.next = head
                sTail = sTail.next
            else:
                bTail.next = head
                bTail = bTail.next
            head = head.next
        bTail.next = None
        sTail.next = bHead.next
        return sHead.next
            
      
        