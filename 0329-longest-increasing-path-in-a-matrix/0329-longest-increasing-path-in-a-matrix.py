class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        memo = dict()
        isValid = lambda r,c,v : 0 <= r < n and 0 <= c < m and (r,c) not in v 
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        def dfs(row, col, visited):
            if (row, col) in memo: 
                return memo[(row, col)] 
            visited.add((row, col))
            maxlength = 1
            for x, y in dirs:
                if isValid(x+row, col+y, visited) and matrix[row][col] < matrix[row+x][col+y]:
                    maxlength = max(dfs(row+x, col+y, visited)+1, maxlength)
            memo[(row,col)] = maxlength 
            visited.remove((row, col))
            return memo[(row, col)] 
        
        ans = 0       
        for i in range(n):
            for j in range(m):
                if (i, j) not in memo:
                    ans = max(ans, dfs(i, j, set()))
        return ans