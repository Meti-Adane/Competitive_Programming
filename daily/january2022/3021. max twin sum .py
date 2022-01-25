class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = float('-inf')
        stack = []
        slow, fast = head, head
        
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
                
        while stack and slow:
            ans = max(stack.pop()+slow.val, ans)
            slow = slow.next
        return ans