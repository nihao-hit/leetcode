class Solution:
    '''我的垃圾代码'''
    def isValidSudoku1(self,board):
        '''
        :type board:List[List[str]]
        :rtype:bool
        '''
        validation = {str(i):0 for i in range(1,10)}
        validationROW = dict(validation)
        validationCOL = dict(validation)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    validationROW[board[i][j]] += 1
                if board[j][i] != '.':
                    validationCOL[board[j][i]] += 1
            if self.validate(validationROW) and self.validate(validationCOL):
                pass
            else:
                return False

        for a in range(3):
            for b in range(3):
                for c in range(a*3,3+a*3):
                    for d in range(b*3,3+b*3):                  
                        if board[c][d] != '.':
                            validation[board[c][d]] += 1
                if self.validate(validation):
                    pass
                else:
                    return False
        return True
    
    def validate(self,validation):
        flag = True
        for i in range(1,10):
            if validation[str(i)] not in (0,1):
                flag = False
            validation[str(i)] = 0
        return flag
    
    '''大佬的精妙代码1'''
    def isValidSudoku2(self,board):
        from collections import Counter
        return 1 == max(Counter(
            x
            for i,row in enumerate(board)
            for j,cell in enumerate(row)
            if cell != '.'
            for x in ((cell,i),(j,cell),(i%3,j%3,cell))
        ).values() + [1])
    
    '''大佬的精妙代码2'''
    def isValidSudoku3(self,board):
        seen = sum(([(cell,i),(j,cell),(i%3,j%3,cell)]
                    for i,row in enumerate(board)
                    for j,cell in enumerate(row)
                    if cell != '.'),[])
        return len(seen) == len(set(seen))
    
    '''大佬的精妙代码3'''
    def isValidSudoku4(self,board):
        seen = set()
        return not any(x in seen or seen.add(x)
                       for i,row in enumerate(board)
                       for j,cell in enumerate(row)
                       if cell != '.'
                       for x in ((cell,i),(j,cell),(i%3,j%3,cell)))
    
    '''大佬的精妙代码4'''
    def isValidSudoku(self,board):
        seen = sum(([(cell,i),(j,cell),(i%3,j%3,cell)]
                    for i in range(9) 
                    for j in range(9)
                    for cell in [board[i][j]]
                    if cell != '.'),[])
        return len(seen) == len(set(seen))

s = Solution()
result = s.isValidSudoku(
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
)
print(result)