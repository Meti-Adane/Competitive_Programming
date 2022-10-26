class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        moves = [(0, 1), (1, 0)]
        rotation = [(1, 0), (0, 1)] #clockwise, counterclockwise
        visited = set()
        que = deque([(0, (0, 0, 0, 1), 1, [])]) # step , positions, alignment 1 == Horizontal 
        
        
        
        def moveright(r1, c1, r2, c2, alignment, path):
            if alignment == 1: #horizontal aligned 
                if c2+1 < m and grid[r2][c2+1] != 1:
                    newpos = (r1, c1+1, r2, c2+1)
                    if newpos not in visited:
                        que.append((step+1, newpos, alignment, path+[" R "]))
                        visited.add(newpos)
                        return True 
                else:
                    return False 
            else: # vertically aligned 
                if c2+1 < m and grid[r1][c1+1] != 1 and grid[r2][c2+1] != 1:
                    newpos = (r1, c1+1, r2, c2+1)
                    if newpos not in visited:
                        que.append((step+1, newpos, alignment, path+[" R "]))
                        visited.add(newpos)
                        return True 
                else:
                    return False 
        def moveDown(r1, c1, r2, c2, alignment, path):
            if alignment == 0: #Vertical aligned 
                if r2+1 < n and grid[r2+1][c2] != 1:
                    newpos = (r1+1, c1, r2+1, c2)
                    if newpos not in visited:
                        que.append((step+1, newpos, alignment, path+[" D "]))
                        visited.add(newpos)
                        return True
                else:
                    return False 
            else: # Horizontal aligned 
                if r2+1 < n and grid[r1+1][c1] != 1 and grid[r2+1][c2] != 1:
                    newpos = (r1+1, c1, r2+1, c2)
                    if newpos not in visited:
                        que.append((step+1, newpos, alignment, path+[" D "]))
                        visited.add(newpos)
                        return True
                else:
                    return False 
                    
        def rotateClockwise(r1, c1, r2, c2, alignment, path):
            if alignment == 0:
                return False
            if r2 +1 < n and grid[r1+1][c1] != 1 and grid[r2+1][c2] != 1:
                newpos = (r1, c1, r1+1, c1)
                if newpos not in visited:
                    que.append((step+1, newpos, 0, path+[" C "]))
                    visited.add(newpos)
                    return True
            else:
                return False
        def rotateCounterClockwise(r1, c1, r2, c2, alignment, path):
            if alignment == 1: 
                return False
            if c2 +1 < n and grid[r1][c1+1] != 1 and grid[r2][c2+1] != 1:
                newpos = (r1, c1, r1, c1+1)
                if newpos not in visited:
                    que.append((step+1, newpos, 1, path+[" CC "]))
                    visited.add(newpos)
                    return True
            else:
                return False
                
        
        
        
        while que:
            step, pos,  alignment, path = que.popleft()
            r1, c1, r2, c2 = pos
            if (r1, c1) == (n-1, m-2) and (r2, c2) == (n-1, m-1):
                print(path)
                return step
            
            moveright(r1, c1, r2, c2, alignment, path)
            moveDown(r1, c1, r2, c2, alignment, path)
            rotateClockwise(r1, c1, r2, c2, alignment, path)
            rotateCounterClockwise(r1, c1, r2, c2, alignment, path)
        return -1
        