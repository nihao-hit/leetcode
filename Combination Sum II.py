class Solution:
    def dfs(self,nums,target,index,path,res):
        if target < 0:
            return
        elif target == 0:
            if path not in res:
                res.append(path)
        else:
            for j in range(index+1,len(nums)):
                self.dfs(nums,target-nums[j],j,path+[nums[j]],res)
    def combinationSum2(self,candidates,target):
        '''
        :type candidates:List[int]
        :type target:int
        :rtype:List[List[int]]
        '''
        candidates.sort(reverse=True)
        res = []
        for i in range(len(candidates)):
            self.dfs(candidates,target-candidates[i],i,[candidates[i]],res)
        return res
    
s = Solution()
result = s.combinationSum2([2,5,2,1,2],5)
print(result)