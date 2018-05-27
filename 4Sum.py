class Solution:
    def fourSum(self,nums,target):
        '''

        :param nums:List[int]
        :param target: int
        :return: List[int]
        '''
        nums.sort()
        results = []
        self.nSum(nums,target,4,[],results)
        return results

    def nSum(self,nums,target,n,result,results):
        if n == 2:
            l,r = 0,len(nums)-1
            while l<r:
                temp = nums[l]+nums[r]
                if temp == target:
                    results.append([nums[l],nums[r]]+result)
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1;r -= 1
                elif temp > target:
                    r -= 1
                else:
                    l += 1
        else:
            for i in range(len(nums)-2):
                if i>0 and nums[i] == nums[i-1]:
                    continue
                self.nSum(nums[i+1:],target-nums[i],n-1,result+[nums[i]],results)
'''
题型：给一个n个整数的数组，求和/差/积/商值为target的m元组。
思路：分别固定m元组的前m-2个数，求四则运算值为target减前m-2个数的二元组，
     返回m元组。
'''