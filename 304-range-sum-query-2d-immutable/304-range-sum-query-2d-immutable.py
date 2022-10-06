class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix[0]), len(matrix)
        self.prefixsum = [[0 for _ in range(m+1)] for _ in range(n)]
        for row in range(n):
            for col in range(m):
                self.prefixsum[row][col+1] = self.prefixsum[row][col] + matrix[row][col]
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2+1):
            res += self.prefixsum[i][col2+1] - self.prefixsum[i][col1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)