class Solution:
    def minCostClimbingStairs(self,cost):
        '''
        :type cost:list[int]
        :rtype:int
        '''
        n = len(cost)
        result = [0]*n
        result[0],result[1] = cost[0],cost[1]
        for i in range(2,n):
            result[i] = cost[i]+min(result[i-1],result[i-2])
        return min(result[n-2],result[n-1])