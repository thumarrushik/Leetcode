def removeKFromList(l, k):
    Temp = ListNode(None)
    Temp.next = l
    current = Temp
    
    while current:
        while current.next and current.next.value == k:
            current.next = current.next.next
        current = current.next
        
    return Temp.next
