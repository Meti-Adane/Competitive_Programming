#7:15 -5
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        dp = [[float('inf') for _ in range(m)] for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    rightPath = bottomPath = float('inf')
                    if j+1 < m:
                        rightPath = dp[i][j+1] + 1
                    if i+1 < n:
                        bottomPath = dp[i+1][j] + 1
                    dp[i][j] = min(rightPath, bottomPath)
        
        for i in range(n):
            for j in range(m):
                leftPath = topPath = float('inf')
                if j-1 >= 0:
                    leftPath = dp[i][j-1] + 1
                if i-1 >= 0:
                    topPath = dp[i-1][j] + 1
                minpath = min(leftPath, topPath)
                dp[i][j] = min(dp[i][j], minpath)
                
        return dp
                
                    
            