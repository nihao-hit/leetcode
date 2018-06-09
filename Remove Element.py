class Solution:
    def removeElement(self,nums,val):
        '''
        :type nums:List[int]
        :type val:int
        :rtype:int
        '''
        if nums == []:
            return 0
        i = count = 0
        while i<len(nums):
            if nums[i] == val:
                nums.pop(i)
                count += 1
            else:
                i += 1
        return count
'''
这题leetcode环境有问题
'''