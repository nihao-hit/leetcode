class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def swapPairs(self,head):
        '''
        :type head:ListNode
        :rtype:ListNode
        '''
        if not head or not head.next:
            return head
        after,ahead = head,head.next
        prev = ListNode(0)
        head = prev
        while ahead and after:
            after.next = ahead.next
            ahead.next = after
            prev.next = ahead
            
            prev = after
            after = after.next
            if after: ahead = after.next
        return head.next