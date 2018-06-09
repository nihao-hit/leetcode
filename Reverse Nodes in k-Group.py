class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    '''
    利用栈的后进先出特性反转链表
    '''
    def MYreverseKGroup(self,head,k):
        '''
        :type head:ListNode
        :type k:int
        :rtype:ListNode
        '''
        if k == 1:
            return head
        stack = []
        ahead = ListNode(0)
        prev = ahead
        temp = head
        next = head
        while True:
            for i in range(k):
                if temp:
                    stack.append(temp)
                    temp = temp.next
                else:
                    prev.next = next
                    return ahead.next
            temp = stack.pop()
            prev.next = temp
            next = temp.next
            for i in range(k-1):
                temp2 = stack.pop()
                temp.next = temp2
                temp = temp.next
            prev = temp
            temp = next
    '''
    利用python连续赋值的特性实现链表反转，
    python连续赋值可用dis.dis()分析，原理如下：
        1：a,b,c = c,b,a:将赋值运算符右边的变量值依次压入栈，然后反转栈元素，再依次赋值给左边
        2:a = b = c:将最右边的变量值压入栈，然后从最左边开始依次赋值
    '''
    def DALAOreverseKGroup(self,head, k):
        '''
        :type head:ListNode
        :type k:int
        :rtype:ListNode
        '''
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        
        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  
                jump.next, jump, l = pre, l, r
            else:
                return dummy.next       