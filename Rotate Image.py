class Solution:
    def rotate(self,matrix):
        '''
        :type matrix:List[List[int]]
        :rtype:void Do not return anything,modify matrix in-place instead.
        '''
        def swap(matrix,i,j):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                swap(matrix,i,j)
s = Solution()
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
s.rotate(matrix)
print(matrix)