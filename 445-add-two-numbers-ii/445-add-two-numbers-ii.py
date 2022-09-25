# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        ans = None
        head = None
        temp1 = l1
        temp2 = l2
        
        while temp1 or temp2:
            if temp1:
                stack1.append(temp1.val)
                temp1 = temp1.next
            if temp2:
                stack2.append(temp2.val)
                temp2 = temp2.next
        carry = 0
        while stack1 or stack2:
            if not stack1:
                val1 = 0
            else:
                val1 = stack1.pop()
            if not stack2:
                val2 = 0
            else:
                val2 = stack2.pop()
                
            res = val1 + val2 + carry
            if res >= 10:
                unitsplace = res % 10
                carry = res // 10
            else:
                unitsplace = res
                carry = 0
            if not ans:
                ans = ListNode(unitsplace)
                head = ans
            else:
                newnode = ListNode(unitsplace)
                temp = head
                newnode.next = temp
                head = newnode
        if carry >= 1:
            newnode = ListNode(carry)
            temp = head
            newnode.next = temp
            head = newnode
        return head
            