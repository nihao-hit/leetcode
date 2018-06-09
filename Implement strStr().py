class Solution:
    def strStr(self,haystack,needle):
        '''
        :type haystack:str
        :type needle:str
        :rtype:int
        '''
        if needle == '':
            return 0
        def getNext(needle):
            '''
            :type needle:List[str]
            :rtype:List[int]
            '''
            next = [-1]*len(needle)
            i,j = 0,-1
            while i<len(needle)-1:
                if j == -1 or needle[i] == needle[j]:
                    i,j = i+1,j+1
                    next[i] = j
                else:
                    j = next[j]
            return next
        next = getNext(needle)
        i = j = 0
        while i<len(haystack) and j<len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i,j = i+1,j+1
            else:
                j = next[j]
        if j == len(needle):
            return i-j
        return -1
'''
KMP(看毛片)算法：利用部分匹配表PMT（Partial Match Table）数组，
                即模式字符串各个前缀的最大相同前缀后缀值，加速匹配。
                实现时求出next数组，即PMT数组向后偏移一位，并置next[0]=-1,方便编程。
     char  a b a b a b c a
     index 0 1 2 3 4 5 6 7
     value 0 0 1 2 3 4 0 1
加速原理：对haystack和needle来说，当发生h[i] != n[j]，
         一般算法会放弃已经匹配的n[0:j],从h[i],n[0]重新开始匹配，
         kmp则利用pmt[j-1]的值，令j = pmt[j-1]，
         假设pmt[j-1] = p,则n[0:p] == n[j-p:j] == h[i-p:i]，
         因此可以利用h[i-p:i] == n[j-p:j]的信息，不用重新匹配这部分，而是直接从h[i],n[p]开始匹配。
如何求next数组？
概要：令needle数组向后偏移一位，然后开始和原needle匹配，
    原needle代表前缀，偏移后的needle代表后缀，相同的位数即为pmt值。


                

                