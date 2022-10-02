class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = (10 ** 9) + 7
        dp = dict()
        
        def rollDice(n, k, target, runningSum):
            if n == 0 and runningSum == target:
                return 1
            if n <= 0:
                return 0
            if (n, runningSum) in dp:
                return dp[(n, runningSum)]
            count = 0
            for i in range(1, k+1):
                count += rollDice(n-1, k, target, runningSum+i)
            dp[(n, runningSum)] = count
            return dp[(n, runningSum)]  
               
                
        return rollDice(n, k, target, 0) % mod
            
            