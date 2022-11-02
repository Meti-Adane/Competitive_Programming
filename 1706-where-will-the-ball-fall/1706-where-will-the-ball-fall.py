class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        canPass = lambda x, y, k:  0 <= k < m and grid[x][y] == grid[x][k]
            
        def outCol(row, col):
            if row == n :
                return col
            
            newcol = col + grid[row][col]
            if canPass(row, col, newcol):
                return outCol(row+1, newcol)
            return -1
                
        ans = []
        for i in range(m):
            ans.append(outCol(0, i))
        return ans
    
            