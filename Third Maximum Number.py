import sys
class Solution:
    def thirdMax(self,nums):
        '''
        :type nums:List[int]
        :rtype:int
        '''
        nums = set(nums)
        first = second = third = -sys.maxsize
        for n in nums:
            if n > first:
                first,second,third = n,first,second
            elif n > second:
                second,third = n,second
            elif n > third:
                third = n
        return third if first != second != third != -sys.maxsize else first
'''
技巧1：sys.maxsize
技巧2：链式比较，例：first != second != third != -sys.maxsize
可以用dis分析
'''