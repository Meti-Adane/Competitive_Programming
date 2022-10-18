class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        memo, n, m = dict(), len(grid), len(grid[0])
        isValid = lambda r,c,v : (0 <= r < n and 0 <= c < m and (r,c) not in v)
        count, mod = 0, pow(10, 9) + 7 
        
        def dfs(r, c, visited):
            if (r,c) in memo:
                return memo[(r,c)]
            visited.add((r,c))
            path = 1
            for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                if isValid(r+x, c+y, visited) and grid[r+x][c+y] > grid[r][c]:
                    path += dfs(r+x, c+y, visited)
            visited.remove((r, c))
            memo[(r,c)] = path
            return path
        
        for i in range(n):
            for j in range(m):
                if (i, j) in memo:
                    count += memo[(i,j)]
                else:
                    count += dfs(i, j, set())
       
        return count % mod
            
                    
                
            