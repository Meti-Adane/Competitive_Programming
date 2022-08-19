class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        visited = set()
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
       
    
        def isValid(row, col):
            if (row, col) in visited or row < 0 or row >= len(land) or col < 0 or col >= len(land[0]) or land[row][col] == 0:
                return False
            return True
                    
        def dfs(row, col):  
            visited.add((row,col))
            for x, y in dirs:
                if isValid(row+x, col+y):
                    w, x = dfs(x+row, col+y)
                    row = max(row, w)
                    col = max(col, x)
                
            return row, col
            
        for i, row in enumerate(land):
            for j, cell in enumerate(row):
                if isValid(i, j):
                    endr, endc = dfs(i, j)
                    ans.append([i, j, endr, endc])
        return ans