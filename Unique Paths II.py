class Solution:
    def uniquePathsWithObstacles(self,obstacleGrid):
        '''
        :type obstacleGrid:list[list[int]]
        :rtype:int
        '''
        rows,cols = len(obstacleGrid),len(obstacleGrid[0])
        result = [[0]*cols for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == 1:
                    result[i][j] = 0
                else:
                    if i-1 < 0 and j-1 < 0:
                        result[i][j] = 1
                    elif i-1 < 0:
                        result[i][j] = result[i][j-1]
                    elif j-1 < 0:
                        result[i][j] = result[i-1][j]
                    else:
                        result[i][j] = result[i-1][j]+result[i][j-1]
        return result[-1][-1]