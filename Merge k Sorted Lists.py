class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    '''
    o(n^2)
    '''
    def MymergeKLists(self,lists):
        '''
        :type lists:List[ListNode]
        :rtype:ListNode
        '''
        head = ListNode(0)
        temp = head
        while True:
            lists = list(filter(lambda x:bool(x),lists))
            if lists == []:
                break
            k = len(lists)
            vals = [0]*k 
            for i in range(len(lists)):
                vals[i] = lists[i].val
            val = min(vals)
            temp.next = ListNode(val)
            temp = temp.next
            j = vals.index(val)
            lists[j] = lists[j].next
        return head.next
    '''
    o(n*lgn)
    '''
    def mergeKLists(self,lists):
        from queue import PriorityQueue as queue
        q = queue()
        head = ListNode(0)
        temp = head
        for i in range(len(lists)):
            q.put((lists[i].val,i,lists[i]))
        while q.qsize():
            _,index,temp.next = *q.get()
            temp = temp.next
            if temp.next: q.put((temp.next.val,index,temp.next))
        return head.next
'''
优先级队列，堆排序实现。
'''