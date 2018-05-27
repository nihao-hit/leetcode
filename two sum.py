class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buff = {}
        for i in range(len(nums)):
            if nums[i] not in buff:
                buff[target-nums[i]] = i
            else:
                return [buff[nums[i]],i]