# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        n = 1 
        temp = head
        mindst, maxdst = 10**5, -1 * 10**5
        start = 10**5
        prev = -1 * 10**5 
        while temp and temp.next:
            curr = temp.next # 5  # node being testet for crtical
            if not curr.next:
                break
            nextnode = curr.next #1
            if (temp.val < curr.val and nextnode.val < curr.val or # 5 3 1
                temp.val > curr.val and nextnode.val > curr.val): # 3 1 5
                start = min(n+1, start) #3
                mindst = min(n+1 - prev, mindst) #float
                maxdst = n+1-start #3-3 0 
                prev = n+1 #3
            n += 1 #7
                
            temp = temp.next #2
        
        if maxdst <= 0 :
            return [-1, -1]
        return [mindst, maxdst]