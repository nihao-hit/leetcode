class Solution:
    def spiralOrder1(self,matrix):
        '''
        :type matrix:list[list[int]]
        :rtype:list[int]
        '''
        if matrix == []:
            return []
        row,col = len(matrix),len(matrix[0])
        flags = [[0]*col for i in range(row)]
        i = j = 0
        flags[i][j] = 1
        result = [matrix[i][j]]
        flag = True
        while flag:
            flag = False
            while j+1 < col and flags[i][j+1] == 0:
                flag = True
                j += 1
                flags[i][j] = 1
                result.append(matrix[i][j])
            while i+1 < row and flags[i+1][j] == 0:
                flag = True
                i += 1
                flags[i][j] = 1
                result.append(matrix[i][j])
            while j-1 >= 0 and flags[i][j-1] == 0:
                flag = True
                j -= 1
                flags[i][j] = 1
                result.append(matrix[i][j])
            while i-1 >= 0 and flags[i-1][j] == 0:
                flag = True
                i -= 1
                flags[i][j] = 1
                result.append(matrix[i][j])
        return result
    
    def spiralOrder2(self,matrix):
        if not matrix: return []
        R,C = len(matrix),len(matrix[0])
        seen = [[False]*C for _ in range(R)]
        ans = []
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        r = c = di = 0
        for _ in range(R*C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr,cc = r+dr[di], c+dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r,c = cr,cc
            else:
                di = (di+1)%4
                r,c = r+dr[di],c+dc[di]
        return ans
    
    def spiralOrder3(self,matrix):
        def spiral_coords(r1,c1,r2,c2):
            for c in range(c1,c2+1):
                yield r1,c
            for r in range(r1+1,r2+1):
                yield r,c2
            if r1 < r2 and c1 < c2:
                for c in range(c2-1,c1,-1):
                    yield r2,c
                for r in range(r2,r1,-1):
                    yield r,c1
        
        if not matrix: return []
        ans = []
        r1,r2 = 0,len(matrix)-1
        c1,c2 = 0,len(matrix[0])-1
        while r1 <= r2 and c1 <= c2:
            for r,c in spiral_coords(r1,c1,r2,c2):
                ans.append(matrix[r][c])
            r1 += 1;r2 -= 1
            c1 += 1;c2 -= 1
        return ans