class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        nHead, flag = ListNode(0), 0
        head = nHead
        while flag or l1 or l2:
            node = ListNode(flag)
            if l1: 
                node.val += l1.val
                l1 = l1.next
            if l2: 
                node.val += l2.val
                l2 = l2.next
            flag = node.val // 10
            node.val %= 10
            head.next, head = node, node
        return nHead.next
        
    
r1 = ListNode(0)
r2 = ListNode(1)
s = Solution()
s.addTwoNumbers(r1, r2)
