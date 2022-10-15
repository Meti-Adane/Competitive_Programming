# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums= []
        temp = head = None
        for listnode in lists:
            while listnode:
                nums.append(listnode.val)
                listnode = listnode.next
        nums.sort()
        
        for num in nums:
            newnode = ListNode(num)
            if not temp:
                temp = newnode
                head = temp
            else:
                temp.next = newnode
                temp = temp.next
        return head