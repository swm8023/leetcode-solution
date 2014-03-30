class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
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
        nHead, flag = ListNode(0), False
        nHead.next, head = head, nHead
        while head:
            if (head.next and head.next.next and head.next.next.val == head.next.val):
                head.next = head.next.next
                flag = True
            elif flag == True and head.next:
                head.next = head.next.next
                flag = False         
            else:
                head = head.next
        return nHead.next

            
        