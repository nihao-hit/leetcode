class Solution:
    def multiply(self,num1,num2):
        '''
        :type num1:str
        :type num2:str
        :rtype:str
        '''
        def str2int(strIn):
            n = len(strIn)
            s2iDICT = {str(i):i for i in range(10)}
            intOut = 0
            for i in range(n-1,-1,-1):
                intOut += s2iDICT[strIn[n-1-i]]*pow(10,i)
            return intOut
        return '{}'.format(str2int(num1)*str2int(num2))