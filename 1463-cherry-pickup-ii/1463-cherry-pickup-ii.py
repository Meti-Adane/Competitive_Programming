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
            for x1,y1 in directions:
                for x2, y2 in directions:
                   if (r1+x1, c1+y1) != (r2+x2, c2+x2):
                       cherries = max(cherries, recurse(r1+x1, c1+y1, r2+x2, c2+y2))

            cherries += (grid[r1][c1] + grid[r2][c2])
            return cherries  
        return recurse(0, 0, 0, COLS-1)
