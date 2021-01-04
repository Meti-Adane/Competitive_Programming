# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.sumListNode = Node()
        head = self.sumListnode

    def insert

    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry=0) -> ListNode:

        val = l1.val + l2.val + carry
        carry = val // 10
        val = val % 10
        sumListNode = ListNode(val)
        head = sumListNode
        temp1 = l1.next
        temp2 = l2.next
        while temp1 or temp2:
            if temp1 == None or temp2 == None:
                if temp1 == None and temp2 != None:
                    temp1 = ListNode(0)
                if temp2 == None and temp1 != None:
                    temp2 = ListNode(0)

            val = temp1.val + temp2.val + carry
            carry = val // 10
            val = val % 10

            newNode = ListNode(val)
            temp3 = sumListNode
            while (temp3.next != None):
                temp3 = temp3.next
            temp3.next = newNode
            sumListNode = temp3

            temp1 = temp1.next
            temp2 = temp2.next

        if carry > 0:
            newNode = ListNode(carry)
            temp3 = sumListNode
            while (temp3.next != None):
                temp3 = temp3.next
            temp3.next = newNode
            sumListNode = temp3

        return head