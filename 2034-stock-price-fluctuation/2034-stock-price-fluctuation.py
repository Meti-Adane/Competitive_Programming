class StockPrice:
    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.latest = 0
        self.stocks = dict()
    
    def update(self, timestamp : int, value:int) -> None: 
        self.latest = max(timestamp, self.latest)
        self.stocks[timestamp] = value
        heappush(self.minheap, (value, timestamp))
        heappush(self.maxheap, (-1*value, timestamp))   
    
    def current(self) -> int:
        return self.stocks[self.latest] if self.latest else None
    
    def maximum(self) -> int:
        while self.maxheap and self.stocks[self.maxheap[0][1]] != -1 * self.maxheap[0][0]:
            value, timestamp = heappop(self.maxheap)
        return self.maxheap[0][0] * -1 
    
    def minimum(self) -> int:
        while self.minheap and self.stocks[self.minheap[0][1]] != self.minheap[0][0]:
            value, timestamp = heappop(self.minheap)
        return self.minheap[0][0] 

        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()