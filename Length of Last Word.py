class Solution:
    def lengthOfLastWord(self,s):
        '''
        :type s:str
        :rtype:int
        '''
        return len(s.split()[-1]) if s.strip() != '' else 0
