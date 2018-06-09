class Solution:
    def generateParenthesis(self,n):
        stack = '('
        lvalid = 1    
        ln = n-1
        rn = n
        result = []
        def generateParenthesis(result,stack,lvalid,ln,rn):
            if ln == 0:
                stack += ')'*rn
                result.append(stack)
                return
            if ln != 0 and lvalid != 0:
                generateParenthesis(result,stack+'(',lvalid+1,ln-1,rn)
                generateParenthesis(result,stack+')',lvalid-1,ln,rn-1)
            else:
                generateParenthesis(result,stack+'(',1,ln-1,rn)
        generateParenthesis(result,stack,lvalid,ln,rn)
        return result
'''
迭代是处理随机问题的好方法，
迭代既可用return传递计算结果，也可用参数传递计算结果，
后一种称为尾递归，可以优化栈调用。
'''