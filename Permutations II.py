class Solution:
    def permuteUnique(self,nums):
        '''
        :type nums:List[int]
        :rtype:List[List[int]]
        '''
        perms = [[]]
        for i in nums:
            new_perms = []
            for perm in perms:
                for index in range(len(perm)+1):
                    new_perms.append(perm[:index]+[i]+perm[index:])
                    if index < len(perm) and perm[index] == i:
                        break
            perms = new_perms
        return perms
'''
消除重复的方法：不太理解。
对4个数的全排列来说，元素2的位置有4种：
[2,x,x,x]
[x,2,x,x]
[x,x,2,x]
[x,x,x,2]
此时再插入相同元素2，则两个2的位置组合有一下几种情况，
break以后的组合都是重复的，因此可以直接跳出循环。
[0,1],break,[0,1]
[0,2],[1,2],break,[2,3],[2,4]
[0,3],[1,3],[2,3],break,[3,4]
[0,4],[1,4],[2,4],[3,4],break
'''
