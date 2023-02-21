# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        while headA or headB:
            if headA in seen:
                return headA
            if headB in seen:
                return headB
            if headA == headB:
                return headA
            
            if headA:
                seen.add(headA)
                headA = headA.next
            if headB:
                seen.add(headB)
                headB = headB.next
        return None