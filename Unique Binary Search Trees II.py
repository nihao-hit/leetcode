class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self,n):
        '''
        :type n:int
        :rtype:list[TreeNode]
        '''
        def buildTree(node,temp):
            if node:
                if not node.left and node.val > temp.val:
                    node.left = temp
                    return
                if not node.right and node.val < temp.val:
                    node.right = temp
                    return
                if node.val > temp.val:
                    buildTree(node.left,temp)
                else:
                    buildTree(node.right,temp)

        def preorder(node,sequence):
            if node:
                sequence.append(node.val)
                preorder(node.left,sequence)
                preorder(node.right,sequence)

        def recursive(n,nums,count,flags,trees,sequences):
            if count == n:
                root = TreeNode(nums[0])
                for i in range(1,n):
                    buildTree(root,TreeNode(nums[i]))
                sequence = []
                preorder(root,sequence)
                if sequence not in sequences:
                    trees.append(root)
                    sequences.append(sequence)
                return
            for i in range(1,n+1):
                if flags[i] == 0:
                    flags[i] = 1
                    recursive(n,nums+[i],count+1,flags,trees,sequences)
                    flags[i] = 0
        
        if n <= 0:
            return []
        trees,sequences = [],[]
        flags = [0]*(n+1)
        recursive(n,[],0,flags,trees,sequences)
        return trees