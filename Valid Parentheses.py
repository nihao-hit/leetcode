class Solution:
    def isValid(self,s):
        lstr = ('(','{','[')
        rstr = (')','}',']')
        stack = []
        for i in s:
            if i in lstr:
                stack.append(i)
            else:
                if not stack or i != rstr[lstr.index(stack.pop())]:
                    return False
        return stack == []