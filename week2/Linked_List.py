class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        temp = self.head
        count = 0
        while temp != None:
            if count == index:
                return temp.data
            count += 1
            temp = temp.next
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        temp = self.head
        if temp == None:
            self.head = Node(val)
        else:
            newNode = Node(val)
            self.head = newNode
            self.head.next = temp

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        temp = self.head
        if self.isEmpty():
            self.head = Node(val)
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        temp = self.head
        count = 0
        if index == 0:
            self.addAtHead(val)
        else:
            while temp != None:
                if count + 1 == index:
                    newNode = Node(val)
                    temp2 = temp.next
                    newNode.next = temp2
                    temp.next = newNode
                count += 1
                temp = temp.next

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        temp = self.head
        count = 0

        if temp.next == None:
            if count == index:
                self.head = Node()
            return
        elif temp.next != None and count == index:
            temp = self.head
            self.head = temp.next
            return

        else:
            while temp and temp.next:
                if count + 1 == index:
                    temp.next = temp.next.next
                    return
                temp = temp.next
                count += 1
            return

    def isEmpty(self):
        return self.head == None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

# [[],[4],[1],[1],[5],[3],[7],[3],[3],[3],[1],[4]]
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)