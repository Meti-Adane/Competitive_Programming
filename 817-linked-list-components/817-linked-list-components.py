# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        component = 0 
        lookup = set(nums)
        
        temp = head
        while temp:
            isConnected = False
            while temp and temp.val in lookup:
                temp = temp.next
                isConnected = True
            if isConnected:
                component += 1
            else:
                temp = temp.next
                
        return component
        
        
        
        