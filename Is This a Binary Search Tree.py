""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    
    def make_list(root, minimum, maximum):
        if root is None:
            return True
        
        return minimum < root.data and root.data < maximum and make_list(root.left, minimum, root.data) and make_list(root.right, root.data, maximum)
            
            
    return make_list(root, float('-inf'), float('inf'))
