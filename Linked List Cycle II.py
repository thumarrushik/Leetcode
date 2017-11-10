# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        temp1 = head
        temp2 = head
        Temp = None
        while temp2.next and temp2.next.next:
            temp1 = temp1.next
            temp2 = temp2.next.next
            if (temp1 == temp2):
                Temp = 1
                break
            
        if Temp is None: 
            return None
        else:
            temp1 = head
            while temp1 != temp2:
                temp1 =temp1.next
                temp2 = temp2.next
            return temp1
