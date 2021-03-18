# question url: https://leetcode.com/contest/weekly-contest-80/problems/linked-list-components/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        temp = head

        if not temp.next and temp.val == G[0]:
            return 1
        else:

            linkage = 0
            links = 0
            while temp and G:
                if temp.val in G:
                    links += 1

                elif links != 0 and temp.val not in G:
                    linkage += 1
                    links = 0

                if temp.next == None and temp.val in G:
                    linkage += 1

                temp = temp.next

        return linkage