class Solution:
    def myAtoi(self,str):
        '''

        :param str:
        :return: int
        '''
        import re
        match = re.match(r'\s*(\+|-|)[0-9]+', str)
        result = int(match.group(0)) if match else 0
        result = 2147483647 if result > 2147483647 else result
        result = -2147483648 if result < -2147483648 else result
        return result