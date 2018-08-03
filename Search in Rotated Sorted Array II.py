class Solution:
    def search(self,nums,target):
        '''
        :type nums:List[int]
        :type target:int
        :rtype:bool
        '''
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            while nums[l] == nums[mid] and l+1 <= mid:
                l += 1
            while nums[r] == nums[mid] and r-1 >= mid:
                r -= 1
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                if nums[mid] <= nums[r] or target >= nums[l]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid] >= nums[l] or target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return False
'''
Search in Rotated Sorted Array的升级版，区别是可能存在重复值。
重复值的影响体现在当nums[mid] == nums[l]或nums[mid] == nums[r]。
此时利用循环消除l或r的重复值。
'''