# question url : https://leetcode.com/problems/minimum-path-sum/


class Solution:
    def minPathSum(self, grid) -> int:
        memo = {}
        row = len(grid)
        col = len(grid[0])
        return self.dfs(grid, row - 1, col - 1, memo)

    def dfs(self, grid, row, col, memo):
        if memo.get((row, col)):
            return memo[(row, col)]
        if row < 0 or col < 0:
            return float('inf')
        if row == col == 0:
            return grid[row][col]
        memo[(row, col)] = grid[row][col] + min(self.dfs(grid, row - 1, col, memo), self.dfs(grid, row, col - 1, memo))
        return memo[(row, col)]