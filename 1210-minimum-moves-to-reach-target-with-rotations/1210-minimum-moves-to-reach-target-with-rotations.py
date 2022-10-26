class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set({(-1, -1, -1, -1)})
        que = deque([(0, (0, 0, 0, 1), 1)]) # step , positions, alignment 1 == Horizontal 
        
        
        def addToPath(newpos, alignment):
            if newpos not in visited:
                que.append((step+1, newpos, alignment))
                visited.add(newpos)
                
        def moveright(r1, c1, r2, c2, alignment):
            if ((alignment == 1 and c2+1 < m and grid[r2][c2+1] != 1) or 
                (alignment == 0 and c2+1 < m and grid[r1][c1+1] != 1 and grid[r2][c2+1] != 1)):
                newpos = (r1, c1+1, r2, c2+1)
                addToPath(newpos, alignment)
                
        def moveDown(r1, c1, r2, c2, alignment):
            if ((alignment == 0 and r2+1 < n and grid[r2+1][c2] != 1) or 
                 (alignment == 1 and r2+1 < n and grid[r1+1][c1] != 1 and grid[r2+1][c2] != 1)):
                newpos = (r1+1, c1, r2+1, c2)
                addToPath(newpos, alignment) 
                
        def rotateClockwise(r1, c1, r2, c2, alignment):
            if alignment == 1 and r2 +1 < n and grid[r1+1][c1] != 1 and grid[r2+1][c2] != 1:
                newpos = (r1, c1, r1+1, c1)
                addToPath(newpos, 0)
                    
        def rotateCounterClockwise(r1, c1, r2, c2, alignment):
            if alignment == 0 and c2 +1 < n and grid[r1][c1+1] != 1 and grid[r2][c2+1] != 1:
                newpos = (r1, c1, r1, c1+1)
                addToPath(newpos, 1)
        
        
        while que:
            step, pos,  alignment = que.popleft()
            r1, c1, r2, c2 = pos
            if (r1, c1) == (n-1, m-2) and (r2, c2) == (n-1, m-1):
                return step
            
            moveright(r1, c1, r2, c2, alignment)
            moveDown(r1, c1, r2, c2, alignment)
            rotateClockwise(r1, c1, r2, c2, alignment)
            rotateCounterClockwise(r1, c1, r2, c2, alignment)
        return -1
        