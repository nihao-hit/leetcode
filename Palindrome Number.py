class Solution:
    def isPalindrome(self,x):
        '''

        :param x:int
        :return: bool
        '''
        '''
        if x < 0 or x > 2147483647:
            return False
        strX = str(x)
        i,j = 0,len(strX)-1
        while i < j:
            if strX[i] != strX[j]:
                return False
            i += 1
            j -= 1
        return True
        '''
        return str(x)[::-1] == str(x)
s = Solution()
result = s.isPalindrome(-11221)
print(result)
