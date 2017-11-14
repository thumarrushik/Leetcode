# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        vals = []
        
        if root is None:
            vals.append("null")
            
        def preorder(root):
            if root:
                vals.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
            else:
                vals.append("null")

        preorder(root)
        return vals
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def reverse_preorder():
            v1 = next(values)
            
            if v1 == "null":
                return None
            
            Node = TreeNode(int(v1))
            Node.left = reverse_preorder()
            Node.right = reverse_preorder()
            
            return Node
        
        values = iter(data)
        return reverse_preorder()
    
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
