class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0 
        visited = set()
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
                    
        def isValid(row, col):
            if (row < 0 or row >= len(grid) or 
                col < 0 or col >= len(grid[0]) or 
                grid[row][col] != "1" or 
                (row, col) in visited):
                return False
            return True
                    
        def dfs(row, col):
            visited.add((row, col))
            for x, y in directions:
                if isValid(row+x, col+y):
                    dfs(row+x, col+y)
                    
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == "1" and (i, j) not in visited: #if land previsouly not discovered
                    count += 1
                    dfs(i, j)
        return count