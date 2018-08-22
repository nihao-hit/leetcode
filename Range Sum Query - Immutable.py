class NumArray:
    def __init__(self,nums):
        '''
        :type nums:list[int]
        '''
        self.nums = list(nums)
        for i in range(1,len(nums)):
            self.nums[i] += self.nums[i-1]
    
    def sumRange(self,i,j):
        '''
        :type i:int
        :type j:int
        :rtype:int
        '''
        return self.nums[j] - self.nums[i-1] if i>0 else self.nums[j]