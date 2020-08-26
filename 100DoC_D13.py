# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def checkPalindrome(self, l1: ListNode):
      t=[]
      while l1 is not None:
        t.append(l1.val)
        l1=l1.next
      s="".join(t)
      return (s==s[::-1])
      
    


    
    
    
    
    
