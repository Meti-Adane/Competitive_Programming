# question url:https://leetcode.com/problems/next-greater-node-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        temp = head
        nextlarger_nums, stack = [], []
        index = 0
        while temp:
            while stack and temp.val > stack[-1][0]:
                val, i = stack.pop()
                nextlarger_nums[i] = temp.val

            stack.append((temp.val, index))
            nextlarger_nums.append(0)
            temp = temp.next
            index += 1
        return nextlarger_nums