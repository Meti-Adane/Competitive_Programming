'''
    3. 10
    11, 2 
    3, 2
    '''

class DetectSquares:
     
    def __init__(self):
        self.counter = Counter()
        self.x_points = defaultdict(Counter)  

    def add(self, point):
        x, y = point
        self.counter[x, y] += 1
        self.x_points[x][y] += 1

    def count(self, point):
        x1, y1 = point
        ans = 0
        for y2 in self.x_points[x1]:
            if y1 != y2: 
                ans += self.counter[x1, y2] * self.counter[x1 + y2 - y1, y1] * self.counter[x1 + y2 - y1, y2]
                ans += self.counter[x1, y2] * self.counter[x1 + y1 - y2, y1] * self.counter[x1 + y1 - y2, y2]
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)