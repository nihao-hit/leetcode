class Solution():
    def search(self,nums,target):
        '''
        :type nums:List[int]
        :type target:int
        :rtype:int
        '''
        i,j = 0,len(nums)-1
        while i <= j:
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[j] > nums[mid] or nums[i] <= target:
                    j = mid-1
                else:
                    i = mid+1
            else:
                if nums[i] < nums[mid] or nums[j] >= target:
                    i = mid+1
                else:
                    j = mid-1
        return -1
'''
二分查找的变形：数组可能升序也可能以某个数旋转，查找target对应的下标。
解题思路：例：nums=[5,6,7,8,1,2,3,4]，target=8。
1、nums[mid] == target
2、nums[mid] != target
2.1、nums=[1,2,3,4,5,6,7,8],mid随意
2.2、nums=[5,6,7,8,1,2,3,4],mid=3
2.3、nums=[5,6,7,8,1,2,3,4],mid=5
对于nums[mid] > target来说：有两种情况，一是nums[right]>nums[mid]，即2.1和2.3，
                                          nums[left]<=target，即2.2中的一部分情况；
                                      二是2.2中的另一部分情况；
对于nums[mid] < target来说：有两种情况，一是nums[left]<nums[mid]，即2.1和2.2，
                                          nums[right]>=target，即2.3中的一部分情况；
                                      二是2.3中的另一部分情况；
'''