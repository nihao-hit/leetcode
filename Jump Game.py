class Solution:
    def canJump(self,nums):
        '''
        :type nums:list[int]
        :rtype:bool
        '''
        if not nums: return
        i = len(nums)-2
        while i >= 0:
            if nums[i] == 0:
                needJumps = 1
                while needJumps > nums[i]:
                    needJumps += 1;i -= 1
                    if i < 0:
                        return False
            i -= 1
        return True
s = Solution()
result = s.canJump([3,2,1,0,4])
print(result)