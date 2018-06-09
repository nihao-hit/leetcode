class Solution:
    def divide(self,dividend,divisor):
        '''
        :type dividend:int
        :type divisor:int
        :rtype:int
        '''
        if dividend>2147483647 or dividend<-2147483648 \
                or divisor<-2147483648 or divisor>2147483647:
            return 2147483647 
        symbol = (dividend > 0) is (divisor > 0)
        quotient = 0
        dividend,divisor = abs(dividend),abs(divisor)
        while dividend>=divisor:
            temp,i = divisor,1
            while dividend>=temp:
                quotient,dividend,temp,i = quotient+i,dividend-temp,temp<<1,i<<1
        quotient = quotient if symbol else 0-quotient
        return min(2147483647,max(quotient,-2147483648))
'''
妙啊：用减法求a/b=c，不断令b左移加倍，则求得的差也应该相应的左移加倍才能等于商，大大加速了算法
'''