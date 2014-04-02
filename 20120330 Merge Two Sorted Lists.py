class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        nHead = ListNode(0)
        lt, rt, backHead = l1, l2, nHead
        while lt or rt:
            if lt is None:
                nHead.next, rt = rt, rt.next
            elif rt is None:
                nHead.next, lt = lt, lt.next
            elif lt.val < rt.val:
                nHead.next, lt = lt, lt.next
            else:
                nHead.next, rt = rt, rt.next
            nHead = nHead.next
        return backHead.next
        