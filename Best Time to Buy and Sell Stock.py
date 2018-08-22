class Solution:
    def maxProfit(self,prices):
        '''
        :type prices:list[int]
        :rtype:int
        '''
        curMax = finalMax = 0
        for i in range(1,len(prices)):
            curMax = max(0,curMax+prices[i]-prices[i-1])
            finalMax = max(finalMax,curMax)
        return finalMax