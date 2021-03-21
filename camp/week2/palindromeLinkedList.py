# questionurl: https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        firstHalf = []

        while fast and fast.next:
            firstHalf.append(slow.val)

            slow = slow.next
            fast = fast.next.next
        if fast:
            firstHalf.append(slow.val)

        for i in range(len(firstHalf) - 1, -1, -1):
            if slow.val != firstHalf[i]:
                return False
            slow = slow.next
        return True