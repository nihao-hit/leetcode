class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

from sys import maxsize
class Solution:
    def isValidBST(self,root):
        '''
        :type root:TreeNode
        :rtype:bool
        '''
        def isValid(root,minVal,maxVal):
            if not root:
                return True
            return minVal < root.val < maxVal and isValid(root.left,minVal,root.val) and isValid(root.right,root.val,maxVal)
        return isValid(root,-maxsize,maxsize)
'''
易错：单独的迭代父节点与左右孩子节点的值大小是否满足关系（如果有的话），
忽略了孙子节点与父节点需要满足的大小关系。
解决：将节点需要满足的大小关系迭代传给子节点。
'''