#Definition for singly-linked list.
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def mergeTwoLists(self,l1,l2):
        '''
        :type l1:ListNode
        :type l2:ListNode
        :rtype:ListNode
        '''
        head = ListNode(0)
        temp = head
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1        
        if l2:
            temp.next = l2
        return head.next
