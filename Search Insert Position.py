class Solution:
    def searchInsert(self,nums,target):
        '''
        :type nums:List[int]
        :type target:int
        "rtype:int
        '''
        l,r = 0,len(nums)-1
        global mid
        while l<=r:
            mid = (l+r)//2
            if target > nums[mid]:
                l = mid+1
            elif target == nums[mid]:
                return mid
            else:
                r = mid-1
        return mid if target<=nums[mid] else mid+1
'''
二分查找虽然简单，但是边界条件很微妙：
循环继续的条件应该是l<=r，
1：如果写l!=r，则当l=mid且target<nums[mid]或r=mid且target>nums[mid]时，出现l>r。
2：如果写l<r,则当len(nums)==1时，不进入循环。
'''