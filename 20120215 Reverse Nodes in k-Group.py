class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
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
    def reverseKGroup(self, head, k):
        nHead = ListNode(0)
        nHead.next = head
        p2, lenl = head, 0
        while p2: p2, lenl = p2.next, lenl + 1
        now, pre, ind = head, nHead, 1
        preHead, preHeadNext = nHead, head
        while now:
            if lenl - ind < lenl % k:
                break
            next = now.next
            now.next = pre
            if ind % k == 0:
                preHead.next = now
                preHeadNext.next = next
                preHead = preHeadNext
                pre = preHead
                preHeadNext = next
            else:
                pre = now
            now, ind = next, ind + 1
        return nHead.next
            
        
        
        
a1 = ListNode(1)
a2 = ListNode(2)        
a3 = ListNode(3)        
a4 = ListNode(4)        
a5 = ListNode(5)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5        


s = Solution()
a1 = s.reverseKGroup(a1, 4)
while a1:
    print a1.val
    a1 = a1.next
        