class Solution:
    def numTrees(self, m: int) -> int:
        
        dp = dict()
        dp[0] = 1
        dp[1] = 1

        def calculate(n):
            if n in dp:
                return dp[n]
            runningTotal = 0
            for i in range(1, n+1):
                runningTotal += calculate(i-1) * calculate(n-i)
            dp[n] = runningTotal
            return dp[n]

        return calculate(m)

      