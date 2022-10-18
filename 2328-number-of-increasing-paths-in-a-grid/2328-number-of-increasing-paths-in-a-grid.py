class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        mod = pow(10, 9) + 7 
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        isValid = lambda r,c: (0 <= r < n and 0 <= c < m)
        
        @cache
        def dfs(r, c):
            path = 1
            for x, y in dirs:
                if isValid(r+x, c+y) and grid[r+x][c+y] > grid[r][c]:
                    path += dfs(r+x, c+y) % mod
            return path
        
        count = 0
        for i in range(n):
            for j in range(m):
                count += dfs(i, j) 
       
        return count % mod
            
                    
                
            