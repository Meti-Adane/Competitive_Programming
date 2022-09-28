#7:05
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prevnode = None
        
        temp = head
        front = temp
        while temp:
            if self.isTargetNode(temp, n):
                if not prevnode:
                    front = temp.next
                    temp.next = None
                    
                else:
                    prevnode.next = temp.next
                return front
            prevnode = temp
            temp = temp.next
            
    def isTargetNode(self, node, k):
        if k <= 0 and not node:
            return True 
        if k <= 0 and node:
            return False
        return self.isTargetNode(node.next, k-1)
        