#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1=head 
        p2=head

        for i in range(n):
            p1=p1.next

        if p1 is None:
            head=head.next
            return head
        while(p1.next is not None):
            p1=p1.next
            p2=p2.next

        p2.next=p2.next.next
        return head

        
      
      
        

    
    


    
    
    
    
    
