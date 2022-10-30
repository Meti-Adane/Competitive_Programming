class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        que = deque([(0, 0, 0, k)]) 
        visited = set() 
        n, m = len(grid), len(grid[0])
        
        if k >= n + m - 2:
            return n + m - 2
        
        isvalid = lambda x, y, v, k: 0 <= x < n and 0 <= y < m and (x,y, k) not in v 
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        while que:
            step, row, col, k = que.popleft()
            if row == n-1 and col == m-1:
                return step
            
            for x, y in dirs:
                newrow, newcol = row+x, col+y
                if newrow == n-1 and newcol == m-1:
                    return step +1
                    
                if k and isvalid(newrow, newcol, visited, k-1) and grid[newrow][newcol] == 1:
                    self.addToPath(step+1, newrow, newcol, k-1, que, visited)
                
                elif isvalid(newrow, newcol, visited, k) and grid[newrow][newcol] == 0:
                    
                    self.addToPath(step+1, newrow, newcol, k, que, visited)
        return -1
                
                
    def addToPath(self, step, row, col, k, que, visited):
            que.append((step, row, col, k))
            visited.add((row, col, k)) 