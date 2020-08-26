# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1,num2=0,0
        while l1:
            num1*=10
            num1+=l1.val
            l1=l1.next
        while l2:
            num2*=10
            num2+=l2.val
            l2=l2.next
        ans=temp=ListNode()
        summ=str(num1+num2)
        for i in range(len(summ)):
            temp.val=int(summ[i])
            if i!=len(summ)-1:
                temp.next=ListNode()
                temp=temp.next
            else:
                temp.next=None
        return ans

    


    
    
    
    
    
