# question url : https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [None] * (n + 1)
        return self.findPossiblePaths(n, memo)

    def findPossiblePaths(self, n, memo):
        if memo[n] != None:
            return memo[n]
        if n <= 2:
            memo[n] = n
        else:
            memo[n] = self.findPossiblePaths(n - 1, memo) + self.findPossiblePaths(n - 2, memo)
        return memo[n]