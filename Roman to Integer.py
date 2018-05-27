class Solution():
    def romanToInt(self,s):
        '''
        :type s:str
        :rtype:int
        '''
        Roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        for j in range(len(s)):
            if j+1 < len(s) and Roman[s[j]] < Roman[s[j+1]]:
                result -= Roman[s[j]]
            else:
                result += Roman[s[j]]
        return result
