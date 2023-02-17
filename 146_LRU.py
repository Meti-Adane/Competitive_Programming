class TreeNode:
    def __init__(self, val=0, nxt= None, prev= None):
        self.val = val
        self.next = nxt 
        self.prev = prev
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.head = None 
        self.tail = None
        self.length = 0 
        self.hashmap = dict()

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self.deleteNode(node)
        self.insertAtTail(node)
        return node.val[1]

    def put(self, key: int, value: int) -> None:
        newnode = TreeNode((key, value))
        if key not in self.hashmap:
            if (self.length >= self.capacity):
                k = self.head.val[0]
                self.deleteFront()
                self.hashmap.pop(k)
            else:
                self.length += 1
        if key in self.hashmap:
            self.deleteNode(self.hashmap[key])
            self.hashmap.pop(key)
            
        self.insertAtTail(newnode)
        self.hashmap[key] = newnode
        
        
    def deleteNode(self, node):
        if node == self.head:
            self.deleteFront()
        elif node == self.tail:
            self.deleteTail()
        else:
            temp = node
            node.prev.next = temp.next
            node.next.prev = temp.prev
        
    def insertAtFront(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            temp = self.head 
            temp.prev = node
            self.head = node
            self.head.next = temp
    
    def deleteFront(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp = self.head.next
            self.head.next.prev = None
            self.head.next = None
            self.head = temp
        
    def deleteTail(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None 
        else:
            temp = self.tail.prev
            self.tail.prev.next = None
            self.tail.prev = None
            self.tail = temp
            
    def insertAtTail(self, node):
        if not self.tail:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)