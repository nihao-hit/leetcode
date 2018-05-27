class Solution:
    def reverse(self,x):
        '''

        :param x:int
        :return: int
        '''
        absX = abs(x)
        result = 0
        while absX != 0:
            y = absX%10
            result = result*10 + y
            absX //= 10
        result = result if x >= 0 else -1*result
        if result > 2147483647 or result < -2147483648:
            return 0
        return result
    def reverseTwo(self,x):
        result = int(''.join(str(abs(x))[::-1]))
        result = result if x > 0 else -result
        if result > 2147483647 or result < -2147483648:
            return 0
        return result
s = Solution()
x = s.reverseTwo(-123)
print(x)