class Solution():
    def longestCommonPrefix(self,strs):
        '''
        :type strs:List[str]
        :rtype:str
        '''
        if strs == []:
            return ''
        for i,common in enumerate(zip(*strs)):
            if len(set(common)) > 1:
                return strs[0][:i]
        return min(strs)
            
'''
bug：[]不等于False也不等于True
bug: 空集合不等于False也不等于True
[],'',()不为None

zip([iterable,...]),函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
然后返回由这些元组组成的列表。如果各个迭代器的元素个数不一致，
则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
'''
