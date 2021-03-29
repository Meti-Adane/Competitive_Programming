# question url :  https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        landCount = 0
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    landCount += 1
                    arr = []
                    self.dfs(grid, i, j, arr)
                    print(arr)
        return landCount

    def dfs(self, grid, row, col, arr):
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
            return
        grid[row][col] = '0'
        arr.append((row, col))
        for d in directions:
            i = row + d[0]
            j = col + d[1]
            self.dfs(grid, i, j, arr)