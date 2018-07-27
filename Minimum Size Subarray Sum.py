class Solution:
    def minSubArrayLen(self,s,nums):
        '''
        :type s:int
        :type nums:List[int]
        :rtype:int
        '''
        i,minL,minR = 0,0,len(nums)
        maxSum = 0
        for j in range(len(nums)):
            maxSum += nums[j]
            if maxSum >= s:
                while maxSum-nums[i] >= s:
                    maxSum -= nums[i]
                    i += 1
                if j - i < minR - minL:
                    minL,minR = i,j
        return minR-minL+1 if minR != len(nums) else 0
'''
通过i，j的右移获取每一个和大于等于s的序列，同时通过minL，minR记录最短序列。
'''