# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head
        stack = []
        
        while fast and fast.next:
            fast = fast.next.next
            stack.append(slow.val)
            slow = slow.next
                
        if fast:
            stack.append(slow.val)
        
        while stack and slow:
            
            if slow.val != stack.pop():
                return False
            slow = slow.next
            
        return True