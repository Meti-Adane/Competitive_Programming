class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        
        for i in range(n):
            for j in range(1+i, m):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
  
        for i in range(n):
            for j in range(n//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][-1*(j+1)] 
                matrix[i][-1*(j+1)] = temp
                