#7:05
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            if i + 1 == n: return i+1, head.next
            return i+1, head
        
        return remove(head)[1]