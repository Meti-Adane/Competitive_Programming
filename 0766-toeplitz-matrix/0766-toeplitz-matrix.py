class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n, m = len(matrix), len(matrix[0])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i+1 < n and j+1 < m and matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True 