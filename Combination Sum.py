class Solution:
    def dfs(self,nums,target,index,path,res):
        if target < 0:
            return
        elif target == 0:
            res.append(path)
        else:
            for i in range(index,len(nums)):
                self.dfs(nums,target-nums[i],i,path+[nums[i]],res)

    def combinationSum(self,candidates,target):
        '''
        :type candidates:List[int]
        :type target:int
        :rtype:List[List[int]]
        '''
        res = []
        candidates.sort(reverse=True)
        self.dfs(candidates,target,0,[],res)
        return res
'''
DFS：深度优先搜索
'''