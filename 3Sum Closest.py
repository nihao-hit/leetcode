class Solution:
    def threeSumClosest(self,nums,target):
        '''

        :param nums:List[int]
        :param target: int
        :return:int
        '''
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                temp = nums[l] + nums[i] + nums[r]
                if temp == target:
                    return temp
                elif temp > target:
                    r -= 1
                else:
                    l += 1
                if abs(temp-target) < abs(result-target):
                    result = temp
        return result
