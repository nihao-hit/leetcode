# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    def removeNthFromEnd(self,head,n):
        '''
        :type head:ListNode
        :type n:int
        :rtype:ListNode
        '''
        ahead ,after = head,head
        for i in range(n):
            ahead = ahead.next
        if not ahead:
            return after.next
        while ahead.next:
            ahead = ahead.next
            after = after.next
        after.next = after.next.next
        return head
