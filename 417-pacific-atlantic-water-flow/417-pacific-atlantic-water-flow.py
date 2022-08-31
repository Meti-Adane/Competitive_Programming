class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n, m = len(heights), len(heights[0]) 
        dp = [[[0, 0] for i in range(m)] for i in range(n)]
        ans = []
        
        visited = set()
        
        def dfs(row, col):
            if (row, col) in visited:
                return dp[row][col] 
            visited.add((row, col))
            for x, y in dirs:
                inbound = True
                if (row+x < 0 or col+y < 0):
                    dp[row][col][0] = 1
                    inbound = False
                if row+x >= n or col+y >= m:
                    dp[row][col][1] = 1
                    inbound = False
                if inbound and heights[row+x][col+y] <= heights[row][col]:
                    ans = dfs(row+x, col+y)
                    p, a = dp[row][col][0], dp[row][col][1]
                    dp[row][col] = [max(ans[0], p), max(ans[1], a)]
                if dp[row][col] == [1, 1]:
                    break
            visited.remove((row, col))
            return dp[row][col]
        
        for i in range(n):
            for j in range(m):
                if dfs(i, j) == [1, 1]:
                    ans.append((i, j))
        return ans