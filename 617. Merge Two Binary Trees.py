class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None
        
        if t1 is None:
            temp = t2
        elif t2 is None:
            temp = t1
        else:
            temp = TreeNode(t1.val + t2.val)
            temp.left = self.mergeTrees(t1.left, t2.left)
            temp.right = self.mergeTrees(t1.right, t2.right)
        return temp
