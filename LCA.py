"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def lca(root , v1 , v2):
  #Enter your code here

    if root is None:
        return None
    
    if root.data == v1 or root.data == v2:
        return root
    
    left_root = lca(root.left, v1, v2)
    right_root = lca(root.right, v1, v2)
    
    if left_root and right_root:
        return root
    
    if left_root is not None:
        return left_root
    else:
        return right_root
    
    
