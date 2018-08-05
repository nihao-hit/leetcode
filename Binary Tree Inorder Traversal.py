class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self,root):
        if not root:
            return []
        stack,out = [],[]
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return out
            root = stack.pop()
            out.append(root.val)
            root = root.right
        return out