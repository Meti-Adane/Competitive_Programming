#7:05
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def recurse(node):
            if not node: 
                return 0
            idx = recurse(node.next) + 1
            if idx > n:
                node.next.val = node.val
                
            return idx
        recurse(head)
        return head.next