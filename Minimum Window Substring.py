from collections import defaultdict
class Solution:
    def minWindow(self,s,t):
        '''
        :type s:str
        :type t:str
        :rtype:str
        '''
        flag = False
        i,minL,minR = 0,0,len(s)
        missing = len(t)
        charDict = defaultdict(int)
        for v in t:
            charDict[v] += 1
        for j in range(len(s)):
            missing -= charDict[s[j]] > 0
            charDict[s[j]] -= 1
            if not missing:
                while i < j and charDict[s[i]] < 0:
                    charDict[s[i]] += 1
                    i += 1
                if j - i < minR - minL:
                    flag = True
                    minL,minR = i,j
        return s[minL:minR+1] if flag else ''            
'''
1：使用defaultdict比Counter快很多。
2：missing等于零以后就不会再改变，即找到第一个substring后,
    对于s中的每一个字符都要通过右移i来尝试得到最小substring。
3：使用flag判断是否找到最小substring，确定返回substring还是''。
'''