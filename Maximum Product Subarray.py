class Solution:
    def maxProduct(self,nums):
        '''
        :type nums:list[int]
        :rtype:int
        '''
        curMax = curMin = finalMax = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < 0:
                curMax,curMin = curMin,curMax
            curMax = max(nums[i],curMax*nums[i])
            curMin = min(nums[i],curMin*nums[i])
            finalMax = max(finalMax,curMax)
        return finalMax