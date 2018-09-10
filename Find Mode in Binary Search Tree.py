class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self,root):
        '''
        :type root:TreeNode
        :rtype:List[int]
        '''
        def recursive(node,args,result):
            if node:
                recursive(node.left,args,result)
                if args[0] == node.val:
                    args[1] += 1
                else:
                    result.setdefault(args[1],[]).append(args[0])
                    args[0],args[1] = node.val,1
                args[2] = max(args[1],args[2])
                recursive(node.right,args,result)

        if root == None:
            return []
        result = {}
        args = [0,0,0]
        recursive(root,args,result)
        result.setdefault(args[1],[]).append(args[0])
        return result[args[2]]