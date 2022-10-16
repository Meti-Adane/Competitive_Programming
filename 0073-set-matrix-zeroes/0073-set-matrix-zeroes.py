#1:47
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        que = deque()
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    que.append((i, j))
        
        while que:
            row, col = que.popleft()
            for i in range(m):
                matrix[row][i] = 0
            for i in range(n):
                matrix[i][col] = 0
            
            
                