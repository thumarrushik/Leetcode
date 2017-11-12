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
        
        if root is None or root is []:
            return []
        
        
        queue = []
        result = []
        queue.append(root)
        result.append([root.val])
        
        while len(queue) > 0:
            
            length = len(queue)
            a1 = 0
            Temp = []
            while a1 < length:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    Temp.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    Temp.append(node.right.val)
                    
                a1 += 1
                
            if Temp != []:
                result.append(Temp)
            
        return result
