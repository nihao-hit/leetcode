class Solution:
    def threeSum(self,nums):
        '''
        :type nums:List[int]
        :rtype:List[List[int]]
        '''
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                temp = nums[l]+nums[r]+nums[i]
                if temp == 0:
                    result.append([nums[l],nums[r],nums[i]])
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif temp > 0:
                    r -= 1
                else:
                    l += 1
        return result
'''
普通算法时间复杂度为n^3，
n^2算法为排序后固定一个数，然后让另两个数分别从首尾开始，往中间循环。
注意：三元组不能重复，即[1,0,-1]和[-1,1,0]视为同一三元组，
     出现重复三元组有两种情况，一是同一个三元组在不同的循环中重复出现，
                           解决：l初始化为i+1
                           二是数组中有相同的数，
                           解决：判断相邻的数是否相同，同则忽略
'''