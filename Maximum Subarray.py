class Solution:
    def maxSubArray(self,nums):
        '''
        :type nums:List[int]
        :rtype:int
        '''
        curSum = maxSum = nums[0]
        for i in nums[1:]:
            curSum = max(i,curSum+i)
            maxSum = max(curSum,maxSum)
        return maxSum
'''
1：假设当前最大连续和为curSum，
对于当前元素i来说，如果加上i之后的curSum还小于i，那就应该丢弃i之前的curSum，
以i为起点，重新开始计算。
2：而对整个数组来说，不知道哪个局部最大连续和全局最大，因此要用maxSum记录全局最大连续和。
'''