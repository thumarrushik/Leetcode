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
        
        def mirror(left, right):
            
            if left is None or right is None:
                return left == right
            
            if left.val != right.val:
                return False
            
            return mirror(left.left, right.right) and mirror(left.right, right.left)
        
        return mirror(root.left, root.right)
            
        
        
