class Solution:
    def findAnagrams(self,s,p):
        '''
        :type s:str
        :type s:str
        :rtype:List[int]
        '''
        result = []
        counter1 = [0]*26
        counter2 = [0]*26
        for i in p:
            counter1[ord(i)-ord('a')] += 1
        j = 0
        length = len(p)
        #优化后的循环
        for j in s[:len(p)-1]:
            counter2[ord(j)-ord('a')] += 1
        for j in range(length-1,len(s)):
            counter2[ord(s[j])-ord('a')] += 1
            if counter2 == counter1:
                result.append(j-length+1)
            counter2[ord(s[j-length+1])-ord('a')] -= 1
        '''
        while j+length-1 < len(s):
            if s[j] in p:
                counter2 = [0]*26
                for k in s[j:j+length]:
                    counter2[ord(k)-ord('a')] += 1
                if counter2 == counter1:
                    result.append(j)
                    break
            j += 1
        while j+length < len(s):
            counter2[ord(s[j])-ord('a')] -= 1
            counter2[ord(s[j+length])-ord('a')] += 1
            if counter2 == counter1:
                result.append(j+1)
            j += 1
        '''
        return result
'''
可优化方向：目前时间复杂度为O(NK)，N为遍历s长度，K为counter比较的p长度。
可用collections.Counter代替数组的counter，则比较时间为O(1)。
'''