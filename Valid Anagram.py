class Solution:
    def isAnagram(self,s,t):
        '''
        :type s:str
        :type t:str
        :rtype:bool
        '''
        counter1 = [0]*26
        counter2 = list(counter1)
        for i in s:
            counter1[ord(i)-ord('a')] += 1
        for j in t:
            counter2[ord(j)-ord('a')] += 1
        return counter1 == counter2