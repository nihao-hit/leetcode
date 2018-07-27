from collections import Counter
class Solution:
    def checkInClusion(self,s1,s2):
        '''
        :type s1:str
        :type s2:str
        :rtype:bool
        '''
        counter1 = Counter(s1)
        length = len(s1)
        counter2 = Counter(s2[:length-1])
        for i in range(length-1,len(s2)):
            counter2[s2[i]] += 1
            if counter1 == counter2:
                return True
            counter2[s2[i-length+1]] -= 1
            if counter2[s2[i-length+1]] == 0:
                del counter2[s2[i-length+1]]
        return False
'''
collections.Counter其实是OrderedDict,
>>>from collections import Counter
>>>c = Counter('aabccc')
>>>c
Counter({'c':3,'a':2,'b':1})
>>>c['d']
0
#取Counter中不存在的键，并不报错。
'''