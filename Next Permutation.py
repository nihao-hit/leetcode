class Solution:
    def nextPermutation(self,nums):
        '''
        :type nums:List[int]
        :rtype:void Do not return anything,modify nums in-place instead.
        '''
        if len(nums) in (0,1):
            return
        i,j = len(nums)-2,len(nums)-1
        while i >= 0:
            if nums[i] >= nums[j]:
                i,j = i-1,i
                continue
            for k in range(len(nums)-1,j-1,-1):
                if nums[k] > nums[i]:
                    nums[i],nums[k] = nums[k],nums[i]
                    nums[j:] = list(reversed(nums[j:]))
                    return
        nums[0:] = list(reversed(nums))
        return
'''
全排列
如何从编程角度获取所有排列，一般按照升序顺序（字典序）获得下一个排列。
例如：对于集合{1,2,3}来说，全排列顺序为{1,2,3},{1,3,2},{2,1,3},{2,3,1},{3,1,2},{3,2,1}。
STL（标准模板库）求下一个全排列算法：
    1：从后向前查找第一个相邻元素对(i,j)，并且满足A[i]<A[j]（此时从j到end是降序）
    2：在[j,end]中寻找一个最小的k使其满足A[i]<A[k]（从后向前查找第一个满足A[i]<A[k]的k）
    3：交换i，k
    4：翻转[j,end]
注意：如果在步骤1找不到符合条件的相邻元素对，说明[start,end]为降序，无下一个全排列，将其翻转为升序。
'''