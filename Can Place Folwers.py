class Solution:
    def canPlaceFlowers(self,flowerbed,n):
        '''
        :type flowerbed:List[int]
        :type n:int
        :rtype:bool
        '''
        i = 0
        while i < len(flowerbed) and n > 0:
            if flowerbed[i] == 1:
                i += 2
            else:
                if i+1 < len(flowerbed):
                    if flowerbed[i+1] == 0:
                        n -= 1
                        i += 2
                    else:
                        i += 3
                else:
                    n -= 1
                    i += 1
        return True if n == 0 else False
'''
动笔而不是只在脑中想有助于理解！！！
规律：因为给定的花圃本身遵守不相邻原则，且当flowerbed[i] == 1时，i += 2，
所以当flowerbed[i] == 0时，flowerbed[i-1]一定为0或者i == 0，此时不需要判断flowerbed[i-1]。
'''
            