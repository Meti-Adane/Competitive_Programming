class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n, m = len(matrix), len(matrix[0])
        isValid = lambda x,y: (x<n and y<m)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if isValid(i+1, j+1) and matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True 