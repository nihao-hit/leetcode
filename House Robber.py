class Solution:
    def rob(self,nums):
        '''
        :type nums:list[int]
        :rtype:int
        '''
        last = now = 0
        for i in nums:
            last,now = now,max(last+i,now)
        return now