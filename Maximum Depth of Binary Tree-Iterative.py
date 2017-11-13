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
        
        #return 1+max(self.maxDepth(root.right), self.maxDepth(root.left))
        
        queue = []
        
        queue.append(root)
        
        height = 0
        
        while len(queue) > 0:
            
            length = len(queue)
            
            height += 1
            a1 = 0
            
            while a1 < length:
                
                node = queue.pop(0)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
                a1 += 1
        return height
        
