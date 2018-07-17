from itertools import groupby
class Solution:
    def countAndSay(self,n):
        '''
        :type n:int
        :rtype:str
        '''
        if n <= 0:
            return None
        if n == 1:
            return '1'
        else:
            result = self.countAndSay(n-1)
            r = ''
            for digit,num in groupby(result):
                r += str(len(list(num))) + digit
            return r
'''
itertools.groupby(iterable,key=None)：
根据key函数结果对可迭代对象的各个元素进行分类，
返回一个生成器，每个元素是由结果标签和对应元素的生成器组成的元组。
注意：分组只作用于相邻的同组元素。
'''