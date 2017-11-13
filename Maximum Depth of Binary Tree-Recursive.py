# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root, height = 0):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None or root == []:
            return 0
        
        return 1+max(self.maxDepth(root.right), self.maxDepth(root.left))
    
