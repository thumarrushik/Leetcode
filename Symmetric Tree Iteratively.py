# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root is None:
            return True
        
        if root.left is None or root.right is None:
            return root.left == root.right
        
        if root.left.val != root.right.val:
            return False
        
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        
        
        while len(stack) != 0:
            
            left = stack.pop(0)
            right = stack.pop(0)
            
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            
            if left.val != right.val:
                return False
            
            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
            
        
        return True
        
        
