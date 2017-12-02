def isListPalindrome(l):

    if l is None:
        return True
        
    current = l
    runner = l
    
    stack = []
    
    while runner and runner.next:
        stack.append(current.value)
        current = current.next
        runner = runner.next.next
        
        
    if runner:
        current = current.next
        
    while current:
        if stack.pop() != current.value:
            return False
        current = current.next
    return True
