class Solution:
    def findPoisonedDuration(self,timeSeries,duration):
        '''
        :type timeSeries:List[int]
        :type duration:int
        :rtype:int
        '''
        if timeSeries == []:
            return 0
        result = duration
        for i in range(len(timeSeries)-1):
            result += min(duration,timeSeries[i+1]-timeSeries[i])
        return result