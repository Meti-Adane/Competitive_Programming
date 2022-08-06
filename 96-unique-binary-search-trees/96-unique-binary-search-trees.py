class Solution:
    def numTrees(self, m: int) -> int:
        
        
        
        def recursive():
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
        
        def iterative():
            dp = dict()
            dp[0] = 1
            dp[1] = 1
            
            for i in range(2, m+1):
                runningTotal = 0
                for j in range(1, i+1):
                    runningTotal += dp[j-1] * dp[i-j]
                dp[i] = runningTotal
                    
            return dp[m]
        
        return iterative()