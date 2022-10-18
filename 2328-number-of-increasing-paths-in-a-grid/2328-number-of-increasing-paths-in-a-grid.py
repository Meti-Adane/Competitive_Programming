class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        memo, n, m = dict(), len(grid), len(grid[0])
        mod = pow(10, 9) + 7 
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        isValid = lambda r,c: (0 <= r < n and 0 <= c < m)
        
        def dfs(r, c):
            if (r,c) in memo:
                return memo[(r,c)]
            
            path = 1
            for x, y in dirs:
                if isValid(r+x, c+y) and grid[r+x][c+y] > grid[r][c]:
                    path += dfs(r+x, c+y) % mod
                    
            memo[(r,c)] = path
            return memo[(r,c)]
        
        count = 0
        for i in range(n):
            for j in range(m):
                count += dfs(i, j) 
       
        return count % mod
            
                    
                
            