# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        paths = []
        if root is None:
            return paths
        
        def dfs(root, path, result):
            if root.left is None and root.right is None:
                result.append(path+str(root.val))
                
            if root.left:
                dfs(root.left, path + str(root.val) + "->", result)
            
            if root.right:
                dfs(root.right, path+ str(root.val) + "->", result)
                
        result = []
        dfs(root, "", result)
        return result
