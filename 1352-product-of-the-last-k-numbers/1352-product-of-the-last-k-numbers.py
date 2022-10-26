class ProductOfNumbers:

    def __init__(self):
        self.runningProd = 1
        self.prods = []
        self.zerolastIndex = -1
        

    def add(self, num: int) -> None:
        if num == 0:
            self.zerolastIndex = len(self.prods)
            self.prods.append(0)
            self.runningProd = 1
        else:
            self.runningProd *= num 
            self.prods.append(self.runningProd)
        

    def getProduct(self, k: int) -> int:
        if self.zerolastIndex >= len(self.prods) -k:
            return 0
        if (k == len(self.prods)) or self.prods[-(k+1)] == 0:
            return self.prods[-1]
        return self.prods[-1] // self.prods[-(k+1)]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)