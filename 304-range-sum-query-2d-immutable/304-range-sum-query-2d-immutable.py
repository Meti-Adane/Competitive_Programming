class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix[0]), len(matrix)
        self.prefixsum = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for row in range(n):
            for col in range(m):
                self.prefixsum[row+1][col+1] = self.prefixsum[row][col+1] + matrix[row][col]+self.prefixsum[row+1][col] - self.prefixsum[row][col]

                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixsum[row2+1][col2+1] - self.prefixsum[row2+1][col1] - self.prefixsum[row1][col2+1] + self.prefixsum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)