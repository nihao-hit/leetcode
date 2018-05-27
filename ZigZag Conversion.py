class Solution:
    def convert(self,s,numRows):
        '''
        :param s: str
        :param numRows: int
        :return: str
        '''
        if numRows == 1 or numRows >= len(s)-1:
            return s
        zigzag = ['']*numRows
        row = 0
        flag = -1
        for ch in s:
            zigzag[row] += ch
            if row == 0 or row == numRows-1:
                flag *= -1
            row += flag
        return ''.join(zigzag)