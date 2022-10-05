class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i+2 >= len(grid) or j+2 >= len(grid[0]):
                    continue 
                ans = max(ans, grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]+grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i+1][j+1])
        return ans