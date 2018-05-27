class Solution():
    def maxArea(self,height):
        '''

        :param height:List[int]
        :return: int
        '''
        result,l,r = min(height[0],height[1]),0,len(height)-1
        while l < r:
            if height[l] < height[r]:
                result,l = max(result,(r-l)*height[l]),l+1
            else:
                result,r = max(result,(r-l)*height[r]),r-1
        return result
'''
如果height[i] < height[j]，则对任何height[k]（i<k<j），高度已确定，(i,k)小于(i,j)。
'''