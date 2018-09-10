class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def recursive(x,n):
            if n == 0:
                return 1.0
            if n == 1:
                return x
            a,b = divmod(n,2)
            result = recursive(x,a)
            return result*result*recursive(x,b)
        
        if x == 0:
            return 1.0
        signal = 1
        if n < 0:
            signal = 0
            n = -n
        result = recursive(x,n)
        return result if signal else 1/result
s = Solution()
result = s.myPow(2.0,10)
print(result)