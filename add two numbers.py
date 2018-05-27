class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = dummy = ListNode(0)
        left = 0
        while l1 or l2 or left == 1:
            (l1, num1) = (l1.next, l1.val) if l1 else (None, 0)
            (l2, num2) = (l2.next, l2.val) if l2 else (None, 0)
            left, num = divmod(num1 + num2 + left, 10)
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next