def dfs(root, path, result):
    
    if root.left is None and root.right is None:
        result.append(int(path + str(root.value)))
        
    if root.left:
        dfs(root.left, path + str(root.value), result)
    
    if root.right:
        dfs(root.right, path + str(root.value), result)
    
    return result



def digitTreeSum(t):
    
    if t is None:
        return []
    
    result = []
    
    Result = dfs(t, "", result)
    
    return (sum(Result))
    
