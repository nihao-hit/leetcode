class Solution:
    def minimumTotal(self,triangle):
        '''
        :type triangle:list[list[int]]
        :rtype:int
        '''
        rows = len(triangle)
        result = [0]*len(triangle)
        for i in range(rows):
            for j in range(i,-1,-1):
                if i == 0:
                    result[j] = triangle[i][j]
                elif j == i:
                    result[j] = result[j-1]+triangle[i][j]
                elif j == 0:
                    result[j] += triangle[i][j]
                else:
                    result[j] = min(result[j-1],result[j])+triangle[i][j]
        return min(result)
s = Solution()
result =  s.minimumTotal([
     [-10]
])
print(result)