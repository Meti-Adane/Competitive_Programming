class Solution:
    def numTrees(self, m: int) -> int:
        dp = dict()
        dp[0] = 1
        dp[1] = 1
        
        ans = 0 
        
       
        def calculate(n):
            if n in dp:
                return dp[n]
            arr = [0] * (n+1)
            for i in range(1, n+1):
                arr[i] = calculate(i-1) * calculate(n-i)
            dp[n] = sum(arr)
            return dp[n]
        
        return calculate(m)