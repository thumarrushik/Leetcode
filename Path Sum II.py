# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        paths = []
        
        if root is None or root == []:
            return paths
        
        def dfs(root, summation, paths, result):
            
            if root.left is None and root.right is None and summation == root.val:
                paths.append(root.val)
                result.append(paths)
                
            if root.left:
                dfs(root.left, summation- root.val, paths+[root.val], result)
                
            if root.right:
                dfs(root.right, summation- root.val, paths+[root.val], result)
                
        result = []
        
        dfs(root, sum, [], result)
        
        return result
