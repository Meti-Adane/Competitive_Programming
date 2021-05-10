# question url : https://leetcode.com/problems/reorder-list/submissions/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.queue = Deque()

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        self.traverse(head)
        if self.queue:
            head.next = self.queue.pop()
        else:
            return head
        n = 0
        curr = head.next
        print(head.val, curr.val)
        while self.queue:
            if n % 2 == 0:
                curr = self.addLeft(curr)
            else:
                curr = self.addRight(curr)
            n += 1
        curr.next = None

    def addLeft(self, node):
        if self.queue:
            node.next = self.queue.popleft()
            return node.next

    def addRight(self, node):
        if self.queue:
            node.next = self.queue.pop()
            return node.next

    def traverse(self, head):
        temp = head.next
        h = []
        while temp:
            self.queue.append(temp)
            h.append(temp.val)
            temp = temp.next

