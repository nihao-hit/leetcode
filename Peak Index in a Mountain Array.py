class Solution:
    def peakIndexInMountainArray(self,A):
        '''
        :type A:List[int]
        :rtype:int
        '''
        l,r = 1,len(A)-2
        while l <= r:
            mid = (l+r)//2
            if A[mid]<A[mid+1]:
                l = mid+1
            elif A[mid]>A[mid-1]:
                return mid
            else:
                r = mid-1