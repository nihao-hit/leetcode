class Solution:
    def groupAnagrams(self,strs):
        '''
        :type strs:List[str]
        :rtype:List[List[str]]
        '''
        strsDict = {}
        for i in strs:
            '''
            iCopy = ''.join(sorted(i))
            try:
                strsDict[iCopy].append(i)
            except:
                strsDict[iCopy] = [i]
            '''
            strsDict.setdefault(''.join(sorted(i)),[]).append(i)
        return list(strsDict.values())             