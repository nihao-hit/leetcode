class Solution:
    def removeDuplicates(self,nums):
        '''
        :type nums:List[int]
        :rtype:int
        '''
        if nums == []:
            return 0
        prev = nums[0]
            i = 1
            while i<len(nums):
                if nums[i] == prev:
                    nums.pop(i)
                else:
                    prev = nums[i]
                    i += 1
            return len(nums)
