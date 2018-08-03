class Solution:
    def findLength(self,A,B):
        '''
        :type A:List[int]
        :type B:List[int]
        :rtype:int
        '''
        lenList = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
        for i in range(1,len(A)+1):
            for j in range(1,len(B)+1):
                if A[i-1] == B[j-1]:
                    lenList[i][j] = lenList[i-1][j-1] + 1
                else:
                    lenList[i][j] = 0 #max(lenList[i-1][j],lenList[i][j-1])
        return max(map(max,lenList))
'''
最长公共子序列问题：
    输入：X = (x 1 ,x 2 ,...,x n ) ， Y = (y 1 ,y 2 ,...y m )
    输出：Z = X 与Y 的最长公共子序列
    优化子结构
        设X=(x 1 , ..., x m ) 、Y=(y 1 , ..., y n )  是两个序列，
        Z=(z 1 , ..., z k ) 是X 与Y 的LCS ，我们有：
        ⑴  如果x m =y n ,  则z k =x m =y n , Z k-1 是X m-1 和Y n-1 的
        LCS ， 即 ，LCS XY  = LCS X m-1 Y n-1 + <x m =y n >.
        ⑵  如果x m ！= y n ， 且z k ！= x m ， 则Z 是X m-1 和Y 的
        LCS ，即 即  LCS XY = LCS X m-1 Y
        ⑶  如果x m ！= y n , 且z k ！= y n , 则Z 是X 与Y n-1 的LCS ，
        即 即  LCS XY = LCS XY n-1
    LCS 长度的递归方程
        C[i, j] = 0 if i=0  或 j=0
        C[i, j] = C[i-1, j-1] + 1 if i, j>0  且 x i  = y j
        C[i, j] = Max(C[i, j-1], C[i-1, j]) if i, j>0  且 x i  ！= y j

疑惑：最长公共子序列的优化子结构有问题，如果x m = y n，并不能代表z k =x m =y n。
例如：X = [1,2,3,4,5],Y = [1,2,5,4,3]，对x[3] = y[3]，对应的最长子序列为[1,2]。

解决：改变递归方程
        C[i,j] = 0 if i=0 或 j=0
        C[i,j] = C[i-1,j-1]+1 if i,j>0 且x i = y j
        C[i,j] = 0 if i,j>0 且x i != y j
    则最长公共子序列不再是结果矩阵的最后一个值。
'''