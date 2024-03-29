class MyCircularQueue:

    def __init__(self, k: int):
        self.que = []
        self.limit = k 
        self.front = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.que.append(value)
        self.size += 1
        return True
        
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front += 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.que[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.que[-1]

    def isEmpty(self) -> bool:
        return self.front >= self.size

    def isFull(self) -> bool:
        return self.size-self.front >= self.limit
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()