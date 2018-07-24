class Solution:
    def permuteMy(self,nums):
        '''
        :type nums:List[int]
        :rtype:List[List[int]]
        '''
        def nextPermutation(nums):
            i,j = len(nums)-2,len(nums)-1
            while i >= 0:
                if nums[i] > nums[j]:
                    i,j = i-1,i
                    continue
                for k in range(len(nums)-1,j-1,-1):
                    if nums[k] > nums[i]:
                        nums[i],nums[k] = nums[k],nums[i]
                        nums[j:] = list(reversed(nums[j:]))
                        return 1
            nums[:] = list(reversed(nums))
            return 0
        if len(nums) == 0:
            return []
        nums.sort()
        result = []
        flag = nextPermutation(nums)
        result.append(list(nums))
        while flag:
            flag = nextPermutation(nums)
            result.append(list(nums))
        return result
    def permute(self, nums):
        perms = [[]]   
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm)+1):   
                    new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
            perms = new_perms
        return perms
'''
大佬的精妙算法：从空列表开始，将nums元素一个一个插入全排列列表的不同位置。
逐渐构成1个数，2个数，······，直到n个数的全排列.
'''       
