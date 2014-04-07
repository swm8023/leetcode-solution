class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        nHead = ListNode(0)
        nHead.next = head
        p1, p2 = nHead, head
        while p2 and p2.next:
            p2 = p2.next.next
            p1.next.next.next = p1.next
            p1.next = p1.next.next
            p1.next.next.next = p2
            p1 = p1.next.next
        return nHead.next
    
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
s = Solution()
x = s.swapPairs(a)
while x:
    print x.val
    x = x.next