from sys import maxsize
class Solution:
    def findPeakElement(self,nums):
        '''
        :type nums:List[int]
        :rtype:int
        '''
        newNums = [-maxsize]+nums+[-maxsize]
        l,r = 1,len(newNums)-2
        while l <= r:
            mid = (l+r)//2
            if newNums[mid]>newNums[mid-1] and newNums[mid]>newNums[mid+1]:
                return mid-1
            elif newNums[mid]<newNums[mid+1]:
                l = mid+1
            else:
                r = mid-1
'''
二分查找：基于尖端原理，如果newNums[mid]<newNums[mid+1]，则存在两种情况：
    1：newNums[mid+1:-1]单调递增，则nums[-1]为尖端。
    2：newNums[mid+1:-1]不单调递增，则必存在一个index，
        newNums[index]>newNums[index-1]且newNums[index]>newNums[index+1]。
newNums[mid]<newNums[mid-1]同理。
'''