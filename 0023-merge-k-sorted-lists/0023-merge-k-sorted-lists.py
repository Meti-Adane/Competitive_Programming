# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = None
        
        for pos, listnode in enumerate(lists):
            if listnode:
                heappush(heap, (listnode.val, pos, listnode))
        while heap:
            val, pos, node = heappop(heap)
            newnode = ListNode(val)
            if not head:
                temp = newnode
                head = temp
            else:
                temp.next = newnode
                temp = temp.next
            node = node.next
            if node:
                heappush(heap, (node.val, pos, node))
        return head