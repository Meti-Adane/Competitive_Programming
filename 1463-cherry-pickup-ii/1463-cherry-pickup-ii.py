class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (1, 1), (1, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        isValid = lambda x, y: 0<=x<ROWS and 0<=y<COLS
        visited = set()


        @cache
        def recurse(r1, c1, r2, c2):
            if (not isValid(r1, c1) or not isValid(r2, c2) 
                 or (r1, c1) == (r2, c2)): return 0 
            cherries = 0
            
            for x,y in directions:
                newr1, newc1 = r1+x, c1+y
                visited.add((newr1, newc1))
                for x2, y2 in directions:
                   newr2, newc2 = r2+x2, c2+y2
                   if (newr2, newc2) not in visited:
                       cherries = max(cherries, recurse(newr1, newc1, newr2, newc2))
                visited.remove((newr1, newc1))

            cherries += (grid[r1][c1] + grid[r2][c2])
            return cherries  
        return recurse(0, 0, 0, COLS-1)
