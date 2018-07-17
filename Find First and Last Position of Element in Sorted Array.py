class Solution:
    def searchRange(self,nums,target):
        '''
        :type nums:List[int]
        :type target:int
        :rtype:List[int]
        '''
        if nums is None or nums == []:
            return [-1,-1]
        i,j = 0,len(nums)-1
        while i <= j:
            mid = (i+j)//2
            if nums[mid] == target:
                l = r = mid
                while l-1 >= 0 and nums[l-1] == nums[mid]:
                    l -= 1
                while r+1 < len(nums) and nums[r+1] == nums[mid]:
                    r += 1
                return [l,r]
            elif nums[mid] > target:
                j = mid-1
            else:
                i = mid+1
        return [-1,-1]
s = Solution()
result = s.searchRange([5,7,7,8,8,10],6)
print(result)