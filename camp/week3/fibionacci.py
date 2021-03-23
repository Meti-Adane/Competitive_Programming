class Solution:
    def fib(self, n: int) -> int:
        arr = [None] * (n + 1)
        return self.fibs(n, arr)

    def fibs(self, n, memo):
        if memo and memo[n] != None:
            return memo[n]
        if n < 2:
            memo[n] = n
        else:
            memo[n] = self.fibs(n - 1, memo) + self.fibs(n - 2, memo)
        return memo[n]