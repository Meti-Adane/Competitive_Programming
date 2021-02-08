class Solution:
    def middleNode(self, head):
        count = 0
        temp = head
        while temp != None:
            count += 1
            temp = temp.next

        target = (count // 2)
        temp2 = head
        i = 0
        while i < target:
            i += 1
            temp2 = temp2.next
        if i == target:
            return temp2

        #     middle node with one pass
        def middleNode(self, head):
            slow = head
            fast = head
            while (fast and fast.next):
                slow = slow.next
                fast = fast.next.next

            return slow