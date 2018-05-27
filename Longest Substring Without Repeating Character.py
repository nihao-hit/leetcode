class Solution:
    def lengthOfLongestSubstring(self,s):
        sub = []
        maxl = 0
        for i in s:
            if i not in sub:
                sub.append(i)
            else:
                idx = sub.index(i)
                sub = sub[idx+1:]
                sub.append(i)
            maxl = max(len(sub),maxl)
        return maxl