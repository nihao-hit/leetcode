'''
马拉车算法
'''
class Solution:
    def longestPalindrome(self,s):
        myS = '@#' + '#'.join(s) + '#$'
        myLength = [1]*len(myS)
        maxIndex = rightIndex = 0
        for i in range(2,len(myS)-2):
            if i < rightIndex:
                myLength[i] = min(myLength[2*maxIndex-i],rightIndex-i)
            while myS[i+myLength[i]] == myS[i-myLength[i]]:
                myLength[i] += 1
            if myLength[i] > myLength[maxIndex]:
                maxIndex = i
                rightIndex = i + myLength[i] - 1
        return ''.join(myS[maxIndex-myLength[maxIndex]+1:maxIndex+myLength[maxIndex]]).replace('#','')