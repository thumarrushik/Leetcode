# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root is None:
            return root
        
        queue = [] 
        Result = []
        queue.append(root)
        Result.append([root.val])
        while(len(queue) > 0):
            node = queue.pop(0)
            Temp = []
            if node.left:
                queue.append(node.left)
                Temp.append(node.left.val)
                
            if node.right:
                queue.append(node.right)
                Temp.append(node.right.val)
                
            if Temp != []:
                Result.append(Temp)
                
                
        return Result
            
