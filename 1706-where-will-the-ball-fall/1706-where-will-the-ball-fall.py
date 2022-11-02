class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        canPass = lambda x, y, k:  0 <= k < m and grid[x][y] == grid[x][k]
            
        def outCol(row, col, visited):
            if (row,col) in visited:
                return visited[(row, col)]
            if row == n :
                return col
            
            newcol = col + grid[row][col]
            visited[(row, col)] = -1
            if canPass(row, col, newcol):
                visited[(row, col)] = outCol(row+1, newcol, visited)
                
            return visited[(row, col)]
        
        dp = dict()
        ans = []
        
        for i in range(m):
            ans.append(outCol(0, i, dp))
        return ans
    
            