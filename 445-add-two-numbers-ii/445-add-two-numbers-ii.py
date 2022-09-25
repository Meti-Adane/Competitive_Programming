# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        temp1, temp2 = l1, l2
        stack1, stack2 = self.fillStacks(temp1, temp2)
                
        carry = 0
        while stack1 or stack2:
            res = self.getSum(stack1, stack2) + carry
            unitsplace, carry = res, 0
            if res >= 10:
                unitsplace, carry = res % 10, res // 10
            if not head:
                head = ListNode(unitsplace)
            else:
                newnode = ListNode(unitsplace, head)
                head = newnode
        if carry >= 1:
            newnode = ListNode(carry, head)
            head = newnode
        return head
    
    
    
    def getSum(self, stack1, stack2):
        if not stack1:
            val1 = 0
        else:
            val1 = stack1.pop()
        if not stack2:
            val2 = 0
        else:
            val2 = stack2.pop()
        return val1+val2
    
    def fillStacks(self, temp1, temp2):
        stack1, stack2 = [], []
        while temp1 or temp2:
            if temp1:
                stack1.append(temp1.val)
                temp1 = temp1.next
            if temp2:
                stack2.append(temp2.val)
                temp2 = temp2.next
        return stack1, stack2