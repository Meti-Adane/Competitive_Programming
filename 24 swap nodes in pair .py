# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        ans = None
        temp = head
        if not temp or not temp.next:
            return head
        
        while temp and temp.next:
            stack.append(temp.next)
            stack.append(temp)
            temp = temp.next.next
        
        if temp:
            stack.append(temp)
        
        for node in stack:
            node.next = None
            if not ans:
                ans = node
                front = ans
            else:
                ans.next = node
                ans = ans.next
            
        return front



# METHOD 2 RECURSION 

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recurse(head)
        
    def recurse(self, node):
        if not node or not node.next:
            return node
        prev = node.next
        node.next = self.recurse(node.next.next)
        prev.next = node
        return prev